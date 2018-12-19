import json
from pprint import pprint
from keras.utils.np_utils import to_categorical
import numpy as np

# Importing the Keras libraries and packages
import keras
from keras import models
from keras import layers
from keras import optimizers

class Profille:
    def __init__(self, label):
        self.label = label

    def load(self, config_file='resp_config.json'):

        with open(config_file, encoding='utf-8-sig') as f:
            self.config_json = json.load(f)

        self.dim_x=len(self.config_json["asks"])

    def fit(self, data_file='resp_fit.json'):
        with open(data_file, encoding='utf-8-sig') as f:
            self.data_json = json.load(f)
        
        x_train = self.sequence_x()
        y_train = self.sequence_y()

        history = self.model().fit(x_train, y_train,
                    epochs=500,
                    verbose=0)

        return history

    def evaluate(self):
        x_train = self.sequence_x()
        y_train = self.sequence_y()
        return self.thisModel.evaluate(
                    x_train, y_train,
                    verbose=0)

    def predict(self, data_file='resp_predict.json'):
        with open(data_file, encoding='utf-8-sig') as f:
            self.data_json = json.load(f)

        x_train = self.sequence_x()
        return self.thisModel.predict(x_train)

    def sequence_x(self):
        x_train=[]
        for x in self.data_json:
            asks = self.data_json[x]["asks"]
            # in
            x=[0]*self.dim_x
            for ask in asks:
                x[ask] = 1.0
            x_train.append(x)
        return np.array(x_train)
        
    def sequence_y(self):

        y_train=[]
        self.labels={}
        
        for x in self.data_json:
            profiles=self.data_json[x]["profiles"]
            if self.label not in profiles:
                continue
            label=profiles[self.label]

            if label not in self.labels:
                self.labels[label]=len(self.labels)

        self.dim_y=len(self.labels)
    
        for x in self.data_json:
            profiles=self.data_json[x]["profiles"]
            if self.label not in profiles:
                continue
            label=profiles[self.label]
            # out
            y=to_categorical(self.labels[label], num_classes=self.dim_y)
            y_train.append(y)
        
        return np.array(y_train)

    def model(self):

        model = models.Sequential()

        model.add(layers.Dense(256, input_shape=(self.dim_x,) , activation='relu'))
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(256, activation='relu'))
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(self.dim_y, activation='softmax'))

        model.compile(loss='categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])
        
        self.thisModel = model

        return model

    def print_predict(self, value):

        profiles=[]
        for i in self.data_json:
            profiles.append(i)

        labels = dict((v,k) for k,v in self.labels.items())

        ii=0
        for x in value:
            ix=x.argmax()
            print(
                profiles[ii]+":",
                "\t", labels[ix],
                "\t", round(x[ix]*100, 1), "%")
            ii += 1

