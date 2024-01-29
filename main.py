from csv_parse import *
from scheduler import *
from plotter import *
import matplotlib.pyplot as plt
import time


# Usage
csv_files_list = ['./csv/bfs.csv', './csv/dxtc.csv', './csv/hist.csv', './csv/hist2.csv', './csv/hotspot.csv', './csv/mmul.csv', './csv/mmul2.csv', './csv/stereodisparity.csv']

def draw_plots(result_dict):
    
    number_cores = 6
    tasks_list = [2, 4, 6, 8, 10, 12]

    normalized_makespan_cooperative_list = []
    normalized_makespan_best_list = []
    normalized_makespan_profile_list = []
    energy_list = []
    execution_times_cooperative = []
    execution_times_best = []
    execution_times_profile = []
    
    for number_tasks in tasks_list:
        Core.id = 1
        scheduler = TaskScheduler(result_dict, number_cores, number_tasks)
        start_time = time.time()
        result_cooperative, makespan_cooperative = scheduler.cooperative_algorithm()
        end_time = time.time()
        execution_times_cooperative.append(end_time - start_time)


        start_time = time.time()
        result_best, makespan_best = scheduler.best_algorithm()
        end_time = time.time()
        execution_times_best.append(end_time - start_time)



        start_time = time.time()
        result_cores, makespan_profile = scheduler.profile_algorithm()
        end_time = time.time()
        execution_times_profile.append(end_time - start_time)

        # Divide makespans by makespan_cooperative
        normalized_makespan_cooperative = makespan_cooperative / makespan_cooperative
        normalized_makespan_best = makespan_best / makespan_cooperative
        normalized_makespan_profile = makespan_profile / makespan_cooperative

        normalized_makespan_cooperative_list.append(normalized_makespan_cooperative)
        normalized_makespan_best_list.append(normalized_makespan_best)
        normalized_makespan_profile_list.append(normalized_makespan_profile)

        # Energy consumption
        energy_list.append([result_cooperative.energy, result_best.energy, scheduler.profile_algorithm_result.energy])

    # Measure execution time for each algorithm


    # for _ in range(number_tasks):
    #     start_time = time.time()
    #     # Execute Cooperative Algorithm
    #     scheduler.cooperative_algorithm()
    #     end_time = time.time()
    #     execution_times_cooperative.append(end_time - start_time)



    #     start_time = time.time()
    #     # Execute Best Algorithm
    #     scheduler.best_algorithm()
    #     end_time = time.time()
    #     execution_times_best.append(end_time - start_time)


    #     start_time = time.time()
    #     # Execute Profile Algorithm
    #     scheduler.profile_algorithm()
    #     end_time = time.time()
    #     execution_times_profile.append(end_time - start_time)

    #     # execution_times_cooperative_list.append(execution_times_cooperative)
    #     # execution_times_best_list.append(execution_times_best)
    #     # execution_times_profile_list.append(execution_times_profile)

    # Plotting
    plt.figure(figsize=(10, 6))

    # Makespans per task with different colors
    draw_makespan(tasks_list, normalized_makespan_cooperative_list, normalized_makespan_best_list, normalized_makespan_profile_list)

    # Energy consumption per task with different colors
    draw_energy(tasks_list, energy_list)

    # Execution time per task with different colors for each algorithm
    draw_execution_time(tasks_list, execution_times_cooperative, execution_times_best, execution_times_profile)


def draw_execution_time(tasks_list, execution_times_cooperative_list, execution_times_best_list, execution_times_profile_list):
    # for i, tasks in enumerate(tasks_list):
    #     plt.plot(range(1, number_tasks + 1), execution_times_cooperative_list[i], marker='o', label=f'Cooperative - Tasks={tasks}')
    #     plt.plot(range(1, number_tasks + 1), execution_times_best_list[i], marker='o', label=f'Best - Tasks={tasks}')
    #     plt.plot(range(1, number_tasks + 1), execution_times_profile_list[i], marker='o', label=f'Profile - Tasks={tasks}')

    plt.plot(tasks_list, execution_times_cooperative_list, label='Co-operative', marker='o')
    plt.plot(tasks_list, execution_times_best_list, label='Best', marker='o')
    plt.plot(tasks_list, execution_times_profile_list, label='Profile', marker='o')

    plt.title('Execution Time per Task')
    plt.xlabel('Task Index')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

def draw_energy(tasks_list, energy_list):
    plt.plot(tasks_list, [l[0] for l in energy_list], 'o-', color='blue', label='Cooperative')
    plt.plot(tasks_list, [l[1] for l in energy_list], 'o-', color='orange', label='Best')
    plt.plot(tasks_list, [l[2] for l in energy_list], 'o-', color='green', label='Profile')

    plt.title('Energy Consumption per Task')
    plt.xlabel('Number of Tasks')
    plt.ylabel('Energy Consumption')
    plt.legend()
    plt.grid(True)
    plt.show()

def draw_makespan(tasks_list, normalized_makespan_cooperative_list, normalized_makespan_best_list, normalized_makespan_profile_list):
    plt.plot(tasks_list, normalized_makespan_cooperative_list, label='Co-operative', marker='o')
    plt.plot(tasks_list, normalized_makespan_best_list, label='Best', marker='o')
    plt.plot(tasks_list, normalized_makespan_profile_list, label='Profile', marker='o')
    
    plt.title('Normalized Makespans per Task')
    plt.xlabel('Number of Tasks')
    plt.ylabel('Normalized Makespan')
    plt.legend()
    plt.grid(True)
    plt.show()




if __name__ == "__main__":
    result_dict = parse_all_csv_files(csv_files_list)
    # Draw  all plots
    draw_plots(result_dict)

    # number_cores = 4
    # number_tasks = 5
    # scheduler = TaskScheduler(result_dict, number_cores,number_tasks)

    # # s_matrix = scheduler.generate_S_matrix(number_tasks, number_cores)

    # result_cooperative,makespan_cooperative = scheduler.cooperative_algorithm()
    # result_best,makespan_best = scheduler.best_algorithm()
    # cores,result_cores,makespan_profile = scheduler.profile_algorithm()

    # plot_schedule_copperative(result_cores.active_tasks)
    # plot_schedule_copperative(result_cooperative.active_tasks)
    # plot_schedule_copperative(result_best.active_tasks)

    # print(f'makespan is : {scheduler.profile_algorithm_result.avg_time} and energy is : {scheduler.profile_algorithm_result.energy}')