import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    inpArr = np.array(list).reshape(3,3)

    calculations = {
        'mean': [inpArr.mean(axis=0).tolist(), inpArr.mean(axis=1).tolist(), inpArr.mean()],
        'variance': [inpArr.var(axis=0).tolist(), inpArr.var(axis=1).tolist(), inpArr.var()],
        'standard deviation': [inpArr.std(axis=0).tolist(), inpArr.std(axis=1).tolist(), inpArr.std()],
        'max': [inpArr.max(axis=0).tolist(), inpArr.max(axis=1).tolist(), inpArr.max()],
        'min': [inpArr.min(axis=0).tolist(), inpArr.min(axis=1).tolist(), inpArr.min()],
        'sum': [inpArr.sum(axis=0).tolist(), inpArr.sum(axis=1).tolist(), inpArr.sum()]
        }
    
    return calculations