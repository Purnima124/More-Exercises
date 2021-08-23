list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
i=0
c=[]
while i<len(list1):
    b=list1[i]
    if b in list2:
        c.append(b)
    i=i+1
print(c)






# def  number_lessthan100(list1):
#     counter=0
#     while counter<len(list1):
#         item=list1[counter]
#         if item >100:
#             list1.remove(item)
#         else:
#             counter+=1
#     return list1
# list1 = [1,342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1] 
# print("Intial list",list1)
# print ("List that doesn't contain numbers less than 342", list2) 
# # list2 = ("numbers_less_than_twenty",list2)


# def numbers_less_than_twenty(list):
#   counter = 0
#   while counter < len(list):
#     item = list[counter]
#     if item > 20:
#       list.remove(item)
#     else:
#       counter +=1
#   return list

# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

# num_list_sub_20 = numbers_less_than_twenty(num_list)

# print ("Initial list", num_list)
# print ("List that doesn't contain numbers greate than 20", num_list_sub_20) 
# from random import randint

# def win():
#     print ('You win!')

# def lose():
#     print ('You lose!')

# while False:
#     player_choice = input('What do you pick? (rock, paper, scissors)')
#     player_choice.strip()
#     random_move = randint(0, 2)
#     moves = ['rock', 'paper', 'scissors']
#     computer_choice = option[random_move]
#     if player_choice == "computer_choice":
#         print ('Draw!')
#     elif  == 'rock' and coMp == 'scissors':
#         win()
#     elif  == 'paper' and comp == 'scissors':
#         lose()
#     elif playe == 'scissors' and comp == 'paper':
#         win()
#     elif player == 'scissors' and Comp == 'rock':
#         lose()
#     elif payer == 'paper' and computer == 'rock':
#         win()
#     elif player ==  and comp == :
#         lose()
#     aGain = input('Do you want to play again? (y or n)').strip()
#     if again == 'n':
#         break 
# list1=[1, 342, 75, 23, 98]
# list2= [75, 23, 98, 12, 78, 10, 1] 
# i=0
# b=[]
# while i<len(list1):
#     k=list1[i]
#     if k not in b:
#         b.append(k)
#     i=i+1
# print(b)
