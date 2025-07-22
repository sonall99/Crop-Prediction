import pickle

def model_func(Temperature, RH, PH, Rain):
    import pickle
    model = pickle.load(open("model.pkl", "rb"))
    scaler = pickle.load(open("scale.pkl", "rb"))
    list_ = pickle.load(open("model_dict.pkl", "rb"))

    # Unpack the predicted class label from array
    Prediction = model.predict(scaler.transform([[Temperature, RH, PH, Rain]]))[0]

    # Safely map label to crop name
    Prediction_final = None
    for crop, num in list_.items():
        if num == Prediction:
            Prediction_final = crop.upper()
            break  # No need to continue loop

    if Prediction_final is None:
        raise ValueError("Predicted crop not found in label dictionary")

    return Prediction_final