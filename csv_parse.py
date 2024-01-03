import csv

class Task:
    def __init__(self, sm, average_time, min_time, max_time, power, energy, energy_in_window):
        self.sm = int(sm)
        self.average_time = float(average_time)
        self.min_time = float(min_time)
        self.max_time = float(max_time)
        self.power = float(power)
        self.energy = float(energy)
        self.energy_in_window = float(energy_in_window)

def parse_csv_to_array(csv_file):
    tasks_array = []

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row

        for row in csv_reader:
            if len(row) == 7:  # Ensure there are 7 columns in each row
                task = Task(*row)
                tasks_array.append([task.sm, task.average_time, task.min_time, task.max_time, task.power, task.energy, task.energy_in_window])

    return tasks_array

def parse_all_csv_files(csv_files):
    result_dict = {}

    for csv_file in csv_files:
        tasks_array = parse_csv_to_array(csv_file)
        result_dict[csv_file.split("/")[-1].split(".")[0]] = tasks_array

    return result_dict