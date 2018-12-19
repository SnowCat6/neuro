from profile import Profille

profile=Profille("Предмет")
profile.load()

history=profile.fit()

#evaluate=profile.evaluate()
#print("score:", evaluate)

predict=profile.predict()
profile.print_predict(predict)
