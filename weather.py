import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

# with open("example_one.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         iso_string = row["Date"]
#         temp = row["min"]

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"
print (format_temperature("40"))

def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_obj = datetime.fromisoformat(iso_string)
    return date_obj.strftime("%A %d %B %Y")
    return weather
convert_date("2021-07-06T00:00:00")
print(convert_date("2021-07-06T00:00:00"))

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_fahrenheit = float(temp_in_fahrenheit)
    temp_in_celsius = (temp_in_fahrenheit - 32) * 5 / 9
    return round(temp_in_celsius, 1)
# convert_f_to_c(temp_in_fahrenheit)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total=0
    count=0
    for number in weather_data:
        total = total + float(number)
        count = count + 1
    mean = total/count
    return float(mean)
    # calculate_mean(weather_data)

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data_list =[]
    with open(csv_file, "r", newline="") as file:
        csv_reader = csv.reader(csv_file)
    for row in reader:
            data_list.append(row)
    return data_list
# load_data_from_csv(csv_file)

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    min_value = float(weather_data[0])
    min_index = 0
    for i, value in enumerate(weather_data):
        value = float(value)
        if value <= min_value:
            min_value = value
            min_index = i
    return (min_value, min_index)

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    max_value = float(weather_data[0])
    max_index = 0
    for i, value in enumerate(weather_data):
        value = float(value)
        if value >= max_value:
            max_value = value
            max_index = i
    return (max_value, max_index)

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    with open(csv_file_path, "r", newline="") as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # skip headers (first row)

        row_count = sum(1 for row in reader)
        print(f"{row_count} Day Overview")
        print(f"The lowest temperature will be {min}, and will occur on {date_obj.st)rftime("%A %d %B %Y")}")
        print(f"The highest temperature will be {max}, and will occur on {date_obj.st)rftime("%A %d %B %Y")}")
        print(f"The average low this week is {mean}.")
        print(f"The average high this week is {mean}.")

def generate_daily_summary(csv_file_path):
    """Outputs a daily summary for the given weather data.

    Args:
        csv_file_path: A string representing the file path to a csv file.
    Returns:
        A string containing the summary information.
    """
    with open(csv_file_path, "r", newline="") as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # skip headers (first row)

        for row in csv_reader:
            if row:
                date = row[0]
                min = row[1]
                max = row[2]
            print(f"{'-' * 4} {date} {'-' * 4}")
            print(f"Minimum temperature: {min}")
            print(f"Maximum temperature: {max}")
