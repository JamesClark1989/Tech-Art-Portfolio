using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class EndingInteractScript : Interactable
{
    [SerializeField] FadeController fadeController;

    [SerializeField] EnterLightUI enterLightUI;

    [SerializeField] AudioSource bgMusic;
    [SerializeField] AudioSource voidSound;
    public bool turnDownMusic = false;
    [SerializeField] float recoveryRate;

    [SerializeField] PlayerStateMachine playerStateMachine;

    [SerializeField] AudioSource audioSource;
    [SerializeField] AudioClip enterHeavenSound;

    bool interacted = false;

    private void Start()
    {
        audioSource = GetComponent<AudioSource>();
        playerStateMachine = FindObjectOfType<PlayerStateMachine>();
        enterLightUI = FindObjectOfType<EnterLightUI>();
    }

    private void Update()
    {
        if (turnDownMusic)
        {
            
            bgMusic.volume = Mathf.MoveTowards(bgMusic.volume, 0, recoveryRate * Time.deltaTime);
            voidSound.volume = Mathf.MoveTowards(voidSound.volume, 0.1f, recoveryRate * Time.deltaTime);
        }
    }

    public override void Interact()
    {
        if(interacted == false)
        {
            interacted = true;
            audioSource.PlayOneShot(enterHeavenSound);
            turnDownMusic = true;
            playerStateMachine.PlayerInMemoryState();
            fadeController.EnterHeaven();
            enterLightUI.ShowEnterMemory(false);
            StartCoroutine(LoadHeaven());
        }   
    }


    public override void InRange()
    {
        enterLightUI.ShowEnterMemory(true);
    }

    public override void OutOfRange()
    {
        enterLightUI.ShowEnterMemory(false);
    }

    private IEnumerator LoadHeaven()
    {
        yield return new WaitForSeconds(3.5f);
        AsyncOperation asyncLoad = SceneManager.LoadSceneAsync(1);
    }
}
