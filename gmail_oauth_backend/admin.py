from django.contrib import admin

from gmail_oauth_backend import RefreshToken


@admin.register(RefreshToken)
class RefreshTokenAdmin(admin.ModelAdmin):
    list_display = ('value', 'created', 'updated')

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj:
            fields = [field for field in fields if field != 'key']
        return fields
