using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class StateMachine : MonoBehaviour
{
    private State currentState;

    public void SwitchState(State newState)
    {
        currentState?.Exit();
        currentState = newState;
        currentState?.Enter();        

    }

    private void Update()
    {
        // currentState? is just if(currentState != null)
        // ? is a 'null conditional operator'. Can't be used with scriptable objects apparently
        currentState?.Tick(Time.deltaTime);

    }


}
