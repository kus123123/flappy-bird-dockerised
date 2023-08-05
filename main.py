# SETUP PYGAME ZERO
import pgzrun
#SCREEN
WIDTH=800
HEIGHT=600

#SETUP SCORE
score=0

#SETUP BRICK
brick=Actor("brick")
brick.x =90
brick.y=250
def on_mouse_down():
  print("the mouse has been clicked!")
  brick.y=brick.y-50
  

#SETUP WALLS
wall_bottom =Actor("wall-bottom")
wall_top =Actor("wall-top")
gap=200
wall_top.x=300
wall_top.y=0
wall_bottom.x=300
wall_bottom.y=wall_top.height+gap
#BUTTON PRESSES
  
#DRAW STUFF TO SCREEN
def draw():
  screen.fill("green")
  brick.draw()
  wall_top.draw()
  wall_bottom.draw()
  screen.draw.text("Score: "+str(score),color="black",topleft=(10,10))  
  
  
  #EACH CYCLE THROUGH THE LOOP
def update():
  global score

  brick.y=brick.y+1
  wall_top.x=wall_top.x-1
  wall_bottom.x=wall_bottom.x-1

#COLLISIONS
  if brick.y>HEIGHT:
     reset()
  if brick.colliderect(wall_top) or brick.colliderect(wall_bottom):
    reset()
  if wall_top.x<=0:
    reset_walls()  
    score=score+1
#RESET
def reset():
  global score
  print("the game is resetting")
  brick.y=250
  wall_bottom.x=300
  wall_top.x=300
  score = 0
def reset_walls():
  wall_top.x=600
  wall_bottom.x=600


#RUN PYGAME ZERO
pgzrun.go()
