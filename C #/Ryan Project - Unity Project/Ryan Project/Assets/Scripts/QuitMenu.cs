using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QuitMenu : MonoBehaviour
{
    public void QuitGame()
    {
        print("SDGDSG");
        Application.Quit();
    }

    public void DontQuit()
    {
        print("DONT");
        gameObject.SetActive(false);
    }
}
