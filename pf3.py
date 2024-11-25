#Task 1
def update_dictionary(dct, key, value):
    if key in dct:
        print(f'Original value of {key}: {dct[key]}')
    dct[key] = value
    print(dct)

#Task 2
dct = {}
key = ('name')
value = ('Alice')
update_dictionary(dct,key,value)

dct = {'age' : 25}
key = ('age')
value = 26
update_dictionary(dct,key,value)