from lib.io_classes import io_config, io_fit_data
from lib.io_classes import config_file, fit_file as data_file
from lib.cmd import Command

config   = io_config(config_file)
data     = io_fit_data(data_file)

cmd = Command()
cmd.parse_arg(config, data)

asks    = config.asks()
print("Добавление новых вопросов, пустая строка для завешения")
while True:
    input_title ="Новый вопрос: "
    ask_value   = input(input_title)
    if ask_value == "":
        break

    config.new_ask(ask_value)

config.write()

import classify
