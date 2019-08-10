import bpy

from . finder import FindTriangles_OT_Operator
from . panel import MyPanel_PT_Panel

bl_info = {
    "name": "LoveQuads",
    "author": "Jonathan Ramos",
    "description": "Highlight all triangles and ngons",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "EditMode: Select > Show ngons",
    "warning": "",
    "category": "Mesh"
}

def menu_func(self, context):
    
    ###usage
    ###self.layout.operator('Class unique id', text='text to overwrite class label', icon='MESH_CUBE')
    self.layout.operator('view3d.cursor_center')

#classes = (FindTriangles_OT_Operator, MyPanel_PT_Panel)
#register, unregister = bpy.utils.register_classes_factory(classes)

def register():
    bpy.utils.register_class(FindTriangles_OT_Operator)
    bpy.types.VIEW3D_MT_select_edit_mesh.append(menu_func)
    

def unregister():
    bpy.utils.unregister_class(FindTriangles_OT_Operator)
    bpy.types.VIEW3D_MT_select_edit_mesh.remove(menu_func)

if __name__ == "__main__":
    register()