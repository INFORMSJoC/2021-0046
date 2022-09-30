import numpy as np
import pandas as pd

seed = 1324231
np.random.seed(seed)

settings = {
    1: [-.05, -.3, -.20, 0.00],
    2: [-.05, 0.2, 0.00, 0.25],
    3: [-.05, 0.7, 0.25, 0.50],
    4: [0.00, -.3, -.20, 0.00],
    5: [0.00, 0.2, 0.00, 0.25],
    6: [0.00, 0.7, 0.25, 0.50],
    7: [0.05, -.3, -.20, 0.00],
    8: [0.05, 0.2, 0.00, 0.25],
    9: [0.05, 0.7, 0.25, 0.50]
}

for _i in range(1,10):
    n = 3
    a = [2.1, 1.8, 1.5]
    b = .2

    theta = settings[_i][0]
    
    cnt = 0
    for seed in np.random.choice(range(10000,90000), 500):
        add = 1
        np.random.seed(seed)
        corr = np.ones((n,n))*settings[_i][1]
        np.fill_diagonal(corr, 1)
        sample = np.random.multivariate_normal(np.zeros(n), corr, size=size)
        p = np.array([0.3, 0.2, 0.1]) + theta
        sample = np.where(sample < np.apply_along_axis(lambda x: np.percentile(x[1:], x[0]*100),
                                                       1, np.concatenate([np.array(p)[:, np.newaxis], sample.T], axis=1)
                                                      ), 1, 0)
        corr = np.corrcoef(sample.T)
        np.fill_diagonal(corr, -np.inf)

        if np.min(np.corrcoef(sample.T))<settings[_i][2] and np.max(corr)>settings[_i][3]:
            continue
            
        cnt = cnt + 1
        if cnt==150:
            break