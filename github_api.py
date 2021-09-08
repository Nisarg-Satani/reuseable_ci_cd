# import subprocess
# subprocess.run(["touch", "filename.txt"], capture_output=True)

import os
os.system('cd ../var/projects/')
os.system('touch filename.txt')
if os.path.isdir('reuseable'):
    print ("Directory exist")
else:
    print ("Directory not exist")