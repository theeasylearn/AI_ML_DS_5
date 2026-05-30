import tensorflow as tf
from tensorflow.keras import layers
# Model combining all requested layers
model = tf.keras.Sequential([
    
    # 1. Embedding layer (for text input)
    # input_dim: Vocabulary size
    # output_dim: Size of the dense embedding
    # input_length: Length of input sequences
    layers.Embedding(input_dim=1000, output_dim=64, input_length=10),
    # 2. Reshape to make it compatible for Conv2D
    # Conv2D expects (height, width, channels)
    layers.Reshape((10, 64, 1)),
    # 3. Conv2D layer
    # 32 filters, 3x3 kernel size
    layers.Conv2D(32, (3, 3), activation='relu'),
    
    # 4. MaxPooling layer
    # Downsamples the input representation
    layers.MaxPooling2D(pool_size=(2, 2)),
    
    # 5. Flatten layer
    # Flattens the multi-dimensional output to 1D
    layers.Flatten(),
    
    # 6. Dense layer
    # Fully connected layer with 64 units
    layers.Dense(64, activation='relu'),
    
    # 7. Dropout layer
    # Regularization to prevent overfitting
    layers.Dropout(0.5),
    
    # 8. Output layer
    # Single unit with sigmoid for binary classification
    layers.Dense(1, activation='sigmoid')
])
# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# Show summary
model.summary()