import os
import numpy as np
import cv2
from django.conf import settings
from tensorflow.keras.models import load_model

# ==== CAMBIO: Solo accede a settings si Django está configurado ====
def get_model_paths():
    try:
        base_dir = settings.BASE_DIR
    except Exception:
        # Si settings no está configurado, usa ruta relativa como fallback
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_modelos = os.path.join(base_dir, 'monitor_ia', 'modelos')
    return {
        "distraction": os.path.join(ruta_modelos, 'distraction_model.hdf5'),
        "hopenet": os.path.join(ruta_modelos, 'hopenet_robust_alpha1.pkl'),
        "dlib": os.path.join(ruta_modelos, 'shape_predictor_68_face_landmarks.dat')
    }

PATHS = get_model_paths()

# ==== Cargar modelo Keras sin recompilar ====
try:
    modelo_distraction = load_model(PATHS["distraction"], compile=False)
    print("✅ Modelo Keras cargado correctamente")
except Exception as e:
    print("❌ Error cargando el modelo Keras:", e)
    modelo_distraction = None

# ==== Lógica real de predicción ====
def analizar_imagen(frame):
    if modelo_distraction is None:
        return {
            "atentos": 0,
            "distraidos": 0,
            "somnolientos": 0,
            "error": "Modelo no cargado"
        }

    try:
        # Preprocesamiento: redimensionar, normalizar y expandir
        frame = cv2.resize(frame, (64, 64))             # Asegura tamaño correcto
        frame = frame / 255.0                           # Normaliza a rango 0-1
        frame = np.expand_dims(frame, axis=0)           # (1, 64, 64, 3)

        # Predicción
        pred = modelo_distraction.predict(frame)        # Resultado: [[0.6, 0.2, 0.2]]
        atentos, distraidos, somnolientos = pred[0]

        return {
            "atentos": round(float(atentos * 100), 2),
            "distraidos": round(float(distraidos * 100), 2),
            "somnolientos": round(float(somnolientos * 100), 2)
        }

    except Exception as e:
        print("❌ Error durante el análisis:", e)
        return {
            "atentos": 0,
            "distraidos": 0,
            "somnolientos": 0,
            "error": str(e)
        }
