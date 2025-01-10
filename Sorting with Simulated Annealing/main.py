import random
import math
from tqdm import tqdm

def cost(c):
    cost = 0
    for i in range(len(c)-1):
        cost += c[i+1] - c[i]
    return cost

def swap_elements(lst):
    i, j = random.sample(range(len(lst)), 2)
    lst[i], lst[j] = lst[j], lst[i]

def sa_sort(input_list, initial_temp=100, cooling_rate=0.99, max_iter=10000000):
    current_state = input_list.copy()
    current_cost = cost(current_state)
    best_state = current_state.copy()
    best_cost = current_cost
    temp = initial_temp
    for iteration in tqdm(range(max_iter)):
        new_state = current_state.copy()
        swap_elements(new_state)
        new_cost = cost(new_state)
        delta_cost = new_cost - current_cost
        if delta_cost < 0 or random.random() < math.exp(-delta_cost / temp):
            current_state = new_state
            current_cost = new_cost
            if current_cost < best_cost:
                best_state = current_state.copy()
                best_cost = current_cost
        temp *= cooling_rate    
    return best_state

input_list = [2, 2, -6, 7]
sorted_list = sa_sort(input_list)
print("Sorted list:", sorted_list)
