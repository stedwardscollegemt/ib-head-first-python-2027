from modules import stats_utils

def convert_str_time_to_hundredths(str_time):
    minutes = "0"
    rest = str_time
    if ":" in str_time:
        minutes, rest = str_time.split(":")
    seconds, hundredths = rest.split(".")
    hundredths_total = (int(minutes) * 60 * 100) + (int(seconds) * 100) + int((hundredths))
    return hundredths_total

def convert_time_to_str_format(int_time):
    str_time = ""

    minutes = int_time // 6000
    rest = int_time % 6000 # seconds + hundredths
    seconds = rest // 100
    hundredths = rest % 100

    if minutes > 0:
        str_time = str(minutes) + ":"

    str_time = str_time + str(seconds) + "." + str(hundredths)
    return str_time


def read_swim_data(filepath):
    try:
        with open(filepath) as file:
            lines = file.readlines()
        lines = lines[0].split(',')
        
        times = []
        for convert in lines:
            converted = convert_str_time_to_hundredths(convert)
            times.append(converted)
        
        # calculate the average and use that stats_utils module
        average = stats_utils.mean(times)

        average_str = convert_time_to_str_format(average)

        filename = filepath
        # check if filename needs to be cleaned from folders
        # e.g. swimdata/Abi-10-50m-Back.txt ---> Abi-10-50m-Back
        if "/" in filename:
            filename = filename.split("/")[-1]
        name, age, distance, stroke = filename.removesuffix(".txt").split("-")

        return name, age, distance, stroke, times, average_str
    except FileNotFoundError:
        return "Error: We cannot open the file."