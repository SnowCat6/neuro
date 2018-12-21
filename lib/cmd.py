import sys, getopt

class Command:
    def parse_arg(self, config, data):
        argv = sys.argv[1:]

        bRemove=False
        bReNew=False
        config.bAppend=False

        try:
            opts, args = getopt.getopt(argv,"hp:rna",["profile="])
        except:
            return

        for opt, arg in opts:
            if opt == '-h':
                print ('use: -p <profile>')
                sys.exit()
            elif opt in ["-p", "--profile"]:
                config.set_profile(arg)
                config.write()
            elif opt in ["-r"]:
                bRemove=True
            elif opt in ["-n"]:
                bReNew=True
            elif opt in ["-a"]:
                config.bAppend=True

        sys.argv = [sys.argv[0]]

        if bRemove:
            print("Remove profile " + config.profile())
            data.remove(config.profile())
            data.write()
            sys.exit()

        if bReNew:
            print("Re-new " + config.profile())
            data.remove(config.profile())
