import json
import numpy as np

from .files import io
from .files import config_file
from .files import fit_file
from .files import predict_file

# Importing the Keras libraries and packages
import keras
from keras import models
from keras import layers
from keras import optimizers
from keras.utils.np_utils import to_categorical

class Profille:
    def __init__(self, label):
        self.label = label

    def load(self, config_file=config_file):
        self.io_config = io(config_file)
        self.dim_x=len(self.io_config.asks())

    def fit(self, data_file=fit_file):
        self.io_data = io(data_file)
        
        x_train = self.sequence_x()
        y_train = self.sequence_y()

        history = self.model().fit(x_train, y_train,
                    epochs=1000,
                    verbose=0)

        return history

    def evaluate(self):
        x_train = self.sequence_x()
        y_train = self.sequence_y()
        return self.thisModel.evaluate(
                    x_train, y_train,
                    verbose=0)

    def predict(self, data_file=predict_file):
        self.io_data = io(data_file)

        x_train = self.sequence_x()
        return self.thisModel.predict(x_train)

    def sequence_x(self):
        x_train=[]
        all_asks=list(self.io_config.asks().keys())

        entryes = self.io_data.entryes()
        for x in entryes:
            asks = entryes[x]["asks"]
            x=[0]*self.dim_x
            for ask in asks:
                ask_ix = all_asks.index(ask)
                x[ask_ix] = 1.0

            x_train.append(x)

        return np.array(x_train)
        
    def sequence_y(self):

        y_train=[]
        self.labels={}
        
        entryes = self.io_data.entryes()
        for x in entryes:
            profiles=entryes[x]["profiles"]
            if self.label not in profiles:
                continue
            label=profiles[self.label]

            if label not in self.labels:
                self.labels[label]=len(self.labels)

        self.dim_y=len(self.labels)
    
        entryes = self.io_data.entryes()
        for x in entryes:
            profiles=entryes[x]["profiles"]
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
        entryes = self.io_data.entryes()
        for i in entryes:
            profiles.append(i)

        labels = dict((v,k) for k,v in self.labels.items())

        ii=0
        for x in value:
            args=np.argsort(-x)
            ix  = args[0]
            ix2 = args[1]
            print(
                profiles[ii].ljust(20),
                (labels[ix] + " (" + str(round(x[ix]*100, 1)) + "%)").ljust(20),
                (labels[ix2]+ " (" + str(round(x[ix2]*100, 1))+ "%)").ljust(20)
                )
            ii += 1

