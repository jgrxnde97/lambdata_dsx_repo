""" lambdata_jgrxnde9701 - a collection of data science helper functions """

# sample codes
import numpy as np
import pandas as pd

# sample datasets
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))


# sample functions
def increment(x):
    return (x + 1)
