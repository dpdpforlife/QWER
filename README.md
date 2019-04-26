# QWER Controls
Industry standard move, rotate and scale interaction for Blender 2.80.

**General Description**

This is a simple addon and accompanying keymaps that make the transform tools and select active tools work in a way more similar to other DCCs while also making the traditional Blender fast transform tools more discoverable. 

Currently, the move rotate and scale operations can be triggered via shortcut key or using the QWER tab in the N panel. 

![QWER Panel](https://i.ibb.co/wwq6V1Z/QWER-Panel.png)

There is also a "Tweak Better" modifier that is meant to take the place of the tweak behavior in the Select Active Tool. 

![Select Active Tool](https://i.ibb.co/D4VLfpM/Select-Active-Tool.png)

What this all means is that the move rotate and scale Active Tools never need to be used. They are replaced with the QWER Panel tools which basically just activate the Gizmos currently found in the Viewport Gizmos dropdown in the 3d View. These work independently of the other Active Tools, meaning you can have Box Select, Circle Select, or Lasso select enabled and a drag in the viewport makes a selection instead of transforming (as in the transform active tools). If instead, you have the Select active tool enabled, a drag will perform the action of whatever Gizmo is currently active. If you have no gizmo active, the tool performs as usual with a move tweak action. Multiple gizmos active will transform based on the highest selected transform type (Move taking precedence over Rotate).

The buttons in the QWER Panel can be assigned shortcuts like any other button in blender. Just right click on the button and choose "Assign Shortcut" from the dropdown. Also the Select Active Tool can be modified to tweak using my Tweak Better transform tool by adding a new entry under the "3D View Tool: Select" category like as in the picture below:
![TweakBetter](https://i.ibb.co/rm8XFcn/Tweak-Better-Keymap.png)

**Background**

The 2.80 active tools are great in some respects, but the paradigm breaks down with the transform active tools. These make selecting and transforming multiple objects a slow, tedious process requiring the user to switch back and forth between transform tools like move and the selection tools like box select. This issue has been addressed by Blender developers by adding gizmo visibility toggles, but these are hidded in a dropdown in the 3d view and require too many clicks to activate. This addon allows you to have various selection modes enabled while also having access to the transform tools. The main difference being that clicking and dragging from a blank area of the screen will select instead of translating. This is not only the most common way of handling select and transform operations by the majority of DCC software, but is also a faster and more intuitive way of working when compared to using the Active Tools alone.

**The addon has 7 operators.**

- Move (view3d.qwer_controls.(mode="Move")) activates only the move gizmo. Other transform gizmos are hidden. 
- Rotate (view3d.qwer_controls.(mode="Rotate")) activates only the rotate gizmo. Other transform gizmos are hidden.
- Scale (view3d.qwer_controls.(mode="Scale")) activates only the scale gizmo. Other transform gizmos are hidden.
- AddMove (view3d.qwer_controls.(mode="AddMove")) activates the move gizmo, and also keeps any other transform gizmos active. This allows you to have any or all transform gizmos active simultaneously.
- AddRotate (view3d.qwer_controls.(mode="AddRotate")) activates the Rotate gizmo, and also keeps any other transform gizmos active.
- AddScale (view3d.qwer_controls.(mode="AddScale")) activates the move gizmo, and also keeps any other transform gizmos active.
- TweakBetter (object.tweak_better) a smart transform operator that checks to see what transform gizmos are active and Moves, Rotates or Scales accordingly.

**There are also three keymaps included for your convenience.**

- WGRS_Blender_Keymap.py is based on the default Blender 2.80 keymap with the following changes:
  - W toggles selection modes.
  - G toggles the Move gizmo.
  - CTRL+Alt+G adds the Move gizmo using the AddMove mode.
  - Dragging the mouse while the G key is pressed (Click Drag behaviour) enables the traditional Blender move operator with all of its associated interaction bindings (MMB+Drag restricts axes, Shift+Z moves along the x and y axes, etc.).
  - R toggles the Rotate gizmo.
  - CTRL+Alt+R adds the Rotate gizmo using the AddRotate mode.
  - Dragging the mouse while the R key is pressed enables the traditional Blender rotate operator with all of its associated interaction.
  - S toggles the Scale gizmo.
  - CTRL+Alt+S adds the Scale gizmo using the AddScale mode.
  - Dragging the mouse while the S key is pressed enables the traditional Blender scale operator with all of its associated interaction.
  - The default tweak behavior of the Select Active Tool has been replaced with TweakBetter

- QWER_Blender_Keymap.py is based on the default Blender 2.80 keymap with the following changes:
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
  - The default tweak behavior of the Select Active Tool has been replaced with TweakBetter

- QWER_Industry_Keymap.py is based on the Industry Compatible Keymap that ships with Blender, but has the following changes:
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
  - The default tweak behavior of the Select Active Tool has been replaced with TweakBetter
