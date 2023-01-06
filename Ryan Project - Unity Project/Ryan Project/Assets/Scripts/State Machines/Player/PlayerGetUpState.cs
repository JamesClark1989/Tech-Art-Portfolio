using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerGetUpState : PlayerBaseState
{
    // readonly kind of like a constant but its not done at compile time. 
    private float TimeTillMoveState;


    // base(stateMachine) is just running the contructor on the inherited class
    public PlayerGetUpState(PlayerStateMachine stateMachine) : base(stateMachine)
    {
        
    }

    public override void Enter()
    {
        int lengthOfAnims = stateMachine.Animator.runtimeAnimatorController.animationClips.Length;
        for(int i = 0; i < lengthOfAnims; i++)
        {
            if(stateMachine.Animator.runtimeAnimatorController.animationClips[i].name == "Get Up")
            {
                TimeTillMoveState = stateMachine.Animator.runtimeAnimatorController.animationClips[i].length;
            }
        }
    }

    public override void Tick(float deltaTime)
    {
        TimeTillMoveState -= Time.deltaTime;
        if(TimeTillMoveState <= 0)
        {
            stateMachine.SwitchState(new PlayerFreeLookState(stateMachine));
        }
    }

    public override void Exit()
    {

    }
    
}
