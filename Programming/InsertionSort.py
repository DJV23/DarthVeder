# InsertionSort.py
# Author
# Version 0.1
# 5 dec 2017
# Python implementaion of insertion InsertionSort

this_file = open('RandomNumbers.txt')

list_to_sort = []

for line in this_file:
    list_to_sort.append(int(line))

this_file.close()

print(list_to_sort)

def insertion_sort(this_list):
    for key_pos in range(1, len(this_list)):

        key_val = this_list[key_pos]


        scan_position = key_pos - 1


        while (scan_position >= 0) and (this_list[scan_position]) > key_val):
            this_list[scan_position + 1] = this_list[scan_position]
            scan_position = scan_position - 1

        this_list[scan_position + 1] = key_val


insertion_sort(list_to_sort)

print(list_to_sort)
