import numpy as np

'''
'arr' use for define position in two-dimension
as 'i' is initial condition of horizontal axis
   'j' is initial condition of vertical axis
   'n' is number of point
'''

def arr(i ,j , n) : 
    x = np.zeros(n) ; y = np.zeros(n)
    x[0] = i ; y[0] = j
    return x , y



def projectile(t, n):

    def arr(i ,j , n) : 
        v1 = np.zeros(n) ; v2 = np.zeros(n)
        v1[0] = i ; v2[0] = j
        return v1 , v2
    
    def motion_vx(v1):

        for i in range(len(v1)-1):
            v1[i+1] = v1[i]

        return v1

    def motion_vy(v2):
        def g():
            return 9.8
        
        for i in range(len(v2)-1):
            v2[i+1] = v2[i] + g() * t
        return v2
    
    def posit_x(x, vx):
        for i in range(len(x)-1):
            x[i+1] = x[i] + vx[i] * t
        return x
    
    def posit_y(y, vy):
        for i in range(len(y)-1):
            y[i+1] = y[i] + vy[i] * t
        return y
    
    x0 , y0 = map(float, input('Inintial position (x y) : ').split())
    vx0, vy0 = map(float, input('Inintial velocity (vx vy) : ').split())

    x , y = arr(x0 , y0 , n)
    vx , vy = arr(vx0 , vy0 , len(x))

    vx_cal = motion_vx(vx) ; vy_cal = motion_vy(vy)
    x_upd = posit_x(x, vx_cal) ; y_upd = posit_y(y, vy_cal)

    return x_upd , y_upd
