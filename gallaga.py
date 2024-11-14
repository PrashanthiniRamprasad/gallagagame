import pgzrun,random
WIDTH=1200
HEIGHT=600

ship=Actor("ship")
bug=Actor("bug")
ship.pos=(WIDTH/2,HEIGHT-50)
speed = 5

#define a list for bullets
bullets = []

#defining a list of enemies
enemies = []

#we want 8 enemies
for x in range(8):
    for y in range(4):
        enemies.append(Actor('bug'))
        #now the enemies will be ina straight line
        enemies[-1].x = 100+ 50*x
        #starting off the screen thats why putting it at -100,
        #slowly the enemy will come down
        enemies[-1].y = 80 + 50*y

score = 0
direction = 1
ship.dead = False
ship.countdown = 90

#for updating the score
def displayScore():
    screen.draw.text(str(score), (50,30))

def gameover():
    screen.draw.text("game over",(300,300))

def on_key_down(key):
    if ship.dead==False:
        bullets.append(Actor("bullet"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-50

def update():
    global score
    global direction
    move_down=False
    #move the ship left or right
    if ship.dead==False:
        if keyboard.left:
            ship.x-=speed
            if ship.x<=0:
                ship.x=0
        elif keyboard.right:
            ship.x+=speed
            if ship.x>=WIDTH:
                ship.x=WIDTH        
    for bullet in bullets:
        if bullet.y<=0:
            bullets.remove(bullet)
        else:
            bullet.y-=10
    if len(enemies)==0:
        gameover()            
    if len(enemies)>0 and (enemies[-1].x>WIDTH-80 or enemies[0].x>80):
        move_down=True
        direction = direction*-1
    for enemy in enemies:
        enemy.x += 5*direction
        if move_down == True:
            enemy.y += 100
        if enemy.y > HEIGHT :
            enemies.remove(enemy)

        #checking if the enemy hits a bullet while moving down
        #iterate over all the bullets and check for a collision
        for bullet in bullets :
            if enemy.colliderect(bullet):
                score +=100
                #we also want to destory the bullet
                bullets.remove(bullet)
                #instead of removing the enemy we could send it back up?
                enemies.remove(enemy)
                if len(enemies) == 0:
                    gameover()
        #checking for enemy hits the ship
        if enemy.colliderect(ship):
            ship.dead = True
    if ship.dead:
        ship.countdown -=1
    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90
def draw():
    screen.clear()
    screen.fill("black")
    #ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    #ship to be drawn last
    if ship.dead == False:
        ship.draw()
    displayScore()
    if len(enemies) == 0:
        gameover() 
pgzrun.go()               
