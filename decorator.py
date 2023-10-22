from django.conf import settings
from functools import wraps
from rauth import OAuth2Service


def fresh_wix(func):
    'refresh Wix token if necessary'
    @wraps(func)
    def fresh_func(self, *args):
        out = func(self, *args)
        if out.get('message') == 'internal error':
            self.refresh()
            return func(self, *args)
        return out
    return fresh_func

class WixAPI:
    access_token_url='https://www.wixapis.com/oauth/access'
    def __init__(self, access_token, refresh_token):
        self.data = {
            'client_id': settings.WIX_CLIENT_ID,
            'client_secret': settings.WIX_CLIENT_SECRET,
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        }
        self.service = OAuth2Service(
            client_id=settings.WIX_CLIENT_ID,
            client_secret=settings.WIX_CLIENT_SECRET,
            access_token_url=self.access_token_url,
        )
        self.session = self.service.get_session(access_token)

    def refresh(self):
        data = self.session.post(
			self.access_token_url, json=self.data, headers={'Content-type': 'application/json'}
		).json()
        self.data['refresh_token'] = data['refresh_token']
        self.session = self.service.get_session(data['access_token'])

    @fresh_wix
    def do_stuff(self, url):
        return self.session.get(url)
