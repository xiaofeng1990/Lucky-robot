import logging
# 支持回滚创建日志文件
from logging.handlers import RotatingFileHandler
import os
from robot import constants


def get_logger(name):
    """
    获得日志对象，并格式化日志输出
    :param name: 当前打印日志的文件名
    :return: logging对象
    """
    # 日志格式化
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 设置日志文件handler
    file_handler = RotatingFileHandler(os.path.join(constants.LOGGER_PATH, 'lucky.log'),
                                       maxBytes=1024 * 1024, backupCount=5, encoding="utf8")
    file_handler.setLevel(level=logging.DEBUG)
    file_handler.setFormatter(formatter)

    # 将日志输出到控制台
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)

    logger.addHandler(file_handler)
    logger.addHandler(console)

    return logger



