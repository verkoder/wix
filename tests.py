from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse, TestCase

from .provider import WixProvider


class BitlyTests(OAuth2TestsMixin, TestCase):
    provider_id = WixProvider.id

    def get_mocked_response(self):
        return MockedResponse(
            200,
            '''{
            'data': {
                'apiKey': 'R_f6397a37e765574f2e198dba5bb59522',
                'custom_short_domain': null,
                'display_name': null,
                'full_name': 'Wix API Oauth Demo Account',
                'is_enterprise': false,
                'login': 'wixapioauthdemo',
                'share_accounts': [],
                'tracking_domains': []
            },
            'status_code': 200,
            'status_txt': 'OK'
        }''',
        )
