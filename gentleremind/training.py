from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer  # or TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Example training data
texts = [
    "I need to check Instagram.",
    "I'm feeling very focused today.",
    "Maybe just one more YouTube video...",
    "I am ready to study now."
]
labels = [3, 2, 3, 2]  # Example labels

# Define pipeline
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),  # or TfidfVectorizer()
    ('classifier', LogisticRegression())
])

# Train the pipeline
pipeline.fit(texts, labels)

# Save the entire pipeline (not just the model!)
joblib.dump(pipeline, 'nudge_model.pkl')
print("Model saved as 'nudge_model.pkl'")
