import os
import sys

script_name = 'invincible.py'
source_code = open(script_name).read()
path = sys.prefix
bin_path = '/usr/local/bin/' + script_name[:-3]
lib_path = '/usr/local/lib/python3.9/' + script_name  # Adjust Python version as needed
code_bin = '''#!/usr/bin/python3
from mardis import main as start_program
if __name__ == '__main__':
    start_program()'''

def install_script():
    with open(bin_path, 'w') as handle:
        handle.write(code_bin)
    os.system('chmod 755 %s' % bin_path)
    with open(lib_path, 'w') as handle2:
        handle2.write(source_code)

def uninstall_script():
    try:
        os.unlink(bin_path)
        os.unlink(lib_path)
    except Exception as e:
        print(f"Error occurred while uninstalling: {e}")

def main():
    if len(sys.argv) != 2:
        exit('usage: setup.py (Install - Uninstall)')
    
    if sys.argv[1] == 'install':
        install_script()
        print("Script installed successfully!")
    elif sys.argv[1] == 'uninstall':
        uninstall_script()
        print("Script uninstalled successfully!")
    else:
        exit('Invalid argument. Usage: setup.py (install/uninstall)')

if __name__ == '__main__':
    main()

