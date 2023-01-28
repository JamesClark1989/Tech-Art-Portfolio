WINDOW_WIDTH, WINDOW_HEIGHT = 900, 700

cities = {
    "Brisbane":{
        "name": "Brisbane",
        "pos" : (760,270),
        "address" : r"https://api.open-meteo.com/v1/forecast?latitude=-27.47&longitude=153.03&hourly=temperature_2m,relativehumidity_2m,rain,cloudcover&daily=weathercode,rain_sum,showers_sum&current_weather=true&timezone=auto"
    },
    "Sydney":{
        "name": "Sydney",
        "pos" : (700,360),
        "address" : r"https://api.open-meteo.com/v1/forecast?latitude=-33.87&longitude=151.21&hourly=temperature_2m,relativehumidity_2m,rain,cloudcover&models=best_match&daily=weathercode,rain_sum,showers_sum&current_weather=true&timezone=auto"
    },
    "Melbourne":{
        "name": "Melbourne",
        "pos" : (610,420),
        "address" : r"https://api.open-meteo.com/v1/forecast?latitude=-37.81&longitude=144.96&hourly=temperature_2m,relativehumidity_2m,rain,cloudcover&models=best_match&daily=weathercode,rain_sum,showers_sum&current_weather=true&timezone=auto"
    },
    "Hobart":{
        "name": "Hobart",
        "pos" : (650,480),
        "address" : r"https://api.open-meteo.com/v1/forecast?latitude=-42.88&longitude=147.33&hourly=temperature_2m,relativehumidity_2m,rain,cloudcover&models=best_match&daily=weathercode,rain_sum,showers_sum&current_weather=true&timezone=auto"
    },
    "Adelaide":{
        "name": "Adelaide",
        "pos" : (525,350),
        "address" : r"https://api.open-meteo.com/v1/forecast?latitude=-34.93&longitude=138.60&hourly=temperature_2m,relativehumidity_2m,rain,cloudcover&models=best_match&daily=weathercode,rain_sum,showers_sum&current_weather=true&timezone=auto"
    },
    "Perth":{
        "name": "Perth",
        "pos" : (170,345),
        "address" : r"https://api.open-meteo.com/v1/forecast?latitude=-31.95&longitude=115.86&hourly=temperature_2m,relativehumidity_2m,rain,cloudcover&models=best_match&daily=weathercode,rain_sum,showers_sum&current_weather=true&timezone=auto"
    },
    "Darwin":{
        "name": "Darwin",
        "pos" : (390,30),
        "address" : r"https://api.open-meteo.com/v1/forecast?latitude=-12.46&longitude=130.84&hourly=temperature_2m,relativehumidity_2m,rain,cloudcover&models=best_match&daily=weathercode,rain_sum,showers_sum&current_weather=true&timezone=auto"
    },
}
