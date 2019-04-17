import bpy

class Qwer_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.qwer_controls"
    bl_label = "qwer Controls"
    bl_description = "qwer Controls"

    mode = bpy.props.StringProperty()
    
    def execute(self, context):        
        areas = bpy.context.workspace.screens[0].areas

        if self.mode == "Move":
            for area in areas:
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.show_gizmo_object_translate^= True
                        space.show_gizmo_object_rotate = False
                        space.show_gizmo_object_scale = False
        if self.mode == "Rotate":
            for area in areas:
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.show_gizmo_object_translate = False
                        space.show_gizmo_object_rotate^= True
                        space.show_gizmo_object_scale = False
        if self.mode == "Scale":
            for area in areas:
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.show_gizmo_object_translate = False
                        space.show_gizmo_object_rotate = False
                        space.show_gizmo_object_scale^= True  
        if self.mode == "AddMove":
            for area in areas:
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.show_gizmo_object_translate^= True
        if self.mode == "AddRotate":
            for area in areas:
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.show_gizmo_object_rotate^= True
        if self.mode == "AddScale":
            for area in areas:
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.show_gizmo_object_scale^= True 
        return {'FINISHED'}