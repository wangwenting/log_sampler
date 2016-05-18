# -*- coding: utf-8 -*-

LOGGING = {
    'version': 1,
# 是否忽略之前的logger(在通过加载文件前可能生成别的logger， 比如导入某个模块，
# 此模块中有生成该模块的logger，如 logger = logging.getLogger(__name__)
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
    'handlers': {
# 文件handler ， 每天晚上凌晨更换文件，最多备份20天
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'MIDNIGHT',
            'interval': 1,
            'backupCount': 20,
            'filename': 'test.log',
            'formatter': 'verbose',
        },
# 打印到控制台
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
# 打印到/de/null 中.
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
'loggers': {
          # propagate  是否同时用parent logger 进行打印
        '':{
            'handlers':['console'],
            'level':'INFO',
        },

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
    }
}
