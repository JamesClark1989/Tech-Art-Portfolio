using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MaterialInstance : MonoBehaviour
{
    [SerializeField] GameObject go;
    [SerializeField] float alpha;
    [SerializeField] float currentAlpha;
    [SerializeField] Material material;
    [SerializeField] bool visible = false;
    [SerializeField] float time;

    void Start()
    {
        go = gameObject;
        if(TryGetComponent(out SkinnedMeshRenderer smr))
            material = smr.material;
        if (TryGetComponent(out MeshRenderer mr))
            material = mr.material;

    }

    // Update is called once per frame
    void Update()
    {
        if (visible)
        {
            
            alpha = Mathf.Lerp(currentAlpha, 1, time);
            time += Time.deltaTime;
            if (time >= 1)
                time = 1;
        }
        else
        {
            alpha = Mathf.Lerp(currentAlpha, 0, time);
            time += Time.deltaTime;
            if (time >= 1)
                time = 1;

        }
        material.SetFloat("_Alpha", alpha);
    }

    public void SetVisibility(bool isVisible)
    {
        time = 0;
        currentAlpha = alpha;
        visible = isVisible;
    }


}
