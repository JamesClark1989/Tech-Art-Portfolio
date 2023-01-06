using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class StartTypeText : MonoBehaviour
{
    [TextArea]
    [SerializeField] string text;

    [SerializeField] TMP_Text tmpText;

    [SerializeField] GameObject nextText;
    void Start()
    {
        StartCoroutine(TypeMessage());
    }

    private IEnumerator TypeMessage()
    {
        for(int i = 0; i <= text.Length; i++)
        {
            yield return new WaitForSeconds(0.05f);
            tmpText.SetText(text.Substring(0, i));            
        }

        yield return new WaitForSeconds(2);
        nextText.SetActive(true);
        gameObject.SetActive(false);
    }


}
