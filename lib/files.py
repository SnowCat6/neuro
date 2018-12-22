import json
import numpy as np

config_file     = 'resp_config.json'
fit_file        = 'resp_fit.json'
predict_file    = 'resp_predict.json'

class io:
    def __init__(self, file_name):
        self.file_name = file_name
        self.encoding = 'utf-8-sig'
        self.arg_profile = ""
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

    def asks(self):
        try:
            return self.json["asks"]
        except:
            return {}

    def new_ask(self, ask_value):
        asks = self.asks()
        keys = list(asks.keys())
        if ask_value in keys:
            return

        asks[self.new_ask_index()] = ask_value

    def new_ask_index(self):
        asks = self.asks()
        keys = list(asks.keys())
        argMax=np.argmax(list(map(int, keys)))+1
        return str(argMax)

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

    def fit_answers(self, config, item_name):
        entry = self.entry(item_name)
        if "asks" in entry:
            return False

        print("Enter answers")
        x_train = []
        asks    = config.asks()
        for i in asks:
            answer=input("[" + item_name + "] " + i + " " + asks[i] + "?:n ")
            if (answer != "" and answer != "n"):
                x_train.append(i)

        entry["asks"]=x_train
        return True

    def fit_profile(self, item_name, profile):
        entry = self.entry(item_name)
        try:
            if profile in entry["profiles"]:
                return False
        except:
            pass

        print("Enter profile")
        profile_name = input("[" + profile + "]: " + item_name + " ")
        if profile_name == "":
            return False

        try:
            entry["profiles"][profile]=profile_name
        except:
            entry["profiles"] = { profile: profile_name}

        return True

    def profile(self, default_profile="Предмет"):
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

    def remove(self, profile):
        entryes = self.entryes()
        for item_name in entryes:
            try:
                entry = self.entry(item_name)
                del entry["profiles"][profile]
            except:
                pass

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