import requests
from django.utils.http import urlencode

from allauth.socialaccount.providers.oauth2.client import (
    OAuth2Client,
    OAuth2Error
)


class WixOAuth2Client(OAuth2Client):
    def get_access_token(self, code):
        resp = requests.post(
            self.access_token_url,
            headers={'Content-Type': 'application/json'},
            json={
                'grant_type': 'authorization_code', # omit redirect_uri
                'client_id': self.consumer_key, # << add fields missing
                'client_secret': self.consumer_secret, # < from allauth
                'code': code
            }
        )
        access_token = None
        if resp.status_code in [200, 201]:
            access_token = resp.json()
        if not access_token or 'access_token' not in access_token:
            raise OAuth2Error(f'Wix access error: {resp.content}')
        return access_token

    def get_redirect_url(self, authorization_url, extra_params):
        params = {
            'appId': self.consumer_key, # instead of client_id
            'redirectUrl': self.callback_url # instead of redirect_uri
        }
        if self.state:
            params['state'] = self.state
        params.update(extra_params)
        return f'{authorization_url}?{urlencode(params)}'
