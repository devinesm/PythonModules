#!/usr/bin/env python3

import sys
import importlib


def analyse_matrix() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    print()

    numbers = np.random.rand(1000)
    print("Processing 1000 data points...")

    df = pd.DataFrame(numbers)

    print("Generating visualization...")
    plt.plot(df)
    plt.savefig("matrix_analysis.png")

    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()

    packages = {"pandas": "Data manipulation",
                "numpy": "Numerical computation",
                "requests": "Network access",
                "matplotlib": "Visualization"}

    print("Checking dependencies:")
    loading_status = True

    for package, util in packages.items():
        try:
            module = importlib.import_module(package)
            print(f"[OK] {package} ({module.__version__}) - {util} ready")
        except ImportError:
            loading_status = False
            print(f"[ERROR] {package} - {util} not ready")

    if loading_status is True:
        analyse_matrix()
    else:
        print()
        print("     With pip: pip install -r requirements.txt")
        print("     With Poetry: poetry install")
        sys.exit(1)


if __name__ == "__main__":
    main()
