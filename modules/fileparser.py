# We are shifting to a more object-oriented approach
# Remove the direct dependency with stats_utils [Done]
# Introduce SwimDataFile class

# from modules import stats_utils # -- analytics engine
class SwimDataFile:
    
    def __init__(self, folder, filename):
        self.__filepath = folder + filename
        self.filename = filename
        self.__raw_data_lines = []

    def extract_swimmer(self):
        # Do you remember the code below from Notebook 3 (strings)?
        filename_without_extension = self.filename.removesuffix(".txt")
        name, age, stroke, distance = filename_without_extension.split("-")
        return name, age, stroke, distance

    def extract_swimdata(self):
        with open(self.__filepath) as file:
            self.__raw_data_lines = file.readlines()

        lines = self.__raw_data_lines[0].split(',')
        times = []
        for convert in lines:
            # Please make the following line work
            converted = convert_str_time_to_hundredths(convert)
            # Convert needs to be replaced with converted in the future
            times.append(converted)


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
        # average = stats_utils.mean(times) -- analytics engine

        # average_str = convert_time_to_str_format(average) -- analytics engine

        filename = filepath
        # check if filename needs to be cleaned from folders
        # e.g. swimdata/Abi-10-50m-Back.txt ---> Abi-10-50m-Back
        if "/" in filename:
            filename = filename.split("/")[-1]
        name, age, distance, stroke = filename.removesuffix(".txt").split("-")

        return name, age, distance, stroke, times # average_str -- analytics engine
    except FileNotFoundError:
        return "Error: We cannot open the file."