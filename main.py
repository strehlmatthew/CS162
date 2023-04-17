import matplotlib.pyplot as plot
# set up your lists
numlist = [9, 2, 3, 7]
namelist = ['seniors', 'sophomores', 'juniors', 'freshmen']
colorlist = ['lightblue', 'red', 'orange', 'purple' ]
explodelist = [0.0, 0.0, 0.1, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%1.5f%%', colors=colorlist,
    	explode = explodelist, startangle = 90)
plot.axis('equal')
plot.savefig('piechart.png')
