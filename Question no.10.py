# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# counter1 = 0
# while counter1 < len(big_list):
#     small_list_length = len(big_list[counter1])
#     counter2 = 0
#     while counter2 < small_list_length:
#         print (big_list[counter1][counter2])
#         counter2 = counter2 + 1
#     counter1 = counter1 + 1
#     print ('-----') 
# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# counter1 = 0
# while counter1 < len(big_list):
#     small_list_length = len(big_list[counter1])
#     counter2 = 0
#     while counter2 < small_list_length:
#         print (big_list[counter1][counter2])
#         counter2 = counter2 + 1
#     counter1 = counter1 + 1
#     print ('-----')

marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
i=0
while i<len(marks):
    j=0
    k=marks[i][j]
    while j<len(marks[i]):
        if marks[i][j]>k:
            k=marks[i][j]
        j=j+1
    i=i+1
    print(k)

# max=[[4,3,5,2,1],[7,5,8,4,3],[10,9,20,5,3]]
# i=0
# while i<len(max):
#     j=0
#     k=max[i][j]
#     while j <len(max[i]):
#         if max[i][j]>k:
#             k=max[i][j]
#         j=j+1
#     i=i+1
#     print(k)
