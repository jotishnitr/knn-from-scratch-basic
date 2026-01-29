# Simple KNN implementation to understand distance-based classification
# Written using basic Python without external ML libraries

import math

points=[[1,2],[2,3],[6,5],[4,5],[3,4]]
labels=['A','A','A','B','B'] #labelling the points taken
test=[2,2]
k=2;

#calculating distances from each point to test point.
distances=[]
for i in range(len(points)):
    x_diff=(points[i][0]-test[0])
    y_diff=(points[i][1]-test[1])
    distance=math.sqrt((x_diff**2)+(y_diff**2))
    distances.append([distance,labels[i]])
print("Distances:",distances)

#sorting the distances so that we can get shorter distance points to forward positions
distances.sort()
print("Sorted Distances:",distances)

#Voting
countA=0
countB=0
for i in range (k):
    if distances[i][1]=='A':
        countA+=1
    else:
        countB+=1

#final decision
if countA>countB:
    prediction='A'
else:
    prediction='B'
    
print("Predicted label:",prediction)
