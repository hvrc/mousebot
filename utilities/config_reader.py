import configparser
import os

# get config variables from config.ini, credentials.ini
# merges credentials into config
def get_config():
    config = configparser.ConfigParser()
    credentials = configparser.ConfigParser()
    base_path = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(base_path, 'config', 'config.ini')
    credentials_path = os.path.join(base_path, 'config', 'credentials.ini')
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")
    
    if not os.path.exists(credentials_path):
        raise FileNotFoundError(f"Credentials file not found at: {credentials_path}")
    
    config.read(config_path)
    credentials.read(credentials_path)
    
    for section in credentials.sections():
        if section not in config:
            config[section] = {}
        for key, value in credentials[section].items():
            config[section][key] = value
    
    return config