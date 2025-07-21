import pickle

def P_prediction(N,Temp,RH,Ph,Rainfall):

    model = pickle.load(open("p_pred_model.pkl", "rb"))
    scaler = pickle.load(open("p_pred_scaler.pkl", "rb"))

# Made by Sonal Singh
    Y_pred = model.predict(scaler.transform([[N,Temp,RH,Ph,Rainfall]]))
    return Y_pred