using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public abstract class PlayerBaseState : State
{
    // Protected means only classes that inherit it can access it
    protected PlayerStateMachine stateMachine;

    public PlayerBaseState(PlayerStateMachine stateMachine)
    {
        // 'this' refers to the protected variable
        this.stateMachine = stateMachine;        
    }
}
