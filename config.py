from dotenv import dotenv_values

config = dotenv_values(".env")
URL = config["URL"]
