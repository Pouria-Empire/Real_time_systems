import matplotlib.pyplot as plt

def plot_schedule(result):
    # Assuming active_tasks is a list of timings for each task in the best schedule
    for i, task_timing in enumerate(result.active_tasks):
        task_name = f'Task {i+1}'
        plt.plot(task_timing, label=task_name)

    plt.xlabel('Cores')
    plt.ylabel('Execution Time')
    plt.title('Task Scheduling Timings')
    plt.legend()
    plt.show()