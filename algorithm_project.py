from itertools import combinations
import time
import math


def naive_process_selection(processes, time_limit):
    # (process_id, duration, value)

    start_time = time.time()

    max_value, best_duration = 0,0
    best_combination = []
        
    # All possible combinations
    for r in range(1, len(processes) + 1):
        for combo in combinations(processes, r):
            total_time = sum([process[1] for process in combo])
            total_value = sum([process[2] for process in combo])
            
            # Check if combo is within the time limit and has a higher value
            if total_time <= time_limit and total_value > max_value:
                max_value = total_value
                best_combination = [process[0] for process in combo]
                best_duration = total_time
    
    end_time = time.time()
    running_time_ms = int((end_time - start_time) * 1000)  # Convert to milliseconds
    
    result = {
        "Solution 1 - Naive": "",
        "Selected processes": best_combination,
        "Total value": max_value,
        "Total duration": best_duration,
        "Running time (ms)": running_time_ms
    }
    
    return result

def greedy_process_selection(processes, time_limit):

    start_time = time.time()
    # Sort processes in descending order with respect to value-to-time ratio (density)
    sorted_processes = sorted(processes, key=lambda x: x[2]/x[1], reverse=True)

    total_value, total_duration = 0, 0
    selected_processes = []

    
    for process in sorted_processes:
        process_id, duration, value = process
        if total_duration + duration <= time_limit:
            selected_processes.append(process_id)
            total_value += value
            total_duration += duration
        else:
            # If the current process exceeds the time limit, skip it
            continue
    
    end_time = time.time()
    running_time_ms = int((end_time - start_time) * 1000)  # Convert to milliseconds
    result = {
        "Solution 2 - Greedy choice ": "Largest density first (value/duration)",
        "Selected processes": selected_processes,
        "Total value": total_value,
        "Total duration": total_duration,
        "Running time (ms)": running_time_ms
    }

    return result

def modified_greedy_process_selection(processes, time_limit):

    start_time = time.time()

    # Sort processes based on modified value-to-time ratio (High Value with Lower Duration by giving more weight to the value.)  value/sqrt(duration)
    sorted_processes = sorted(processes, key=lambda x: x[2] / math.sqrt(x[1]), reverse=True)
    
    total_value, total_duration = 0, 0
    selected_processes = []
    
    for process in sorted_processes:
        process_id, duration, value = process
        if total_duration + duration <= time_limit:
            selected_processes.append(process_id)
            total_value += value
            total_duration += duration
        else:
            # If the current process exceeds the time limit, skip it
            continue
    
    end_time = time.time()
    running_time_ms = int((end_time - start_time) * 1000)  # Convert to milliseconds

    result = {
        "Solution 3 - Greedy choice ": "Largest density first (value/sqrt(duration))",
        "Selected processes": selected_processes,
        "Total value": total_value,
        "Total duration": total_duration,
        "Running time (ms)": running_time_ms
    }

    return result

def main():
    process_data = input("Enter processes P: ").replace(' ', ',').split(',')
    time_limit = int(input("Enter time limit T: "))
    print()

    processes = []
    for i in range(0, len(process_data), 3):
        process_id = int(process_data[i])
        duration = int(process_data[i+1])
        value = int(process_data[i+2])
        processes.append((process_id, duration, value))

    # Run the algorithms
    naive = naive_process_selection(processes, time_limit)
    greedy = greedy_process_selection(processes, time_limit)
    modified_greedy = modified_greedy_process_selection(processes, time_limit)

    algorithms = [naive, greedy, modified_greedy]
    
    for algorithm in algorithms:
        for k,v in algorithm.items():
            print(f"{k}: {v}")
        print()
main()

