# django-gmail-oauth-backend

Simplifies Gmail authentication for Django applications using OAuth 2.0. WITHOUT App Passwords!

## Installation

```bash
pip install django-gmail-oauth-backend
```

Add settings to your Django project settings file.

```python
GMAIL_OAUTH_CLIENT_ID = 'YOUR_CLIENT_ID'
GMAIL_OAUTH_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

INSTALLED_APPS = [
    ...,
    'gmail_oauth_backend',
    ...
]
```

And execute the following command at least once initially. This command will launch a web browser and request OAuth approval through the user’s browser. Once the request is completed, a Refresh Token for the Gmail API will be automatically issued. __Before running this init command, please make sure to add `http://localhost:8912/` to the redirect URLs in your Cloud Console settings.__

```bash
# Create RefreshToken table First
./manage.py migrate

# Then get the RefreshToken
./manage.py init_gmail_oauth_token
```

> Note: The Refresh Token is stored in the database and is used to automatically refresh the Access Token when it expires. The Google OAuth 2.0 refresh token typically **does not have an expiration date**, but if a refresh token becomes invalid or expires for other reasons, it will need to be reissued following the procedure above.

## Credits

- [django-gmailapi-backend](https://github.com/dolfim/django-gmailapi-backend)

## Authors & Contributors

- [Yeongbin Jo](iam.yeongbin.jo@gmail.com)