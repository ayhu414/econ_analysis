import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from sympy import init_printing
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

'''
Elementary code to run analysis on difference equations

key equations:
1) for c in (-1,1), c converges through an infinite sum to 1 / (1  -c)
2) for c in R, c converges through a finite sum to (1 - c^(T+1)) / (1 - c)
'''
def diff_eq(X_t,a,b,delta,epsilon):
    if abs(delta) < epsilon:
        return X_t
    else:
        X_next = X_t**a + b
        gap = X_next - X_t
        return diff_eq(X_next,a,b,gap,epsilon)

def solve_dynamic(X_t,a,b,iter = -1):
    gap = X_t
    if iter == -1:
        return round(diff_eq(X_t,a,b,delta = X_t,epsilon = 10**(-7)), 7)
    else:
        return
def iterative_diff_eq(X_0,a,b,t):
    seq = np.zeros(t+1)
    seq[0] = X_0
    for i in range(1,t+1):
        print(i)
        print(seq[i-1])
        seq[i] = seq[i-1]**a + b
    return seq

def draw_diff_eq(X_0,a,b,t):
    X_seq = iterative_diff_eq(X_0,a,b,t)
    plt.plot(range(t+1), X_seq)
    plt.axis([0,t,0,np.amax(X_seq)+1])
    plt.show()
'''

print(solve_dynamic(0.1,0.5,2))
print(solve_dynamic(10,0.5,2))
print(solve_dynamic(0.1,-0.9,2))
print(solve_dynamic(10,-0.9,2))
print(iterative_diff_eq(10,0.5,2,200))
'''
draw_diff_eq(10,0.5,2,100)
