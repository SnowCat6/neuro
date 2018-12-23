from lib.io_classes import io_config, io_fit_data
from lib.io_classes import config_file, fit_file as data_file
from lib.cmd import Command

config   = io_config(config_file)
data     = io_fit_data(data_file)

cmd = Command()
cmd.parse_arg(config, data)

print("Записи для обучения")
print()

profile = config.profile()

def fit(item_name):
    bOK = data.fit_answers(config, item_name)
    bOK = data.fit_profile(item_name,profile) or bOK
    return bOK

bOK = False
for item_name in data.entryes():
    bOK = fit(item_name) or bOK

if bOK:
    print()

print("Создать нофую референтную запись, пустая строка для завершения")
while True:
    input_title="Имя для нового референта: "
    item_name= input(input_title)
    if item_name == "":
        break

    fit(item_name)

data.write()

import classify
