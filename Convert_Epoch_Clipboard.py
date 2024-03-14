import datetime
import zoneinfo
import pyperclip

def convert_epoch_to_readable(epoch_time, tz=datetime.timezone.utc):
    """Convert epoch time to a human-readable date and time in the given timezone."""
    dt = datetime.datetime.fromtimestamp(int(epoch_time), tz=tz)
    return dt.strftime('%Y-%m-%d %H:%M:%S %Z')

if __name__ == "__main__":
    # Fetch the epoch time from the macOS clipboard
    epoch_time = pyperclip.paste()

    # Attempt to convert and print times; catch exception if clipboard content is not a valid epoch time
    try:
        print(f"UTC Time: {convert_epoch_to_readable(epoch_time)}")
        # Central Time
        central_time = convert_epoch_to_readable(epoch_time, tz=zoneinfo.ZoneInfo("America/Chicago"))
        print(f"Central Time (CST/CDT): {central_time}")
        # Eastern Time
        eastern_time = convert_epoch_to_readable(epoch_time, tz=zoneinfo.ZoneInfo("America/New_York"))
        print(f"Eastern Time (EST/EDT): {eastern_time}")
        # Pacific Time
        pacific_time = convert_epoch_to_readable(epoch_time, tz=zoneinfo.ZoneInfo("America/Los_Angeles"))
        print(f"Pacific Time (PST/PDT): {pacific_time}")
    except ValueError:
        print("The clipboard content is not a valid epoch time.")
