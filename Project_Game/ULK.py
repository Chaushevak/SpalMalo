import cocos
from cocos.director import director
from cocos.layer import ColorLayer
from cocos.sprite import Sprite
from cocos.scenes import *
from cocos.text import Label
from cocos import mapcolliders
import pyglet
from pyglet.window import key

# ===============================MENU==================================================
class Menu_Scene(cocos.scene.Scene):
    def __init__(self):
        super().__init__()
        self.add(Menu_BG())
        self.add(MainMenu())

class Menu_BG(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        menu_bg = cocos.sprite.Sprite("menu_bg.jpg")
        menu_bg.position = 630, 360
        self.add(menu_bg)

class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super().__init__("Bauman School")

        items = []

        items.append(cocos.menu.MenuItem("New Game", self.on_new_game))
        items.append(cocos.menu.MenuItem("Load Game", self.on_load_game))
        items.append(cocos.menu.MenuItem("Quit", self.on_quit))

        self.create_menu(items, cocos.menu.shake(), cocos.menu.shake_back())

            
    def on_new_game(self):
        active_scene = Game_Scene()
        director.replace(active_scene)

    def on_load_game(self):
        print("Load Game")

    def on_quit(self):
        director.window.close()

# ===============================END==================================================

# =============================Game-Scene===================================================
class Game_Scene(cocos.scene.Scene):
    def __init__(self):
        super().__init__()
        self.add(scroller)
        print("in game schene")

        

class Player(cocos.layer.ScrollableLayer, cocos.actions.Move):
    is_event_handler = True
    def __init__(self):
        super().__init__()
        print('Player loaded')
        img = pyglet.image.load("Guy.png")
        img_grid = pyglet.image.ImageGrid(img, 4, 3, item_width = 40, item_height= 40)
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:3], 0.1, loop=True)

        player = cocos.sprite.Sprite(anim)
        player.image = anim
        player.position = 630, 360
        player.velocity = (0, 0)


        player.do(Mover())
        player.do(Animation())
        self.add(player)
        def update(t):
            print('hi')

class Animation(cocos.actions.Move):
    def step(self, dt):
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 200
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 200
        print('hi')
        if vel_x > 0:
            print("right")

            
        elif vel_x <0:
            print("left")
            img = pyglet.image.load("Guy.png")
            img_grid = pyglet.image.ImageGrid(img, 4, 3, item_width = 40, item_height= 40)
            anim = pyglet.image.Animation.from_image_sequence(img_grid[0:3], 0.1, loop=True)
            self.target.image(anim)

        elif vel_y > 0:
            print("Up")

        elif vel_y < 0:
            print("down")
           
       
                    

class Mover(cocos.actions.Move):
    def step(self, dt):
        
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 200
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 200

        dx = vel_x * dt
        dy = vel_y * dt

        last = self.target.get_rect()

        new = last.copy()
        new.x += dx
        new.y += dy
        self.target.velocity = (vel_x, vel_y)

        self.target.position = new.center
        scroller.set_focus(*new.center)            

class BackgroundLayer(cocos.layer.ScrollableLayer):
    def __init__(self):
        super().__init__()
        bg = cocos.sprite.Sprite('maxresdefault.jpg')
        bg.position = 630, 360
        self.add(bg)

'''            
class BackgroundLayer():
    def __init__(self):

        bg = cocos.tiles.load("Greenland.tmx")
        self.layer_ground = bg["ground"]
        self.layer_groundtwo = bg["Rivers"]
        self.colliders = bg["colliders"]

'''
# =============================END===================================================

if __name__ == "__main__":

    director.init(width=1260, height=720, caption="University")
    director.window.pop_handlers()

    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)
    
#=========game_scene scroller=====================
    scroller = cocos.layer.ScrollingManager()
    scroller.add(BackgroundLayer())
    scroller.add(Player())
#===============END===============================

    active_scene = Menu_Scene()


    director.run(active_scene)
