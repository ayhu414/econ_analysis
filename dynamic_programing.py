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
        print()
        return X_t
    else:
        X_next = X_t**a + b
        print(X_t)
        gap = X_next - X_t
        return diff_eq(X_next,a,b,gap,epsilon)

def solve_dynamic(X_t,a,b,iter = -1):
    gap = X_t
    if iter == -1:
        return diff_eq(X_t,a,b,delta = X_t,epsilon = 10**(-7))
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

def get_present_val(X_0,g,r,t):
    G = (1 + g)
    R = (1 + r)
    return (X_0 * (1 - G**(t + 1) * R**(-t - 1))) / (1 - G * R**(-1))

def get_present_val_approx1(X_0,g,r,t):

    return (X_0*(t + 1)) + (X_0*r*g*(t + 1))/(r - g)

def get_present_val_approx2(X_0,g,r,t):

    return (X_0*(t + 1))

def inf_period_val(X_0,g,r):
    return (X_0/(1-(1+g)*(1+r)**(-1)))

def plots(axes, x_vals, fn, args):
    axes.plot(x_vals, fn(*args), label = fn.__name__)

def go_plot():

    fns = [get_present_val,
           get_present_val_approx1,
           get_present_val_approx2]

    fig, ax = plt.subplots()
    ax.set_title('Present Value of $T$ Periods')
    for f in fns:
        plots(ax, t, f, our_args)
    ax.legend()
    ax.set_xlabel("$T$ Periods ahead")
    ax.set_ylabel("Present val, $p_0$")
    plt.ylim(0 , t_max + 1)
    plt.show()

#go_plot()

def go_convergence(X_0,g,r,t):
    t_max = 1000
    t = np.arange(0, t_max + 1)
    fig, ax = plt.subplots()
    ax.set_title("dumb $botch$")
    f_1 = get_present_val(X_0,g,r,t)
    f_2 = inf_period_val(X_0,g,r) * np.ones(t_max + 1)
    ax.plot(t, f_1, label = 't-period lease present val')
    ax.plot(t, f_2, color = 'red', marker = 'o', linestyle = ':')
    ax.set_xlabel('$T$ periods ahead botch')
    ax.set_ylabel('nani the $present val$')
    ax.legend('best')
    plt.show()

t_max = 50
t = np.arange(0, t_max + 1)
g = 0.02
r = 0.03
x_0 = 1

our_args = (x_0, g, r, t)

#go_convergence(*our_args)

def plot_different_rg(x_0,t_max):
    rs, gs = (0.9, 0.5, 0.4001, 0.4), (0.4, 0.4, 0.4, 0.5)
    t = np.arange(0, t_max + 1)
    fig, ax = plt.subplots()
    ax.set_xlabel('time $t$ elapsed')
    ax.set_ylabel('present value in the future time $t$')

    comparisons = ('$\gg$','$>$', r'$approx$','$<$')
    for r, g, comp in zip(rs,gs,comparisons):
        ax.plot(get_present_val(x_0,g,r,t), label=f'r(={r}) {comp} g(={g})')

    ax.legend()
    plt.show()

#print(solve_dynamic(0.1,0.5,-3))
#print(solve_dynamic(10,-.9,2))
print(solve_dynamic(10,-0.9,-3))
#print(solve_dynamic(0.1,-0.9,2))
#print(solve_dynamic(10,0.99,2))

plot_different_rg(1,10)


'''
print(solve_dynamic(0.1,-0.9,2))
print(solve_dynamic(10,-0.9,2))
print(iterative_diff_eq(10,0.5,2,200))
draw_diff_eq(10,0.5,2,100)
'''



