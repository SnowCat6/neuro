from lib.files import io, config_file

io_config   = io(config_file)

asks    = io_config.asks()

print("Добавление новых вопросов, пустая строка для завешения")
while True:
    input_title="Новый вопрос: ".format(io_config.new_ask_index())
    ask_value= input(input_title)
    if ask_value == "":
        break

    io_config.new_ask(ask_value)

io_config.write()

import predict
