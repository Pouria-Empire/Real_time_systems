from csv_parse import *

# Usage
csv_files_list = ['./csv/bfs.csv', './csv/dxtc.csv', './csv/hist.csv', './csv/hist2.csv', './csv/hotspot.csv', './csv/mmul.csv', './csv/mmul2.csv', './csv/stereodisparity.csv']


result_dict = parse_all_csv_files(csv_files_list)

# Accessing the result dictionary
for csv_file, tasks_array in result_dict.items():
    print(f"\nCSV File: {csv_file}")
    for row in tasks_array:
        print(row)