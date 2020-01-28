# -*- coding: utf-8 -*-
import joblib
model = joblib.load('./infra.h5')

ratings = ['poor', 'negative', 'average', 'positive']


class Prediction():
    def predict(text):
        result = model.predict([text])[0]
        return ratings[result]


# The plot is romantic comedy boilerplate from start to finish
# it 's inoffensive and actually rather sweet
# There 's a lot of good material here , but there's also a lot of unsuccessful
# hard to dismiss -- moody , thoughtful
# I had a lot of problems with this movie
# Poignant and funny
# the plot weaves us into a complex web
# humor and eye-popping
# print(Prediction.predict('its wonderful'))
