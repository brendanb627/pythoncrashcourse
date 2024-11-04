import pyglet
from pyglet import shapes

window = pyglet.window.Window(600, 600, "Pyglet 3D Example")
circle = shapes.Circle(x=100, y=150, radius=100, color=(50, 225, 30))


@window.event
def on_draw():
    window.clear()
    circle.draw()
    

pyglet.app.run()

