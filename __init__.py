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
from . qwer_panel import Qwer_PT_Panel,draw_topbar

def register():
    bpy.utils.register_class(Qwer_OT_Operator)
    bpy.utils.register_class(Cycle_OT_Operator)
    bpy.utils.register_class(MoveInvoke)
    bpy.utils.register_class(RotateInvoke)
    bpy.utils.register_class(ScaleInvoke)
    bpy.utils.register_class(TweakBetter)
    bpy.utils.register_class(Qwer_PT_Panel)
    #bpy.types.VIEW3D_HT_tool_header.append(draw_topbar)
    bpy.types.VIEW3D_PT_tools_active.prepend(draw_topbar)

def unregister():
    bpy.utils.unregister_class(Qwer_OT_Operator)
    bpy.utils.unregister_class(Cycle_OT_Operator)
    bpy.utils.unregister_class(MoveInvoke)
    bpy.utils.unregister_class(RotateInvoke)
    bpy.utils.unregister_class(ScaleInvoke)
    bpy.utils.unregister_class(TweakBetter)
    bpy.utils.unregister_class(Qwer_PT_Panel)
    #bpy.types.VIEW3D_HT_tool_header.remove(draw_topbar)
    bpy.types.VIEW3D_PT_tools_active.remove(draw_topbar)

if __name__ == "__main__":
    register()
    
