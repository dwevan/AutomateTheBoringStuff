supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is:' + item )

#  above code is example of enumerate - can also be done as per below:

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
