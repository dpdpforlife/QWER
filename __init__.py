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

from . qwer_op import Qwer_OT_Operator
from . qwer_panel import Qwer_PT_Panel

classes = (Qwer_OT_Operator, Qwer_PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)