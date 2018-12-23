from lib.io_classes import io_config, io_data
from lib.io_classes import io, config_file, fit_file, predict_file
from lib.profile import Profille
from lib.cmd import Command

config       = io_config(config_file)
fit_data     = io_data(fit_file)
predict_data = io_data(predict_file)

cmd=Command()
cmd.parse_arg(config, fit_data)
profile     = config.profile()

cnn_profile = Profille()
cnn_profile.load(config, fit_data, predict_data)

print("Обучение по референту {0}".format(profile))
history=cnn_profile.fit()
if history  is  None:
    print("Нет референтов")
else:
    #evaluate=profile.evaluate()
    #print("score:", evaluate)

    print("Соответствия по референту {0} ".format(profile))
    print("Запись в БД".ljust(20), "Вероятность макс.".ljust(20), "Вероятность след.".ljust(20))
    print("===========".ljust(20), "=================".ljust(20), "=================".ljust(20))
    predict=cnn_profile.predict()
    cnn_profile.print_predict(predict)

print()
input("Нажмите хоть что-то для выхода...")

