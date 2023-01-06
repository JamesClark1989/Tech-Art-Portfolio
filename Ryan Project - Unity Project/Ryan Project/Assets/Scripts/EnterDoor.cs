
using UnityEngine;

public class EnterDoor : MonoBehaviour
{
    [SerializeField] EnterMemoryUI enterMemoryUI;


    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            enterMemoryUI.ShowEnterMemory(true);
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            enterMemoryUI.ShowEnterMemory(false);
        }
    }

    public EnterDoor()
    {
        print("ENTER");
    }

}
