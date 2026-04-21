# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:00:53 2026

@author: theja
"""

import numpy as np

def main():
    
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)

    print(f"{'x':>10} | {'sin(x)':>10}")
    print("-" * 25)

    for i in range(len(x)):
        print(f"{x[i]:10.4f} | {y[i]:10.4f}")

if __name__ == "__main__":
    main()