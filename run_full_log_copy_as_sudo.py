import os
import subprocess

def run_full_log_copy_as_sudo():
    #needs a command to cd to whatever directory we save copy_logs.py to
    #something like: 
    #change_directory = "/var/log/asterisk/full"
    #os.chdir(change_directory)
    #add a print statmement for testing to confirm the cd worked
    #print("New directory is:", os.getcwd())
    
    sudo_command = "sudo python3 copy_logs.py"
    
    try:
        subprocess.run(sudo_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Sudo command executed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error executing sudo command:", e)