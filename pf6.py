def find_first_negative(lst):
    first_negative = 0
    while first_negative < len(lst):
        if lst[first_negative] <0:
            return lst[first_negative]
        first_negative += 1
    return 'No Negative'

print(find_first_negative([3, 5, -1, 7, -2, 8]))

print(find_first_negative([2, 10, 7, 0]))