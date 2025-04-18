# views.py
from django.http import JsonResponse
import joblib
from .predict_labels import predict_nudge_label
import os
model_path = os.path.join(os.path.dirname(__file__), 'nudge_model.pkl')
from django.shortcuts import render

def homepage(request):
    return render(request, 'gentleremind.html')

# Load the model
model = joblib.load(model_path)

def predict_nudge(request):
    if request.method == "POST":
        input_text = request.POST.get('text')
        if input_text:
            prediction = predict_nudge_label(model, input_text)
            return JsonResponse({'nudge': prediction})
        else:
            return JsonResponse({'error': 'No text provided'}, status=400)
