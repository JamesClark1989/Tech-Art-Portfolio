using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using TMPro;

public class WeatherDataSetup : MonoBehaviour
{

    [SerializeField] TMP_Text textTest;

    [SerializeField] List<SetupDataObject> weatherDataObjects;

    void Start()
    {
        StartCoroutine(getData());
    }

    IEnumerator getData(){

        // Initialize an int to count how many data objects have finished loading.
        int dataLoaded = 1;

        textTest.SetText("Loading Data " + dataLoaded.ToString() + "/" + weatherDataObjects.Count.ToString());

        // Loop through data objects and use their respective url's to obtain data from the api
        
        foreach(SetupDataObject dataObj in weatherDataObjects){
            using(UnityWebRequest request = UnityWebRequest.Get(dataObj.url)){
                yield return request.SendWebRequest();
                if(request.result == UnityWebRequest.Result.ConnectionError || request.result == UnityWebRequest.Result.ProtocolError)
                {
                    
                    textTest.SetText(request.error);               

                }
                else
                {

                    textTest.SetText("GOT IT");
                    dataLoaded++;
                    dataObj.SetupData(request.downloadHandler.text);                    
                    
                }
            
            }
            textTest.SetText("Loading Data " + dataLoaded.ToString() + "/" + weatherDataObjects.Count.ToString());
        }

        textTest.SetText("Hover over Cities for more info!");
  
    }
}
