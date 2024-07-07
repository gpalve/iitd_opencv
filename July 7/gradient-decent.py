import numpy as np
import torch

X = torch.tensor([1,2,3,4],dtype = torch.float32)
Y = torch.tensor([2,4,6,8], dtype = torch.float32)

m = torch.tensor(1.0,requires_grad=True)
alpha = 0.01


J = ((m*X-Y)**2).sum()
J.backward()
print(m.grad)


while abs(m.grad.item())>0.01:
    dw = m.grad.item()
    m.grad.zero_()
    with torch.no_grad():
        m -= alpha*dw
    J = ((m*X-Y)**2).sum()
    J.backward()
    
    print(m.item())