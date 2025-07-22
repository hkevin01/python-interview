"""
Logging utilities for user actions, errors, and test results.
"""
import logging
import os


def setup_logging(log_file='logs/app.log'):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )

def log_action(action: str):
    logging.info(f'Action: {action}')

def log_error(error: str):
    logging.error(f'Error: {error}')

def log_test_result(test: str, result: str):
    logging.info(f'Test: {test} Result: {result}')
