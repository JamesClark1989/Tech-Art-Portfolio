using UnityEngine;

public class FadeController : MonoBehaviour
{
    [SerializeField] Animator anim;
    [SerializeField] GameObject[] memoryObjects;
    [SerializeField] LeaveMemoryUI leaveMemoryUI;

    public void EnterMemory()
    {
        anim.SetTrigger("Fade");
    }


    public void EnterHeaven()
    {
        anim.SetTrigger("Fade Into Heaven");
    }


}
