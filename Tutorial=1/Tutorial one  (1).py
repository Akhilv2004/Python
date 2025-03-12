def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

total_seconds = int(input("Enter time in seconds: "))
formatted_time = convert_seconds_to_time(total_seconds)
print(f"The time is: {formatted_time}")
