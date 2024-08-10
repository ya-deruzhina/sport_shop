from .common import *

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'logfile_format': {
            'format': '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': None,
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        }
    }
}

DEBUG = False
LOG_REQUEST = True
LOG_RESPONSE = True
