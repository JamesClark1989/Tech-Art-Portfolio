bl_info = {
    "name": "Rig-A-Roblox",
    "blender": (2, 90, 0),
    "category": "Rigging",
    "version": (0, 1, 2),
    "description": "Rig A Roblox character",
}

# This script rigs a roblox character (I wrote this early in the morning)


import bpy
import os

from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper

class Rig_A_Roblox(bpy.types.Panel):
    bl_label = "Rig-A-Roblox"
    bl_idname = "RDC"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Rig A Roblox Character'   

    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Step 1: Mass Import Character Parts", icon = 'IMPORT')
        row = layout.row()
        row.operator('import.obj_character')
        row.operator('import.fbx_character')
        row = layout.row()
        row = layout.row()
        row.label(text = "Optional:", icon = 'LIGHT_SUN')
        row = layout.row()
        row.operator('view.character')
        row = layout.row()
        row.operator('clean.character')
        row = layout.row()
        row.operator('center.character')   
        row = layout.row()
        row = layout.row()
        row.label(text = "Step 2: Set Pivot Points", icon = 'CON_PIVOT')
        row = layout.row()
        row.operator('set.pivot')
        row = layout.row()
        row.operator('toggle.visibility')
        row.operator('select.face')
        row = layout.row()
        row = layout.row()
        row.label(text = "Step 3: Set the names", icon = 'FILE_TEXT')
        row = layout.row()
        row.label(text = "")
        row.operator('name.head')
        row.label(text = "")
        row = layout.row()
        row.operator('name.upper_arm_r')
        row.operator('name.torso') 
        row.operator('name.upper_arm_l') 
        row = layout.row()
        row.operator('name.lower_arm_r')
        row.label(text = "")
        row.operator('name.lower_arm_l') 
        row = layout.row()
        row.operator('name.hand_r')
        row.label(text = "")      
        row.operator('name.hand_l')
        row = layout.row() 
        row.label(text = "")
        row.operator('name.waist')
        row.label(text = "")
        row = layout.row()
        row.operator('name.upper_leg_r')
        row.label(text = "")
        row.operator('name.upper_leg_l')
        row = layout.row()
        row.operator('name.lower_leg_r')
        row.label(text = "")
        row.operator('name.lower_leg_l')
        row = layout.row()
        row.operator('name.foot_r')
        row.label(text = "")
        row.operator('name.foot_l')
        row = layout.row()
        row = layout.row()
        row.label(text = "Step 4:", icon = 'MOD_ARMATURE')
        row = layout.row()
        row.operator('rig.character')
        row = layout.row()
        row.operator('xray.rig')
        row = layout.row()
        row = layout.row()
        row.label(text = "Remove all Vertex Groups\nClick this if you need to re-rig", icon = 'UV_VERTEXSEL')
        row = layout.row()
        row.operator("remove.vertgroups")
        row = layout.row()
        row = layout.row()
        row.label(text = "--- Other Useful Tools ---", icon = 'TOOL_SETTINGS')
        row = layout.row()
        row.operator("make.opaque")
        

class Xray_Rig(bpy.types.Operator):
    bl_label = "Xray Rig"
    bl_idname = "xray.rig"
    
    def execute (self,context):
        
        if bpy.context.object.show_in_front == True:
            bpy.context.object.show_in_front = False
        else:
            bpy.context.object.show_in_front = True
        
        return {'FINISHED'}

class View_Character(bpy.types.Operator):
    bl_label = "View Character"
    bl_idname = "view.character"
    
    def execute (self,context):
        bpy.ops.view3d.view_selected(use_all_regions = False)
        
        return {'FINISHED'}

class Toggle_Visibility(bpy.types.Operator):
    bl_label = "Toggle Visibility"
    bl_idname = "toggle.visibility"
    
    def execute (self,context):
        bpy.ops.view3d.localview()
        
        return {'FINISHED'}

class Select_Face(bpy.types.Operator):
    bl_label = "Select Face"
    bl_idname = "select.face"
    
    def execute (self,context):
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        bpy.ops.mesh.select_all(action='DESELECT')

        
        return {'FINISHED'}       
        
        
class Make_Opaque(bpy.types.Operator):
    bl_label = "Make Opaque"
    bl_idname = "make.opaque"
    
    def execute (self,context):
        bpy.ops.object.select_all(action='SELECT')

        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                bpy.context.view_layer.objects.active = obj                
                for m in range(len(bpy.context.object.material_slots)):
                    try:
                        bpy.context.object.active_material_index = m
                        obj.active_material.blend_method = 'OPAQUE'
                    except:
                        continue
        
        return {'FINISHED'}   
        
class Remove_Vertex_Groups(bpy.types.Operator):
    bl_label = "Remove Vertex Groups"
    bl_idname = "remove.vertgroups"
    
    def execute (self,context):
        bpy.ops.object.select_all(action='SELECT')

        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                bpy.context.view_layer.objects.active = obj
                try:
                    bpy.ops.object.vertex_group_remove(all=True)
                except:
                    continue
        
        return {'FINISHED'}
            
class Rig_Character(bpy.types.Operator):
    bl_label = "Rig Character"
    bl_idname = "rig.character"  
      
        
    def execute (self, context):
        
        self.bone_part_list = ["Waist", "Torso", "Head", "Upper_Arm_R", "Lower_Arm_R", "Hand_R", "Upper_Arm_L", "Lower_Arm_L", "Hand_L", "Upper_Leg_R", "Lower_Leg_R", "Foot_R", "Upper_Leg_L", "Lower_Leg_L", "Foot_L"]
        
        # Purge orphan data to clean project
        bpy.ops.outliner.orphans_purge()
        
        # Create the armature
        self.create_rig()
        
        # Skin the mesh
        self.skin_mesh()
        
        
        return {'FINISHED'}
    
    def skin_mesh(self):
        
        for body_part in self.bone_part_list:
            print(body_part)
        
            bpy.ops.object.select_all(action='DESELECT')
            
            bpy.data.objects[body_part].select_set(True)
            bpy.context.view_layer.objects.active = bpy.data.objects[body_part]
            bpy.context.object.data.name = body_part

            
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            
            obj = bpy.data.objects[body_part]
            
            
            for i in range(0, len(obj.vertex_groups)):
                print(obj.vertex_groups[i])
                group = obj.vertex_groups[i]
                if group.name == body_part + "_Bone":
                    
                    bpy.ops.object.vertex_group_set_active(group=str(group.name))
                    bpy.ops.object.vertex_group_assign()
                    
                    print("ASSIGNED")
                    break
                  
            bpy.ops.object.mode_set(mode='OBJECT')
                    

    def create_rig(self):
              

        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects[self.bone_part_list[0]].select_set(True)

        # Setup the first bone
        self.first_bone_setup(self.bone_part_list[0])

        # Create Torso Bone        
        self.extrude_bone("Waist_Bone", bpy.data.objects['Head'].location)
        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Waist_Bone.001", self.bone_part_list[1])
        bpy.ops.object.mode_set(mode='EDIT')
        self.select_bone_part(tail = True, bone_name = self.bone_part_list[1] + "_Bone")

        # Create Head Bone
        bpy.context.scene.cursor.location[2] = bpy.context.scene.cursor.location[2] + 2

        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        # The whole renaming and selecting bone part process
        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone(self.bone_part_list[1] + "_Bone.001", self.bone_part_list[2])
        bpy.ops.object.mode_set(mode='EDIT')
        self.select_bone_part(tail = True, bone_name = self.bone_part_list[2] + "_Bone")

        # ------- Create Right Arm Bones ------- #

        # Upper_Arm_R
        bpy.context.scene.cursor.location = bpy.data.objects['Upper_Arm_R'].location

        bpy.ops.armature.bone_primitive_add()

        bpy.context.scene.cursor.location = bpy.data.objects['Lower_Arm_R'].location

        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Bone", self.bone_part_list[3])
        bpy.ops.object.mode_set(mode='EDIT')
        self.select_bone_part(tail = True, bone_name = 'Upper_Arm_R' + "_Bone")

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        # Lower_Arm_R

        bpy.context.scene.cursor.location = bpy.data.objects['Hand_R'].location

        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)


        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Upper_Arm_R_Bone.001", "Lower_Arm_R")
        bpy.ops.object.mode_set(mode='EDIT')
        self.select_bone_part(tail = True, bone_name = "Lower_Arm_R_Bone")

        # Hand_R

        bpy.context.scene.cursor.location[1] *= -2.5
        bpy.context.scene.cursor.location[2] *= 1.6     
                
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Lower_Arm_R_Bone.001", "Hand_R")
        bpy.ops.object.mode_set(mode='EDIT')

        # Parent to Torso Bone

        bpy.ops.armature.select_all(action='DESELECT')

        bpy.data.armatures["Armature"].edit_bones['Upper_Arm_R_Bone'].parent = bpy.data.armatures["Armature"].edit_bones['Torso_Bone']


        # ------- Create LEFT Arm Bones ------- #

        # Upper_Arm_L
        bpy.context.scene.cursor.location = bpy.data.objects['Upper_Arm_L'].location

        bpy.ops.armature.bone_primitive_add()

        bpy.context.scene.cursor.location = bpy.data.objects['Lower_Arm_L'].location

        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Bone", 'Upper_Arm_L')
        bpy.ops.object.mode_set(mode='EDIT')
        self.select_bone_part(tail = True, bone_name = 'Upper_Arm_L' + "_Bone")

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        # Lower_Arm_L

        bpy.context.scene.cursor.location = bpy.data.objects['Hand_L'].location

        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)


        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Upper_Arm_L_Bone.001", "Lower_Arm_L")
        bpy.ops.object.mode_set(mode='EDIT')
        self.select_bone_part(tail = True, bone_name = "Lower_Arm_L_Bone")

        # Hand_L

        bpy.context.scene.cursor.location[1] *= -2.5
        bpy.context.scene.cursor.location[2] *= 1.6     
                
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Lower_Arm_L_Bone.001", "Hand_L")
        bpy.ops.object.mode_set(mode='EDIT')

        # Parent to Torso Bone

        bpy.ops.armature.select_all(action='DESELECT')

        bpy.data.armatures["Armature"].edit_bones['Upper_Arm_L_Bone'].parent = bpy.data.armatures["Armature"].edit_bones['Torso_Bone']
        
        # Parent Torso to Waist
        
        bpy.data.armatures["Armature"].edit_bones['Torso_Bone'].parent = bpy.data.armatures["Armature"].edit_bones['Waist_Bone']


        # ------- Create RIGHT Leg Bones ------- #

        # Upper_Leg_R
        bpy.context.scene.cursor.location = bpy.data.objects['Upper_Leg_R'].location

        bpy.ops.armature.bone_primitive_add()

        bpy.context.scene.cursor.location = bpy.data.objects['Lower_Leg_R'].location

        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Bone", 'Upper_Leg_R')
        bpy.ops.object.mode_set(mode='EDIT')
        self.select_bone_part(tail = True, bone_name = 'Upper_Leg_R' + "_Bone")

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        # Lower_Leg_R

        bpy.context.scene.cursor.location = bpy.data.objects['Foot_R'].location

        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})



        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)


        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Upper_Leg_R_Bone.001", "Lower_Leg_R")
        bpy.ops.object.mode_set(mode='EDIT')
        self.select_bone_part(tail = True, bone_name = "Lower_Leg_R_Bone")

        # Foot_R  

        bpy.context.scene.cursor.location[1] *= -3.5  
                
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Lower_Leg_R_Bone.001", "Foot_R")
        bpy.ops.object.mode_set(mode='EDIT')

        # Parent to Torso Bone

        bpy.ops.armature.select_all(action='DESELECT')

        bpy.data.armatures["Armature"].edit_bones['Upper_Leg_R_Bone'].parent = bpy.data.armatures["Armature"].edit_bones['Waist_Bone']

        # ------- Create LEFT Leg Bones ------- #

        # Upper_Leg_L
        bpy.context.scene.cursor.location = bpy.data.objects['Upper_Leg_L'].location

        bpy.ops.armature.bone_primitive_add()

        bpy.context.scene.cursor.location = bpy.data.objects['Lower_Leg_L'].location

        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Bone", 'Upper_Leg_L')
        bpy.ops.object.mode_set(mode='EDIT')
        self.select_bone_part(tail = True, bone_name = 'Upper_Leg_L' + "_Bone")

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        # Lower_Leg_L

        bpy.context.scene.cursor.location = bpy.data.objects['Foot_L'].location

        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})



        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)


        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Upper_Leg_L_Bone.001", "Lower_Leg_L")
        bpy.ops.object.mode_set(mode='EDIT')
        self.select_bone_part(tail = True, bone_name = "Lower_Leg_L_Bone")

        # Foot_L

        bpy.context.scene.cursor.location[1] *= -3.5  
                
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        bpy.ops.object.mode_set(mode='POSE')
        self.rename_bone("Lower_Leg_L_Bone.001", "Foot_L")
        bpy.ops.object.mode_set(mode='EDIT')

        # Parent to Torso Bone

        bpy.ops.armature.select_all(action='DESELECT')

        bpy.data.armatures["Armature"].edit_bones['Upper_Leg_L_Bone'].parent = bpy.data.armatures["Armature"].edit_bones['Waist_Bone']


        #### PARENTING ####

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.parent_set(type='ARMATURE_NAME')
    
    def first_bone_setup(self, bone_name):
        
        # Add the armature
        bpy.ops.object.armature_add(enter_editmode=False, align='WORLD', location=bpy.data.objects[self.bone_part_list[0]].location, scale=(1, 1, 1))
        armature_name =  bpy.context.object.data.name
        
        # Set it to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        
        
        # Change bone name
        new_bone_name = self.rename_bone("Bone", bone_name)
#        name_of_bone = bone_name + "_Bone" 
#        bpy.context.object.data.bones["Bone"].name = name_of_bone    
        
        self.select_bone_part(tail = True, bone_name = new_bone_name)
        
        bpy.ops.transform.translate(value=(-0, -0, -2), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        
        self.select_bone_part(tail = True, bone_name = new_bone_name)
        
        self.select_bone_part(head = True, bone_name = new_bone_name)
        
    
    def extrude_bone(self, bone_name, extrude_location):
        
        bpy.context.scene.cursor.location = extrude_location
        
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        
#        bpy.ops.object.mode_set(mode='POSE') 
#        bpy.context.object.data.bones["Waist_Bone.001"].name = "Torso_Bone" 
#        
#        self.select_bone_part(False, True, False, bone_name + ".001")
        
#        bpy.context.object.data.bones["Waist_Bone.001"].name = "Torso_Bone" 
        
#        bpy.ops.object.mode_set(mode='EDIT')
        
    def select_bone_part(self, tail = False, body = False, head = False, bone_name = "Bone"):
        bpy.ops.armature.select_all(action='DESELECT')
        bpy.data.armatures["Armature"].edit_bones[bone_name].select_tail = tail
        bpy.data.armatures["Armature"].edit_bones[bone_name].select = body
        bpy.data.armatures["Armature"].edit_bones[bone_name].select_head = head
        bpy.ops.object.mode_set(mode='EDIT')
        
    def rename_bone(self, original_bone_name, new_bone_name):
         # Change bone name
        name_of_bone = new_bone_name + "_Bone" 
        bpy.context.object.data.bones[original_bone_name].name = name_of_bone
        
        return name_of_bone

class Center_Character(bpy.types.Operator):
    bl_label = "Center Character (Select the Torso before clicking)"
    bl_idname = "center.character"
        
    def execute (self, context):
        
        bpy.context.object.name = "Torso"
        
        bpy.ops.object.select_all(action='SELECT')
        
        bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
        
        for obj in bpy.context.selected_objects:
            if obj != bpy.context.active_object:
                obj.select_set(False)
        
        bpy.ops.object.location_clear(clear_delta=False)
        
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        bpy.ops.object.select_all(action='DESELECT')


        return {'FINISHED'}

class Clean_Character(bpy.types.Operator):
    bl_label = "Clean Character"
    bl_idname = "clean.character"
        
    def execute (self, context):
        
        bpy.ops.object.select_all(action='SELECT')

        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.remove_doubles()
                bpy.ops.mesh.tris_convert_to_quads()
                bpy.ops.mesh.customdata_custom_splitnormals_clear()
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.shade_smooth()
                bpy.context.object.data.use_auto_smooth = True
                bpy.context.object.data.auto_smooth_angle = 1.22173

        
        self.report({'INFO'}, 'CLEANED!')  
        return {'FINISHED'}
    
class Name_Head(bpy.types.Operator):
    bl_label = "Head"
    bl_idname = "name.head" 
    
    def execute (self, context):
        bpy.context.object.name = "Head"
        
        return {'FINISHED'}
    
class Name_Upper_Arm_R(bpy.types.Operator):
    bl_label = "Upper_Arm_R"
    bl_idname = "name.upper_arm_r" 
    
    def execute (self, context):
        bpy.context.object.name = "Upper_Arm_R"
        
        return {'FINISHED'}
    
    
class Name_Torso(bpy.types.Operator):
    bl_label = "Torso"
    bl_idname = "name.torso" 
    
    def execute (self, context):
        bpy.context.object.name = "Torso"
        
        return {'FINISHED'}
    
    
class Name_Upper_Arm_L(bpy.types.Operator):
    bl_label = "Upper_Arm_L"
    bl_idname = "name.upper_arm_l" 
    
    def execute (self, context):
        bpy.context.object.name = "Upper_Arm_L"
        
        return {'FINISHED'}

class Name_Lower_Arm_R(bpy.types.Operator):
    bl_label = "Lower_Arm_R"
    bl_idname = "name.lower_arm_r" 
    
    def execute (self, context):
        bpy.context.object.name = "Lower_Arm_R"
        
        return {'FINISHED'}
    

class Name_Lower_Arm_L(bpy.types.Operator):
    bl_label = "Lower_Arm_L"
    bl_idname = "name.lower_arm_l" 
    
    def execute (self, context):
        bpy.context.object.name = "Lower_Arm_L"
        
        return {'FINISHED'}
    
class Name_Hand_R(bpy.types.Operator):
    bl_label = "Hand_R"
    bl_idname = "name.hand_r" 
    
    def execute (self, context):
        bpy.context.object.name = "Hand_R"
        
        return {'FINISHED'}
    
class Name_Waist(bpy.types.Operator):
    bl_label = "Waist"
    bl_idname = "name.waist" 
    
    def execute (self, context):
        bpy.context.object.name = "Waist"
        
        return {'FINISHED'}
    
class Name_Hand_L(bpy.types.Operator):
    bl_label = "Hand_L"
    bl_idname = "name.hand_l" 
    
    def execute (self, context):
        bpy.context.object.name = "Hand_L"
        
        return {'FINISHED'}
    
class Name_Upper_Leg_R(bpy.types.Operator):
    bl_label = "Upper_Leg_R"
    bl_idname = "name.upper_leg_r" 
    
    def execute (self, context):
        bpy.context.object.name = "Upper_Leg_R"
        
        return {'FINISHED'}
    
class Name_Upper_Leg_L(bpy.types.Operator):
    bl_label = "Upper_Leg_L"
    bl_idname = "name.upper_leg_l" 
    
    def execute (self, context):
        bpy.context.object.name = "Upper_Leg_L"
        
        return {'FINISHED'}
    
class Name_Lower_Leg_R(bpy.types.Operator):
    bl_label = "Lower_Leg_R"
    bl_idname = "name.lower_leg_r" 
    
    def execute (self, context):
        bpy.context.object.name = "Lower_Leg_R"
        
        return {'FINISHED'}
        
class Name_Lower_Leg_L(bpy.types.Operator):
    bl_label = "Lower_Leg_L"
    bl_idname = "name.lower_leg_l" 
    
    def execute (self, context):
        bpy.context.object.name = "Lower_Leg_L"
        
        return {'FINISHED'}
    
class Name_Foot_R(bpy.types.Operator):
    bl_label = "Foot_R"
    bl_idname = "name.foot_r" 
    
    def execute (self, context):
        bpy.context.object.name = "Foot_R"
        
        return {'FINISHED'}
        
class Name_Foot_L(bpy.types.Operator):
    bl_label = "Foot_L"
    bl_idname = "name.foot_l" 
    
    def execute (self, context):
        bpy.context.object.name = "Foot_L"
        
        return {'FINISHED'}

#class Set_Name(bpy.types.Operator):
#    bl_label = "Set Names"
#    bl_idname = "set.name"    
#            
#    preset_enum : bpy.props.EnumProperty(
#        name = "NAMER",
#        description= "Name current object",
#        items = [ 
#            ('OP1', "Head", "Set name to 'Head'"),
#            ('OP2', "Torso", "Set name to 'Torso'"),        
#            ('OP3', "Waist", "Set name to 'Waist'"),        
#            ('OP4', "Upper_Leg_R", "Set name to 'Upper_Leg_R'"),        
#            ('OP5', "Lower_Leg_R", "Set name to 'Lower_Leg_R'"),        
#            ('OP6', "Foot_R", "Set name to 'Foot_R'"),        
#            ('OP7', "Upper_Arm_R", "Set name to 'Upper_Arm_R'"),        
#            ('OP8', "Lower_Arm_R", "Set name to 'Lower_Arm_R'"),        
#            ('OP9', "Hand_R", "Set name to 'Hand_R'"), 
#            ('OP10', "Upper_Leg_L", "Set name to 'Upper_Leg_L'"),        
#            ('OP11', "Lower_Leg_L", "Set name to 'Lower_Leg_L'"),        
#            ('OP12', "Foot_L", "Set name to 'Foot_L'"),        
#            ('OP13', "Upper_Arm_L", "Set name to 'Upper_Arm_L'"),        
#            ('OP14', "Lower_Arm_L", "Set name to 'Lower_Arm_L'"),        
#            ('OP15', "Hand_L", "Set name to 'Hand_L'")            
#        ]
#    )
#    
#    def invoke(self, context, event):
#        wm = context.window_manager
#        return wm.invoke_props_dialog(self)
#    
#    def draw(self, context):
#        layout = self.layout
#        layout.prop(self, "preset_enum")
#        
#    def execute (self, context):
#        
#        if self.preset_enum == 'OP1':
#            bpy.context.object.name = "Head"
#        elif self.preset_enum == 'OP2':
#            bpy.context.object.name = "Torso"
#        elif self.preset_enum == 'OP3':
#            bpy.context.object.name = "Waist"
#        elif self.preset_enum == 'OP4':
#            bpy.context.object.name = "Upper_Leg_R"
#        elif self.preset_enum == 'OP5':
#            bpy.context.object.name = "Lower_Leg_R"
#        elif self.preset_enum == 'OP6':
#            bpy.context.object.name = "Foot_R"
#        elif self.preset_enum == 'OP7':
#            bpy.context.object.name = "Upper_Arm_R"
#        elif self.preset_enum == 'OP8':
#            bpy.context.object.name = "Lower_Arm_R"
#        elif self.preset_enum == 'OP9':
#            bpy.context.object.name = "Hand_R"
#        elif self.preset_enum == 'OP10':
#            bpy.context.object.name = "Upper_Leg_L"
#        elif self.preset_enum == 'OP11':
#            bpy.context.object.name = "Lower_Leg_L"
#        elif self.preset_enum == 'OP12':
#            bpy.context.object.name = "Foot_L"
#        elif self.preset_enum == 'OP13':
#            bpy.context.object.name = "Upper_Arm_L"
#        elif self.preset_enum == 'OP14':
#            bpy.context.object.name = "Lower_Arm_L"
#        elif self.preset_enum == 'OP15':
#            bpy.context.object.name = "Hand_L"
#                
#            
#        return {'FINISHED'}       
        
class Import_OBJ_Character(bpy.types.Operator, ImportHelper):
    bl_label = "Import OBJ Character"
    bl_idname = "import.obj_character"
    
    filter_glob: StringProperty(
        default='*.obj',
        options = {'HIDDEN'}
    )
    
    some_boolean: BoolProperty(
        name='Import these dudes',
        description='Do a thing with the file you\'ve selected',
        default=True,
    )
    
    def execute (self, context):
        
        filename, extension = os.path.splitext(self.filepath)
        
        print("Test: " + filename, extension)
        
        print('Selected file: ', self.filepath)
        print('File name: ', filename)
        print('File extension: ', extension)
        print('Some Boolean: ', self.some_boolean)
        
        dir_name, file_name = os.path.split(self.filepath)
        
        print("---------------------------------------")
        
        # Iterate through files in directory
        #print(os.listdir(dir_name))
        
        
        # Purge orphan data to clean project
        bpy.ops.outliner.orphans_purge()
        
        for obj_file in os.listdir(dir_name):
            
            # Import each file with the obj extension
            if obj_file.endswith(".obj"):
                bpy.ops.import_scene.obj(filepath=os.path.join(dir_name,obj_file))
            
        return {'FINISHED'}
    
class Import_FBX_Character(bpy.types.Operator, ImportHelper):
    bl_label = "Import FBX Character"
    bl_idname = "import.fbx_character"
    
    filter_glob: StringProperty(
        default='*.fbx',
        options = {'HIDDEN'}
    )
    
    some_boolean: BoolProperty(
        name='Import FBX character',
        description='Select the directory with the FBX character and select \'Import\'',
        default=True,
    )
    
    def execute (self, context):
        
        filename, extension = os.path.splitext(self.filepath)
        
        print("Test: " + filename, extension)
        
        print('Selected file: ', self.filepath)
        print('File name: ', filename)
        print('File extension: ', extension)
        print('Some Boolean: ', self.some_boolean)
        
        dir_name, file_name = os.path.split(self.filepath)
        
        print("---------------------------------------")
        
        # Iterate through files in directory
        #print(os.listdir(dir_name))
        
        
        # Purge orphan data to clean project
        bpy.ops.outliner.orphans_purge()
            
        for obj_file in os.listdir(dir_name):
            
            # Import each file with the obj extension
            if obj_file.endswith(".fbx"):
                bpy.ops.import_scene.fbx(filepath=os.path.join(dir_name,obj_file))
            
        return {'FINISHED'}
    
class Set_Pivot(bpy.types.Operator):
    bl_label = "Set Pivot"
    bl_idname = "set.pivot"
        
    def execute (self, context):
        
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.mode_set(mode='OBJECT') 
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
            
        return {'FINISHED'}
        

          
classes = [Rig_A_Roblox, Import_OBJ_Character, Import_FBX_Character, Set_Pivot, Rig_Character, Clean_Character, Center_Character, Remove_Vertex_Groups, Make_Opaque, Name_Head, Name_Upper_Arm_R, Name_Torso, Name_Upper_Arm_L, Name_Lower_Arm_R, Name_Lower_Arm_L, Name_Hand_R, Name_Waist, Name_Hand_L, Name_Upper_Leg_R, Name_Upper_Leg_L, Name_Lower_Leg_R, Name_Lower_Leg_L, Name_Foot_R, Name_Foot_L, Toggle_Visibility, View_Character, Select_Face, Xray_Rig]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == "__main__":
    register()
