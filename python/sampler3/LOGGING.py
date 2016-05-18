import logging


class MyFilter(logging.Filter):
    def __init__(self, param=None):
        self.param = param

    def filter(self, record):
        if self.param is None:
            allow = True
        else:
            allow = self.param not in record.msg
        if allow:
            record.msg = 'changed: ' + record.msg
        return allow

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : '[%(levelname)s %(asctime)s %(name)s @ %(process)d (%(filename)s:%(lineno)d)] - %(message)s',
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(name)s  %(message)s'
        },
    },
    'filters': {
        'myfilter': {
            '()': MyFilter,
            'param': 'noshow',
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'MIDNIGHT',
            'interval': 1,
            'backupCount': 20,
            'filename': 'test.log',
            'formatter': 'verbose',
            'filters': ['myfilter'],
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'modulea': {
            'handlers':['null'],
            'propagate': False,
            'level':'INFO',
        },
        'moduleb': {
            'handlers': ['file'],
            'propagate': False,
            'level': 'DEBUG',
        },
    },
    'root':{
            'handlers':['console'],
            'level':'INFO',
    },
}
