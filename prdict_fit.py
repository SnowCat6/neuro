from lib.files import io
from lib.files import config_file
from lib.files import predict_file as data_file

io_config   = io(config_file)
io_data     = io(data_file)

profile = "Предмет"
asks    = io_config.asks()

while True:
    print("Empty to end")
    item_name   = input("[" + profile + "]" + " name: ")
    if item_name == "":
        break

    x_train = []

    for i in asks:
        answer=input("[" + item_name + "] " + i + " " + asks[i] + "?:n ")
        if (answer != ""):
            x_train.append(i)

    entry = io_data.entry(item_name)
    entry["asks"]=x_train

    print()

io_data.write()
