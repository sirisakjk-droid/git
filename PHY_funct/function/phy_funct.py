import numpy as np

def arr(i : float = 0.0 ,j : float = 0.0 , n : int = 0) : 
    x = np.zeros(n) ; y = np.zeros(n)
    x[0] = i ; y[0] = j
    return x , y



def projectile(n : int = 50 , ax : float = 0.0 , ay : float = -9.8):

    t = 1/n

    def arr(i ,j , n) : 
        v1 = np.zeros(n) ; v2 = np.zeros(n)
        v1[0] = i ; v2[0] = j
        return v1 , v2
    
    def motion_vx(v1, ax):

        for i in range(len(v1)-1):
            v1[i+1] = v1[i] + ax * t

        return v1

    def motion_vy(v2, ay):
        
        for i in range(len(v2)-1):
            v2[i+1] = v2[i] + ay * t
        return v2
    
    def posit_x(x, vx , y):
        for i in range(len(x)-1):
            if y[i+1] <= 0 and i > 0:
                x[i+1] = x[i]
            else : 
                x[i+1] = x[i] + vx[i] * t
        return x
    
    def posit_y(y, vy):
        for i in range(len(y)-1):
            if y[i] <= 0 and i > 0 :
                y[i+1] = y[i] = 0
            else :
                y[i+1] = y[i] + vy[i] * t
        return y
    
    x0 , y0 = map(float, input('Initial position (x y) : ').split())
    vx0, vy0 = map(float, input('Initial velocity (vx vy) : ').split())

    x , y = arr(x0 , y0 , n)
    vx , vy = arr(vx0 , vy0 , len(x))

    vx_cal = motion_vx(vx , ax) ; vy_cal = motion_vy(vy , ay)
    y_upd = posit_y(y, vy_cal)
    x_upd = posit_x(x, vx_cal, y_upd)

    return x_upd , y_upd


def euler_method(f ,n ):
    def input_initial():
        x = map(float, input('define x0 : '))
        y = map(float, input('define y0 : '))
        return x
    
    def arr(i : float = 0.0 ,j : float = 0.0 , n : int = 0) : 
        x = np.zeros(n) ; y = np.zeros(n)
        x[0] = i ; y[0] = j
        return x , y
    
    def deri(f, x , y ,h):
        for i in range(n-1):
            x[i+1] = x[i] + h
            y[i+1] = y[i] + f(x[i], y[i]) * h
        return x , y
    
    h = 1/ (n * 10)
    x0 , y0 = input_initial()
    x , y = arr(x0 , y0 , n)
    dx , dydx = deri(f , x , y , h)
    return dx , dydx
            
        

def pendulum():
    return