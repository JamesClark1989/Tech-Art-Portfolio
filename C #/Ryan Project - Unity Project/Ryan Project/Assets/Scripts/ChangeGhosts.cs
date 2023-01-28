using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChangeGhosts : MonoBehaviour
{

    [SerializeField] float timeTillNextGhosts;
    [SerializeField] ShowGhostsInMemory showGhostsInMemory1;

    void Start()
    {
        StartCoroutine(ChangeTheGhosts());
    }

    private IEnumerator ChangeTheGhosts()
    {
        yield return new WaitForSeconds(timeTillNextGhosts);
        showGhostsInMemory1.ChangeGhosts();
    }
}
