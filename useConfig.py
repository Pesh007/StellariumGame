import os
import platform
import configparser

def find_config_path():
    system = platform.system()
    if system == 'Windows':
        return os.path.join(os.environ['APPDATA'], 'Stellarium', 'config.ini')
    elif system == 'Linux':
        return os.path.expanduser('~/.stellarium/config.ini')
    else:
        return None

def get_remote_control_port(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)

    if 'RemoteControl' in config and 'port' in config['RemoteControl']:
        return config['RemoteControl']['port']
    else:
        return None

def find_port():
    try:
        path = find_config_path()
        port = get_remote_control_port(path)

        if port:
            return port
        else:
            return None
    except Exception as e:
        return False