using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerFreeLookState : PlayerBaseState
{
    // readonly kind of like a constant but its not done at compile time. 
    private readonly int FreeLookSpeedHash = Animator.StringToHash("FreeLookSpeed");

    private const float AnimatorDampTime = 0.1f;

    private Vector3 momentum;

    // base(stateMachine) is just running the contructor on the inherited class
    public PlayerFreeLookState(PlayerStateMachine stateMachine) : base(stateMachine)
    {
        
    }

    public override void Enter()
    {
        stateMachine.InputReader.EnterEvent += OnInteract;
    }

    public override void Tick(float deltaTime)
    {
        Vector3 movement = CalculateMovement();


        if (!stateMachine.CharacterController.isGrounded)
        {
            movement.y += Physics.gravity.y;
        }

        stateMachine.CharacterController.Move(movement * stateMachine.FreeLookMovementSpeed * deltaTime);
        
        if (stateMachine.InputReader.MovementValue == Vector2.zero) 
        {
            stateMachine.Animator?.SetFloat(FreeLookSpeedHash, 0, AnimatorDampTime, deltaTime);
            if (stateMachine.Animator?.GetFloat(FreeLookSpeedHash) < 0.1f)
                stateMachine.Animator?.SetFloat(FreeLookSpeedHash,0);
            return;
        }

        stateMachine.Animator?.SetFloat(FreeLookSpeedHash, 1, AnimatorDampTime, deltaTime);

        FaceMovementDirection(movement, deltaTime);
    }

    public override void Exit()
    {
        stateMachine.InputReader.EnterEvent -= OnInteract;
    }

    private void OnInteract()
    {
        if (!stateMachine.InteractTargeter.CheckIfCanInteract())
        {
            return;
        }
        stateMachine.InteractTargeter.Interacting();
        stateMachine.Animator?.SetFloat(FreeLookSpeedHash, 0);
        //stateMachine.SwitchState(new PlayerInMemoryState(stateMachine));
    }

    private Vector3 CalculateMovement()
    {
        Vector3 camForward = stateMachine.MainCameraTransform.forward;
        Vector3 camRight= stateMachine.MainCameraTransform.right;

        camForward.y = 0f;
        camRight.y = 0f;

        camForward.Normalize();
        camRight.Normalize();

        return camForward * stateMachine.InputReader.MovementValue.y + camRight * stateMachine.InputReader.MovementValue.x;
    }

    private void FaceMovementDirection(Vector3 movement, float deltaTime)
    {
        // Set this to 0 or you get weird rotation
        movement.y = 0;
        stateMachine.transform.rotation = Quaternion.Lerp(stateMachine.transform.rotation, Quaternion.LookRotation(movement), deltaTime * stateMachine.RotationSmoothValue);
    }


    
}
