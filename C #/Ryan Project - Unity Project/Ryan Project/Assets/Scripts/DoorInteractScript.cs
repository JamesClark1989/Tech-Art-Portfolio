using UnityEngine;
using System.Collections;

public class DoorInteractScript : Interactable
{
    [SerializeField] int memoryIterator;
    [SerializeField] FadeController fadeController;

    [SerializeField] EnterMemoryUI enterMemoryUI;

    [SerializeField] GameObject[] memories;

    [SerializeField] PlayerStateMachine playerStateMachine;
    [SerializeField] BoxCollider boxCollider;
    [SerializeField] GameObject doorGlow;
    [SerializeField] GameObject doorGlowSoft;

    [SerializeField] AudioSource audioSource;
    [SerializeField] AudioClip teleportAudio;

    [SerializeField] Animator doorTextAnim;

    [SerializeField] int currentDoorState = 0;
    [SerializeField] DoorInteractScript[] otherDoors;


    private void Start()
    {
        audioSource = GetComponent<AudioSource>();
        boxCollider = GetComponent<BoxCollider>();
        playerStateMachine = FindObjectOfType<PlayerStateMachine>();
        enterMemoryUI = FindObjectOfType<EnterMemoryUI>();
    }

    public override void Interact()
    {
        if(memoryIterator < memories.Length)
        {
            if(currentDoorState == 0)
            {
                audioSource.PlayOneShot(teleportAudio);
                enterMemoryUI.ShowEnterMemory(false);
                playerStateMachine.PlayerInMemoryState();
                StartCoroutine(LoadMemory());
                fadeController.EnterMemory();
            }
            else if (currentDoorState == 1)
            {
                doorTextAnim.SetTrigger("Show Door Text");
            }
           
        }
     
    }

    private void ChangeDoorGlow()
    {
        if (currentDoorState == 0)
        {
            doorGlow.SetActive(true);
            doorGlowSoft.SetActive(false);
        }
        else if (currentDoorState == 1)
        {
            doorGlow.SetActive(false);
            doorGlowSoft.SetActive(true);
        }

    }


    private IEnumerator LoadMemory()
    {
        yield return new WaitForSeconds(1.5f);
        memories[memoryIterator].SetActive(true);
        memoryIterator++;

        currentDoorState = 1;

        for(int i = 0; i < otherDoors.Length; i++)
        {
            otherDoors[i].ResetDoorState();
        }

        ChangeDoorGlow();


        if (memoryIterator >= memories.Length)
        {
            currentDoorState = 2;
            boxCollider.enabled = false;
            doorGlow.SetActive(false);
            doorGlowSoft.SetActive(false);
        }
    }

    public override void InRange()
    {
        enterMemoryUI.ShowEnterMemory(true);
    }

    public override void OutOfRange()
    {
        enterMemoryUI.ShowEnterMemory(false);
    }

    public void ResetDoorState()
    {
        if (memoryIterator < memories.Length)
        {

            currentDoorState = 0;
            ChangeDoorGlow();
        }    
    }
}
