using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class PlayerStateMachine : StateMachine
{
    // field: makes the field for us and shows it in the inspector
    [field: SerializeField] public InputReader InputReader {get; private set;}
    [field: SerializeField] public CharacterController CharacterController {get; private set;}
    [field: SerializeField] public float FreeLookMovementSpeed {get; private set;}
    [field: SerializeField] public float RotationSmoothValue {get; private set;}
    [field: SerializeField] public Animator Animator {get; private set;}
    [field: SerializeField] public InteractTargeter InteractTargeter { get; private set; }
    [field: SerializeField] public FadeController FadeController { get; private set; }
    public Transform MainCameraTransform {get; private set;}

    private void Start()
    {
        MainCameraTransform = Camera.main.transform;
        SwitchState(new PlayerKneelState(this));
    }

    private void OnEnable()
    {
        InteractTargeter.OnInteracted += HandleInteraction;
    }

    private void OnDisable()
    {
        InteractTargeter.OnInteracted -= HandleInteraction;
    }

    public void HandleInteraction()
    {
        //SwitchState(new PlayerInMemoryState(this));
        print("HANDLE INTERACTION");
    }


    public void PlayerInMemoryState()
    {
        SwitchState(new PlayerInMemoryState(this));
        print("HANDLE INTERACTION");
    }

    public void BackToFreeLookState()
    {
        SwitchState(new PlayerFreeLookState(this));
    }

    public void GetUp()
    {
        SwitchState(new PlayerGetUpState(this));
    }

}
