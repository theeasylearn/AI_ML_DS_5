import tensorflow as tf 
from tensorflow.keras.layers import Dense
#create model 
model = tf.keras.Sequential([
    Dense(4,activation='relu',input_shape=(3,)),
    Dense(2,activation='relu'),
    Dense(1),
])

model.compile(optimizer='adam',loss='mse')
model.summary()