import numpy as np
import pandas as pd

seed = 1324231
np.random.seed(seed)

a = np.dot([ 2, .4, -.4, -1],1)
b = np.dot([ 0, 0.5, 1.5, 3],1)
settings = {
    1: [-0.05, .05, -.20, 0],
    2: [-0.05, .25, 0, 0.25],
    3: [-0.05, .5, 0.25, 0.5],
    4: [0.00, .05, -.20, 0],
    5: [0.00, .25, 0, 0.25],
    6: [0.00, .5, 0.25, 0.5],
    7: [0.05, .05, -.20, 0],
    8: [0.05, .25, 0, 0.25],
    9: [0.05, .5, 0.25, 0.5]
}

cnt = 0

for _i in range(1,10):
    for seed in np.random.choice(range(100000,900000), 1000):
    #     K     = 20
    #     size  = 400
        theta = settings[_i][0]
        corr  = np.ones((2,2))*settings[_i][1]
        np.fill_diagonal(corr, 1)
        p = np.array([0.25, 0.15]) + theta

        np.random.seed(seed)
        sample = np.random.multivariate_normal(np.zeros(2), corr, size=size)
        sample = np.where(sample < np.apply_along_axis(lambda x: np.percentile(x[1:], x[0]*100),
                                                       1, np.concatenate([np.array(1-p)[:, np.newaxis], sample.T], axis=1)
                                                      ), 1, 0)
        corrcoef = np.corrcoef(sample.T)[0,1]
        if corrcoef<settings[_i][2] or corrcoef>settings[_i][3]:
            continue

        cnt = cnt + 1
        if cnt>=150:
            break     