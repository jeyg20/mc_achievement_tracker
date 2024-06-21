import subprocess


def select_file():
    # Open Zenity file selection dialog
    process = subprocess.Popen(
        ["zenity", "--file-selection"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    stdout, stderr = process.communicate()

    if process.returncode == 0:
        selected_file = stdout.decode("utf-8").strip()
        return selected_file
    else:
        print(f"Error opening Zenity: {stderr.decode('utf-8')}")
