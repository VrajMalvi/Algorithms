def minimumWaitingTime(queries):
    # O(nlogn - cus we are using sort) | O(1)
    queries.sort()
    time=0
    sum_of_time = 0
    for i in range(len(queries) -1):
        time += queries[i]
        sum_of_time += time

    return (sum_of_time)