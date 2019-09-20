bl_info = {
    "name" : "qwer_addon",
    "author" : "Dan Pool (dpdp)",
    "description" : "QWER Addon",
    "blender" : (2, 80, 0),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from . qwer_op import Qwer_OT_Operator, Cycle_OT_Operator, TweakBetter, MoveInvoke, RotateInvoke, ScaleInvoke
from . qwer_panel import Qwer_PT_Panel,draw_topbar,draw_tools

from bpy.types import Operator, AddonPreferences
from bpy.props import BoolProperty


class QWERAddonPreferences(AddonPreferences):
    bl_idname = __name__

    panel_bool: BoolProperty(
        name="Enable Panel",
        default=True,
    )

    topbar_bool: BoolProperty(
        name="Show in Tools Settings Bar",
        default=True,
    )

    tools_bool: BoolProperty(
        name="Show in Active Tools Bar",
        default=True,
    )   
    def draw(self, context):
        layout = self.layout
        layout.label(text="The QWER Addon Panel is convenient for assigning shortcuts.")
        layout.prop(self, "panel_bool")
        layout.label(text="Choose where you would like to see the Move, Rotate and Scale buttons.")
        layout.prop(self, "topbar_bool")
        layout.prop(self, "tools_bool")
        layout.operator('object.qwer_prefs_update', text="Update")


class OBJECT_OT_qwer_prefs_update(Operator):
    """Update QWER preferences"""
    bl_idname = "object.qwer_prefs_update"
    bl_label = "QWER Preferences Update"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        if addon_prefs.panel_bool == True:
            try:
                bpy.utils.register_class(Qwer_PT_Panel)
            except:
                pass
        else:
            try:
                bpy.utils.unregister_class(Qwer_PT_Panel)
            except:
                pass

        info = ("Panel Enabled %r, Toolbar Enabled %r, Topbar Enabled %r" %
                (addon_prefs.panel_bool, addon_prefs.topbar_bool, addon_prefs.tools_bool))

        self.report({'INFO'}, info)
        print(info, "  ", addon_prefs)

        for region in context.area.regions:
            if region.type == "UI":
                region.tag_redraw()

        return {'FINISHED'}

def register():
 
    bpy.utils.register_class(QWERAddonPreferences)
    
    preferences = bpy.context.preferences
    addon_prefs = preferences.addons[__name__].preferences
 
    bpy.utils.register_class(OBJECT_OT_qwer_prefs_update)
    bpy.utils.register_class(Qwer_OT_Operator)
    bpy.utils.register_class(Cycle_OT_Operator)
    bpy.utils.register_class(MoveInvoke)
    bpy.utils.register_class(RotateInvoke)
    bpy.utils.register_class(ScaleInvoke)
    bpy.utils.register_class(TweakBetter)
    if addon_prefs.panel_bool == True:
        try:
            bpy.utils.register_class(Qwer_PT_Panel)
        except:
            pass
    bpy.types.VIEW3D_HT_tool_header.append(draw_topbar)
    bpy.types.VIEW3D_PT_tools_active.prepend(draw_tools)

def unregister():
    preferences = bpy.context.preferences
    addon_prefs = preferences.addons[__name__].preferences
    
    bpy.utils.unregister_class(OBJECT_OT_qwer_prefs_update)
    bpy.utils.unregister_class(QWERAddonPreferences)
    bpy.utils.unregister_class(Qwer_OT_Operator)
    bpy.utils.unregister_class(Cycle_OT_Operator)
    bpy.utils.unregister_class(MoveInvoke)
    bpy.utils.unregister_class(RotateInvoke)
    bpy.utils.unregister_class(ScaleInvoke)
    bpy.utils.unregister_class(TweakBetter)
    try:
        bpy.utils.unregister_class(Qwer_PT_Panel)
    except:
        pass
    bpy.types.VIEW3D_HT_tool_header.remove(draw_topbar)
    bpy.types.VIEW3D_PT_tools_active.remove(draw_tools)
    
if __name__ == "__main__":
    register()
    
