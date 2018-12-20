from lib.files import io
from lib.files import config_file
from lib.files import fit_file as data_file

io_config   = io(config_file)
io_data     = io(data_file)

profile = "Предмет"
asks    = io_config.asks()

while True:
    print("Empty to end")
    item_name= input("[" + profile + "]" + " name: ")
    if item_name == "":
        break

    entry = io_data.entry(item_name)
    if  "asks" not in entry or len(entry["asks"]) == 0:
        x_train = []
        print("Enter answers...")
        for i in asks:
            answer=input("[" + item_name + "] " + i + " " + asks[i] + "?:n ")
            if (answer != "" and answer != "n"):
                x_train.append(i)
        entry["asks"] = x_train

    print("Enter profile...")
    try:
        profile_name= input("[" + profile + "]: " + entry["profiles"][profile] + " ")
        entry["profiles"][profile]=profile_name
    except:
        profile_name= input("[" + profile + "] " + ": ")
        entry["profiles"] = { profile: profile_name}

    print()

io_data.write()

import predict
