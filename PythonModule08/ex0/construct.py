#!/usr/bin/env python3

import os
import sys
import site


def main() -> None:
    environment = os.environ.get('VIRTUAL_ENV')
    status: str
    current_py: str
    environment_name: str

    if environment:
        status = "Welcome to the construct"
        current_py = sys.executable
        environment_name = os.path.basename(environment)
    else:
        status = "You're still plugged in"
        current_py = f"{sys.executable}.{sys.version_info.minor}"
        environment_name = "None detected"

    print()
    print(f"MATRIX STATUS: {status}")
    print()
    print(f"Current Python: {current_py}")
    print(f"Virtual Environment: {environment_name}")
    if environment:
        print(f"Environment Path: {environment}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        package_paths = site.getsitepackages()
        for path in package_paths:
            print(path)
    else:
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
