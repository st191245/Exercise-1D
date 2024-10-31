import math as m


def calc_discharge(b, h, k_st, m_bank, S):
    A=h*(b+h*m_bank)
    P=b+2*h*(m_bank**2+1)**0.5
return k_st*(S)**(1/2)*(A/P)**(2/3)*A



def cal_discharge(b, h,m_bank,S, k_st= None, n_m=None, D_90=None):
    if n_m:
          k_st=1/n_m
          print("The calculated k_st value is"+str(k_st)+"m1/3/s")
    elif D_90:
         k_st= 26/(D_90)**(1/6)
        print("The calculated k_st value is"+str(k_st)+"m1/3/s")

 def cal_discharge( k_st, n_m, D_90):
   for  kwarg in kwargs.items():
       if "D_90" in kwarg[0]
           k_st=26/kwarg[1]**(1/6))
       elif "k_st" in kwarg[0]
             k_st=kwarg[1]
       elif "n_m"  in kwarg[0]
             k_st=1/kwarg[1]


/def interpolate_h(*args, **kwargs):
    pass


if __name__ == '__main__':
    # input parameters
    Q = 15.5        # discharge in (m3/s)
    b = 5.1         # bottom channel width (m)
    m_bank = 2.5    # bank slope
    k_st = 20       # Strickler value
    n_in_main = 1 / k_st  # Manning's n
    S_0 = 0.005     # channel slope

    Q = calc_discharge(b, 2.0, k_st,m_bank=m_bank, S_0=S_0)
    print("The calculated discharge is %0.2f m3/s" % Q)

    # call the solver with user-defined channel geometry and discharge
    h_n = interpolate_h(Q, b, n_m=n_m, m_bank=m_bank, S0=S_0)
