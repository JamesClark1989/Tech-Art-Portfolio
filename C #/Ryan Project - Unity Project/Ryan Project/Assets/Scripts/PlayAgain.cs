using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;

public class PlayAgain : MonoBehaviour
{
    public void PlayGameAgain()
    {
        StartCoroutine(WaitTillPlayAgain());
    }

    private IEnumerator WaitTillPlayAgain()
    {
        yield return new WaitForSeconds(2);
        AsyncOperation asyncLoad = SceneManager.LoadSceneAsync(0);
    }
}
