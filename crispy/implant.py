import platform

from os_types.mac_os import enum_users

if platform.system() == 'Darwin':
    print enum_users()
    