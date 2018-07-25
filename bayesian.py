import numpy as np
from matplotlib import pyplot as plt


class naiveBayesian():
    def __init__(self):

    def features_count(training_data):
        row, column = training_data.shape
        features_num = []
        for i in range(column):
            features = set(training_data[:, i])
            features_num.append(len(features))
        return features_num

    def labels_count(labels):
        label = set(labels.reshape((1, -1)).tolist()[0])
        labels_num = {}
        for l in label:
            labels_num[str(l)] = sum(labels == l.tolist()[0])
        return labels_num

    def train(training_data, labels):
        row, column = training_data.shape
        features_num = self.features_count(training_data)
        labels_num = self.labels_count(labels)
        return features_num, labels_num

