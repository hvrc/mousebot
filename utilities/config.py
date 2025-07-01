import configparser
import os

# get config variables from config.ini, credentials.ini
# merges credentials into config
def get_config():
    base_path = os.path.dirname(os.path.dirname(__file__))
    config_file = os.environ.get('TEST_CONFIG_FILE')
    if not config_file:
        config_file = os.path.join(base_path, 'config', 'config.ini')
    env = os.environ.get('TEST_ENV', 'dev')
    credentials_path = os.path.join(base_path, 'config', 'credentials.ini')

    config = configparser.ConfigParser()
    credentials = configparser.ConfigParser()

    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file not found at: {config_file}")
    if not os.path.exists(credentials_path):
        raise FileNotFoundError(f"Credentials file not found at: {credentials_path}")

    config.read(config_file)
    credentials.read(credentials_path)

    if env not in config:
        raise ValueError(f"Section [{env}] not found in {config_file}")
    merged = dict(config[env])
    if env in credentials:
        merged.update(credentials[env])
    return merged