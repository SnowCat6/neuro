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
        
    def entryes(self):
        return self.json

    def entry(self, entry_name):
        entryes = self.entryes()
        if entry_name not in entryes:
            entryes[entry_name] = {}

        return entryes[entry_name]
