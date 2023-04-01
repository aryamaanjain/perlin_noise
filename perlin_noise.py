import math
import numpy as np
np.random.seed(0)


def give_grad(x, y):
    gx = hash((x,y)) % 256 - 128
    gy = hash((y,x+1)) % 256 - 128   # +1 to avoid same grad along diagonal
    gx_normalized = gx / (gx**2 + gy**2)**0.5
    gy_normalized = gy / (gx**2 + gy**2)**0.5
    return gx_normalized, gy_normalized


def interpolate(t):
    return 6*t**5 - 15*t**4 + 10*t**3


def noise(x, y):
    # calculate closest integer grid points
    x0, y0 = math.floor(x), math.floor(y)
    x1, y1 =  math.ceil(x),  math.ceil(y)
    if x0 == x1:
        x1 += 1.0
    if y0 == y1:
        y1 += 1.0
    
    # calculate gradients at those grid points
    g00x, g00y = give_grad(x0, y0)
    g01x, g01y = give_grad(x0, y1)
    g10x, g10y = give_grad(x1, y0)
    g11x, g11y = give_grad(x1, y1)
    
    # calculate direction vectors
    h00x, h00y = x-x0, y-y0
    h01x, h01y = x-x0, y-y1
    h10x, h10y = x-x1, y-y0
    h11x, h11y = x-x1, y-y1
    
    # calculate values via dot product
    v00 = g00x * h00x + g00y * h00y
    v01 = g01x * h01x + g01y * h01y
    v10 = g10x * h10x + g10y * h10y
    v11 = g11x * h11x + g11y * h11y
    
    # interpolate the values using an interpolating function
    vx0 = interpolate(x1-x) * v00 + interpolate(x-x0) * v10
    vx1 = interpolate(x1-x) * v01 + interpolate(x-x0) * v11
    z   = interpolate(y1-y) * vx0 + interpolate(y-y0) * vx1
        
    return z


def perlin(x, y, octaves=3, frequency=2, persistence=0.5):
    z = 0
    f = 1
    p = 1
    for i in range(octaves):
        z += p * noise(f*x, f*y)
        f *= frequency
        p *= persistence
    return z


def give_grid(N=256):
    points = np.linspace(0, 8, N)
    grid = np.random.random((N,N))
    for i in range(N):
        for j in range(N):
            grid[i,j] = perlin(points[i], points[j])
    return grid

