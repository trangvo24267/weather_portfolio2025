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
# print (format_temperature("40"))

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
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if row:
                date=row[0]
                min=int(row[1])
                max=int(row[2])
                data_list.append([date,min,max])
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
    
    dates=[]
    min_temp_list = []
    max_temp_list = []
    for row in weather_data:
        if row:
            dates.append(row[0])
            min_temp_list.append(round(convert_f_to_c(row[1]),1))
            max_temp_list.append(round(convert_f_to_c(row[2]),1))

    row_count = len(dates)
    minimum_temp, min_position = find_min(min_temp_list) #storing function returns in 2 variables
    min_temp_date = convert_date(dates[min_position]) #using above function for matching equivalent date to the above min temp
    maximum_temp, max_position = find_max(max_temp_list)
    max_temp_date = convert_date(dates[max_position])
    mean_min_temp = round(calculate_mean(min_temp_list),1)
    mean_max_temp = round(calculate_mean(max_temp_list),1)

    summary_string = (
        f"{row_count} Day Overview\n" 
        f"  The lowest temperature will be {minimum_temp}{DEGREE_SYMBOL}, and will occur on {min_temp_date}.\n"
        f"  The highest temperature will be {maximum_temp}{DEGREE_SYMBOL}, and will occur on {max_temp_date}.\n"
        f"  The average low this week is {mean_min_temp}{DEGREE_SYMBOL}.\n"
        f"  The average high this week is {mean_max_temp}{DEGREE_SYMBOL}.\n"
    ) #string all functions together

    return (summary_string)

def generate_daily_summary(csv_file_path):
    """Outputs a daily summary for the given weather data.

    Args:
        csv_file_path: A string representing the file path to a csv file.
    Returns:
        A string containing the summary information.
    """
    date_daily =[]
    min_daily_temp =[]
    max_daily_temp =[]
    
    for row in csv_file_path:
            if row:
                date_daily = convert_date(row[0])
                min_daily_temp = round(convert_f_to_c(row[1]), 1)
                max_daily_temp = round(convert_f_to_c(row[2]), 1)
    
            summary_daily_string =(
                f"{'-' * 4} {date_daily} {'-' * 4}\n"
                f"  Minimum temperature: {min_daily_temp}{DEGREE_SYMBOL}\n"
                f"  Maximum temperature: {max_daily_temp}{DEGREE_SYMBOL}\n"
            )

    return (summary_daily_string)
