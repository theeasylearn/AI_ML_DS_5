import tensorflow.random as rd 
from tensorflow import int32
#create float vector
vector1 = rd.uniform(shape=[3,3],minval=1,maxval=100)
print(vector1)

#integer vector
vector2 = rd.uniform(shape=[10],minval=1,maxval=100,dtype=int32)
print(vector2)