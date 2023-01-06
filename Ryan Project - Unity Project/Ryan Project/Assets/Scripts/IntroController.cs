using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IntroController : MonoBehaviour
{

    [SerializeField] GameObject WASD;
    public void StartGetUp()
    {
        StartCoroutine(WaitTillGetUp());
    }

    private IEnumerator WaitTillGetUp()
    {
        yield return new WaitForSeconds(3);
        GetUp();
        yield return new WaitForSeconds(1);
        WASD.SetActive(true);
    }

    public void GetUp()
    {
        FindObjectOfType<PlayerStateMachine>().GetUp();
    }
}
