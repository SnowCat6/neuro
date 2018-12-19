import json

config_file = 'resp_config.json'
data_file   = 'resp_fit.json'

with open(config_file, encoding='utf-8-sig') as f:
    try:
        config_json = json.load(f)
    except:
        config_json = {}

with open(data_file, encoding='utf-8-sig') as f:
    try:
        data_json = json.load(f)
    except:
        data_json = {}

profile     = "Предмет"
while True:
    print("Empty to end")
    profile_name= input("[" + profile + "]" + " name: ")
    item_name   = profile_name
    if profile_name == "":
        break

    asks    = config_json["asks"]
    x_train = []

    for i in asks:
        answer=input("[" + profile_name + "] " + asks[i] + "?:n ")
        if (answer == "y"):
            x_train.append(int(i))

    if item_name not in data_json:
        data_json[item_name] = {}

    if "profiles" not in data_json[item_name]:
        data_json[item_name]["profiles"]={}

    if "asks" not in data_json[item_name]:
        data_json[item_name]["asks"]=[]

    data_json[item_name]["profiles"][profile]=profile_name
    data_json[item_name]["asks"]=x_train

    print()

with open(data_file, "w", encoding='utf-8-sig') as f:
    val=json.dumps(data_json, ensure_ascii=False, indent=4, sort_keys=True)
    f.write(val)
