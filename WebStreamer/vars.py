# (c) @AvishkarPatil | @EverythingSuckz

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('9583452'))
    API_HASH = str(getenv('4f8972504d056a30bfec5220375c3492'))
    BOT_TOKEN = str(getenv('5272344708:AAGn01_FI6rePXnSFhdDuka4DpMPf5XIYmU'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'AviStreamBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('1001320621761'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = int(getenv('5007319313', '797848243'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('ksjncjkjcnd'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('mongodb+srv://uadxeocsqdfogim:]LFwlg6[@cluster0.lirgy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '500'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001296894100")).split()))
