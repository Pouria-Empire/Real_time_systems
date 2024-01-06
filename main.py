from csv_parse import *
from scheduler import *
from plotter import *
# Usage
csv_files_list = ['./csv/bfs.csv', './csv/dxtc.csv', './csv/hist.csv', './csv/hist2.csv', './csv/hotspot.csv', './csv/mmul.csv', './csv/mmul2.csv', './csv/stereodisparity.csv']


if __name__ == "__main__":
    result_dict = parse_all_csv_files(csv_files_list)
    number_cores = 4
    number_tasks = 4
    scheduler = TaskScheduler(result_dict, number_cores,number_tasks)
    # result_best = scheduler.cooperative_algorithm()
    result_best = scheduler.best_algorithm()
    plot_schedule_copperative(result_best.active_tasks)
    x = 1 

