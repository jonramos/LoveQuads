import bpy

from . finder import FindTriangles_OT_Operator
from . panel import MyPanel_PT_Panel

bl_info = {
    "name": "LoveQuads",
    "author": "Jonathan Ramos",
    "description": "dsadsads",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}

classes = (FindTriangles_OT_Operator, MyPanel_PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)
