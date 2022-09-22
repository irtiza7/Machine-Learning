import pandas as pd
import numpy as np

def read_dataset(dataset_choice):
    datasets = [
        r"./Bank_Customer_Churn_Prediction.csv",
        r"./Realestate.csv"
    ]

    if dataset_choice == 1:
        dataset = pd.read_csv(datasets[0], header=None, delimiter=",")
        dataset = dataset.drop('No', axis=1)
        print(dataset)
        dataset = dataset.to_numpy()
        #         print(dataset)
        #         print(dataset.shape)
        total_samples, total_features = dataset.shape
        #         print(total_samples, total_features)
        total_features -= 1
        total_classes = 10
    elif dataset_choice == 2:
        dataset = pd.read_csv(datasets[1], header=None, delimiter=",")
        dataset = dataset.to_numpy()
        total_samples, total_features = dataset.shape
        total_features -= 1
        total_classes = 3
    else:
        assert ("Invalid Dataset Choice")

    return (dataset, total_samples, total_features, total_classes)