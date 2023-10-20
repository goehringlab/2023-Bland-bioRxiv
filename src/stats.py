import numpy as np


def bootstrap(data, func, niter=1000):
    """
    
    data: list of np arrays
    func:
    
    """
    
    # Results containter
    output = np.zeros(niter)
    
    # ninter bootstraps
    for i in range(niter):
        
        # Loop through datasets, taking a subsample of each with replacement
        _data = []
        for d in data:
            d_sample = d[np.random.choice(range(len(d)), len(d))]
            _data.append(d_sample)

        # Perform function on _data to calculate output
        output[i] = func(_data)
    
    return output 


# def func(x):
#     return np.mean(x[1]) - np.mean(x[0])
