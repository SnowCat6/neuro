import json
from pprint import pprint
from keras.utils.np_utils import to_categorical
import numpy as np

def make_vector(json_elm, vector_size):
    result=[0]*vector_size
    for i in json_elm:
        result[int(i)] = float(json_elm[i])
    return result

def make_sequence(json, data_json, label):
    x_train=[]
    y_train=[]

    input_askes_len = len(json["asks"])
    output_types_len= len(json["profiles"][label])
    
    for x in data_json:
        asks = data_json[x]["asks"]
        profiles = data_json[x]["profiles"]
        # in
        x_train.append(make_vector(asks, input_askes_len))
        # out
        label_ix = profiles[label]
        y_train.append(to_categorical(label_ix, num_classes=output_types_len))

    x_train=np.array(x_train)
    y_train=np.array(y_train)

    return (x_train, y_train)

def print_predict(predict, json, label):
#    recepients=json["recepients"].keys()
    labels=json["profiles"][label]

    for x in predict:
        ix=x.argmax()
        print(labels[str(ix)], ":\t", round(x[ix]*100, 1), "%")
