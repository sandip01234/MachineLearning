import math
import numpy as np
import pandas as pd
 
#  function to calculate the distance between two points
def distance(x1, x2):
    return math.sqrt(np.sum((x1 - x2) ** 2))
