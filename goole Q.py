

# num=0
# count=0
# sum=0

# while num>=0:
#     num = int(input('enter any number .. -1 to exit: '))
#     if num >= 0:
#         count = count + 1 # this counts number of inputs
#         sum = sum + num # this adds input number cumulatively.
# avg = sum/count
# print('Total numbers: ', count, ', Average: ', avg)

# When a negative number is provided by the user, the loop terminates and displays the average of the numbers provided so far. A sample run of the above code is below:
# Output

# enter any number .. -1 to exit: 10
# enter any number .. -1 to exit: 20
# enter any number .. -1 to exit: 30
# enter any number .. -1 to exit: -1
# Total numbers: 3, Average: 20.0

num = 0

while num < 3:
	num += 1   # num += 1 is same as num = num + 1
	print('num = ', num)
else:
    print('else block executed')
