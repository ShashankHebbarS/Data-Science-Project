import numpy as np
import pickle

def irispred(inp):
    arr = np.array(inp).reshape(1, 4)
    iris_model = pickle.load(open('iris.pkl', 'rb'))
    result = iris_model.predict(arr)
    return result[0]

def titanicpred(inp):
    arr = np.array(inp).reshape(1, 6)
    titanic_model = pickle.load(open('titanic.pkl', 'rb'))
    result = titanic_model.predict(arr)
    return result[0]