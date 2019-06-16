# -*- coding: utf-8-*-
import yaml

from robot import log
from robot import constants

logger = log.get_logger(__name__)
g_config = {}
has_init = False


def init():
    """
    加载配置文件
    :return: 配置文件字典
    """
    global g_config
    global has_init
    # read config
    logger.debug("Trying to read config file")
    try:
        with open(constants.DEFAULT_CONFIG_FILE, "r", encoding="utf8") as f:
            g_config = yaml.safe_load(f)
            has_init = True
    except Exception as e:
        logger.error("加载配置文件{} 失败：{}".format(constants.DEFAULT_CONFIG_FILE, e))
        raise


def get_path(items, default=None):
    global g_config
    cur_config = g_config
    # 判断 items是否是字符串
    if isinstance(items, str) and items[0] == '/':
        items = items.split('/')[1:]
    for key in items:
        if key in cur_config:
            cur_config = cur_config[key]
        else:
            logger.warning("{} not specified in profile, return default value {}"
                           .format('/'.join(items), default))
            return default
    return cur_config


def get(item='', default=None):
    """
    获取某个配置的值
    :param item: 配置项名称，如果是多级配置，则以“/a/b”的形式提供
    :param default: 配置值返回默认值，如果配置项不存在就返回默认值
    :return: 配置项的值，如果为空就返回默认值
    """
    global has_init
    # 加载配置文件
    if not has_init:
        init()
    # 如果输入item为空，着返回全部配置
    if not item:
        return g_config
    # 判断是否是多级配置
    if item[0] == '/':
        return get_path(item, default)
    try:
        return g_config[item]
    except KeyError:
        logger.warning("{} not specified in profile, return default value {}"
                       .format(item, default))
        return default
    except TypeError:
        logger.error(TypeError)
        raise


def add(dic):
    """
    增加配置项
    :param dic: 配置项字典
    :return: 无
    """
    with open(constants.DEFAULT_CONFIG_FILE, "a", encoding="utf8") as f:
        yaml.dump(dic, f, encoding="utf8")
