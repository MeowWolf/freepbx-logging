def run_full_log_copy_as_sudo():
    
    sudo_command = "sudo python3 copy_logs.py"
    
    try:
        subprocess.run(sudo_command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Sudo command executed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error executing sudo command:", e)
