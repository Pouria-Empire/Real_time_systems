import time
import random 
import itertools
import matplotlib.pyplot as plt
import math
from helper import *

class TaskScheduler:
    def __init__(self, result_dict, num_cores, num_tasks):
        self.result_dict = result_dict
        self.num_cores = num_cores
        self.num_tasks = num_tasks
        self.tasks = self.generate_tasks(self.num_tasks)
        self.co_operative_result = Result()
        self.best_result = Result()
        self.profile_algorithm_result = Result()

    def generate_tasks(self,num:int):
        space = ['bfs','dxtc','hist','hist2','hotspot','mmul','mmul2','stereodisparity']
        tasks = random.sample(space * (num // len(space) + 1), num)
        return tasks

    def cooperative_algorithm(self):
        start_time = 0
        # cores = [Core() for _ in range(self.num_cores)]
        for task in self.tasks:
            # Find avg time
            self.co_operative_result.avg_time += self.result_dict[task][self.num_cores - 1][1]
            # Find min time
            self.co_operative_result.min_time += self.result_dict[task][self.num_cores - 1][2]
            # Find max time
            self.co_operative_result.max_time += self.result_dict[task][self.num_cores - 1][3]
            # Find total energy
            self.co_operative_result.energy += self.result_dict[task][self.num_cores - 1][5]
            # Find order of tasks
            end_time = start_time + self.result_dict[task][self.num_cores - 1][1]

            # for core in range(1, self.num_cores + 1):
            #     self.co_operative_result.active_tasks.append((start_time, end_time, core,task))

            # for core in cores:
            #     core.tasks.append((start_time, end_time, task))
            
            start_time = end_time

        # plot(cores)


        return self.co_operative_result,end_time


    
    def best_algorithm(self):
        # Initialize the best result with a large value
        best_makespan = float('inf')

        for cores_combination in itertools.combinations_with_replacement(range(1, self.num_cores + 1), self.num_tasks):
            temp_schedule = [[] for _ in range(self.num_cores)]
            temp_result = Result()

            for core, task in zip(cores_combination, self.result_dict):
                for index in range(core):
                    earliest_core = min(range(self.num_cores), key=lambda c: sum(map(lambda t: t[2], temp_schedule[c])))

                    start_time = sum(map(lambda t: t[1], temp_schedule[earliest_core]))
                    end_time = start_time + self.result_dict[task][core-1][3]

                    temp_schedule[earliest_core].append((start_time, end_time, self.result_dict[task][core-1][3], core))
                    if core == 7:
                        x = 1
                    self.save_result(temp_result, core, task, earliest_core, start_time, end_time)

            # Calculate makespan for the current configuration
            current_makespan = max(end_time for core_schedule in temp_schedule for (_, end_time, _, _) in core_schedule)

            # Update the best result if the current configuration has a smaller makespan
            if current_makespan < best_makespan:
                best_makespan = current_makespan
                self.best_result = temp_result

        print(f"\nBest Algorithm Result - Makespan: {best_makespan:.2f}s")
        print(f"Avg Time: {self.best_result.avg_time:.2f}s, Min Time: {self.best_result.min_time:.2f}s, Max Time: {self.best_result.max_time:.2f}s")
        print(f"Total Energy: {self.best_result.energy:.2f}, Active Tasks Order: {self.best_result.active_tasks}")
        return self.best_result,best_makespan

    def save_result(self, temp_result, core, task, earliest_core, start_time, end_time):
        temp_result.avg_time += self.result_dict[task][core-1][1]
        temp_result.min_time += self.result_dict[task][core-1][2]
        temp_result.max_time += self.result_dict[task][core-1][3]
        temp_result.energy += self.result_dict[task][core-1][5]
        temp_result.active_tasks.append((start_time, end_time, earliest_core, task))






    def profile_algorithm(self):
        # for i in self.result_dict:
        #     print(self.result_dict[i])
            
        #TODO we must update profiles acoording to remaining tasks
        #TODO there is a bug, this code must calculate Num tasks not cores
        
        temp_result = Result()
        profiles = self.calculate_profile(self.num_cores)
        
        cores = [Core() for _ in range(self.num_cores)]

        time = 0
        
        while(profiles):
            
            for core in cores:
                if core.next_idle_time <= time:
                    core.is_active = False
                    print(f'core with id {core.id} was released at {time}')
                    
            idle_cores = [core for core in cores if core.is_active == False]
            

            #must have task name and core count and min_time
            current_tasks = self.find_tasks(len(idle_cores), profiles)
            
            
            while(len(idle_cores) > 0 and current_tasks):
                for i in current_tasks:
                    self.profile_algorithm_result.energy += self.result_dict[i[1]][i[0] - 1][5]
                    for j in range(i[0]):
                        idle_cores[0].is_active = True
                        idle_cores[0].next_idle_time = time + self.result_dict[i[1]][i[0] - 1][1]
                        idle_cores[0].tasks.append((time, idle_cores[0].next_idle_time, i[1]))
                        print(f'core with id {idle_cores[0].id} is running task {i[1]}, starting time {time}')
                        
                        idle_cores.pop(0)
                    
                    current_tasks.remove(i)
            
            true_objects = [core for core in cores if core.is_active]

            # Find the object with the minimum value among the True objects
            min_value_object = min(true_objects, key=lambda obj: obj.next_idle_time)
                    
                        
            time = min_value_object.next_idle_time
            # profiles = self.calculate_profile()


        #update time one final time
        true_objects = [core for core in cores if core.is_active]

        # Find the object with the minimum value among the True objects
        max_value_object = max(true_objects, key=lambda obj: obj.next_idle_time)
                    
                        
        time = max_value_object.next_idle_time

        makespan = time
        self.profile_algorithm_result.avg_time = makespan
        
        plot(cores)
        
        return cores,makespan
        
        
    def find_tasks(self, core_count, profiles):
        result = []
        if(core_count <= len(profiles)):
            while(core_count > 0 and profiles):

                core_count -= 1
                result.append((1, profiles[0][0]))
                profiles.pop(0)
        else:

            max_gain = 0
            
            for i in range(7 ** len(profiles)):
                num_cores = 0
                gain = 0
                for j in range(len(profiles)):
                    
                    num_cores += int(i / (7 ** j)) % 7
                    current_core = int(i / (7 ** j)) % 7
                    print(i)
                    print(num_cores)
                    if current_core > 0:
                        gain += profiles[j][current_core]
                    
                if(num_cores <= core_count and gain > max_gain):
                    result = []
                    max_gain = gain
                    for j in range(len(profiles)):
                    
                        cores = int(i / (7 ** j)) % 7
                    
                        if cores > 0:
                            result.append((cores, profiles[j][0]))
                
            
            for i in result:
                for j in range(len(profiles)):
                    profiles[j][0] == i[1]
                    profiles.pop(j)
                    break    
                
            
        return result
        
    
    

    def calculate_profile(self, N):
        result = [[0 for _ in range(7)] for _ in range(self.num_tasks)]
        for i in range(self.num_tasks):
            result[i][0] = self.tasks[i]
            result[i][1] = 1.0
            for j in range(2,7):
                result[i][j] = ((self.result_dict[self.tasks[i]][0][1] / self.result_dict[self.tasks[i]][j - 1][1]) ** (1/N))
        
        
        
        return result

                
                
    



class Result:

    def __init__(self):
        self.min_time = 0
        self.avg_time = 0
        self.max_time = 0
        self.energy = 0
        self.active_tasks = []


class Core:
    
    id = 1
    
    def __init__(self):
        self.next_idle_time = 0
        self.is_active = False
        self.tasks = []
        self.id = Core.id
        Core.id += 1
        
        

        



def plot(cores):
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
    
    
    
def knapsack(W, V, capacity):
    n = len(W)
    
    # Initialize a 2D list to store the maximum values for each subproblem
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if W[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], V[i - 1] + dp[i - 1][w - W[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the selected items
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= W[i - 1]
        i -= 1

    selected_items.reverse()
    
    # Return the maximum value and the selected items
    return dp[n][capacity], selected_items