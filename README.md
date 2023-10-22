# wix
Wix allauth provider

Not yet posted to allauth repo, but free to use.

# Provider files
- client.py
- provider.py
- urls.py
- views.py

# Bonus file - decorator.py
Wix tokens persist for 5 minutes, but renew with a refesh token. While not part of the allauth provider, a sample refresh token decorator is included. The decorator gets the client ID and secret from django settings. Note: this decorator would be in a different app, and is not required by the wix provider.
