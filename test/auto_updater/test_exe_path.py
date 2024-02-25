import os
import subprocess
import sys

if getattr(sys, 'frozen', False):
    if os.name == "posix":
        application_path = os.path.join(os.path.dirname(sys.executable), "AU")
        pass
    else:
        application_path = os.path.join(os.path.dirname(sys.executable), "PostureFIT.exe")
elif __file__:
    application_path = os.path.dirname(__file__) + "/index.py"

config_path = os.path.join(application_path)
print(config_path)
subprocess.call([
    application_path,
    "1.0.0",
    application_path
])
