
import matplotlib.pyplot as plt
from collections import defaultdict

def plot_schedule_copperative(task_timings):
    fig, ax = plt.subplots(figsize=(30, 6))

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


def plot_energy_vs_tasks(self, max_tasks,generate_tasks,cooperative_algorithm):
    task_range = range(10, max_tasks + 1, 15)
    energy_values = []

    for num_tasks in task_range:
        num_tasks = num_tasks
        tasks = generate_tasks(self.num_tasks)

        cooperative_algorithm()
        energy_values.append(self.co_operative_result.energy)
    
    plt.plot(task_range, energy_values, marker='o')
    plt.xlabel('Number of Tasks')
    plt.ylabel('Energy')
    plt.title('Energy vs Number of Tasks')
    plt.show()




def plot_cores(cores):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Extract unique core labels
    core_labels = set(("Core " + str(core.id)) for core in cores)

    # Set ticks on the Y-axis and label them with unique core labels
    ax.set_yticks(range(len(core_labels)))
    ax.set_yticklabels(core_labels)

    for core in cores:
        # Plot the time segments for each entry
        for entry in core.tasks:
            start_point = entry[0]
            end_point = entry[1]
            entry_name = entry[2]
            core_label = "Core " + str(core.id)

            # Find the index of the core label for positioning on the Y-axis
            core_index = list(core_labels).index(core_label)

            # Draw a horizontal bar for each time segment
            ax.barh(y=core_index, width=end_point - start_point, left=start_point, label=entry_name)
            segment_center = start_point + (end_point - start_point) / 2
            ax.text(segment_center, core_index, entry_name, ha="center", va="center", color="white")

    # Set labels and legend
    ax.set_xlabel("Time")
    ax.set_title("Time Segments Labeled as 'CORE' on Y-axis")
    ax.legend()

    # Show the plot
    plt.show()