import bpy
from bpy.props import StringProperty

class Qwer_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.qwer_controls"
    bl_label = "qwer Controls"
    bl_description = "qwer Controls"

    mode: StringProperty()
    
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

class TweakBetter(bpy.types.Operator):
    """Fix the select active tool"""
    bl_idname = "object.tweak_better"
    bl_label = "Tweak Better"

    tmode: StringProperty()

    def modal(self, context, event):
        if event.type == 'MOUSEMOVE':
            bpy.ops.transform.transform(
                            'INVOKE_DEFAULT',
                            mode=self.tmode)
            return {'FINISHED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.object:
            
            if context.space_data.show_gizmo_object_translate==True:
                self.tmode = 'TRANSLATION'
            elif context.space_data.show_gizmo_object_rotate==True:
                self.tmode = 'ROTATION'
            elif context.space_data.show_gizmo_object_scale==True:
                self.tmode = 'RESIZE'
            elif context.space_data.show_gizmo_object_rotate==True:
                self.tmode = 'ROTATION'
            else: self.tmode = 'TRANSLATION'
                
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}
