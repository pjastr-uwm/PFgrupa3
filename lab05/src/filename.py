from datetime import datetime


def generate_unique_filename():
    return f"file_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt"