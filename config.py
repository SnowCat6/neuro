from lib.files import io, config_file

io_config   = io(config_file)

asks    = io_config.asks()

print("Empty to end")
while True:
    ask_value= input("New ask [" + io_config.new_ask_index() + "]: ")
    if ask_value == "":
        break

    io_config.new_ask(ask_value)

    print()

io_config.write()

import predict
