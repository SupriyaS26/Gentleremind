# nudges/utils.py
import joblib

# Load the pre-trained model
model = joblib.load('nudges/models/nudge_model.pkl')

def predict_nudge_label(input_text):
    pred = model.predict([input_text])[0]
    label_map = {
        0: "Take a short break",
        1: "Refocus on your task",
        2: "You're doing great!",
    }
    return label_map.get(pred, "Keep going!")
