#This program peforms linear regression using gradient descent to fine a line of best-fit for the given data set
#in the specified number of iterations.

#Calculate the gradient of loss at the line's intercept
def calculate_b_gradient(x, y, b, m):

    num_points = len(x)
    total_diff = 0

    #Get the total difference in each point's y-value from its predicted y-value
    for i in range(num_points):
        total_diff += y[i] - ((m * x[i]) + b)
    
    b_gradient = -2 / num_points * total_diff

    return b_gradient

#Calculate the gradient of loss for the line's slope
def calculate_m_gradient(x, y, b, m):

    num_points = len(x)
    total_diff = 0

    #Get the total difference in each point's x-value from its predicted x-value
    for i in range(num_points):
        total_diff += x[i] * (y[i] - ((m * x[i]) + b))
    
    m_gradient = (-2 / num_points) * total_diff

    return m_gradient


#Function to use gradient descent to get the line of best-fit for the data set
def gradient_descent(x, y, rate, iterations):

    #Variables to hold the final modified y-intercept and slope
    b = 0
    m = 0

    #Iterate and modify the predicted line of best-fit's y-intercept and slope
    for _ in range (num_iterations): 
        b, m = step_gradient(b, m, x, y, rate) 
    
    return [b, m]


#Function to modify the y-intercept and slope based on the gradient error
def step_gradient(old_b, old_m, x, y, rate):

    b_gradient = calculate_b_gradient(x, y, old_b, old_m)
    m_gradient = calculate_m_gradient(x, y, old_b, old_m)

    new_b = old_b - (rate * b_gradient)
    new_m = old_m - (rate * m_gradient)

    return [new_b, new_m]


#---------------------------------------------------------------------#

#The x-value data set to be used
months = [1,2,3,4,5,6,7,8,9,10,11,12]

#The y-value data set to be used
sales = [200,224,242,233,260,314,299,344,387,404,403,450]

#The final slope and y-intercept of the line of best-fit for the data set
slope = 0
y_intercept = 0

#The learning rate for each step
learning_rate = 0.01

#The number of iterations to perform in deriving the line of best-fit
num_iterations = 1000

#Calculate the line of best-fit
slope, y_intercept = gradient_descent(months, sales, learning_rate, num_iterations)

print("The slope and y-intercept of the returned line are: " + str(slope) + ", " + str(y_intercept))
