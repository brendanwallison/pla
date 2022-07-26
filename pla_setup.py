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


# verify

# Create dataset of N = 10 points
# and label them using real weights

# Define PLA algorithm
def pla(X, sol, max_iterations = 10000):
    # Initialize weight vector

        # Calculate solution based on w_star

        # Find at least one misclassified point

        # return soln if no misclassified points remain

        # update weights


# Run PLA loop until convergence

#print(test)
#print(w)

# Calculate error rate


# Create dataset of N = 100 points 


# PLA loop


# Error rate


