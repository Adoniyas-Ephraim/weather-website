from flask import Flask, render_template, request, flash
import requests
import socket

app = Flask(__name__)
app.secret_key="manbearpig_MUDMAN888"

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/weather", methods=["POST", "GET"])
def weather():
    location = request.form['location_input']
    location = str(location).rstrip()
    api_key = '30d4741c779ba94c470ca1f63045390a'

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        print(f"\n[-] No City Found {location}\n")
        flash(f"Unable to find {location}")
        try:
            print(f'USER: {socket.gethostname()}\n')
        except:
            print('error')
    else:
        weather = weather_data.json()['weather'][0]['description']
        temp = round(weather_data.json()['main']['temp'])
        try:
            print(f'\n USER: {socket.gethostname()}')
        except:
            print('error')
        print(f'\n[+] location: {location} weather: {weather}, temperature: {temp}\n')
        flash(f"It's {weather} in {location}")
        flash(f"The temperature in {location} is {temp}ºF")
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True,)