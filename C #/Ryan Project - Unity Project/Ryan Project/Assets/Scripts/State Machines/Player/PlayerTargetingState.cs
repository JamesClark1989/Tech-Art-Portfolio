using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerTargetingState : PlayerBaseState
{

    private float rotationSpeed = 4;

    public Transform target;

    public PlayerTargetingState(PlayerStateMachine stateMachine) : base(stateMachine)
    {

    }

    public override void Enter()
    {      
    }

    public override void Tick(float deltaTime)
    {
        Quaternion oldRotation = stateMachine.transform.rotation;

        Vector3 targetDir = target.position - stateMachine.transform.position;
        targetDir.y = 0;
        float step = rotationSpeed * Time.deltaTime;

        Vector3 newDir = Vector3.RotateTowards(stateMachine.transform.forward, targetDir, step, 0.0F);
        Debug.DrawRay(stateMachine.transform.position, newDir, Color.red);

        stateMachine.transform.rotation = Quaternion.LookRotation(newDir);

        Quaternion newRotation = stateMachine.transform.rotation;



        if (oldRotation == newRotation)
        {

            // End State here and assign grabbing state
            stateMachine.SwitchState(new PlayerInMemoryState(stateMachine));
        }


    }

    public override void Exit()
    {

    }



}
