This Unity app will obtain weather data for all Australian capital cities using hte open-metro api found at the following link.

 https://open-meteo.com/en/docs#latitude=-37.81&longitude=144.96&hourly=temperature_2m,rain,showers,cloudcover&current_weather=true&timezone=Australia%2FSydney

It sets the variables of a DataVar class using json data collected from the api and uses those variables to set the Text of the data objects in the scene. The text will show an icon that shows if its raining or not, the current temperature, wind speed and rain fall in mm.

