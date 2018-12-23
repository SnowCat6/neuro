from lib.io_classes import io_config, io_data
from lib.io_classes import io, config_file, predict_file as data_file
from lib.cmd import Command

config   = io_config(config_file)
data     = io_data(data_file)

cmd=Command()
cmd.parse_arg(config, data)

profile = config.profile()
asks    = config.asks()

def fit(item_name):
    return data.fit_answers(config, item_name)

bOK = False
for item_name in data.entryes():
    bOK = fit(item_name) or bOK

if bOK:
    print()

print("Добавить запись в базу данных, пустая строка для завершения")
while True:
    input_title = "Название дя новой записи: "
    item_name   = input(input_title)
    if item_name == "":
        break
    
    fit(item_name)

data.write()

import predict
