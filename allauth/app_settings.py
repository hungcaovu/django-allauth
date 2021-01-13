from django.conf import settings


SOCIALACCOUNT_ENABLED = "allauth.socialaccount" in settings.INSTALLED_APPS

LOGIN_REDIRECT_URL = getattr(settings, "LOGIN_REDIRECT_URL", "/")

USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")

AWESOME_AVATAR = {
    'width': 100,
    'height': 100,

    'select_area_width': 400,
    'select_area_height': 300,

    'save_quality': 90,
    'save_format': 'png',
}