from lib.files import io, config_file, fit_file as data_file
from lib.cmd import Command

io_config   = io(config_file)
io_data     = io(data_file)

cmd=Command()
cmd.parse_arg(io_config, io_data)

profile = io_config.profile()

def fit(item_name):
    bOK = io_data.fit_answers(item_name)
    bOK = io_data.fit_profile(item_name,profile) or bOK
    if bOK:
        print()

for item_name in io_data.entryes():
    fit(item_name)

print("Add new item, empty to end")
while True:
    item_name= input("[" + profile + "]" + " new name: ")
    if item_name == "":
        break

    fit(item_name)

io_data.write()

import predict
