#!/bin/env python3
import os

def main():
    print(f"This is a test: {os.getenv('AS_ENV', 'NA')}")


if __name__ == '__main__':
    main()

