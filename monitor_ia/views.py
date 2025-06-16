# monitor_ia/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import numpy as np
import cv2
from monitor_ia.deteccion import analizar_imagen

@csrf_exempt
def analizar_frame(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        if 'imagen' not in data:
            return JsonResponse({'error': 'No se recibió imagen'}, status=400)

        import json
        data_json = json.loads(data)
        imagen_base64 = data_json.get('imagen', '')
        if not imagen_base64:
            return JsonResponse({'error': 'Imagen vacía'}, status=400)

        header, encoded = imagen_base64.split(',', 1)
        img_bytes = base64.b64decode(encoded)
        nparr = np.frombuffer(img_bytes, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        print("Frame recibido y analizado")

        resultados = analizar_imagen(frame)
        return JsonResponse(resultados)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
