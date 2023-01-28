using UnityEngine;

public class TeleportPlayerIntoMemory : MonoBehaviour
{
    private void OnEnable()
    {
        var player = GameObject.FindGameObjectWithTag("Player");
        player.GetComponent<CharacterController>().enabled = false;
        player.transform.position = transform.position;
        player.GetComponent<CharacterController>().enabled = true;
        player.GetComponent<PlayerStateMachine>().BackToFreeLookState();
    }
}
