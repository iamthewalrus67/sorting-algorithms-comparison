from sorting_algorithms import *
import random
import time
from copy import deepcopy
import matplotlib.pyplot as plt

def test_algorithms_1(algorithms):
    algorithms_time_list = []
    algorithms_comparisons_list = []

    for k in range(7, 16):
        time_list = [0 for _ in range(len(algorithms))]
        comparisons_list = [0 for _ in range(len(algorithms))]
        # 5 experiments
        for _ in range(5):
            arr = [random.randint(0, 1000) for _ in range(2**(k))]
            # Iterate through all algorithms to test their efficiency on equal arrays
            for i, algorithm in enumerate(algorithms):
                start = time.time()
                
                # Make a deepcopy of an array so the original won't get sorted
                comparisons = algorithm(deepcopy(arr))

                end = time.time()
                time_list[i] = (time_list[i]+(end - start))
                comparisons_list[i] += comparisons
        # Get average value of time taken to sort an array and comparisons made
        time_list = [time_list[x]/5 for x in range(len(time_list))]
        comparisons_list = [comparisons_list[x]//5 for x in range(len(comparisons_list))]
        algorithms_time_list.append(time_list)
        algorithms_comparisons_list.append(comparisons_list)
    return algorithms_time_list, algorithms_comparisons_list


def test_algorithms_2(algorithms):
    algorithms_time_list = []
    algorithms_comparisons_list = []
    for k in range(7, 16):
        time_list = [0 for _ in range(len(algorithms))]
        comparisons_list = [0 for _ in range(len(algorithms))]
        for j in range(1, 6):
            arr = sorted([random.randint(0, 1000) for _ in range(2**(k))])
            for i, algorithm in enumerate(algorithms):
                start = time.time()
                
                comparisons = algorithm(deepcopy(arr))

                end = time.time()
                time_list[i] = (time_list[i]+(end - start))
                comparisons_list[i] += comparisons
        time_list = [time_list[x]/5 for x in range(len(time_list))]
        comparisons_list = [comparisons_list[x]//5 for x in range(len(comparisons_list))]
        algorithms_time_list.append(time_list)
        algorithms_comparisons_list.append(comparisons_list)
    return algorithms_time_list, algorithms_comparisons_list


def test_algorithms_3(algorithms):
    algorithms_time_list = []
    algorithms_comparisons_list = []
    for k in range(7, 16):
        time_list = [0 for _ in range(len(algorithms))]
        comparisons_list = [0 for _ in range(len(algorithms))]
        for j in range(1, 6):
            arr = sorted([random.randint(0, 1000) for _ in range(2**(k))], reverse=True)
            for i, algorithm in enumerate(algorithms):
                start = time.time()
                
                comparisons = algorithm(deepcopy(arr))

                end = time.time()
                time_list[i] = (time_list[i]+(end - start))
                comparisons_list[i] += comparisons
        time_list = [time_list[x]/5 for x in range(len(time_list))]
        comparisons_list = [comparisons_list[x]//5 for x in range(len(comparisons_list))]
        algorithms_time_list.append(time_list)
        algorithms_comparisons_list.append(comparisons_list)
    return algorithms_time_list, algorithms_comparisons_list


def test_algorithms_4(algorithms):
    algorithms_time_list = []
    algorithms_comparisons_list = []
    for k in range(7, 16):
        time_list = [0 for _ in range(len(algorithms))]
        comparisons_list = [0 for _ in range(len(algorithms))]
        arr = [random.randint(0, 1000) for _ in range(2**(k))]
        for j in range(1, 4):
            random.shuffle(arr)
            for i, algorithm in enumerate(algorithms):
                start = time.time()
                
                comparisons = algorithm(deepcopy(arr))

                end = time.time()
                time_list[i] = (time_list[i]+(end - start))
                comparisons_list[i] += comparisons
        time_list = [time_list[x]/3 for x in range(len(time_list))]
        comparisons_list = [comparisons_list[x]//3 for x in range(len(comparisons_list))]
        algorithms_time_list.append(time_list)
        algorithms_comparisons_list.append(comparisons_list)
    print(algorithms_time_list)
    return algorithms_time_list, algorithms_comparisons_list
        

def plot_test(test_num: int):
    algorithms = [merge_sort, shell_sort, insertion_sort, selection_sort]
    tests = [test_algorithms_1, test_algorithms_2, test_algorithms_3, test_algorithms_4]
    time_list, comparisons_list = tests[test_num-1](algorithms)

    print(comparisons_list)

    fig, ax = plt.subplots(1, 2)
    for j in range(len(algorithms)):
        ax[1].plot([2**i for i in range(7, 7+len(time_list))], [time_list[i][j] for i in range(len(time_list))], label=algorithms[j].__name__)
        ax[0].plot([2**i for i in range(7, 7+len(comparisons_list))], [comparisons_list[i][j] for i in range(len(comparisons_list))], label=algorithms[j].__name__)
    
    ax[1].set_ylabel('Average sorting time')
    ax[0].set_ylabel('Number of comparisons')
    for a in ax:
        a.set_yscale('log')
        a.set_xscale('log', base=2)
        a.set_xlabel('Array size')
        a.legend()
        a.grid()
    plt.show()



if __name__ == '__main__':
    plot_test(1)