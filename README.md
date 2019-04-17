# QWER Controls
Industry standard move, rotate and scale interaction for Blender 2.80.

This is a simple addon and accompanying keymaps that make the transform tools work in a way more similar to other DCCs while also making the traditional Blender fast transform tools more discoverable. The 2.80 active tools are great in some respects, but the paradigm breaks down with the transform active tools. These make selecting and transforming multiple objects a slow, tedious process requiring the user to switch back and forth between transform tools like move and the selection tools like box select. This issue has been addressed by Blender developers by adding gizmo visibility toggles, but these are hidded in a dropdown in the 3d view and require too many clicks to activate. This addon allows you to have various selection modes enabled while also having access to the transform tools. The main difference being that clicking and dragging from a blank area of the screen will select instead of translating. This is not only the most common way of handling select and transform operations by the majority of DCC software, but is also a faster and more intuitive way of working when compared to using the Active Tools alone.

####The addon has 6 methods.

- Move (view3d.qwer_controls.(mode="Move")) activates only the move gizmo. Other transform gizmos are hidden. 
- Rotate (view3d.qwer_controls.(mode="Rotate")) activates only the rotate gizmo. Other transform gizmos are hidden.
- Scale (view3d.qwer_controls.(mode="Scale")) activates only the scale gizmo. Other transform gizmos are hidden.
- AddMove (view3d.qwer_controls.(mode="AddMove")) activates the move gizmo, and also keeps any other transform gizmos active. This allows you to have any or all transform gizmos active simultaneously.
- AddRotate (view3d.qwer_controls.(mode="AddRotate")) activates the Rotate gizmo, and also keeps any other transform gizmos active.
- AddScale (view3d.qwer_controls.(mode="AddScale")) activates the move gizmo, and also keeps any other transform gizmos active.

####There are also two keymaps included for your convenience.

QWER_Blender_Keymap.py is based on the default Blender 2.80 keymap with the following changes:
- Q toggles selection modes.
- W toggles the Move gizmo.
- CTRL+Alt+W adds the Move gizmo using the AddMove mode.
- Dragging the mouse while the W key is pressed (Click Drag behaviour) enables the traditional Blender move operator with all of its associated interaction bindings (MMB+Drag restricts axes, Shift+Z moves along the x and y axes, etc.).
- E toggles the Rotate gizmo.
- CTRL+Alt+E adds the Rotate gizmo using the AddRotate mode.
- Dragging the mouse while the E key is pressed enables the traditional Blender rotate operator with all of its associated interaction.
- R toggles the Scale gizmo.
- CTRL+Alt+R adds the Scale gizmo using the AddScale mode.
- Dragging the mouse while the R key is pressed enables the traditional Blender scale operator with all of its associated interaction.
- E shortcut for extrude in edit mode was changed to CTRL+E
- X was changed from delete to the Quick User Menu

QWER_Industry_Keymap.py is based on the Industry Compatible Keymap that ships with Blender, but has the following changes:
- Q toggles selection modes.
- W toggles the Move gizmo.
- CTRL+Alt+W adds the Move gizmo using the AddMove mode.
- Dragging the mouse while the W key is pressed (Click Drag behaviour) enables the traditional Blender move operator with all of its associated interaction bindings (MMB+Drag restricts axes, Shift+Z moves along the x and y axes, etc.).
- E toggles the Rotate gizmo.
- CTRL+Alt+E adds the Rotate gizmo using the AddRotate mode.
- Dragging the mouse while the E key is pressed enables the traditional Blender rotate operator with all of its associated interaction.
- R toggles the Scale gizmo.
- CTRL+Alt+R adds the Scale gizmo using the AddScale mode.
- Dragging the mouse while the R key is pressed enables the traditional Blender scale operator with all of its associated interaction.
