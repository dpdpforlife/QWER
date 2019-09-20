import bpy
from bpy.props import StringProperty, BoolProperty

class Qwer_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.qwer_controls"
    bl_label = "qwer Controls"
    bl_description = "qwer Controls"

    mode: StringProperty()
    
    def invoke(self, context, event):

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

class Qwer_OT_Buttons(bpy.types.Operator):
    bl_idname = "view3d.qwer_Buttons"
    bl_label = "qwer Buttons"
    bl_description = "qwer Buttons"

    move: BoolProperty()
    rotate: BoolProperty()
    scale: BoolProperty()
    
    def invoke(self, context, event):

        areas = bpy.context.workspace.screens[0].areas

        if self.move:
            if event.shift:
                for area in areas:
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            space.show_gizmo_object_translate^= True   
            else:
                for area in areas:
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            space.show_gizmo_object_translate^= True
                            space.show_gizmo_object_rotate = False
                            space.show_gizmo_object_scale = False   
            self.move = False
        if self.rotate:
            if event.shift:
                for area in areas:
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            space.show_gizmo_object_rotate^= True   
            else:
                for area in areas:
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            space.show_gizmo_object_translate = False
                            space.show_gizmo_object_rotate^= True
                            space.show_gizmo_object_scale = False   
            self.rotate = False
        if self.scale:
            if event.shift:
                for area in areas:
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            space.show_gizmo_object_scale^= True
            else:
                for area in areas:
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            space.show_gizmo_object_translate = False
                            space.show_gizmo_object_rotate = False
                            space.show_gizmo_object_scale^= True   
            self.scale = False
        return {'FINISHED'}

class Cycle_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.qwer_cycle"
    bl_label = "Cycle xform Gizmos"
    bl_description = "Cycle through the transform gizmos"
    
    def invoke(self, context, event):
        
        areas = bpy.context.workspace.screens[0].areas
 
        for area in areas:
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    if space.show_gizmo_object_translate:
                        space.show_gizmo_object_translate = False
                        space.show_gizmo_object_rotate = True
                        space.show_gizmo_object_scale = False
                    elif space.show_gizmo_object_rotate:
                        space.show_gizmo_object_translate = False
                        space.show_gizmo_object_rotate = False
                        space.show_gizmo_object_scale = True
                    elif space.show_gizmo_object_scale:
                        space.show_gizmo_object_translate = True
                        space.show_gizmo_object_rotate = False
                        space.show_gizmo_object_scale = False
                    else:
                        space.show_gizmo_object_translate = True 
        return {'FINISHED'}

class TweakBetter(bpy.types.Operator):
    """Fix the select active tool"""
    bl_idname = "object.tweak_better"
    bl_label = "Tweak Better"

    tmode: StringProperty(name="Transform Mode")
    release: BoolProperty(name="Confirm on Release")

    def modal(self, context, event):
        if event.type == 'MOUSEMOVE':
            bpy.ops.transform.transform(
                            'INVOKE_DEFAULT',
                            mode=self.tmode,
                            release_confirm=self.release)
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

class MoveInvoke(bpy.types.Operator):
    bl_idname = "view3d.move_invoke"
    bl_label = "Invoke Move with Gizmo"
    bl_description = "Enable the move gizmo and invoke the move command"
    
    release: BoolProperty(name="Confirm on Release")

    def modal(self, context, event):
        bpy.ops.transform.transform(
                    'INVOKE_DEFAULT',
                    mode='TRANSLATION',
                    release_confirm=self.release)
        return {'FINISHED'}

    def invoke(self, context, event):        
        areas = bpy.context.workspace.screens[0].areas
        if context.object:
            for area in areas:
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.show_gizmo_object_translate = True
                        space.show_gizmo_object_rotate = False
                        space.show_gizmo_object_scale = False
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}

class RotateInvoke(bpy.types.Operator):
    bl_idname = "view3d.rotate_invoke"
    bl_label = "Invoke Rotate with Gizmo"
    bl_description = "Enable the rotate gizmo and invoke the rotate command"
    
    release: BoolProperty(name="Confirm on Release")

    def modal(self, context, event):
        bpy.ops.transform.transform(
                    'INVOKE_DEFAULT',
                    mode='ROTATION',
                    release_confirm=self.release)
        return {'FINISHED'}

    def invoke(self, context, event):        
        areas = bpy.context.workspace.screens[0].areas
        if context.object:
            for area in areas:
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.show_gizmo_object_translate = False
                        space.show_gizmo_object_rotate = True
                        space.show_gizmo_object_scale = False
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}

class ScaleInvoke(bpy.types.Operator):
    bl_idname = "view3d.scale_invoke"
    bl_label = "Invoke Scale with Gizmo"
    bl_description = "Enable the scale gizmo and invoke the scale command"
    
    release: BoolProperty(name="Confirm on Release")

    def modal(self, context, event):
        bpy.ops.transform.transform(
                    'INVOKE_DEFAULT',
                    mode='RESIZE',
                    release_confirm=self.release)
        return {'FINISHED'}

    def invoke(self, context, event):        
        areas = bpy.context.workspace.screens[0].areas
        if context.object:
            for area in areas:
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.show_gizmo_object_translate = False
                        space.show_gizmo_object_rotate = False
                        space.show_gizmo_object_scale = True
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}