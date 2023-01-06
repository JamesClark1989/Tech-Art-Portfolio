using UnityEngine;

public class DontDestroyObject : MonoBehaviour
{

    [SerializeField] string objectTag;
    void Awake()
    {
        GameObject[] objs = GameObject.FindGameObjectsWithTag(objectTag);

        if (objs.Length > 1)
        {
            Destroy(this.gameObject);
        }

        DontDestroyOnLoad(this.gameObject);
    }
}
