using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FloorRise : MonoBehaviour
{
    [SerializeField] float randomRotation;
    [SerializeField] float randomSpeed;
    [SerializeField] bool move = false;
    [SerializeField] BoxCollider theCollider;
    void Start()
    {
        randomRotation = Random.Range(-80, 80);
        randomSpeed = Random.Range(0.6f, 2f);
        theCollider = GetComponent<BoxCollider>();
    }

    void Update()
    {
        if (move)
        {
            transform.Translate(0, randomSpeed * Time.deltaTime, 0, Space.World);
            float rotSpeed = randomRotation * Time.deltaTime;
            transform.Rotate(rotSpeed, rotSpeed, rotSpeed);
        }
    }

    public void Float()
    {
        if(theCollider != null)
            Destroy(theCollider);
        Destroy(gameObject, 10);
        move = true;
    }
}
