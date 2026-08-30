def binary_serch(numbers, target):
    left = 0
    right = len(numbers)-1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        
        elif numbers[mid]<target:
            left = mid+1

        # middle is too small -> discard the left side and middle. 

        else:
            right = mid -1 

    return -1


numbers_list = [15,20,25,30,35,40,45,50]
target = 35

print(binary_serch(numbers_list, 37))