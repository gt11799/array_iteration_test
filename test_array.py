from numpy import *

def func_x(v, u):
    answer = [((1. + value_v / 2. * cos(u/2.)) * cos(u)) for value_v in v]
    return array(answer)
    
def func_y(v, u):
    answer = [((1. + v / 2. * cos(value_u/2.)) * cos(value_u)) for value_u in u]
    return array(answer)
    
if __name__ == '__main__':
    from timeit import Timer
    v = linspace(-1.0, 1.0, num=10000, endpoint=True)
    u = linspace(0, 2*pi, num=10000, endpoint=True)
    
    t1 = Timer("func_x", "from __main__ import func_x")
    t2 = Timer("func_y", "from __main__ import func_y")
    winx, winy = (0,0)
    for temp in range(100):
        if t1.timeit(1000) < t2.timeit(1000):
            winx +=1
        else:
            winy +=1
    print("func_x win:%d \nfunc_y win:%d" %(winx, winy))
