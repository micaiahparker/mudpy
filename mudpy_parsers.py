def parse_data(data):
    try:
        return data.decode().strip()
    except UnicodeDecodeError:
        print("failed to decode.")
        return ""
