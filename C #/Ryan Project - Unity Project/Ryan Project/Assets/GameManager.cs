using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameManager : MonoBehaviour
{

    public static GameManager instance;
    [SerializeField] GameObject endingLight;
    [SerializeField] int memoriesCollected = 0;
    private int maxMemories = 8;

    private void Awake()
    {
        GameManager[] objs = FindObjectsOfType<GameManager>();

        if (objs.Length > 1)
        {
            Destroy(this.gameObject);
        }
        instance = this;
    }



    public void MemoryCollected()
    {
        memoriesCollected++;
        if(memoriesCollected == maxMemories)
        {
            endingLight.SetActive(true);
        }
    }

}
