from django.core.management.base import BaseCommand
from google_auth_oauthlib.flow import InstalledAppFlow
from django.conf import settings
import json
import os
import tempfile


# OAuth 2.0 스코프 정의
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send']

class Command(BaseCommand):
    help = 'Launches a browser to authenticate the user and obtain a refresh token for Gmail API'

    def add_arguments(self, parser):
        default_client_id = settings.GMAIL_OAUTH_CLIENT_ID if hasattr(settings, 'GMAIL_OAUTH_CLIENT_ID') else None,
        default_client_secret = settings.GMAIL_OAUTH_CLIENT_SECRET if hasattr(settings, 'GMAIL_OAUTH_CLIENT_SECRET') else None,
        parser.add_argument('--client-id', type=str, required=True, help='Your Google OAuth 2.0 Client ID', default=default_client_id)
        parser.add_argument('--client-secret', type=str, required=True, help='Your Google OAuth 2.0 Client Secret', default=default_client_secret)

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        client_secret = kwargs['client_secret']

        # 임시 파일을 생성하여 OAuth 2.0 클라이언트 시크릿 정보를 담음
        with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.json') as temp_client_secret_file:
            client_config = {
                "installed": {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "redirect_uris": ["http://localhost"]
                }
            }

            # 임시 파일에 클라이언트 정보 작성
            json.dump(client_config, temp_client_secret_file)
            temp_client_secret_file_path = temp_client_secret_file.name

        try:
            # OAuth 인증 플로우 시작
            flow = InstalledAppFlow.from_client_secrets_file(temp_client_secret_file_path, SCOPES)
            creds = flow.run_local_server(port=0)

            # refresh token 저장
            try:
                from gmail_oauth_backend.models import RefreshToken
                RefreshToken.objects.update_or_create(
                    key='PyLab',
                    defaults={'value': creds.to_json()}
                )
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Can not save Refresh Token to database: {e}'))

            self.stdout.write(self.style.SUCCESS(f'Refresh Token: {creds.refresh_token}'))

        finally:
            # 임시 파일 삭제
            if os.path.exists(temp_client_secret_file_path):
                os.remove(temp_client_secret_file_path)
