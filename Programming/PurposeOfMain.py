#
#
#
#
#
#
#
Black = (0, 0, 0)
White = (255, 255, 255)

def average(list_of_nums):
    sum = 0

    for num in list_of_nums:
        sum += num
    return sum / len(list_of_nums)

def main():
    '''
    All the code that you excecute
    will exist inside this main function
    '''
    print(average([10, 11, 12, 13, 14, 15, 16]))

if __name__ == "__main__":
    main()
