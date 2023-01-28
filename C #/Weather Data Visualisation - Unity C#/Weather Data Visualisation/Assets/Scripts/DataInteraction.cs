using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DataInteraction : MonoBehaviour
{

    [SerializeField] Animator anim;
    [SerializeField] Animator locationAnim;
    [SerializeField] AudioSource audioSource;

    private void OnMouseEnter() {
        audioSource.Play();
        anim.SetBool("show_extra_data", true);
        locationAnim.SetBool("Hovering", true);
    }

    private void OnMouseExit() {
        anim.SetBool("show_extra_data", false);
        locationAnim.SetBool("Hovering", false);
    }

    public void ShowData(){
        anim.SetTrigger("data_collected");
    }
}
