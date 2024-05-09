pip install "zenml["server"]"
zenml up --blocking
zenml integration install mlflow -y
zenml experiment-tracker register mlflow_tracker --flavor=mlflow



# 


# Predicting how a customer will feel about a product before they even ordered it

**Problem statement**: For a given customer's historical data, we are tasked to predict the review score for the next order or purchase.(https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

## INSTALLATIONS
```
pip install requirements.txt
pip install "zenml["server"]"
zenml integration install mlflow -y

```

Run zenml
```
zenml up --blocking
zenml experiment-tracker register mlflow_tracker --flavor=mlflow [register mlflow tracker]
zenml stack register mlflow_stack -a default -o default -d mlflow -e mlflow_tracker --set
zenml stack describe [check stack]
```

Run mlflow
```
mlflow ui --backend-store-uri "file:C:\Users\MSI\AppData\Roaming\zenml\local_stores\111f84d9-ab92-4eea-9e5d-4828913d9353\mlruns"
run_pipeline.py printing path there, for me its -> "file:C:\Users\MSI\AppData\Roaming\zenml\local_stores\111f84d9-ab92-4eea-9e5d-4828913d9353\mlruns"
```

- Training pipeline:

```
python run_pipeline.py
```

- The continuous deployment pipeline:

```
python run_deployment.py
```





### Training Pipeline

- `ingest_data`: This step will ingest the data and create a `DataFrame`.
- `clean_data`: This step will clean the data and remove the unwanted columns.
- `train_model`: This step will train the model and save the model using [MLflow autologging](https://www.mlflow.org/docs/latest/tracking.html).
- `evaluation`: This step will evaluate the model and save the metrics -- using MLflow autologging -- into the artifact store.

### Deployment Pipeline

- `deployment_trigger`: The step checks whether the newly trained model meets the criteria set for deployment.
- `model_deployer`: This step deploys the model as a service using MLflow (if deployment criteria is met).

ISSUES
1. When running the continuous deployment pipeline, I get an error stating: `No Step found for the name mlflow_deployer`.

   Solution: It happens because your artifact store is overridden after running the continuous deployment pipeline. So, you need to delete the artifact store and rerun the pipeline. You can get the location of the artifact store by running the following command:

   ```bash
   zenml artifact-store describe
   ```

   and then you can delete the artifact store with the following command:

   **Note**: This is a dangerous / destructive command! Please enter your path carefully, otherwise it may delete other folders from your computer.

   ```bash
   rm -rf PATH
   ```

2. When running the continuous deployment pipeline, I get the following error: `No Environment component with name mlflow is currently registered.`

   Solution: You forgot to install the MLflow integration in your ZenML environment. So, you need to install the MLflow integration by running the following command:

   ```bash
   zenml integration install mlflow -y
   ```
