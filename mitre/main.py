import subprocess
import os

def run_all_scripts():
    base_dir = "C:\\Users\\Atharv\\Desktop\\Chatgpt\\SIH\\mitre"
    
    # Full paths for the scripts
    scripts = ["1.py", "2.py"]
    
    for script in scripts:
        script_path = os.path.join(base_dir, script)
        try:
            subprocess.run(["python", script_path], check=True)
            print(f"Successfully executed {script}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing {script}: {e}")

if __name__ == "__main__":
    run_all_scripts()
