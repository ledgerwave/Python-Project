"""
Loading environment variables from a .env file
"""

import os
from dotenv import load_dotenv


def main():
    """
    Main function
    """
    load_dotenv()

    secret = os.getenv("SECRET")

    print(secret)


if __name__ == "__main__":
    main()
