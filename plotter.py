
import matplotlib.pyplot as plt
from collections import defaultdict

def plot_schedule_copperative(task_timings):
    fig, ax = plt.subplots()

    # Get the unique core numbers, sorted numerically
    unique_cores = sorted(set(core for _, _, core, _ in task_timings))

    # Set the y-axis limits
    ax.set_ylim(0, len(unique_cores) + 1)
    
    # Use the unique core numbers as ticks and labels
    ax.set_yticks(range(1, len(unique_cores) + 1))
    ax.set_yticklabels([f'Core {core}' for core in unique_cores])

    # Set the x-axis limits
    ax.set_xlim(0, max(end_time for _, end_time, _, _ in task_timings))

    # Define a dictionary to store colors for each task name
    task_colors = defaultdict(lambda: plt.cm.get_cmap('tab10').colors[len(task_colors) % 10])

    # Plot each task
    for i, core in enumerate(unique_cores, start=1):
        tasks_for_core = [(start_time, end_time, task_name) for start_time, end_time, c, task_name in task_timings if c == core]
        for start_time, end_time, task_name in tasks_for_core:
            color = task_colors[task_name]
            ax.barh(i, end_time - start_time, left=start_time, color=color, edgecolor='black', label=task_name)

    # Set labels and legend
    ax.set_xlabel('Time')
    ax.set_title('Gantt Chart')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # Show the Gantt chart
    plt.show()
