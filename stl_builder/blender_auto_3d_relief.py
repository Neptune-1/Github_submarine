import bpy
import random
name = 'Gridtastic'
rows = 5
columns = 20
size = 1

def vert(column, row):
    global u
    
    if row==0:
        u=random.randint(1,3)
        
    return (column*3 , row , u)
 
 
def face(column, row):
 
    return (column* rows + row,
            column * rows + 1 + row,
            (column + 1) * rows + 1 + row,
            (column + 1) * rows + row)
 
 
verts = [vert(x, y) for x in range(columns) for y in range(rows)]
faces = [face(x, y) for x in range(columns - 1) for y in range(rows - 1)]
 
mesh = bpy.data.meshes.new(name)
mesh.from_pydata(verts, [], faces)
 
obj = bpy.data.objects.new(name, mesh)
bpy.context.scene.objects.link(obj)
 
