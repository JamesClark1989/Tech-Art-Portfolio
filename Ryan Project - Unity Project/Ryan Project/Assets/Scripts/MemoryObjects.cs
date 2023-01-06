using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MemoryObjects : MonoBehaviour
{
    [SerializeField] GameObject[] memoryObjects;

    public void TurnOnMemoryObjects(int memory)
    {
        memoryObjects[memory].SetActive(true);
    }
}
