import torch as tc 

#crease tensor 
t1 = tc.tensor([10,20,30,40,50])
print(t1)

t2 = tc.zeros(3,5) #create 2d tensor with 3 rows and 5 column 
print(t2)

t3 = tc.rand(3,4) #create 2d tensor with 3 row and 4 column each has rondom numbers 
print(t3)


