import json
import numpy as np

from .io_classes import io_config, io_data

# Importing the Keras libraries and packages
import keras
from keras import models, layers, optimizers
from keras.utils.np_utils import to_categorical

class Profille:
    def load(self, config : io_config, io_fit_data : io_data, io_prdict_data : io_data):
        self.io_config      = config
        self.io_fit_data    = io_fit_data
        self.io_prdict_data = io_prdict_data
        self.label          = config.profile()

        self.dim_x          = len(self.io_config.asks())

    def fit(self):
        self.io_data = self.io_fit_data
        
        x_train = self.sequence_x(True)
        y_train = self.sequence_y()
#        print(x_train)
#        print(y_train)

        if self.dim_x == 0 or self.dim_y == 0:
            return None

        return self.model().fit(x_train, y_train,
                    epochs=200,
                    verbose=0)

    def evaluate(self):
        x_train = self.sequence_x(True)
        y_train = self.sequence_y()
        return self.thisModel.evaluate(x_train, y_train,
                    verbose=0)

    def predict(self):
        self.io_data = self.io_prdict_data

        x_train = self.sequence_x(False)
#        print(x_train)

        return self.thisModel.predict(x_train)

    # fit and predict shape
    def sequence_x(self, bCheckProfile):
        x_train=[]
        # Get all ask keys for check exists answers
        all_asks=list(self.io_config.asks().keys())

        entryes = self.io_data.entryes()
        # for each item
        for x in entryes:
            try:
                if bCheckProfile:
                    entryes[x]["profiles"][self.label]
                asks = entryes[x]["asks"]
                x=[0]*self.dim_x
                # for each answers search ask
                for ask in asks:
                    ask_ix = all_asks.index(ask)
                    x[ask_ix] = 1.0

                x_train.append(x)
            except:
                continue

        return np.array(x_train)
    
    # fit shape
    def sequence_y(self):
        self.labels=self.io_data.labels(self.label)
        self.dim_y=len(self.labels)
   
        y_train=[]
        entryes = self.io_data.entryes()
        for x in entryes:
            try:
                label=entryes[x]["profiles"][self.label]
                y=to_categorical(self.labels[label], num_classes=self.dim_y)
                y_train.append(y)
            except:
                continue
        
        return np.array(y_train)

    def model(self):
        self.thisModel = models.Sequential()

        self.thisModel.add(layers.Dense(256, input_shape=(self.dim_x,) , activation='relu'))
        self.thisModel.add(layers.Dropout(0.5))
        self.thisModel.add(layers.Dense(256, activation='relu'))
        self.thisModel.add(layers.Dropout(0.5))
        self.thisModel.add(layers.Dense(self.dim_y, activation='softmax'))

        self.thisModel.compile(loss='categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])
        
        return self.thisModel

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

