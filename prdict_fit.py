from lib.files import io, config_file, predict_file as data_file
from lib.cmd import Command

io_config   = io(config_file)
io_data     = io(data_file)

cmd=Command()
cmd.parse_arg(io_config, io_data)

profile = io_config.profile()
asks    = io_config.asks()

def fit(item_name):
    if io_data.fit_answers(io_config, item_name):
        print()

for item_name in io_data.entryes():
    fit(item_name)

print("Добавить запись в базу данных, пустая строка для завершения".format(profile))
while True:
    input_title = "Название дя новой записи: ".format(profile)
    item_name   = input(input_title)
    if item_name == "":
        break
    
    fit(item_name)

io_data.write()

import predict
