using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;
using UnityEngine.InputSystem;

public class MemoryTextType : MonoBehaviour
{
    [TextArea]
    [SerializeField] string[] memoryText;
    [SerializeField] TMP_Text messageText;
    [SerializeField] float textTime;
    [SerializeField] FadeController fadeController;
    LeaveMemoryUI leaveMemoryUI;
    bool finishedTyping = false;

    [SerializeField] Transform beginning;

    [SerializeField] GameObject memoryToTurnOff;

    [SerializeField] Controls controls;

    private InputAction advance;
    bool interacted = false;
    

    private void OnEnable()
    {
        controls.Enable();

        advance = controls.UI.Advance;
        advance.Enable();
        advance.performed += Advance;
    }

    private void OnDisable()
    {
        controls.Disable();
        advance.Disable();
    }

    private void Awake()
    {
        controls = new Controls();
    }
    void Start()
    {
        leaveMemoryUI = FindObjectOfType<LeaveMemoryUI>();
        fadeController = FindObjectOfType<FadeController>();
        StartCoroutine(TypeText());
    }



    public void Advance(InputAction.CallbackContext context)
    {
        if (finishedTyping && interacted == false)
        {

            leaveMemoryUI.ShowLeaveMemory(false);
            StartCoroutine(GoBackToStart());
            interacted = true;
        }
    }

    private IEnumerator GoBackToStart()
    {
        fadeController.EnterMemory();
        yield return new WaitForSeconds(1.5f);
        memoryToTurnOff.SetActive(false);
        var player = GameObject.FindGameObjectWithTag("Player");
        player.GetComponent<CharacterController>().enabled = false;
        player.transform.position = beginning.position;
        player.transform.rotation = beginning.rotation;
        player.GetComponent<CharacterController>().enabled = true;
        player.GetComponent<PlayerStateMachine>().BackToFreeLookState();


    }
 
    private IEnumerator TypeText()
    {
        yield return new WaitForSeconds(2);
        for(int sentence = 0; sentence < memoryText.Length; sentence++)
        {
            for (int i = 0; i <= memoryText[sentence].Length; i++)
            {
                messageText.SetText(memoryText[sentence].Substring(0, i));
                yield return new WaitForSeconds(textTime);
            }
            yield return new WaitForSeconds(2);
            messageText.SetText("");
        }
 
        ShowLeaveMemory();
    }

    private void ShowLeaveMemory()
    {
        finishedTyping = true;
        leaveMemoryUI.ShowLeaveMemory(true);
    }
}
