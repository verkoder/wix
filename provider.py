from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class WixAccount(ProviderAccount):
    pass

class WixProvider(OAuth2Provider):
    id = 'wix'
    name = 'Wix'
    account_class = WixAccount

    def extract_uid(self, data):
        return str(data['site']['siteDisplayName'])

provider_classes = [WixProvider]
