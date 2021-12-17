#test input. the matrix can be any n * n size.
matrix = [[82, 83,69, 92],[77, 37, 49,92],[11, 69, 5, 86],[8, 9, 98, 23]]
# row1, row2, row3, row4

#assistant array to track which numbers we have already used.
#check[i] = 1 if i has been used
check = [0]* len(matrix)

#max sum
max_sum = 0

def getMax(matrix,check,row,curr_sum):
    global max_sum
    #base case, we have reached the last element.
    #check to see if this combination is max
    if(row==len(matrix)-1):
        for i in range(len(check)):
            if(check[i]==0 and (matrix[row][i]+curr_sum)>max_sum):
                max_sum = matrix[row][i]+curr_sum
    #recursive case, pick the current available number, go to next Number.
    else:
        for i in range(len(check)):
            if(check[i]==0):
                check[i]=1
                getMax(matrix,check,row+1,curr_sum+matrix[row][i])
                check[i]=0

getMax(matrix,check,0,0)

print(max_sum)

# output - 344
#This algorithm give the maximum kideney donar matching but take higher iterations as it finds out recursivrly by trial and error
#Has an improvement over greedy as the Algo gives the expected output.
# fails miserably in time complexity
#Solution 1: Brute Force
#We generate n! possible job assignments and for each such assignment, we compute its total matching percent and return the highest matching assignment. Since the solution is a permutation of the n jobs, its complexity is O(n!).#
# Here we try all the combinations one by one to find the optimal solution. This is a tedious approach because as the number of tasks and cranes go on increasing , the number of calculations also increase. The complexity is n! which is very inefficient.

