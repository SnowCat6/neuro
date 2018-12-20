from lib.files import io
from lib.files import config_file
from lib.files import fit_file as data_file

io_config   = io(config_file)
io_data     = io(data_file)

profile = "Предмет"
asks    = io_config.asks()

while True:
    print("Empty to end")
    profile_name= input("[" + profile + "]" + " name: ")
    if profile_name == "":
        break

    x_train = []

    for i in asks:
        answer=input("[" + profile_name + "] " + i + " " + asks[i] + "?:n ")
        if (answer == "y"):
            x_train.append(i)

    entry = io_data.entry(profile_name)
    try:
        entry["profiles"][profile]=profile_name
    except:
        entry["profiles"] = { profile: profile_name}

    entry["asks"] = x_train

    print()

io_data.write()
