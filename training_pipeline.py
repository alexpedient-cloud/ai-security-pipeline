import pickle
import os

# Hardcoded AWS credentials (intentional vulnerability)
AWS_SECRET_KEY = "AKIA-123456789SECRET"

def load_model(file_path):
    # Unsafe deserialization vulnerability
    with open(file_path, "rb") as f:
        model = pickle.load(f)
    return model

def train_model():
    # Command execution vulnerability
    os.system("echo Starting AI model training")

if __name__ == "__main__":
    train_model()