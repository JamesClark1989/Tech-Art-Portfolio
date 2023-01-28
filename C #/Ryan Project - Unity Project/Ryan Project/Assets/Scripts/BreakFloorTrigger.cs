using UnityEngine;

public class BreakFloorTrigger : MonoBehaviour
{
    [SerializeField] FloorRise[] floorRiseScripts;
    [SerializeField] bool canBreak;
    [SerializeField] GameObject boundary;
    [SerializeField] bool interacted = false;
    [SerializeField] AudioSource audioSource;
    [SerializeField] AudioClip breakSound;
    private void Start()
    {
        audioSource = GetComponent<AudioSource>();
    }
    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player") && !interacted)
        {
            interacted = true;
            boundary.SetActive(true);
            for (int i = 0; i < floorRiseScripts.Length; i++)
            {
                floorRiseScripts[i].Float();
            }
            audioSource.PlayOneShot(breakSound);
            Destroy(gameObject, 3);
        }

    }
}
