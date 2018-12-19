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

    def load(self, config_file='resp.json'):

        with open(config_file, encoding='utf-8-sig') as f:
            self.config_json = json.load(f)

    def fit(self, data_file='resp_data.json'):
        with open(data_file, encoding='utf-8-sig') as f:
            self.data_json = json.load(f)
        
        x_train, y_train = self.sequence()
        history = self.model().fit(x_train, y_train,
                    epochs=500,
                    verbose=0)

        return history

    def evaluate(self):
        x_train, y_train = self.sequence()
        return self.thisModel.evaluate(x_train, y_train)

    def predict(self, data_file='resp_data.json'):
        with open(data_file, encoding='utf-8-sig') as f:
            self.data_json = json.load(f)

        x_train, _ = self.sequence()
        return self.thisModel.predict(x_train)

    def dims(self):
        input_askes_len = len(self.config_json["asks"])
        output_types_len= len(self.config_json["profiles"][self.label])
        return(input_askes_len, output_types_len)

    def sequence(self):
        x_train=[]
        y_train=[]
        input_askes_len, output_types_len = self.dims()
        
        for x in self.data_json:
            asks = self.data_json[x]["asks"]
            profiles = self.data_json[x]["profiles"]
            # in
            x=[0]*input_askes_len
            for ask in asks:
                x[ask] = 1.0
            x_train.append(x)
            # out
            label_ix = profiles[self.label]
            y_train.append(to_categorical(label_ix, num_classes=output_types_len))

        x_train=np.array(x_train)
        y_train=np.array(y_train)

        return (x_train, y_train)

    def model(self):
        x_inputs, y_inputs = self.dims()

        model = models.Sequential()
        model.add(layers.Dense(256, input_shape=(x_inputs,) , activation='relu'))
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(256, activation='relu'))
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(y_inputs, activation='softmax'))
        model.compile(loss='categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])
        
        self.thisModel = model

        return model

    def print_predict(self, value):
        labels=self.config_json["profiles"][self.label]

        for x in value:
            ix=x.argmax()
            print(labels[str(ix)], ":\t", round(x[ix]*100, 1), "%")
