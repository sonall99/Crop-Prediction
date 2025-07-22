import pickle

def model_func(Temperature, RH, PH, Rain):
    import pickle
    model = pickle.load(open("Crop_Data_Prediction/model.pkl", "rb"))
    scaler = pickle.load(open("Crop_Data_Prediction/scale.pkl", "rb"))
    list_ = pickle.load(open("Crop_Data_Prediction/model_dict.pkl", "rb"))


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