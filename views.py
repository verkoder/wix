import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .client import WixOAuth2Client
from .provider import WixProvider


class WixOAuth2Adapter(OAuth2Adapter):
    provider_id = WixProvider.id
    access_token_url = 'https://www.wixapis.com/oauth/access'
    authorize_url = 'https://www.wix.com/installer/install'
    profile_url = 'https://www.wixapis.com/apps/v1/instance'
    members_url = 'https://www.wixapis.com/members/v1/members?fieldsets=FULL'
    supports_state = True
    client_class = WixOAuth2Client

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.profile_url, headers={'Authorization': token.token})
        extra_data = resp.json()
        resp = requests.get(self.members_url, headers={'Authorization': token.token})
        extra_data.update(resp.json())
        return self.get_provider().sociallogin_from_response(request, extra_data)


oauth2_login = OAuth2LoginView.adapter_view(WixOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(WixOAuth2Adapter)
