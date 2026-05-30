import tensorflow as tf 

age = tf.Variable(42)

print(age)
age.assign(41)
# age.assign(41.25) can not change type of tensor
print("now age has ",age)