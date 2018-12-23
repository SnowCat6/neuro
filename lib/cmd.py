import sys, getopt
from .io_classes import io_config, io_data

class Command:
    def parse_arg(self, config : io_config, data : io_data):
        argv = sys.argv[1:]

        bRemove=False
        bReNew=False
        bList=False

        try:
            opts, args = getopt.getopt(argv,"hp:rnal",["profile="])
        except:
            return

        for opt, arg in opts:
            if opt == '-h':
                print ('use: -p <profile> [-r -n -l -h]')
                sys.exit()
            elif opt in ["-p", "--profile"]:
                config.set_profile(arg)
                config.write()
            elif opt in ["-r"]:
                bRemove=True
            elif opt in ["-n"]:
                bReNew=True
            elif opt in ["-l"]:
                bList=True
        sys.argv = [sys.argv[0]]

        if bList:
            print("List exists profiles:")
            for x in data.profiles():
                print(x)

        if bRemove:
            print("Remove profile " + config.profile())
            data.remove(config.profile())
            data.write()

        if bReNew:
            print("Re-new profile " + config.profile())
            data.remove(config.profile())
