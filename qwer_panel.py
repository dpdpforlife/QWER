import bpy

class Qwer_PT_Panel(bpy.types.Panel):
    bl_idname = "QWER_PT_Panel"
    bl_label = "QWER Panel"
    bl_category = "QWER Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        dep_move = False
        dep_rot = False
        dep_scale = False

        area = next(area for area in bpy.context.screen.areas if area.type == 'VIEW_3D')
        space = next(space for space in area.spaces if space.type == 'VIEW_3D')
    
        if space.show_gizmo_object_translate:
            dep_move = True
        if space.show_gizmo_object_rotate:
            dep_rot = True
        if space.show_gizmo_object_scale:
            dep_scale = True
        
        layout = self.layout
        
        row = layout.row(align=True)
        row.operator('view3d.qwer_buttons', text="Move", depress=dep_move).move = True
        row.operator('view3d.qwer_buttons', text="Rotate", depress=dep_rot).rotate = True
        row.operator('view3d.qwer_buttons', text="Scale", depress=dep_scale).scale = True
        row = layout.row(align=True)
        row.operator('view3d.qwer_controls', text="ExMove").mode = "Move"
        row.operator('view3d.qwer_controls', text="ExRotate").mode = "Rotate"
        row.operator('view3d.qwer_controls', text="ExScale").mode = "Scale"
        row = layout.row(align=True)
        row.operator('view3d.qwer_controls', text="AMove").mode = "AddMove"
        row.operator('view3d.qwer_controls', text="ARotate").mode = "AddRotate"
        row.operator('view3d.qwer_controls', text="AScale").mode = "AddScale"
        row = layout.row(align=True)
        row.operator('view3d.qwer_cycle', text="Cycle Gizmo Visibility")
        
def draw_topbar(self, context):
    dep_move = False
    dep_rot = False
    dep_scale = False

    area = next(area for area in bpy.context.screen.areas if area.type == 'VIEW_3D')
    space = next(space for space in area.spaces if space.type == 'VIEW_3D')
    
    if space.show_gizmo_object_translate:
        dep_move = True
    if space.show_gizmo_object_rotate:
        dep_rot = True
    if space.show_gizmo_object_scale:
        dep_scale = True

    if context.region.alignment != 'RIGHT':
        layout = self.layout
        row = layout.row(align=True)
        row.operator('view3d.qwer_buttons', text="M", depress=dep_move).move = True
        row.operator('view3d.qwer_buttons', text="R", depress=dep_rot).rotate = True
        row.operator('view3d.qwer_buttons', text="S", depress=dep_scale).scale = True

    