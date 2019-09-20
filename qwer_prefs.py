import bpy
from bpy.types import Operator, AddonPreferences
from bpy.props import BoolProperty


class QWERAddonPreferences(AddonPreferences):
    # this must match the add-on name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __name__

    panel_bool: BoolProperty(
        name="Enable Panel",
        default=False,
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="The QWER Addon Panel is convenient for assigning shortcuts")
        layout.prop(self, "boolean")
        row.operator('object.qwer_prefs_update', text="Update")


class OBJECT_OT_qwer_prefs_update(Operator):
    """Update QWER preferences"""
    bl_idname = "object.qwer_prefs_update"
    bl_label = "QWER Preferences Update"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        info = ("Boolean %r" %
                (addon_prefs.panel_bool))

        self.report({'INFO'}, info)
        print(info)

        return {'FINISHED'}


# Registration
def register():
    bpy.utils.register_class(OBJECT_OT_qwer_prefs_update)
    bpy.utils.register_class(QWERAddonPreferences)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_qwer_prefs_update)
    bpy.utils.unregister_class(QWERAddonPreferences)