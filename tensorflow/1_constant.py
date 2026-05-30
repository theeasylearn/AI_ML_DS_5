import tensorflow as tf 

list = [10,20,30,50,90]

#create tensor
vector = tf.constant(list)

print(vector)

list2 = [5.0,12.11,0.25]
vector2 = tf.constant(list2)
print(vector2)