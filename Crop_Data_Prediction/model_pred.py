import pickle

def model_func(Temperature,RH,PH,Rain):
    model = pickle.load(open("model.pkl", "rb"))

    scaler= pickle.load(open("scale.pkl", "rb"))

    list_ = pickle.load(open("model_dict.pkl", "rb"))

    Prediction = model.predict(scaler.transform([[Temperature,RH,PH,Rain]]))
    for crop,num in list_.items():
        if num == Prediction:
            Prediction_final = crop.upper()

    return Prediction_final