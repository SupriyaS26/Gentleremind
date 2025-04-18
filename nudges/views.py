from django.http import JsonResponse
import json
import os
import joblib
from . import views

from gentleremind.predict_labels import predict_nudge_label  # adjust if needed


def predict_nudge(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            input_text = data.get('text', '')  # assumes your POST includes JSON with { "text": "your input" }

            if not input_text:
                return JsonResponse({'error': 'Missing "text" in request'}, status=400)

            prediction = predict_nudge_label(input_text)
            return JsonResponse({'result': 'success', 'prediction': prediction})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Only POST allowed'}, status=405)
