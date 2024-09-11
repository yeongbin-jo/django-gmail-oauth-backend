from django.contrib import admin

from gmail_oauth_backend.models import RefreshToken


@admin.register(RefreshToken)
class RefreshTokenAdmin(admin.ModelAdmin):
    list_display = ['get_refresh_token', 'created', 'updated']

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj:
            fields = [field for field in fields if field != 'key']
        return fields

    def get_refresh_token(self, obj):
        return obj.value.get('refresh_token', '-')  # 'age' 키가 없으면 'N/A' 출력
    get_refresh_token.short_description = 'Refresh Token'
