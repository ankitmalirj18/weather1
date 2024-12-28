import requests
from flask import Flask, request, render_template
from datetime import datetime


app = Flask(__name__)

l=[]
def weather(City):
    l.clear()
    api_key="b0a4dd6a0512fb9c37fc91441ebb35c6"
    api=f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={api_key}&units=metric"
    resp=requests.get(api)
    temp=resp.json()
    City=temp["name"]
    l.append(City)
    tempr=temp["main"]["temp"]
    l.append(tempr)
    speed=temp["wind"]["speed"]
    l.append(speed)
    visibility=temp["visibility"]
    l.append(visibility)
    humidity=temp["main"]["humidity"]
    l.append(humidity)
    pressure=temp["main"]["pressure"]
    l.append(pressure)
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    year=time[:4]
    month=time[5:7]
    day=time[8:10]
    if month > "10" or month < "3" :
        if time >= f"{year}-{month}-{day} 20:00:00 " or time < f"{year}-{month}-{day} 05:00:00 " :
            return "night1"
        elif time >= f"{year}-{month}-{day} 05:00:00 " and time < f"{year}-{month}-{day} 10:00:00 " :
            return "morning1"
        if time >= f"{year}-{month}-{day} 10:00:00 " and time < f"{year}-{month}-{day} 16:00:00 " :
            return "afternoon1"  
        if time >= f"{year}-{month}-{day} 16:00:00 " and time < f"{year}-{month}-{day} 20:00:00 " :
            return "evening1"
        
    elif month > "2" and month < "11" :
        if time >= f"{year}-{month}-{day} 21:00:00 " or time < f"{year}-{month}-{day} 04:00:00 " :
            return "night2"
        elif time >= f"{year}-{month}-{day} 04:00:00 " and time < f"{year}-{month}-{day} 09:00:00 " :
            return "morning2"
        if time >= f"{year}-{month}-{day} 09:00:00 " and time < f"{year}-{month}-{day} 17:00:00 " :
            return "afternoon2"
        if time >= f"{year}-{month}-{day} 17:00:00 " and time < f"{year}-{month}-{day} 21:00:00 " :
            return "evening2"
        
    else:
        return "------ the end of the world "
    




@app.route("/")
def home():
    url="https://ipinfo.io/json"
    response=requests.get(url).json()
    City=response["city"]
    weather(f"{City}")
    return render_template("index.html",c=l[0], t=l[1], s=l[2], h=l[3], v=l[4], p=l[5],i=weather(f"{City}"))


@app.route("/aftersearching/", methods=['GET','POST'])
def aftersearching():
    if request.method=="POST":
        City=request.form.get("search")
        weather(f"{City}")
        return render_template("index.html", c=l[0], t=l[1], s=l[2], h=l[3], v=l[4], p=l[5],i=weather(f"{City}"))


app.run(debug=True)