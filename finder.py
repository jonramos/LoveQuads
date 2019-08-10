import bpy


class FindTriangles_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.cursor_center" # unique identifier for buttons and menu items to reference.
    bl_label = "Show Ngons" # display name in the interface/search. can be overwritten in menu_func
    bl_description = "Display all triangles and ngons on your mesh" # display a description on mouse hover.
    bl_options = {'REGISTER', 'UNDO'} # enable undo for the operator.

    # execute() is called by blender when running the operator.
    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()
        return {'FINISHED'} # this lets blender know the operator finished successfully.
