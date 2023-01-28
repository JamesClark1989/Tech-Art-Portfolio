#ifndef SUPERSIMPLESKYBOX_INCLUDED
#define SUPERSIMPLESKYBOX_INCLUDED

#ifdef UNIVERSAL_LIGHTING_INCLUDED
float3 _WorldSpaceLightPos0;
#endif

void GetLightDirection_float(out float3 Out){
	Out = _WorldSpaceLightPos0;
}

#endif