# import subprocess

# # Function to run a script
# def run_script(script_name):
#     try:
#         # Run the Python script
#         subprocess.run(["python3", script_name], check=True)
#         print(f"Successfully executed {script_name}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error executing {script_name}: {e}")

# # Execute the scripts in order
# run_script("1.py")
# run_script("2.py")
# run_script("3.py")

import subprocess
import os

def run_all_scripts():
    base_dir = "C:\\Users\\Atharv\\Desktop\\Chatgpt\\SIH\\cert.in"
    
    # Full paths for the scripts
    scripts = ["1.py", "2.py", "3.py"]
    
    for script in scripts:
        script_path = os.path.join(base_dir, script)
        try:
            subprocess.run(["python", script_path], check=True)
            print(f"Successfully executed {script}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing {script}: {e}")

if __name__ == "__main__":
    run_all_scripts()
