import matplotlib.pyplot as plt
x = [1,2,3,4,5] # Hours studied
y = [15,30,40,55,65] # Marks scored
n = len(x) # Assigning a value of the length of x to n

def loss(x,y,w): # This is called a function
    total_error = 0 # Total error will be initially 0
    for i in range(n): # This is a for loop and will loop the len(x number or times or n
        temp = (y[i]-w*x[i])**2 # Now we calculate error and square it (Expected output - Obtained)
        # We have to specify i because we want the loop to compute loss for all 5 digits in our list
        total_error = total_error + temp # Now we add the squared error to 
    return total_error/n #Divide total by n to get mean squared loss
wei = [1,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25]
los = [1710,331,222,135,70,27,7,30,75,142,231,342,475,630,807,1006,1227,1470]
print(loss([1,2,3,4,5],[15,30,40,55,65],1)) # Calling the loss function using w = 1
print(loss([1,2,3,4,5],[15,30,40,55,65],8)) # Calling the loss function using w = 8
print(loss([1,2,3,4,5],[15,30,40,55,65],9))# Calling the loss function using w = 9
print(loss([1,2,3,4,5],[15,30,40,55,65],10)) # Calling the loss function using w = 10
print(loss([1,2,3,4,5],[15,30,40,55,65],11)) # Calling the loss function using w = 11
print(loss([1,2,3,4,5],[15,30,40,55,65],12)) # Calling the loss function using w = 12
print(loss([1,2,3,4,5],[15,30,40,55,65],14)) # Calling the loss function using w = 14
print(loss([1,2,3,4,5],[15,30,40,55,65],15)) # Calling the loss function using w = 15
print(loss([1,2,3,4,5],[15,30,40,55,65],16)) # Calling the loss function using w = 16
print(loss([1,2,3,4,5],[15,30,40,55,65],17)) # Calling the loss function using w = 17
print(loss([1,2,3,4,5],[15,30,40,55,65],18)) # Calling the loss function using w = 18
print(loss([1,2,3,4,5],[15,30,40,55,65],19)) # Calling the loss function using w = 19
print(loss([1,2,3,4,5],[15,30,40,55,65],20)) # Calling the loss function using w = 20
print(loss([1,2,3,4,5],[15,30,40,55,65],21)) # Calling the loss function using w = 21
print(loss([1,2,3,4,5],[15,30,40,55,65],22)) # Calling the loss function using w = 22
print(loss([1,2,3,4,5],[15,30,40,55,65],23)) # Calling the loss function using w = 23
print(loss([1,2,3,4,5],[15,30,40,55,65],24)) # Calling the loss function using w = 24
print(loss([1,2,3,4,5],[15,30,40,55,65],25)) # Calling the loss function using w = 25


plt.plot(wei, los)
plt.show()
