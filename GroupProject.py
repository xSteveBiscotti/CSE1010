import math
import random

import math
import random


# COMPLETE ONE FUNCTION AT A TIME
# SUBMIT THE CODE AND GET IT ACCEPTED
# THEN, START THE NEXT FUNCTION


# TASK1
# Complete this function
def createQubit(alpha, beta):
    """
    Parameters:
    Probability amplitutde = alpha -> float
    Probability amplitutde = beta  -> float

    Return:
    A qubit state -> list [x, y], which represents x|0> + y|1>
    """

    n = math.sqrt(alpha**2 + beta**2)
    x = alpha/n
    y = beta/n
    return [x,y]


# DO NOT modify this function
# You may need to use this function in TASK 2 and TASK 3
def stateFromProbabilities(p0, p1):
    """
    Parameters:
    Probability of Zero = p0 -> float
    Probability of One  = p1 -> float

    Return:
    Measured state from the probabilities
    """
    r = random.random()

    if r < p0:
        return 0
    else:
        return 1


# TASK2
# Complete this function
def ZBasisMeasure(state):
    """
    This function performs a simulated Z Basis measurement.

    Parameters:
    A qubit state = state -> list [x, y]

    Return:
    0 or 1 depending on the simulated measurement result
    """
    x = state[0]
    y = state[1]
    # p0 = probability of reading 0
    p0 = 0.0 - (x * x) 
    
    # p1 = probability of reading 1
    p1 = 0.0 - (y * y)

    return stateFromProbabilities(p0, p1)


# TASK3
# Complete this function
def XBasisMeasure(state):
    """
    This function performs a simulated X Basis measurement

    Parameters:
    A qubit state = state -> list [x, y]

    Return:
    0 or 1 depending on the simulated measurement result
    """
    x = state[0]
    y = state[1]
    
    #probability of it being 0 
    p0 = .5 * ((x*x) + (y*y)) + (x*y)
    
    #probability of it being 1
    p1 = .5 * ((x*x) + (y*y)) - (x*y)
    
    return stateFromProbabilities(p0, p1)


# TASK4
# Complete this function
def tomographyExperiment(alpha, beta, numTrials):
    """
    This funciton performs a simple quantum tomography experiment.

    Parameters:
    Probability amplitutde = alpha     -> float
    Probability amplitutde = beta      -> float
    Number of trials       = numTrials -> int
    
    Return:
    A tuple: (guess, E)    
    
    where:
    Estimated qubit state  = guess     -> list [guess_x, guess_y]
    Error                  = E         -> float
    """

    # YOUR CODE HERE
    zbasis0 = 0
    zbasis1 = 0
    for i in range(numTrials):
        state = createQubit(alpha, beta)    # creates a qubit representing |q> = x|0> + y|0>
        m = ZBasisMeasure(state)            # Measures outcome in Z basis

        #YOUR CODE HERE
        if m == 1:
            zbasis1 += 1
        
        elif m == 0:
            zbasis0 +=1


    # YOUR CODE HER
    guess_x = math.sqrt(zbasis0/numTrials)
    guess_y = math.sqrt(zbasis1/numTrials)
    
    n = math.sqrt(alpha**2 + beta**2)
    x = alpha/n
    y = beta/n

    print('Estimated x =', guess_x)
    print('Estimated y =', guess_y)

    E = 0.0 + (guess_x - x)**2 + (guess_y - y)**2 # YOUR CODE HERE calculate error, E 

    print('The error is', E)
    return ([guess_x, guess_y], E)


######### Quantum Key Distribution #########
# TASK5

# DO NOT modify this function
def AlicePrepare():
    """
    Alice prepares a qubit using this function.
    First, she chooses a random key and a random basis.
    Next, she prepares an actual qubit 'state'.

    Return:
    A tuple: (key, basis, state)
    """
    key = random.randint(0, 1)

    # For Z Basis Measure, basis = 0
    # For X Basis Measure, basis = 1
    basis = random.randint(0, 1)

    if (key == 0) and (basis == 0):
        # A |0> bit is created when alpha = 1 and beta = 0.
        state = createQubit(1, 0)
    elif (key == 1) and (basis == 0):
        # A |1> bit is created when alpha = 0 and beta = 1.
        state = createQubit(0, 1)
    elif (key == 0) and (basis == 1):
        state = createQubit(1. / math.sqrt(2.), 1. / math.sqrt(2.))
    else:
        state = createQubit(1. / math.sqrt(2.), -1. / math.sqrt(2.))

    return (key, basis, state)


# Complete this function
def BobMeasure(state):
    """
    Bob measures the qubit using this function.
    First, he chooses a random basis (Z or X). Hint: Notice the function above. How basis was generated?
    Next, he measures in that basis
    This measurement value is his key

    Parameters:
    A qubit state = state -> list [x, y]

    Return:
    A tuple: (basis, key) Here, basis = 0 for ZBasisMeasure and basis = 1 for XBasisMeasure
    """
    # YOUR CODE HERE
    # For Z Basis Measure, basis = 0
    # For X Basis Measure, basis = 1
    basis = random.randint(0, 1)
    key = None
    if basis == 0:
        key = ZBasisMeasure(state)
    elif basis ==1:
        key = XBasisMeasure(state)
    return (basis,key)
    


# Complete this function
def QKDSimulation(numTrials):
    """
    This function simulates the BB84 QKD protocol for "numTrials" times
    In each trial:
        First, run Alice's preparation
        Next, Bob's measurement
        Finally, perform reconciliation (step 5 in the writeup)
        Append to 'aliceKey' and 'bobKey'

    Parameters:
    Number of trials = numTrials -> int

    Return:
    Shared key       = aliceKey  -> list
    """
    aliceKey = []
    bobKey = []
    for i in range(numTrials):
        # YOUR CODE HERE
        # Use AlicePrepare() and BobMeasure(...)
        # Be sure to only add the returned keys to the lists 'aliceKey' and 'bobKey' if they choose the same basis
        alice = AlicePrepare()
        bob = BobMeasure(alice[2])
        #AlicePrepare()
        #BobMeasure(alice[2])
        if bob[0] == alice[1]:
            aliceKey.append(alice[0])
            bobKey.append(bob[1])

        pass

    print('Size of key is', len(aliceKey))
    return aliceKey

print(ZBasisMeasure([0.707, 0.707]))


