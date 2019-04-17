import bpy

class Qwer_PT_Panel(bpy.types.Panel):
    bl_idname = "QWER_PT_Panel"
    bl_label = "QWER Panel"
    bl_category = "QWER Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row(align=True)
        row.operator('view3d.qwer_controls', text="Move").mode = "Move"
        row.operator('view3d.qwer_controls', text="Rotate").mode = "Rotate"
        row.operator('view3d.qwer_controls', text="Scale").mode = "Scale"
        row = layout.row(align=True)
        row.operator('view3d.qwer_controls', text="AMove").mode = "AddMove"
        row.operator('view3d.qwer_controls', text="ARotate").mode = "AddRotate"
        row.operator('view3d.qwer_controls', text="AScale").mode = "AddScale"