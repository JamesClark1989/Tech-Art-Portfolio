using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MemoryInteract : Interactable
{
    [SerializeField] GameObject memory;
    [SerializeField] bool hasInteracted = false;
    [SerializeField] Animator anim;
    [SerializeField] GetMemoryUI getMemoryUI;
    PlayerStateMachine playerStateMachine;
    [SerializeField] AudioSource audioSource;
    [SerializeField] AudioClip audioClip;

    private void Start()
    {
        audioSource = GetComponent<AudioSource>();
        playerStateMachine = FindObjectOfType<PlayerStateMachine>();
        getMemoryUI = FindObjectOfType<GetMemoryUI>();
    }

    public override void Interact()
    {
        if(hasInteracted == false)
        {
            audioSource.PlayOneShot(audioClip);
            GameManager.instance.MemoryCollected();
            playerStateMachine.PlayerInMemoryState();
            getMemoryUI.ShowGetMemory(false);
            anim.SetTrigger("Memory Accessed");
            memory.SetActive(true);
            hasInteracted = true;
        }
    }

    public override void InRange()
    {
        if (hasInteracted == false)        
            getMemoryUI.ShowGetMemory(true);
    }

    public override void OutOfRange()
    {
        if (hasInteracted == false)
            getMemoryUI.ShowGetMemory(false);
    }

}
