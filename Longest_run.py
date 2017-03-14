def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """

    higher_index = lower_index = 0
    max_index_higher = max_index_lower = 0
    max_increase= [L[0]]
    max_decrease= [L[0]]
    increasing = max_increase[:]
    decreasing = max_decrease[:]

    for n in range(len(L) -1):
        if L[n] <= (L[n + 1]):
            increasing.append(L[n + 1])
            if len(increasing) > len(max_increase):
                max_increase = increasing[:]
                max_index_higher = higher_index
        else:
            increasing = [L[n + 1]]
            higher_index = n + 1

        if L[n] >= L[n + 1]:
            decreasing.append(L[n + 1])
            if len(decreasing) > len(max_decrease):
                max_decrease = decreasing[:]
                max_index_lower = lower_index

            else:
                decreasing = [L[n + 1]]
                decreasing_index = n + 1
    if len(max_increase) > len(max_decrease):
        return sum(max_increase)
    elif len(max_increase) < len(max_decrease):
        return sum(max_decrease)
    else:
        return sum(max_increase
                   if max_index_higher < max_index_lower else
                   max_decrease)

'''
some test cases are below....
'''

L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
M = [5, 4, 10]
N = [4, 10]

print(longest_run(L))
print(longest_run(M))
print(longest_run(N))

