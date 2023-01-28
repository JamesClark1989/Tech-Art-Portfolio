using UnityEngine;

public class Interactable : MonoBehaviour
{

    public virtual void Interact()
    {
        Debug.Log("Interacting with" + gameObject.name);
    }

    public virtual void InRange()
    {
        return;
    }

    public virtual void OutOfRange()
    {
        return;
    }
}
