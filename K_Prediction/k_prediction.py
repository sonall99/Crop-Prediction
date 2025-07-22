import pickle

def K_prediction(N,Temp,RH,Ph,Rainfall,P):

    model = pickle.load(open("K_Prediction/K_pred_model.pkl", "rb"))

    scaler = pickle.load(open("K_Prediction/K_pred_scale.pkl", "rb"))


    Y_pred = model.predict(scaler.transform([[N,Temp,RH,Ph,Rainfall,P]]))
    return Y_pred