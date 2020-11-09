
def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) -1
    
    while begin_index <= end_index:
        midpoint_index = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint_index]
        if midpoint_value == item:
            return midpoint_index
        elif item < midpoint_value:
            end_index = midpoint_index - 1
        else:
            begin_index = midpoint_index + 1
    return None

sequence_a = [1,3,69,45,66,95,2,7,88,666]
item_a = 95

print(binary_search(sequence_a, item_a))