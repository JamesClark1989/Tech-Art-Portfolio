using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;

public class EnterMemoryUI : MonoBehaviour
{
    [SerializeField] bool visible;
    [SerializeField] float alpha;
    float currentAlpha;
    float time;
    [SerializeField] Image eIcon;
    [SerializeField] TMP_Text textColor;

    void Update()
    {
        if (visible)
        {

            alpha = Mathf.Lerp(currentAlpha, 1, time);
            time += Time.deltaTime;
            if (time >= 1)
                time = 1;
        }
        else
        {
            alpha = Mathf.Lerp(currentAlpha, 0, time);
            time += Time.deltaTime;
            if (time >= 1)
                time = 1;
        }

        eIcon.color = new Color(1, 1, 1, alpha);
        textColor.color = new Color(1, 1, 1, alpha);
    }

    public void ShowEnterMemory(bool isVisible)
    {
        currentAlpha = alpha;
        time = 0;
        visible = isVisible;
        
    }

}
