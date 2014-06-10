A = [[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0]]

for row in A:
    for val in row:
        print '{:10}'.format(val),
    print

pointA=[2,5]
pointB=[5,8]

print "The points given are:",pointA[0],",",pointA[1],"&",pointB[0],",",pointB[1]

direc= (pointB[1]-pointA[1])/(pointB[0]-pointA[0])

print "Direction is:", direc

cross= pointB[1] - (direc*pointB[0])

print "Cross Y point is:", cross

for x in range(pointA[0], pointB[0]+1):
	i= (direc*x) + cross
	A[x][i]=1
	print "We're on x point %d" % (x), "-- We're on y point %d" % (i) 

for row in A:
    for val in row:
        print '{:10}'.format(val),
    print