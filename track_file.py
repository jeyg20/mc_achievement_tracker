import time, re


def follow(files):
    files.seek(0, 2)
    while True:
        line = files.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def process_log(file_path):
    with open(file_path, "r") as log_file:
        log_lines = follow(log_file)
        pattern = r"^\[\d{2}:\d{2}:\d{2}\] \[Server thread/INFO\]:\s+.* has made the advancement \[.*\]$"
        for line in log_lines:
            if re.match(pattern, line):
                print(line.strip())
