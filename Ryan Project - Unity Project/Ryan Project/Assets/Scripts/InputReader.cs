using System.Collections;
using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class InputReader : MonoBehaviour, Controls.IPlayerActions
{
    public Vector2 MovementValue { get; private set; }
    public event Action EnterEvent;

    private Controls controls;

    public GameObject settingsMenu;

    private void Start()
    {
        controls = new Controls();
        // Hooks up our callbacks in this script, i.e. jump, attack, etc
        controls.Player.SetCallbacks(this);

        controls.Player.Enable();
    }

    private void OnDestroy() 
    {
        controls.Player.Disable();
    }


    public void OnMove(InputAction.CallbackContext context)
    {
        MovementValue = context.ReadValue<Vector2>();
    }


    public void OnEnter(InputAction.CallbackContext context)
    {
        // performed means pressed
        if (context.performed)
            EnterEvent?.Invoke();
    }
}