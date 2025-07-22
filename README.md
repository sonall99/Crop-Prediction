# 🌾 Crop Prediction App

This is a web-based application built with **Streamlit** that helps predict the **most suitable crop** to sow based on current environmental conditions such as **soil parameters** and **weather data** for the selected location.

---

## 🚀 Features

- 📍 Interactive map to select your farming location based on your interest  
- ✏️ Manual coordinate input to check weather & best crop for that location  
- 🌐 Auto-detect current location using IP  
- 📊 Real-time weather & soil data fetching using APIs  
- 🤖 **Machine learning-based crop prediction** (Soul purpose of the app 😁)  
- 🌱 Displays environmental parameters:
  - Temperature  
  - Humidity  
  - Rainfall  
  - Soil pH  
  - Nitrogen  
  - Phosphorus  
  - Potassium  
- 📈 User-friendly layout for understanding each parameter  
- 📋 Clear prediction summary  
- 📄 Educational facts and dataset information included (see below)

---

## 📌 Technologies Used

- Python  
- Streamlit (UI)  
- Scikit-learn (ML Model)  
- Folium / Streamlit-Folium (Map integration)  
- Geopy / IPinfo API (Location detection)  
- OpenWeather & SoilGrids APIs (Environmental data)  
- Pandas, NumPy (Data handling and EDA)

---

## 🧠 ML Model

The model is trained using the **Crop Recommendation Dataset**, and predicts the best crop based on:

- Temperature (°C)  
- Humidity (%)  
- Rainfall (mm)  
- Soil pH (unitless)  
- Nitrogen (mg/kg)  
- Phosphorus (mg/kg)  
- Potassium (mg/kg)

---

## 🗺️ How to Use

1. Choose a method to enter your location:
   - Type coordinates manually  
   - Select from map (**My FAV 😋**)  
   - Auto-detect using IP  

2. Click **Submit**

3. View the **recommended crop** based on your soil & weather

4. Review the **parameters and prediction summary**

---

## ⚙️ Installation & Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/crop-prediction-app.git
cd crop-prediction-app
```
### 2.Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the app
```bash
streamlit run final_app.py
```
## ⚠️ Disclaimer

- Predictions are based on environmental data only  
- Please consult a professional agronomist before real-world implementation  
- Accuracy may vary depending on the API and data quality

---

## 👨‍💻 Author

**Sonal Singh**  
Built with ❤️ and ☕ using Streamlit  
Feel free to fork, star ⭐, or contribute!
