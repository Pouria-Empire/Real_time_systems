import matplotlib.pyplot as plt
import plotly.express as px

def plot_schedule_copperative(task_timings):
    fig, ax = plt.subplots()

    # Set the y-axis limits
    ax.set_ylim(0, len(set(core for _, _, core in task_timings)) + 1)
    ax.set_yticks(range(1, len(set(core for _, _, core in task_timings)) + 1))
    ax.set_yticklabels([f'Core {core}' for core in sorted(set(core for _, _, core in task_timings))])

    # Set the x-axis limits
    ax.set_xlim(0, max(end_time for _, end_time, _ in task_timings))

    # Define colors for each task
    colors = ['blue', 'green', 'orange', 'red', 'purple', 'brown', 'pink', 'gray']

    # Plot each task
    for i, (start_time, end_time, core) in enumerate(task_timings):
        ax.barh(core, end_time - start_time, left=start_time, color=colors[i % len(colors)], edgecolor='black')

    # Set labels
    ax.set_xlabel('Time')
    ax.set_title('Gantt Chart')

    # Show the Gantt chart
    plt.show()
