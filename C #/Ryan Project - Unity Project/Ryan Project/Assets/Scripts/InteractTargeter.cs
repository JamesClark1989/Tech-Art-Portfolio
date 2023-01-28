using UnityEngine;
using System;

public class InteractTargeter : MonoBehaviour
{

    [SerializeField] Interactable interactScript;
    [SerializeField] bool inMemory = false;

    public event Action OnInteracted;

    private void OnTriggerEnter(Collider other)
    {
        if(other.CompareTag("Interactable"))
        {
            interactScript = other.GetComponent<Interactable>();
            interactScript.InRange();
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Interactable"))
        {
            interactScript?.OutOfRange();
            interactScript = null;
        }
    }

    public bool CheckIfCanInteract()
    {
        return interactScript != null;
    }

    // Functions for memory states

    public void Interacting()
    {
        OnInteracted?.Invoke();
        interactScript.Interact();
    }


}
