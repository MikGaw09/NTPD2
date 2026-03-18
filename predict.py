import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris

mlflow.set_tracking_uri("http://localhost:5000")

run_id = "c136d73481a64d11b1ab90e4ae6b5add"
model_uri = f"runs:/{run_id}/model"

loaded_model = mlflow.sklearn.load_model(model_uri)
print("Model pobrany")

iris = load_iris()
sample_data = iris.data[0:1]
print("dane:", iris.target[0])
print("predykcja:", loaded_model.predict(sample_data))
print("prawdopodobienstwo:", loaded_model.predict_proba(sample_data))