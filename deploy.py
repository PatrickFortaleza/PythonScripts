import subprocess
subprocess.run(["scp", "-r", '/PATH/TO/FOLDER', "USER@SERVERIP:PATH/TO/REMOTE/FOLDER"])
# subprocess.run(["scp", "-r", './project', "pfteza@server.com:/var/www/pfteza/server"])
# Recursively scp's all files in folder to destination path.
# Assumptions: 
# - Server is set-up to handle project's infrastructure and technology
# - SSH keys have been set-up on local machine