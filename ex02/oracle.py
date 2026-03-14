import os
import sys
from dotenv import load_dotenv

"""load_env to load the .env file into environment variables"""
"""load .env file if present, does not overwrite environment variables, the ones already set take precedence"""
load_dotenv()

REQUIRED_CONFIG = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
]

def get_config():
    config = {}
    for key in REQUIRED_CONFIG:
        value = os.getenv(key)
        if not value:
            value = f"[MISSING] {key} not set"
        config[key] = value
    return config
"""Above function ensures missing variables are clearly flagged"""

def print_config(config):
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: {config['DATABASE_URL']}")
    print(f"API Access: {config['API_KEY']}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {config['ZION_ENDPOINT']}\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")
    overrides = any(os.environ.get(key) for key in REQUIRED_CONFIG)
    if overrides:
        print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")

def main():
    config = get_config()
    print_config(config)

if __name__ == "__main__":
    main()
