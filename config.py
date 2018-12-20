from lib.files import io
from lib.files import config_file

io_config   = io(config_file)

asks    = io_config.asks()

while True:
    print("Empty to end")
    ask_value= input("New ask [" + io_config.new_ask_index() + "]: ")
    if ask_value == "":
        break

    io_config.new_ask(ask_value)

    print()

io_config.write()

import predict
