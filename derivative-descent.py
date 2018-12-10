def cost(x,y,w):
    n = len(x)
    total_error = 0.0
    for i in range(n):
        cost = (y[i]-w*x[i])**2
        total_error+=cost
    return total_error/n        
        
        
def update(x,y,w,lr):
    m_deriv = 0
    n = len(x)
    for i in range(n):
        m_deriv = m_deriv - 2*x[i] * (y[i] - (w*x[i]))
    w = w - (m_deriv / float(n)) * lr
    return w   
        
       
n_weight = 2
for epoch in range(500):
    error = cost([1,2,3,4,5],[15,30,40,55,65],n_weight)
    print("error is",error)
    n_weight = update([1,2,3,4,5],[15,30,40,55,65],n_weight,0.0009)
    print("Weight:", n_weight)
        
