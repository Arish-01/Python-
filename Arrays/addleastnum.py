num=[19, 5, 42, 2, 77]
def sum_two_smallest_numbers(num):
    num.sort()
    print(num[0]+num[1])

sum_two_smallest_numbers(num)