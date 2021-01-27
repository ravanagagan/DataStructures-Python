# we can implement 4 - Stack using list also but the problem with list is: Memory allocation
# It will allocate memory like dynamic array : if size is 10 if you insert 11th element then
# It will allocate 10*2 extra memory then it will copy those 10 elements after that it will add 11th element

# List implementation
stack = []
stack.append('https://edition.cnn.com/')
stack.append('https://edition.cnn.com/politics')
stack.append('https://edition.cnn.com/entertainment')
stack.append('https://edition.cnn.com/style')

# now it added items in stack format if we want to show last added item we should use stack.pop().
# this will remove item from the stack. if we just want to display element at top will use slicing stack[-1]
print('1st POP: ', stack.pop())  # https://edition.cnn.com/style
print('2nd POP: ', stack.pop())  # https://edition.cnn.com/entertainment

print('Display Element at top without popping :', stack[-1])



