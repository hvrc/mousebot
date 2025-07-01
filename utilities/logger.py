import os
import time

# writes logs to a file
class Logger:
    def __init__(self, log_dir, test_name):
        os.makedirs(log_dir, exist_ok=True)
        self.log_path = os.path.join(log_dir, 'log.txt')
        self.test_name = test_name
        self.start_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.log(f"[START] {self.test_name} at {self.start_time}")

    def log(self, message):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {message}\n")

    def end(self, status):
        end_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.log(f"[END] {self.test_name} at {end_time} - STATUS: {status}")

