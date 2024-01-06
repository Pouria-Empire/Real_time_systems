
import matplotlib.pyplot as plt
from collections import defaultdict

def plot_schedule_copperative(task_timings):
    fig, ax = plt.subplots()

    # Set the y-axis limits
    ax.set_ylim(0, len(set(core for _, _, _, core in task_timings)) + 1)
    ax.set_yticks(range(1, len(set(core for _, _, _, core in task_timings)) + 1))
    ax.set_yticklabels([f'Core {core}' for core in sorted(set(core for _, _, _, core in task_timings))])

    # Set the x-axis limits
    ax.set_xlim(0, max(end_time for _, end_time, _, _ in task_timings))

    # Define a dictionary to store colors for each task name
    task_colors = defaultdict(lambda: plt.cm.get_cmap('tab10').colors[len(task_colors) % 10])

    # Plot each task
    for i, (start_time, end_time, core, task_name) in enumerate(task_timings):
        color = task_colors[task_name]
        ax.barh(core, end_time - start_time, left=start_time, color=color, edgecolor='black', label=task_name)

    # Set labels and legend
    ax.set_xlabel('Time')
    ax.set_title('Gantt Chart')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # Show the Gantt chart
    plt.show()

