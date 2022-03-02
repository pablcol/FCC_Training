import numpy as np


def calculate(list):
    if len(list) == 9:
        array = np.array(list).reshape((3, 3))
        mean = [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array)]
        std = [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array)]
        var = [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array)]
        max = [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array)]
        min = [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array)]
        sum = [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array)]

        calculations = {'mean': mean,
                        'variance': var,
                        'standard deviation': std,
                        'max': max,
                        'min': min,
                        'sum': sum
                        }
    else:
        raise ValueError('List must contain nine numbers.')

    return calculations
