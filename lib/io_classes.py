import json
import numpy as np

config_file     = 'resp_config.json'
fit_file        = 'resp_fit.json'
predict_file    = 'resp_predict.json'

class io:
    def __init__(self, file_name):
        self.file_name = file_name
        self.encoding = 'utf-8-sig'
        self.load()

    def load(self):
        try:
            with open(self.file_name, encoding=self.encoding) as f:
                self.json = json.load(f)
        except:
            self.json = {}

    def write(self):
        try:
            with open(self.file_name, "w", encoding=self.encoding) as f:
                val=json.dumps(self.json, ensure_ascii=False, indent=4, sort_keys=True)
                f.write(val)
        finally:
            return

class io_config(io):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.arg_profile = ""

    def profile(self, default_profile="Объект"):
        try:
            if self.arg_profile != "":
                return self.arg_profile
        except:
            pass

        try:
            return self.json["default_profile"]
        except:
            return default_profile

    def set_profile(self, profile):
        self.json["default_profile"] = profile

    def asks(self):
        try:
            return self.json["asks"]
        except:
            self.json["asks"] = {}
            return self.json["asks"]

    def new_ask(self, ask_value):
        asks = self.asks()
        keys = list(asks.values())
        if ask_value in keys:
            return

        askIx = self.new_ask_index()
        asks[askIx] = ask_value

    def new_ask_index(self):
        try:
            asks = self.asks()
            keys = list(asks.keys())
            argMax=np.argmax(list(map(int, keys)))+1
            return str(argMax)
        except:
            return str(0)

class io_data(io):
    def __init__(self, file_name):
        super().__init__(file_name)

    def labels(self, label):
        labels={}
        entryes = self.entryes()
        for x in entryes:
            try:
                l=entryes[x]["profiles"][label]
                if l in labels:
                    continue
                labels[l]=len(labels)
            except:
                continue

        return labels

    def entryes(self):
        return self.json

    def entry(self, entry_name):
        entryes = self.entryes()
        try:
            return entryes[entry_name]
        except:
            entryes[entry_name] = {}
        finally:
            return entryes[entry_name]

    def profiles(self):
        result=set()
        entryes=self.entryes()
        for x in entryes:
            try:
                for profile in entryes[x]["profiles"]:
                    result.add(profile)
            except:
                pass
        return result      

    def fit_answers(self, config : io_config, item_name):
        entry = self.entry(item_name)
        if "asks" in entry:
            return False

        print("Введите ответы для {0}".format(item_name))
        x_train = []
        asks    = config.asks()
        for i in asks:
            input_title = "{0} {2} (y/n): ".format(item_name, i, asks[i])
            answer=input(input_title)
            if (answer != "" and answer != "n"):
                x_train.append(i)

        entry["asks"]=x_train
        return True

    def remove_profile(self, profile):
        entryes = self.entryes()
        for item_name in entryes:
            try:
                entry = self.entry(item_name)
                del entry["profiles"][profile]
            except:
                pass

class io_fit_data(io_data):
    def __init__(self, file_name):
        super().__init__(file_name)

    def fit_profile(self, item_name, profile):
        entry = self.entry(item_name)
        try:
            if profile in entry["profiles"]:
                return False
        except:
            pass

#        print("Введите опеределение {0} для {1}".format(profile, item_name))
        input_title = "На сколько {1} {0}?: ".format(profile, item_name)
        profile_name= input(input_title)
        if profile_name == "":
            return False

        try:
            entry["profiles"][profile]=profile_name
        except:
            entry["profiles"] = { profile: profile_name}

        return True
