#task1
def find_and_replace(lst, find_val, replace_val):
    for x in range(len(lst)):
        if lst[x] == find_val:
            lst[x] = replace_val
    return lst

#task2
lst = [1,2,3,4,2,2]
find_val = 2
replace_val = 5
result = find_and_replace(lst,find_val,replace_val)
print(result)

lst = ['apple','banana','apple']
find_val = 'apple'
replace_val = 'orange'
result = find_and_replace(lst,find_val,replace_val)
print(result)