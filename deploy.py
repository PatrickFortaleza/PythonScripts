import subprocess
subprocess.run(["scp", "-r", '/PATH/TO/FOLDER', "USER@SERVERIP:PATH/TO/REMOTE/FOLDER"])
# subprocess.run(["scp", "-r", './password-strength', "pfteza@45.32.87.66:/var/www/pfteza-dev/signup"])
# Recursively scp's all files in folder to destination path.
# Assumptions: 
# - Server is set-up to handle project's infrastructure and technology
# - SSH keys have been set-up on local machine