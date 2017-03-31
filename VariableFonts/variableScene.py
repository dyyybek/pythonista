import scene
from variableTools import glyphsListConstruct

glyphs_list = glyphsListConstruct()
x_factor = 10.24 / 2


class MyScene(scene.Scene):
    def setup(self):
        self.myPath = scene.ShapeNode(glyphs_list[0])
        self.myPath.anchor_point = 0, 0
        self.myPath.position = (1024 - self.myPath.bbox.width * 1.75,
                                 768 - self.myPath.bbox.height * 1.3)
        self.add_child(self.myPath)
        self.background_color = 'lightgrey'

    def touch_began(self, touch):
        x, y = touch.location
        z = int(x / x_factor)
        self.myPath.path = glyphs_list[z]

    def touch_moved(self, touch):
        x, y = touch.location
        z = int(x / x_factor)
        self.myPath.path = glyphs_list[z]


scene.run(MyScene(), show_fps=True)
