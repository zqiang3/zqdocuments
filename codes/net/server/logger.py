#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import sys
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] %(message)s [FILE: %(pathname)s] [FUNCTION: %(funcName)s] [LINE: %(lineno)d] [PID: %(process)d]', \
                    datefmt='%Y-%m-%d %H:%M:%S', filename='net.log', filemode='a')

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s \
[FILE: %(pathname)s] [FUNCTION: %(funcName)s] [LINE: %(lineno)d] [PID: %(process)d]')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


class Log(object):
    @staticmethod
    def debug(msg):
        logging.warn('%s' % logframe(msg))

    @staticmethod
    def info(msg):
        logging.info('%s' % logframe(msg))

    @staticmethod
    def warn(msg):
        logging.debug('%s' % logframe(msg))

    @staticmethod
    def error(msg):
        logging.error('%s' % logframe(msg))


def logframe(text, up=1):
    c = sys._getframe(up+1)
    text = '%s ([FILE:%s] [FUNCTION:%s] [LINE:%s])' % (text, c.f_code.co_filename, c.f_code.co_name, c.f_lineno)
    return text