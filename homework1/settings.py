API_KEY = ''
PROXY_URL = ''
PROXY_USERNAME = ''
PROXY_PASSWORD = ''

try:
    from settings_local import *
except ImportError:
    print("Import Error")
