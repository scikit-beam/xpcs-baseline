#! /usr/bin/env python

import numpy as np
import mdscatter
import matplotlib.pyplot as plt
import time
import glob

N = 128

npys = glob.glob('data/step_40*_coord_array.npy')
#npy = 'step_0_coord_array.npy'

th = np.deg2rad(np.linspace(-10, 10, N))
al = np.deg2rad(np.linspace(-10, 10, N))
th, al = np.meshgrid(th, al)


wavelen = 0.1
k0 = 2 * np.pi / wavelen
qx = k0 * (np.cos(al) * np.cos(th) - 1)
qy = k0 * (np.cos(al) * np.sin(th))
qz = k0 * np.sin(al)
qvals = np.array([qx.ravel(), qy.ravel(), qz.ravel()]).T

for npy in npys:
    pts = np.load(npy).T 
    img = mdscatter.dft(pts, qvals)
    img = np.abs(img)**2
    img = img.reshape(N, N)
    plt.imshow(np.log(img))
    plt.axis('off')
    img_name = npy.replace('data', 'imgs').replace('npy', 'png')
    plt.savefig(img_name)
