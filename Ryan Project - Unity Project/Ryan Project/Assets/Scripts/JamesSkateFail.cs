using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class JamesSkateFail : MonoBehaviour
{
    [SerializeField] Animator anim;
    void Start()
    {
        anim = GetComponent<Animator>();
        StartCoroutine(TimeTillFail());
    }

    private IEnumerator TimeTillFail()
    {
        yield return new WaitForSeconds(15);
        anim.SetTrigger("Skate Fail");
    }
}
