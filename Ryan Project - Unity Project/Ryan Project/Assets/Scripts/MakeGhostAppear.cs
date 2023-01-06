using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MakeGhostAppear : MonoBehaviour
{

    [SerializeField] MaterialInstance[] ghosts;

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            for(int i = 0; i < ghosts.Length; i++)
            {
                ghosts[i].SetVisibility(true);
            }
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            for (int i = 0; i < ghosts.Length; i++)
            {
                ghosts[i].SetVisibility(false);
            }
        }
    }
}
