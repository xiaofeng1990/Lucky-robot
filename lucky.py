# -*- coding: utf-8-*-
from robot import log
from robot import config
logger = log.get_logger(__name__)

logger.debug('debug {}'.format(2))
logger.info('警告 {}'.format(1))

location = {
    'location': "武汉"
}
config.add(location)
a = config.get('location', 'hh')
print(a)
