"""
Script to run static analysis and type checking on source code.
"""
import subprocess


def run_static_analysis():
    print("Running flake8...")
    subprocess.run(["flake8", "src/", "tests/"])
    print("Running mypy...")
    subprocess.run(["mypy", "src/"])

if __name__ == "__main__":
    run_static_analysis()
