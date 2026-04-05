#!/usr/bin/env python3
import os
import subprocess

def main():
    src_directory = os.getcwd()
    report_directory = os.path.join(src_directory, "report")

    if not os.path.isdir(report_directory):
        print("Initially creating persistent directories")
        os.makedirs(report_directory, exist_ok=True)
        os.chmod(report_directory, 0o777)

    # Make sure we are using the latest version
    print("Pulling latest secfigo/bandit docker image...")
    subprocess.run(["docker", "pull", "secfigo/bandit:latest"], check=False)

    print("Running bandit...")
    subprocess.run([
        "docker", "run", "--rm",
        "--volume", f"{src_directory}:/src",
        "--volume", f"{report_directory}:/report",
        "secfigo/bandit:latest"
    ], check=False)

if __name__ == "__main__":
    main()
