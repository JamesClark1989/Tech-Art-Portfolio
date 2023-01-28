using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;
using TMPro;
using UnityEngine.UI;

public class SetupDataObject : MonoBehaviour
{
    // UI Elements
    [SerializeField] TMP_Text cityNameText;
    [SerializeField] TMP_Text degrees;
    [SerializeField] TMP_Text windSpeed;
    [SerializeField] TMP_Text rain;
    [SerializeField] string cityName;
    [SerializeField] Image weatherIcon;
    public string url;
    public DataVars json;
    [SerializeField] DataInteraction dataInteraction;

    // Weather Icons
    [SerializeField] Sprite sunSprite;
    [SerializeField] Sprite rainSprite;

    public void SetupData(string jsonData)
    {
        // Set variables in the Datavars class using jsonData
        json = JsonUtility.FromJson<DataVars>(jsonData);

        // Set the text using the data from the Datavars
        cityNameText.SetText(cityName);

        degrees.SetText(String.Format("{0:0.0#}", float.Parse(json.current_weather.temperature)) + "°c");
        windSpeed.SetText("Wind Speed: " + String.Format("{0:0.0#}", float.Parse(json.current_weather.windspeed)) + " km/h");

        int iterator = 0;
        foreach(string timeSlot in json.hourly.time){

            if(timeSlot == json.current_weather.time){
                break;
            }
            iterator++;
        }

        rain.SetText(String.Format("Rain: " + "{0:0.0#}", float.Parse(json.hourly.rain[iterator])) + "mm");

        if(float.Parse(json.hourly.rain[iterator]) > 0){
            weatherIcon.sprite = rainSprite;
        }

        dataInteraction.ShowData();
    }
    
}
