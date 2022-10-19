from os import getenv

PARAMS = {
    "BASE_ID": getenv("BASE_ID", ""),
    "API_KEY": getenv("API_KEY", ""),
    "TABLE": getenv("TABLE", ""),
}
