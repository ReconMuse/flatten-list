


def flatten_list(row):
    result = []
    for item in row:
        if isinstance(item, list):
            result.extend(flatten_list(item)) 
        else:
            result.append(item)
    return result
print(flatten_list([1, [2], [3, [4, 5, [6]]], 7]))
print(flatten_list([1, 2, [3], [4,5]]))



# FUNCTION flatten(list):

# for the items on the list:
#     if the item is a list
#     do __ with it
#     but if its _____
#     then do this with it
    
#kicker    