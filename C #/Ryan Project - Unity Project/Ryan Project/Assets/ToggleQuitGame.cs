using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class ToggleQuitGame : MonoBehaviour
{

    [SerializeField] GameObject quitGameMenu;
    [SerializeField] Controls controls;
    private InputAction quit;


    private void OnEnable()
    {
        controls.Enable();
        quit = controls.UI.Quit;
        quit.Enable();
        quit.performed += ToggleQuitGameMenu;
    }

    private void OnDisable()
    {
        controls.Disable();
    }

    private void Awake()
    {
        controls = new Controls();
    }

    public void ToggleQuitGameMenu(InputAction.CallbackContext context)
    {
        if(quitGameMenu.activeSelf)
        {
            quitGameMenu.SetActive(false);
        }
        else
        {
            quitGameMenu.SetActive(true);
        }
    }
}
