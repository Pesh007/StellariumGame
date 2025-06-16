import os
import platform

def find_config_path():
    system = platform.system()
    if system == 'Windows':
        return os.path.join(os.environ['APPDATA'], 'Stellarium', 'config.ini')
    elif system == 'Linux':
        return os.path.expanduser('~/.stellarium/config.ini')
    elif system == 'Darwin':  # macOS
        return os.path.expanduser('~/Library/Application Support/Stellarium/config.ini')
    else:
        return None

path = find_config_path()
print(f"Stellarium config path: {path if path and os.path.exists(path) else 'Not found'}")
