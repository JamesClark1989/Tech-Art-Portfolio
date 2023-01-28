using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class StartTypeTextEnd : MonoBehaviour
{
    [TextArea]
    [SerializeField] string text;

    [SerializeField] TMP_Text tmpText;

    [SerializeField] Animator anim;
    [SerializeField] Animator fadeAnimator;
    [SerializeField] GameObject startTextParent;

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
        StartGame();
    }

    private void StartGame()
    {
        anim.SetTrigger("FadeStartText");
    }

    public void FadeIntoGame()
    {
        fadeAnimator.SetTrigger("Fade Out Start");
        startTextParent.SetActive(false);
    }


}
