def shrink_list(list):
    for i in range(1, len(list)):
        if list[i] != 0:
            j = i
            while (j > 0):
                if list[j-1] == 0:
                    list[j-1] = list[j]
                    list[j] = 0
                    j-=1
                else:
                    break
                
list = [4, 0, 5, 0, 3, 0, 0, 5]
shrink_list(list)
print(list)