from prettytable import PrettyTable
import os
from collections import defaultdict

"""This class reads sensor data from iot files and generates tables to summarize the data"""
class SensorInfo:
    def __init__(self, directory):
        try:
            os.chdir(directory)
        except FileNotFoundError:
            raise NotADirectoryError ("Please provide a valid directory")
        self.sens_day_sum = PrettyTable(field_names= ["Sensor", "Day", "Count", "Avg", "Min", "Max", "Distinct"])
        self.sens_sum = PrettyTable(field_names= ["Sensor", "Count", "Avg", "Min", "Max", "Distinct"])
        self.list_of_iot_files = list()
        self.list_of_info = list()
        self.files_to_open()
        self.record_info_from_files(self.list_of_iot_files)
        self.generate_sens_pretty_tables()
        self.generate_sens_day_pretty_tables()

    def files_to_open(self):
        """This generates a list of the files that should be opened"""
        for file in os.listdir():
            if file.endswith(".iot"):
                self.list_of_iot_files.append(file)
        return None

    def record_info_from_files(self, files):
        """This method analyzes the information and adds it to the prettytables"""
        for file in files:
            read_file = self.read_files(file, 3, "This file does not contain the appropriate number of values")
            for sensor, day, value in read_file:
                self.list_of_info.append([sensor, day, value])
        return None

    def generate_sens_pretty_tables(self):
        """This method generates the total sensor summary"""
        sensor_table_info = defaultdict(list)
        test_list = list()
        for sensor, day, value in self.list_of_info:
            sensor_table_info[sensor].append(int(value))
        for sensor in sensor_table_info.keys():
            vals = sensor_table_info[sensor]
            self.sens_sum.add_row([sensor, len(vals), float("%.1f"%(sum(vals)/(len(vals)))), min(vals), max(vals), len(set(vals))])
            test_list.append([sensor, len(vals), float("%.1f"%(sum(vals)/(len(vals)))), min(vals), max(vals), len(set(vals))])
        print(self.sens_sum.get_string(sortby = "Sensor"))
        return (test_list)

    def generate_sens_day_pretty_tables(self):
        """This method generates the sensor day summary"""
        sensor_day_table_info = defaultdict(list)
        test_list = list()
        for sensor, day, value in self.list_of_info:
            sensor_day_table_info[(sensor, day)].append(int(value))
        days_in_order = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for sensor, day in sorted(sensor_day_table_info.keys(), key = lambda day:(day[0], days_in_order.index(day[1]))):
            vals = sensor_day_table_info[(sensor, day)]
            self.sens_day_sum.add_row([sensor, day, len(vals), float("%.1f"%(sum(vals)/(len(vals)))), min(vals), max(vals), len(set(vals))])
            test_list.append([sensor, day, len(vals), float("%.1f"%(sum(vals)/(len(vals)))), min(vals), max(vals), len(set(vals))])
        print(self.sens_day_sum)
        return (test_list)
    
    def read_files(self, file_name, expec_num_values, error_mess, seperator = "|"):
        """A generic read file generator to check bad file inputs and read line by line"""
        try:
            fp = open(file_name, 'r')
        except FileNotFoundError:
            raise FileNotFoundError ("Could not open {}".format(file_name))
        else:
            with fp:
                for line in fp:
                    l = line.strip().split(seperator)
                    if len(l) == expec_num_values:
                        yield l
                    else:
                        raise ValueError (error_mess)


def main():
    x = os.getcwd() 
    sensor = SensorInfo("Final Exam/IOT_test")
    os.chdir(x)
    sensor1 = SensorInfo("Final Exam/IOT") 

if __name__ == '__main__':
    main()