from pipelines.training_pipeline import train_pipeline
from zenml.client import Client

if __name__ == "__main__":
    # get path for mlflow
    # print(Client().active_stack.experiment_tracker.get_tracking_uri())
    # mlflow ui --backend-store-uri "file:C:\Users\MSI\AppData\Roaming\zenml\local_stores\111f84d9-ab92-4eea-9e5d-4828913d9353\mlruns"

    train_pipeline(data_path="data/olist_customers_dataset.csv")

