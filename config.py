from lib.io_classes import io_config, io_data
from lib.io_classes import config_file

config   = io_config(config_file)
asks    = config.asks()

print("Добавление новых вопросов, пустая строка для завешения")
while True:
    input_title ="Новый вопрос: "
    ask_value   = input(input_title)
    if ask_value == "":
        break

    config.new_ask(ask_value)

config.write()

import predict
