import time
import random 
import itertools

class TaskScheduler:
    def __init__(self, result_dict, num_cores, num_tasks):
        self.result_dict = result_dict
        self.num_cores = num_cores
        self.num_tasks = num_tasks
        self.tasks = self.generate_tasks(self.num_tasks)
        self.co_operative_result = Result()
        self.best_result = Result()

    def generate_tasks(self,num:int):
        space = ['bfs','dxtc','hist','hist2','hotspot','mmul','mmul2','stereodisparity']
        tasks = random.sample(space * (num // len(space) + 1), num)
        return tasks

    def process_task(self, task):
        return "khar"

    def cooperative_algorithm(self):
        start_time = 0
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
            end_time = start_time + self.result_dict[task][self.num_cores - 1][3]

            for core in range(1, self.num_cores + 1):
                self.co_operative_result.active_tasks.append((start_time, end_time, core,task))

            start_time = end_time

        return self.co_operative_result


    
    def best_algorithm(self):
            # Initialize the best result with a large value
        best_makespan = float('inf')

        for task in self.tasks:
            for cores_combination in itertools.combinations_with_replacement(range(1, self.num_cores + 1), self.num_tasks):
                temp_schedule = [[] for _ in range(self.num_cores)]
                temp_result = Result()

                for core, execution_data in zip(cores_combination, self.result_dict[task]):
                    earliest_core = min(range(core), key=lambda c: sum(map(lambda t: t[3], temp_schedule[c])))

                    start_time = sum(map(lambda t: t[1], temp_schedule[earliest_core]))
                    end_time = start_time + execution_data[1]

                    temp_schedule[earliest_core].append((start_time, end_time, execution_data[3], core))
                    temp_result.avg_time += execution_data[1]
                    temp_result.min_time += execution_data[2]
                    temp_result.max_time += execution_data[3]
                    temp_result.energy += execution_data[5]
                    temp_result.active_tasks.append((start_time, end_time, core))

                # Calculate makespan for the current configuration
                current_makespan = max(map(lambda c: sum(map(lambda t: self.result_dict[task][c][3], temp_schedule[c])), range(self.num_cores)))

                # Update the best result if the current configuration has a smaller makespan
                if current_makespan < best_makespan:
                    best_makespan = current_makespan
                    self.best_result = temp_result

        print(f"\nBest Algorithm Result - Makespan: {best_makespan:.2f}s")
        print(f"Avg Time: {self.best_result.avg_time:.2f}s, Min Time: {self.best_result.min_time:.2f}s, Max Time: {self.best_result.max_time:.2f}s")
        print(f"Total Energy: {self.best_result.energy:.2f}, Active Tasks Order: {self.best_result.active_tasks}")
        return self.best_result





def profile_algorithm(self):
    profiles = self.calculate_profile()
    x = 1
    
    
    

def calculate_profile(self):
    result = [[0 for _ in range(6)] for _ in range(self.num_tasks)]
    for i in range(self.num_tasks):
        for j in range(6):
            result[i][j] = self.result_dict[self.tasks[i]][0][1] / self.result_dict[self.tasks[i]][j][1]
    
    return result

                
                




class Result:

    def __init__(self):
        self.min_time = 0
        self.avg_time = 0
        self.max_time = 0
        self.energy = 0
        self.active_tasks = []