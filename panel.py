import bpy


class MyPanel_PT_Panel(bpy.types.Panel):
    bl_idname = "MYPANEL_PT_Panel"
    bl_label = "Test Panel"
    bl_category = "Teste Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('view3d.cursor_center', text='Call to Action')
