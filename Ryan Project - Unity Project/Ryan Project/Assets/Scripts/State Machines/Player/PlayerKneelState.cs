using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerKneelState : PlayerBaseState
{
    // readonly kind of like a constant but its not done at compile time. 
    private readonly int GetUpHash = Animator.StringToHash("Get Up");


    // base(stateMachine) is just running the contructor on the inherited class
    public PlayerKneelState(PlayerStateMachine stateMachine) : base(stateMachine)
    {
        
    }

    public override void Enter()
    {
    }

    public override void Tick(float deltaTime)
    {

    }

    public override void Exit()
    {
        stateMachine.Animator.SetTrigger(GetUpHash);
    }
    
}
