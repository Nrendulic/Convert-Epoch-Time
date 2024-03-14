import datetime

def convert_epoch_to_readable(epoch_time):
    """Convert epoch time to a human-readable date and time."""
    return datetime.datetime.fromtimestamp(int(epoch_time)).strftime('%Y-%m-%d %H:%M:%S UTC')

if __name__ == "__main__":
    epoch_time = input("Enter the epoch time: ")
    readable_time = convert_epoch_to_readable(epoch_time)
    print(f"Readable date and time: {readable_time}")
