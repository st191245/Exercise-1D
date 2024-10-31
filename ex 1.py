import math as m

def cal_discharge(b, h,m_bank,S, k_st= None, n_m=None, D_90=None):
    if n_m:
        k_st=1/n_m
        print("The calculated k_st value is"+str(k_st)+"m1/3/s")
    elif D_90:
        k_st= 26/(D_90)**(1/6)
        print("The calculated k_st value is"+str(k_st)+"m1/3/s")

def calc_discharge(b, h, n_m, m_bank, S_0):
    A = h * (b + h * m_bank)
    P = b + 2 * h * (m_bank**2 + 1)**0.5
    return 1/n_m*(S_0)**(1/2) * (A/P)**(2/3) * A
    #return k_st * (S_0)**(1/2) * (A/P)**(2/3) * A# he we have K_st,this is sticklers co-efficient,if we want to use mannings,then chage the formula

if __name__ == '__main__':
    # input parameters
    Q = 15.5        # discharge in (m3/s)
    b = 5.1         # bottom channel width (m)
    m_bank = 2.5    # bank slope
    k_st = 20       # Strickler value
    n_in_main = 1 / k_st  # Manning's n
    S_0 = 0.005     # channel slope

    # Corrected function call
    Q = calc_discharge(b, 2.0,n_m=n_in_main,m_bank=m_bank, S_0=S_0)# when we call a function it should be same parameters in the function mentioned above
    print("The calculated discharge is %0.2f m3/s" % Q)
