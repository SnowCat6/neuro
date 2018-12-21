from lib.files import io, config_file, fit_file, predict_file
from lib.profile import Profille
from lib.cmd import Command

io_config       = io(config_file)
io_fit_data     = io(fit_file)
io_predict_data = io(predict_file)

cmd=Command()
cmd.parse_arg(io_config, io_fit_data)
profile     = io_config.profile()

cnn_profile = Profille()
cnn_profile.load(io_config, io_fit_data, io_predict_data)

print("Fit profile " + profile)
history=cnn_profile.fit()
if history  is  None:
    print("No entryes to fit")
    exit()

#evaluate=profile.evaluate()
#print("score:", evaluate)

print("Predict profile " + profile)
predict=cnn_profile.predict()
cnn_profile.print_predict(predict)
