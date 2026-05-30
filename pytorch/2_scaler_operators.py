import torch as tc 

#crease tensor 
t1 = tc.tensor([10,20,30,40,50])
print(t1)

t2 = tc.tensor([1,2,3,4,5])
print(t2)

# #scaler addition 
# print(t1.add(3))

# #scaler subtraction 
# print(t1.sub(2))

# #scaler multiplication 
# print(t1.mul(4))

# #scaler division
# print(t1.divide(3))

print(t1+t2)
print(t1-t2)
print(t1*t2)
print(t1/t2)


