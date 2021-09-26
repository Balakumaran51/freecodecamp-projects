import numpy as np

def calculate(list):
    if (len(list) != 9):
        raise ValueError('List must contain nine numbers.')
    l = np.array(list).reshape((3, 3))
    return {
        'mean': [l.mean(axis=0).tolist(), l.mean(axis=1).tolist(), l.mean()],
        'variance': [l.var(axis=0).tolist(), l.var(axis=1).tolist(), l.var()],
        'standard deviation': [l.std(axis=0).tolist(), l.std(axis=1).tolist(), l.std()],
        'max': [l.max(axis=0).tolist(), l.max(axis=1).tolist(), l.max()],
        'min': [l.min(axis=0).tolist(), l.min(axis=1).tolist(), l.min()],
        'sum': [l.sum(axis=0).tolist(), l.sum(axis=1).tolist(), l.sum()]
    }
