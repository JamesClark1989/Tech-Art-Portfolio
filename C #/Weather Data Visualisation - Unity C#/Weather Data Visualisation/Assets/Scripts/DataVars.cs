using System;
using System.Collections.Generic;
using UnityEngine;

[Serializable]
public class DataVars
{    
    public string latitude;
    public string elevation;
    public curWeather current_weather;
    public hrly hourly;

}

[Serializable]
public class curWeather{
    public string temperature;
    public string windspeed;
    public string winddirection;
    public string time;
}

[Serializable] 
public class hrly{
    public List<string> time;
    public List<string> rain;
}
