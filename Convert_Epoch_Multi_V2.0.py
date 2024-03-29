from datetime import datetime, timezone
import zoneinfo

def convert_epoch_to_readable(epoch_time, tz=timezone.utc):
    """Convert epoch time to a human-readable date and time in the given timezone."""
    epoch_time = int(epoch_time[:10])  # Convert to integer and truncate input to first 10 characters
    dt = datetime.fromtimestamp(epoch_time, tz=tz)
    return dt.strftime('%Y-%m-%d %H:%M:%S %Z')

if __name__ == "__main__":
    epoch_time = input("Enter the epoch time:\n")
    print(f"UTC Time: {convert_epoch_to_readable(epoch_time)}")

    # Pacific Time
    pacific_time = convert_epoch_to_readable(epoch_time, tz=zoneinfo.ZoneInfo("America/Los_Angeles"))
    print(f"Pacific Time (PST/PDT): {pacific_time}")

    # Central Time
    central_time = convert_epoch_to_readable(epoch_time, tz=zoneinfo.ZoneInfo("America/Chicago"))
    print(f"Central Time (CST/CDT): {central_time}")

    # Eastern Time
    eastern_time = convert_epoch_to_readable(epoch_time, tz=zoneinfo.ZoneInfo("America/New_York"))
    print(f"Eastern Time (EST/EDT): {eastern_time}")
