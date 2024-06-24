import time, re


def follow(files):
    files.seek(0, 2)
    while True:
        line = files.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


if __name__ == "__main__":
    log_file = open("/home/jeison/.minecraft/logs/latest.log", "r")
    log_lines = follow(log_file)
    pattern = r"^\[\d{2}:\d{2}:\d{2}\] \[Server thread/INFO\]: .* \[.*\]$"
    for line in log_lines:
        if re.match(pattern, line):
            print(line)
