"""
Script to summarize logs in the logs/ folder.
"""
import os


def summarize_logs():
    log_dir = os.path.join(os.path.dirname(__file__), '../logs')
    for log_file in os.listdir(log_dir):
        if log_file.endswith('.log'):
            print(f'--- {log_file} ---')
            with open(os.path.join(log_dir, log_file), 'r', encoding='utf-8') as f:
                print(f.read())

if __name__ == "__main__":
    summarize_logs()
