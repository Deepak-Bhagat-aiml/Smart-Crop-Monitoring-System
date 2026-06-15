
import gradio as gr
import joblib
import pandas as pd

model = joblib.load("crop_monitoring_model.pkl")

def recommend_crop(temp, humidity, moisture, ph, nitrogen, phosphorus, potassium):

    sample = pd.DataFrame([{
        "Temperature": temp,
        "Humidity": humidity,
        "Soil_Moisture": moisture,
        "pH": ph,
        "Nitrogen": nitrogen,
        "Phosphorus": phosphorus,
        "Potassium": potassium
    }])

    prediction = model.predict(sample)

    if moisture < 40:
        irrigation = "Irrigation Required"
    elif moisture < 60:
        irrigation = "Monitor Soil Moisture"
    else:
        irrigation = "No Irrigation Required"

    return f"""
Recommended Crop: {prediction[0]}

Irrigation Status: {irrigation}
"""

interface = gr.Interface(
    fn=recommend_crop,
    inputs=[
        gr.Slider(0,50,value=25,label="Temperature (°C)"),
        gr.Slider(0,100,value=70,label="Humidity (%)"),
        gr.Slider(0,100,value=60,label="Soil Moisture (%)"),
        gr.Slider(0,14,value=6.5,label="pH"),
        gr.Slider(0,150,value=90,label="Nitrogen"),
        gr.Slider(0,150,value=50,label="Phosphorus"),
        gr.Slider(0,150,value=120,label="Potassium")
    ],
    outputs="text",
    title="Smart Crop Monitoring System",
    description="""
Simulation-Based IoT Crop Monitoring System

Features:
• Crop Recommendation
• Irrigation Monitoring
• Simulated IoT Sensors
• Future ESP32/Arduino Integration
"""
)

interface.launch()
