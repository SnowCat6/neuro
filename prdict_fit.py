from lib.files import io, config_file, predict_file as data_file

io_config   = io(config_file)
io_data     = io(data_file)

profile = "Предмет"
asks    = io_config.asks()

def fit(item_name):
    if io_data.fit_answers(item_name):
        print()

for item_name in io_data.entryes():
    fit(item_name)

while True:
    print("Add new item, empty to end")
    item_name   = input("[" + profile + "]" + " name: ")
    if item_name == "":
        break
    
    fit(item_name)

io_data.write()

import predict
