import os

# main directory
APP_PATH = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))

# logging path
LOGGER_PATH = os.path.join(APP_PATH, "log")
CONFIG_PATH = os.path.join(APP_PATH, "config")
DEFAULT_CONFIG_FILE = os.path.join(CONFIG_PATH, "default.yml")
CUSTOMER_CONFIG_FILE = os.path.join(CONFIG_PATH, "customer.yml")
