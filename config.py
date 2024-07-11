import configparser
import os

def load_config():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'settings.ini'))
    return config