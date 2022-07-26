import numpy as np

## CREATE DATA ##

# Draw two points #
#random.uniform(low=0.0, high=1.0, size=None)
#Draw samples from a uniform distribution.
#Samples are uniformly distributed over the half-open interval [low, high) (includes low, but excludes high). In other words, any value within the given interval is equally likely to be drawn by uniform.

points = np.random.uniform(low=-1, high=1, size=4)
point_1 = points[0:2] 
point_2 = points[2:4] 

# Manually calculate equation of line #
# y = mx + b -> 
# b + mx - y = 0 
# or using our variable names:
# w0*1 + w1*x1 + w2*x2  = 0
# where w0 = b, w1 = m, and w2 = -1 

m = (point_1[1] - point_2[1])/(point_1[0] - point_2[0])
b = -m*point_1[0] + point_1[1]
w = np.array([b, m, -1])

# verify
dummy = np.ones((2,1))
points = points.reshape((2,2))
points = np.concatenate((dummy, points), 1)
points@w

# Create dataset of N = 10 points
# and label them using real weights
X = np.random.uniform(low=-1, high=1, size=20)
X = X.reshape((10, 2))
dummy = np.ones((10,1))
X = np.concatenate((dummy, X), 1)
sol = np.sign(X@w)

# Define PLA algorithm
def pla(X, sol, max_iterations = 10000):
    # Initialize weight vector
    w_star = np.array([0, 0, 0])
    for i in range(max_iterations):
        # Calculate solution based on w_star
        proposed_sol = np.sign(X@w_star)
        # Find at least one misclassified point
        err = sol != proposed_sol
        misclassified = np.where(sol != proposed_sol)[0]
        #print("misclassified_points: " + str(misclassified))
        # return soln if no misclassified points remain
        if misclassified.shape[0] == 0:
            return w_star, i
        else:
        # update weights
            random_misclassified = np.random.choice(misclassified)
            y = sol[random_misclassified]
            x = X[random_misclassified]
            w_star = w_star + y*x
    return w_star, max_iterations

# Run PLA loop until convergence
test = pla(X, sol)
#print(test)
#print(w)

# Calculate error rate


# Create dataset of N = 100 points 


# PLA loop


# Error rate


