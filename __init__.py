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

from . qwer_op import Qwer_OT_Operator, Cycle_OT_Operator, TweakBetter, Qwer_OT_Buttons
from . qwer_panel import Qwer_PT_Panel,draw_topbar

def register():
    bpy.utils.register_class(Qwer_OT_Operator)
    bpy.utils.register_class(Qwer_OT_Buttons)
    bpy.utils.register_class(Cycle_OT_Operator)
    bpy.utils.register_class(TweakBetter)
    bpy.utils.register_class(Qwer_PT_Panel)
    bpy.types.VIEW3D_HT_tool_header.append(draw_topbar)

def unregister():
    bpy.utils.unregister_class(Qwer_OT_Operator)
    bpy.utils.unregister_class(Qwer_OT_Buttons)
    bpy.utils.unregister_class(Cycle_OT_Operator)
    bpy.utils.unregister_class(TweakBetter)
    bpy.utils.unregister_class(Qwer_PT_Panel)
    bpy.types.VIEW3D_HT_tool_header.remove(draw_topbar)

if __name__ == "__main__":
    register()
    
