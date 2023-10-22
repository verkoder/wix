from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import WixProvider


urlpatterns = default_urlpatterns(WixProvider)
