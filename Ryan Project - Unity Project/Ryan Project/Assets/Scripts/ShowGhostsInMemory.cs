using UnityEngine;

public class ShowGhostsInMemory : MonoBehaviour
{

    [SerializeField] MaterialInstance[] ghosts;
    [SerializeField] MaterialInstance[] ghosts2;

    [SerializeField] GameObject fieldGhostToActive;

    private void OnEnable()
    {
        fieldGhostToActive.SetActive(true);
        for (int i = 0; i < ghosts.Length; i++)
        {
            ghosts[i].SetVisibility(true);
        }
    }

    public void ChangeGhosts()
    {
        for (int i = 0; i < ghosts.Length; i++)
        {
            ghosts[i].SetVisibility(false);
        }

        for (int i = 0; i < ghosts.Length; i++)
        {
            ghosts2[i].SetVisibility(true);
        }
    }
}
