import numpy as np

def collapse(probas, output_type = 'bin'):
    """
    Parameters
    ----------
    probas: An array of probablities.
    output_type: If ternary, output can be -1, 0 and 1.
    
    Returns
    -------
    b: An array of binary states, whose dimensionality is identical to probas.
    """
    p = np.abs(probas)
    b = (p >= np.random.rand(*p.shape)).astype(np.int)
    return np.where(probas >= 0, b, {'bin': 0, 'ter': -b}[output_type])        

def duoramp(x, low = None, high = None):
    """
    Parameters
    ----------
    x : Anything that can be transformed into an numpy array
    low : A number, optional
        The lowest value an entry in x can be. The default is None. 
    high : A number, optional
        The highest value an entry in x can be. The default is None.

    Returns
    -------
    y : A numpy array
        The value of each element is between low and high.

    """
    y = np.asarray(x)
    if low is not None:
        y[y < low] = low
    if high is not None:
        y[y > high] = high
    return y

def logistic(x, temperature = 1.0):
    """
    Parameters
    ----------
    x: A numeric array.
    temperature: A non-negative number controlling the slope of the function.
    
    Returns
    -------
    y: The value of the function, which is often used as a probability.
    
    -------
    The function is numerically stable for very big/small values.
    """
    _x = np.asarray(x)
    if temperature == 0: # The logistic function is reduced to a step function.
        y = np.zeros(_x.shape)
        y[_x > 0] = 1.0
        y[_x == 0] = 0.5     
    else:
        norx = _x / temperature
        mask_p = norx > 0
        mask_n = norx < 0        
        y = np.ones_like(norx)
        y[mask_p] = 1 / (1 + np.exp(-norx[mask_p]))
        # positive x gives small exp(-x): 1<denom<2
        z = np.zeros_like(y[mask_n])
        z = np.exp(norx[mask_n])
        y[mask_n] = z / (1 + z)        
        # negative x gives small exp(x)=z: 1<denom<2
    return y

def softmax(x, temperature = 1.0):
    """
    Parameters
    ----------
    x: A two-dimensional numeric array; each row is a distribution of activations.
    temperature: A non-negative number controlling the slope of the function.
    
    Returns
    -------
    P: The value of the function, which is often used as a probability. Each row adds up to 1.
    
    -------
    The function is numerically stable for very big/small values.
    """
    # normalise x so that the biggest value is 0; this stablises np.exp
    norx = x - np.amax(x, axis = 1).reshape(len(x), 1)
    _p = []
    if temperature == 0:
        for xrow in norx:
            prow = np.zeros_like(xrow, dtype = float)
            mask_max = xrow == 0
            prow[mask_max] = 1 / np.count_nonzero(mask_max)
            _p.append(prow)
    else:
        for xrow in norx:
            e = np.exp(xrow / temperature)
            prow = e / np.sum(e)
            _p.append(prow)
    P = np.reshape(_p, norx.shape)
    return P

def entropy(P, base = None):
    """
    Parameters
    ----------
    P: A two-dimensional numeric array; each row is a probability distribution.
    base: The logarithmic base when calculating entropy with the default value being e.
    
    Returns
    -------
    H: The entropy of each distribution in P.
    """
    norp = P / np.sum(P, axis = 1).reshape(len(P), 1)
    norp[norp == 0] = 1 # plog(p) = when p = 0 or 1
    if base is None:
        denom = 1
    else:
        denom = np.log(base)
    logp = np.log(norp) / denom
    H = np.asarray([-np.dot(ps, logps) for ps, logps in zip(norp, logp)])
    return H

def kl_divergence(p, q, base = np.e):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0)) / np.log(base)