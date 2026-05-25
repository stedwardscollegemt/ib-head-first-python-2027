
def convert_str_time_to_hundredths(str_time):
    minutes = "0"
    rest = str_time
    if ":" in str_time:
        minutes, rest = str_time.split(":")
    seconds, hundredths = rest.split(".")
    hundredths_total = (int(minutes) * 60 * 100) + (int(seconds) * 100) + int((hundredths))
    return hundredths_total

def read_swim_data(filepath):
    try:
        with open(filepath) as file:
            lines = file.readlines()
        lines = lines[0].split(',')
        
        times = []
        for convert in lines:
            converted = convert_str_time_to_hundredths(convert)
            times.append(converted)
    except FileNotFoundError:
        return "Error: We cannot open the file."