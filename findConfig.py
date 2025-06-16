import os
import platform

def find_config_path():
    system = platform.system()
    if system == 'Windows':
        return os.path.join(os.environ['APPDATA'], 'Stellarium', 'config.ini')
    elif system == 'Linux':
        return os.path.expanduser('~/.stellarium/config.ini')
    else:
        return None

