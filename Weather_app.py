import streamlit as st
import requests
from datetime import datetime 
API_KEY="e34ec4da8155335c212f1823a7c031f2"


st.set_page_config(page_title="Weather App", page_icon="🌦️")

st.title("🌦️ Live Weather App")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    with st.spinner("Fetching weather data..."):
        response = requests.get(url)
        data = response.json()

    if data["cod"] == 200:

        st.success(f"Weather in {data['name']}")
        current_time = datetime.now()

        st.write("📅 Date:", current_time.strftime("%d-%m-%Y"))
        st.write("🕒 Time:", current_time.strftime("%I:%M:%S %p"))
        #icon = data["weather"][0]["icon"]
        #st.image(f"https://openweathermap.org/img/wn/{icon}@2x.png")

        st.metric("🌡️ Temperature", f"{data['main']['temp']} °C")
        st.metric("🤗 Feels Like", f"{data['main']['feels_like']} °C")
        st.metric("💧 Humidity", f"{data['main']['humidity']} %")
        st.metric("🌬️ Wind Speed", f"{data['wind']['speed']} m/s")

        st.write(f"🌍 Country: {data['sys']['country']}")
        st.write(f"☁️ Weather: {data['weather'][0]['description']}")
        st.write(f"👀 Visibility: {data['visibility']/1000} km")
        st.write(f"📊 Pressure: {data['main']['pressure']} hPa")
    else:
        st.error("❌ City not found. Please enter a valid city name.")