import subprocess

# Function to run a script
def run_script(script_name):
    try:
        # Run the Python script
        subprocess.run(["python3", script_name], check=True)
        print(f"Successfully executed {script_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_name}: {e}")

# Execute the scripts in order
run_script("1.py")
run_script("2.py")
run_script("3.py")

