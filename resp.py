from profile import Profille

profile=Profille("Профессия")
profile.load()

history=profile.fit()
#print("score:", profile.evaluate())
predict=profile.predict()
#print(predict)
profile.print_predict(predict)
