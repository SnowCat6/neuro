import utils
import json

# Importing the Keras libraries and packages
import keras
from keras import models
from keras import layers
from keras import optimizers

with open('resp.json', encoding='utf-8-sig') as f:
    config_json = json.load(f)

with open('resp_data.json', encoding='utf-8-sig') as f:
    data_json = json.load(f)

x_train, y_train = utils.make_sequence(config_json, data_json, "Профессия")
x_inputs = len(x_train[0])
y_inputs = len(y_train[0])

model = models.Sequential()
model.add(layers.Dense(256, input_shape=(x_inputs,) , activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(y_inputs, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#plot_model(model, to_file='model.png', show_shapes=True)

history = model.fit(x_train, y_train,
                    epochs=80,
                    verbose=0)

print(x_train)
print(y_train)

print("score:", model.evaluate(x_train, y_train, batch_size=128))

predict=model.predict(x_train)
print(predict)
utils.print_predict(predict, config_json, "Профессия")
