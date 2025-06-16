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

path = find_config_path()
print(path)
if None:
    print("Неуспешно намиране на пътя до конфигурационния файл на Stellarium.")