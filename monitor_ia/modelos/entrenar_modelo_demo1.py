import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense

# Crear modelo compatible con imágenes 2D (64x64 RGB)
model = Sequential([
    Input(shape=(64, 64, 3)),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(3, activation='softmax')  # 3 clases: atentos, distraídos, somnolientos
])

# Entrenamiento ficticio con datos aleatorios
X = np.random.rand(100, 64, 64, 3)           # 100 imágenes de entrada
y = np.random.randint(0, 3, size=(100,))     # 100 etiquetas entre 0 y 2
y = np.eye(3)[y]                              # One-hot encoding

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=3, verbose=1)

# Guardar modelo como distraction_model.hdf5
model.save("distraction_model.hdf5")
print("✅ Modelo de prueba guardado exitosamente.")
