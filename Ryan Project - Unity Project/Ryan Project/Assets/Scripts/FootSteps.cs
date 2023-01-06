using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FootSteps : MonoBehaviour
{
    [SerializeField] string stepType;

    [SerializeField] AudioSource audioSource;

    [SerializeField] AudioClip[] grassSteps;
    [SerializeField] AudioClip[] woodSteps;
    [SerializeField] AudioClip[] carpetSteps;
    [SerializeField] AudioClip[] concreteSteps;
    [SerializeField] AudioClip[] dirtSteps;


    // Update is called once per frame
    void FixedUpdate()
    {
        RaycastHit hit;

        if(Physics.Raycast(transform.position, Vector3.down, out hit, 3))
        {
            stepType = hit.transform.gameObject.tag;

        }
    }

    public void Step()
    {
        if(stepType == "Concrete")
        {
            audioSource.PlayOneShot(concreteSteps[Random.Range(0, concreteSteps.Length)]);
        }
        else if (stepType == "Wood")
        {
            audioSource.PlayOneShot(woodSteps[Random.Range(0, woodSteps.Length)]);
        }        
        else if (stepType == "Carpet")
        {
            audioSource.PlayOneShot(carpetSteps[Random.Range(0, carpetSteps.Length)]);
        }        
        else if (stepType == "Grass")
        {
            audioSource.PlayOneShot(grassSteps[Random.Range(0, grassSteps.Length)]);
        }        
        else if (stepType == "Dirt")
        {
            audioSource.PlayOneShot(dirtSteps[Random.Range(0, dirtSteps.Length)]);
        }
    }
}
