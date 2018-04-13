#dream team
#layerz of dreamz
#derim,nick,kysani,jack
#you are a bunny that must defeat your enemys and reach the nightmare level and waake up.

#jumping on platform in level 2

from gamelib import*
#game object
game = Game(1500,900,"layerz of dreams")
#background object
bk = Image("images\\jungle2.jpg",game)
bk.resizeTo(1500,900)


game.setBackground(bk)

#variable for jumping action
jumping = False#Used to check to see if you are jumping
landed = False#Used to check to see if you have landed on the "ground" (platform)
factor = 1#Used for a slowing effect of the jumping
onplatform = False
#characters
bunnyl = Animation("images\\bunnyl.png",4,game,236/4,68/1,frate = 5,use_alpha=False)
bunnyr = Animation("images\\bunnyr.png",4,game,236/4,68/1,frate = 5,use_alpha=False)
mushroom = Animation("images\\mushroom.png",4,game,440/2,439/2,frate = 8)
mushroom2 = Animation("images\\mushroom2.png",4,game,439/2,439/2,frate = 8)
launcher = Image("images\\launcher.png",game)
carrot = Image("images\\carrot.PNG",game)
explosion = Animation("images\\fireworks.png",27,game,1000/5,1138/6,frate = 2)
transition =Image("images\\b.png",game)
transition.resizeTo(game.width,game.height)
arrow = Image("images\\arrowz.png",game)
menu = Image("images\\menu.jpg",game)
menu.resizeTo(game.width,game.height)
title = Image("images\\title.png",game)
title.resizeBy(50)
title.moveTo(750,200)
story = Image("images\\story.png",game)
story.moveTo(game.width/2,600)
play = Image("images\\play.png",game)
instructions = Image("images\\int.png",game)
instructions.moveTo(game.width/2,750)
forest = Image("images\\forest.jpg",game)
forest.resizeTo(1500,900)
arrow.resizeBy(-50)
arrow.moveTo(1300,600)
arrow.visible = False
bk2 = Image("images\\storybk.jpg",game)
bk2.resizeTo(1500,900)
wolf = Animation("images\\moving wolf.png",6,game,1532/2,1164/3,frate = 5)
wolf.resizeBy(-50)
wolf.moveTo(1300,700)
cactus = Animation("images\\cactus.png",63,game,4535/9,3528/7,use_alpha=False)
cactus.moveTo(-200,625)
cactus.setSpeed(3,270)
platform = Image("images\\platforms.png",game)
platform.resizeTo(500,100)
platform.moveTo(700,620)
heart = []
heartcount = 8
for index in range(heartcount):
    heart.append(Image("images\\heart.png",game))
for index in range(heartcount):
    heart[index].resizeBy(-70)
ammo = Image("images\\carrot.PNG",game)
ammo.visible = False
ammo.resizeBy(-82)
heart[0].moveTo(50,50)
heart[1].moveTo(100,50)
heart[2].moveTo(150,50)
heart[3].moveTo(200,50)
heart[4].moveTo(50,100)
heart[5].moveTo(100,100)
heart[6].moveTo(150,100)
heart[7].moveTo(200,100)
explosion.visible = False
bunnyl.visible = False
launcher.visible = False
carrot.resizeBy(-80)
carrot.moveTo(150,800)
carrotcount = 0
bunnyr.resizeBy(125)
bunnyr.moveTo(600,680)
bunnyr.stop()
bunnyl.stop()
bunnyl.resizeBy(125)
bunnyl.moveTo(600,680)
mushroom.resizeBy(-40)
mushroom.moveTo(1630,690)
x = randint(1,10)
mushroom.setSpeed(x,90)
mushroom2.resizeBy(-40)
mushroom2.moveTo(-100,690)
y = randint(1,10)
mushroom2.setSpeed(y,270)
launcher.resizeBy(-87)
launcher.moveTo(550,740)
int1 = Image("images\\1int.png",game)
int2 = Image("images\\2int.png",game)
en = Image("images\\en.png",game)
en.moveTo(game.width/2,200)
en.resizeBy(-10)
thorn = Image("images\\thorn.png",game)
thorn.resizeBy(-70)
thorn2 = Image("images\\thorn.png",game)
thorn2.resizeBy(-70)
thorn3 = Image("images\\thorn.png",game)
thorn3.resizeBy(-70)
collect=Image("images\\collect.png",game)
winner=Image("images\\winner.jpg",game)
winner.resizeTo(game.width,game.height)
win=Image("images\\win.png",game)
win.moveTo(700,200)
bye=Image("images\\none.png",game)
bye.moveTo(700,300)
cac = Image("images\\cac.png",game)
tiger = Animation("images\\tiger1.png",9,game,78,802/9,frate = 5)#tiger
end = Animation("images\\tiger2.png",6,game,76,542/6,frate = 5)#defeated
portal = Image("images\\Portal.png",game)
light = Animation("images\\lightning.png",9,game,513/3,498/3,use_alpha = False,frate = 4)#
light.visible = False
light.rotateBy(300,"left")
end.resizeBy(200)
end.moveTo(1300,700)
tiger.resizeBy(200)
tiger.moveTo(1300,700)
tigerhealth = []
th = 16
for index in range(th):
    tigerhealth.append(Image("images\\heart.png",game))
for index in range(th):
    tigerhealth[index].resizeBy(-70)
tigerhealth[0].moveTo(1450,50)
tigerhealth[1].moveTo(1400,50)
tigerhealth[2].moveTo(1350,50)
tigerhealth[3].moveTo(1300,50)
tigerhealth[4].moveTo(1250,50)
tigerhealth[5].moveTo(1200,50)
tigerhealth[6].moveTo(1150,50)
tigerhealth[7].moveTo(1100,50)
tigerhealth[8].moveTo(1450,100)
tigerhealth[9].moveTo(1400,100)
tigerhealth[10].moveTo(1350,100)
tigerhealth[11].moveTo(1300,100)
tigerhealth[12].moveTo(1250,100)
tigerhealth[13].moveTo(1200,100)
tigerhealth[14].moveTo(1150,100)
tigerhealth[15].moveTo(1100,100)
##############################################
door = Animation("images\\door.jpg",1,game,800,800,use_alpha=False)
door.resizeBy(-70)
door.moveTo(1400,700)
doortxt = Image("images\\doortxt.png",game)

esc = Image("images\\esc.png",game)
esc.moveTo(esc.x,350)

esc2 = Image("images\\esc3.png",game)
esc2.moveTo(game.width/2,200)
#############################################
firework=[]
for index in range(20):
    firework.append(Animation("images\\firework6.png",5,game,128/1,652/5,frate=3,use_alpha=False))
for index in range(20):
    x = randint(0,1500)
    y = randint(0,700)
    firework[index].moveTo(x,y)

firework1=[]
for index in range(20):
    firework1.append(Animation("images\\firework7.png",5,game,128/1,768/5,frate=3,use_alpha=False))
for index in range(20):
    x = randint(0,1500)
    y = randint(0,700)
    firework1[index].moveTo(x,y)

firework2=[]
for index in range(20):
    firework2.append(Animation("images\\firework5.png",5,game,128/1,596/5,frate=2,use_alpha=False))
for index in range(20):
    x = randint(0,1500)
    y = randint(0,700)
    firework2[index].moveTo(x,y)
over=Image("images\\dark background.jpg",game)
over.resizeTo(game.width,game.height)
death=Image("images\\gg2.png",game)
gameover=Animation("images\\lose.png",2,game,137/2,52/1,frate=10,use_alpha=False)
gameover.resizeTo(220,200)
gameover.moveTo(1400,700)
gameover.setSpeed(5,90)


#menu screen
while not game.over:
    game.processInput()
    menu.draw()
    title.draw()
    story.draw()
    play.draw()
    instructions.draw()
    if play.collidedWith(mouse) and mouse.LeftButton:
        game.over = True


    
    game.update(60)

    
game.over = False    
#level one game loop
while not game.over:
    game.processInput()
    bk.draw()
    explosion.draw(False)
    bunnyr.draw()
    bunnyl.draw()
    mushroom.move()
    mushroom2.move()
    launcher.draw()
    carrot.draw()
    arrow.draw()
    for index in range(heartcount):
        heart[index].draw()



    if bunnyr.y< 725 or bunnyl.y< 725:
        landed = False#not landed

    

    
    else:
        landed = True
    
    if keys.Pressed[K_UP] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True
        
    if landed and bunnyr.collidedWith(mushroom) or bunnyr.collidedWith(mushroom):
        mushroom.visible = False
        explosion.moveTo(mushroom.x,mushroom.y)
        mushroom.moveTo(game.width+50,690)
        explosion.visible = True
        heartcount-=1
        x = randint(1,10)
        mushroom.setSpeed(x,90)
        mushroom.visible = True

    if landed and bunnyl.collidedWith(mushroom2) or bunnyl.collidedWith(mushroom2):
        mushroom2.visible = False
        explosion.moveTo(mushroom2.x,mushroom2.y)
        mushroom2.moveTo(-50,690)
        heartcount-=1
        explosion.visible = True
        y = randint(1,10)
        mushroom2.setSpeed(y,270)
        mushroom2.visible = True
        
    if jumping:
        bunnyr.y -=24*factor
        bunnyl.y -=24*factor
        #make the character go up. factor creates a slowing effect 
        factor*=.95
        bunnyr.nextFrame()
        bunnyl.nextFrame()
        launcher.draw()
        carrot.draw()
            
        
    
        landed = False

        if factor < .18:
            jumping = False
            factor = 1

    if not landed:#is jumping

        bunnyr.y +=5
        bunnyl.y +=5
        bunnyr.nextFrame()
        bunnyl.nextFrame()
        carrot.draw()
        launcher.draw()
        if bunnyr.collidedWith(mushroom) or bunnyl.collidedWith(mushroom):
            explosion.moveTo(mushroom.x,mushroom.y)
            explosion.visible = True
            mushroom.visible = False
            mushroom.moveTo(game.width+50,690)
            mushroom.visible = True
            carrotcount+=1
            x = randint(1,10)
            mushroom.setSpeed(x,90)
        
        if bunnyr.collidedWith(mushroom2) or bunnyl.collidedWith(mushroom2):
            explosion.moveTo(mushroom2.x,mushroom2.y)
            explosion.visible = True
            mushroom2.visible = False
            mushroom2.moveTo(-50,690)
            mushroom2.visible = True
            carrotcount+=1
            y = randint(1,10)
            mushroom2.setSpeed(y,270)
        
    if mushroom.isOffScreen("left"):
        x = randint(1,10)
        mushroom.setSpeed(x,90)
        mushroom.moveTo(game.width+100,690)

    if mushroom2.isOffScreen("right"):
        y = randint(1,10)
        mushroom2.setSpeed(y,270)
        mushroom2.moveTo(-100,690)                

    if keys.Pressed[K_RIGHT]:
        bunnyl.x+=3
        bunnyl.visible = False
        bunnyr.visible = True
        bunnyr.x+=3
        bunnyr.nextFrame()
        bunnyr.draw()
        mushroom.draw()
        mushroom2.draw()
        launcher.draw()
        carrot.draw()

        

 
    if keys.Pressed[K_LEFT]:
        bunnyr.x-=3
        bunnyr.visible = False
        bunnyl.visible = True
        bunnyl.x-=3
        bunnyl.nextFrame()
        bunnyl.draw()
        mushroom.draw()
        mushroom2.draw()
        launcher.draw()
        carrot.draw()


    game.drawText("Carrots: " + str(carrotcount),200,800)

    
    if carrotcount > 0:
        launcher.visible = True
        mushroom.visible = False
        mushroom2.visible = False
        arrow.visible = True
        collect.moveTo(700,400)
        collect.draw()
        
    if heartcount <1:
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()


    if carrotcount<4 and heartcount>1:
        int1.draw()


        
    if bunnyr.collidedWith(launcher) or bunnyl.collidedWith(launcher):
        launcher.moveTo(-100,-100)


    if bunnyr.isOffScreen("right") or bunnyl.isOffScreen("right") or bunnyr.isOffScreen("left") or bunnyl.isOffScreen("left"):
        game.over = True
        healthcount = 0
    if bunnyr.isOffScreen("right") or bunnyl.isOffScreen("right") and carrotcount > 24:
        game.over = True        


    game.update(60)

game.over = False


#transition

heartcount = 8
bunnyr.moveTo(100,760)
while not game.over and heartcount>1:
    game.processInput()
    transition.draw()
    bunnyr.draw()
    cac.draw()
    bunnyr.nextFrame()
    bunnyr.x+=3
    carrot.draw()
    cactus.move()
    int2.moveTo(game.width/2,200)
    int2.draw()
    game.drawText("Carrots: " + str(carrotcount),200,800)
    for index in range(heartcount):
        heart[index].draw()
    if cactus.isOffScreen("right"):
        game.over = True
    game.update(60)


game.over = False








#jumping on platforms
#second game loop
game.over = False
x = randint(1,10)
mushroom.setSpeed(x,90)
cactus.moveTo(-400,625)
hit = False
ammo.visible = False
bunnyr.moveTo(100,760)
bunnyl.moveTo(100,760)
mushroom.moveTo(game.width+150,710)
wolfhealth = 3
wolf.setSpeed(3,90)
mushroom.visible =True
while not game.over and heartcount>1:
    game.processInput()
    bk2.draw()
    bunnyr.draw()
    bunnyl.draw()
    carrot.draw()
    explosion.draw(False)
    wolf.move()
    ammo.move()
    cactus.move()
    mushroom.move()
    arrow.draw()
    arrow.visible = True
    game.drawText("Carrots: " + str(carrotcount),200,800)

    launcher.moveTo(bunnyr.x+80,bunnyr.y)
    for index in range(heartcount):
        heart[index].draw()

    if keys.Pressed[K_UP] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True

    if keys.Pressed[K_SPACE] and carrotcount>0:
        ammo.moveTo(bunnyr.x+150,bunnyr.y)
        ammo.setSpeed(50,-90)
        ammo.visible = True
        launcher.visible = True
    else:
        launcher.visible = False
    if keys.Pressed[K_RIGHT]:
        bunnyl.x+=4
        bunnyl.visible = False
        bunnyr.visible = True
        bunnyr.x+=4
        bunnyr.nextFrame()
        bunnyr.draw()
    if keys.Pressed[K_LEFT]:
        bunnyr.x-=4
        bunnyr.visible = False
        bunnyl.visible = True
        bunnyl.x-=4
        bunnyl.nextFrame()
        bunnyl.draw()


                
    if bunnyr.y< 725 or bunnyl.y< 725 and not landed:
        landed = False#not landed
    else:
        landed = True
    
    if jumping:
        bunnyr.y -=24*factor
        bunnyl.y -=24*factor
        #make the character go up. factor creates a slowing effect 
        factor*=.95


    
        landed = False

        if factor < .18:
            jumping = False
            factor = 1

    if not landed:#is jumping

        bunnyr.y +=5
        bunnyl.y +=5
        bunnyr.nextFrame()
        bunnyl.nextFrame()
        carrot.draw()

    if ammo.collidedWith(mushroom):
        explosion.moveTo(mushroom.x,mushroom.y)
        explosion.visible = True
        mushroom.visible = False
        ammo.visible = False
        mushroom.moveTo(game.width+150,710)
        mushroom.visible = True
        x = randint(1,10)
        mushroom.setSpeed(x,90)

    if landed and bunnyr.collidedWith(mushroom) or bunnyr.collidedWith(mushroom):
        mushroom.visible = False
        explosion.moveTo(mushroom.x,mushroom.y)
        mushroom.moveTo(game.width+150,710)
        explosion.visible = True
        heartcount-=1
        x = randint(1,10)
        mushroom.setSpeed(x,90)
        mushroom.visible = True

    if wolf.collidedWith(bunnyr) or wolf.collidedWith(bunnyl):
        wolf.moveTo(game.width+300,690)
        heartcount-=2
    if keys.Pressed[K_SPACE] and carrotcount>0:
        ammo.moveTo(bunnyr.x+150,bunnyr.y)
        ammo.setSpeed(50,-90)
        ammo.visible = True
        launcher.visible = True
    else:
        launcher.visible = False

    if ammo.collidedWith(wolf):
        wolfhealth-=1
        ammo.visible = False
        hit = True
        explosion.moveTo(wolf.x,wolf.y)
        wolf.moveTo(game.width+300,690)
    if hit:
        carrotcount-=1
        hit = False
    if wolfhealth<1:
        explosion.visible = True
        wolfhealth = 3

    if bunnyr.isOffScreen("right") or bunnyl.isOffScreen("right"):
        mushroom.moveTo(game.width+500,690)
        wolf.moveTo(game.width+500,690)
        game.over = True

    if heartcount <1:
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)

    if bunnyr.collidedWith(cactus):
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()

    if mushroom.isOffScreen("left"):
        x = randint(1,10)
        mushroom.setSpeed(x,90)
        mushroom.moveTo(game.width+100,690)
        
    if bunnyl.collidedWith(cactus):
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()

    if keys.Pressed[K_RIGHT] and bunnyr.collidedWith(cactus) or bunnyl.collidedWith(cactus):
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()
            
    if keys.Pressed[K_LEFT] and bunnyr.collidedWith(cactus) or bunnyl.collidedWith(cactus):
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()




    game.update(60)


#lvel2 pt2
x = randint(1,10)
mushroom.setSpeed(x,90)
wolf.moveTo(game.width+300,690)
thorn.moveTo(700,725)
game.over = False
cactus.moveTo(-400,625)
hit = False
ammo.visible = False
bunnyr.moveTo(100,760)
bunnyl.moveTo(100,760)
mushroom.moveTo(game.width+150,710)
wolfhealth = 3
wolf.setSpeed(3,90)
while not game.over and heartcount>1:
    game.processInput()
    bk2.draw()
    bunnyr.draw()
    bunnyl.draw()
    carrot.draw()
    explosion.draw(False)
    wolf.move()
    ammo.move()
    cactus.move()
    mushroom.move()
    arrow.draw()
    arrow.visible = True
    thorn.draw()
    game.drawText("Carrots: " + str(carrotcount),200,800)

    launcher.moveTo(bunnyr.x+80,bunnyr.y)
    for index in range(heartcount):
        heart[index].draw()

    if keys.Pressed[K_UP] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True

    if keys.Pressed[K_SPACE] and carrotcount>0:
        ammo.moveTo(bunnyr.x+150,bunnyr.y)
        ammo.setSpeed(50,-90)
        ammo.visible = True
        launcher.visible = True
    else:
        launcher.visible = False
    if keys.Pressed[K_RIGHT]:
        bunnyl.x+=4
        bunnyl.visible = False
        bunnyr.visible = True
        bunnyr.x+=4
        bunnyr.nextFrame()
        bunnyr.draw()
    if keys.Pressed[K_LEFT]:
        bunnyr.x-=4
        bunnyr.visible = False
        bunnyl.visible = True
        bunnyl.x-=4
        bunnyl.nextFrame()
        bunnyl.draw()

    if bunnyr.collidedWith(thorn) or bunnyl.collidedWith(thorn):
        if keys.Pressed[K_RIGHT]:
            bunnyl.x-=3
            bunnyl.visible = False
            bunnyr.visible = True
            bunnyr.x-=3
            bunnyr.nextFrame()
            bunnyr.draw()
        if keys.Pressed[K_LEFT]:
            bunnyr.x+=3
            bunnyr.visible = False
            bunnyl.visible = True
            bunnyl.x+=3
            bunnyl.nextFrame()
            bunnyl.draw()

    if bunnyr.y< 725 or bunnyl.y< 725 and not landed:
        landed = False#not landed
    else:
        landed = True
    
    if jumping:
        bunnyr.y -=24*factor
        bunnyl.y -=24*factor
        #make the character go up. factor creates a slowing effect 
        factor*=.95


    
        landed = False

        if factor < .18:
            jumping = False
            factor = 1

    if not landed:#is jumping

        bunnyr.y +=5
        bunnyl.y +=5
        bunnyr.nextFrame()
        bunnyl.nextFrame()
        carrot.draw()

    if ammo.collidedWith(mushroom):
        explosion.moveTo(mushroom.x,mushroom.y)
        explosion.visible = True
        mushroom.visible = False
        ammo.visible = False
        mushroom.moveTo(game.width+150,710)
        mushroom.visible = True
        x = randint(1,10)
        mushroom.setSpeed(x,90)

    if landed and bunnyr.collidedWith(mushroom) or bunnyr.collidedWith(mushroom):
        mushroom.visible = False
        explosion.moveTo(mushroom.x,mushroom.y)
        mushroom.moveTo(game.width+150,710)
        explosion.visible = True
        heartcount-=1
        x = randint(1,10)
        mushroom.setSpeed(x,90)
        mushroom.visible = True

    if wolf.collidedWith(bunnyr) or wolf.collidedWith(bunnyl):
        wolf.moveTo(game.width+300,690)
        heartcount-=2
    if keys.Pressed[K_SPACE] and carrotcount>0:
        ammo.moveTo(bunnyr.x+150,bunnyr.y)
        ammo.setSpeed(50,-90)
        ammo.visible = True
        launcher.visible = True
    else:
        launcher.visible = False
    if mushroom.isOffScreen("left"):
        x = randint(1,10)
        mushroom.setSpeed(x,90)
        mushroom.moveTo(game.width+100,690)

    if wolf.isOffScreen("left"):
        wolf.moveTo(game.width+300,690)
    if ammo.collidedWith(wolf):
        wolfhealth-=1
        ammo.visible = False
        hit = True
        explosion.moveTo(wolf.x,wolf.y)
        wolf.moveTo(game.width+300,690)
    if hit:
        carrotcount-=1
        hit = False
    if wolfhealth<1:
        explosion.visible = True
        wolfhealth = 3

    if bunnyr.isOffScreen("right") or bunnyl.isOffScreen("right"):
        mushroom.moveTo(game.width+500,690)
        wolf.moveTo(game.width+500,690)
        game.over = True 
 
    if heartcount <1:
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)

    if bunnyr.collidedWith(cactus):
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()
            
    if bunnyl.collidedWith(cactus):
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()

    if keys.Pressed[K_RIGHT] and bunnyr.collidedWith(cactus) or bunnyl.collidedWith(cactus):
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()
            
    if keys.Pressed[K_LEFT] and bunnyr.collidedWith(cactus) or bunnyl.collidedWith(cactus):
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()




    game.update(60)

#lvel2 pt3
x = randint(1,10)
mushroom.setSpeed(x,90)
wolf.moveTo(game.width+300,690)
thorn.moveTo(600,725)
thorn2.moveTo(400,725)
thorn3.moveTo(850,725)
game.over = False
cactus.moveTo(-400,625)
arrow.rotateBy(30)
arrow.moveTo(1200,600)
hit = False
ammo.visible = False
bunnyr.moveTo(100,760)
bunnyl.moveTo(100,760)
mushroom.moveTo(game.width+150,710)
wolfhealth = 3
wolf.setSpeed(3,90)
while not game.over and heartcount>1:
    game.processInput()
    bk2.draw()
    door.draw()
    arrow.draw()
    bunnyr.draw()
    bunnyl.draw()
    carrot.draw()
    explosion.draw(False)
    wolf.move()
    ammo.move()
    cactus.move()
    mushroom.move()
    arrow.visible = True
    thorn.draw()
    thorn2.draw()
    thorn3.draw()
    doortxt.draw()
    game.drawText("Carrots: " + str(carrotcount),200,800)

    launcher.moveTo(bunnyr.x+80,bunnyr.y)
    for index in range(heartcount):
        heart[index].draw()

    if keys.Pressed[K_UP] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True

    if keys.Pressed[K_SPACE] and carrotcount>0:
        ammo.moveTo(bunnyr.x+150,bunnyr.y)
        ammo.setSpeed(50,-90)
        ammo.visible = True
        launcher.visible = True
    else:
        launcher.visible = False
    if keys.Pressed[K_RIGHT]:
        bunnyl.x+=4
        bunnyl.visible = False
        bunnyr.visible = True
        bunnyr.x+=4
        bunnyr.nextFrame()
        bunnyr.draw()
    if keys.Pressed[K_LEFT]:
        bunnyr.x-=4
        bunnyr.visible = False
        bunnyl.visible = True
        bunnyl.x-=4
        bunnyl.nextFrame()
        bunnyl.draw()
    if mushroom.isOffScreen("left"):
        x = randint(1,10)
        mushroom.setSpeed(x,90)
        mushroom.moveTo(game.width+100,690)
    if bunnyr.collidedWith(thorn) or bunnyl.collidedWith(thorn):
        if keys.Pressed[K_RIGHT]:
            bunnyl.x-=3
            bunnyl.visible = False
            bunnyr.visible = True
            bunnyr.x-=3
            bunnyr.nextFrame()
            bunnyr.draw()
        if keys.Pressed[K_LEFT]:
            bunnyr.x+=3
            bunnyr.visible = False
            bunnyl.visible = True
            bunnyl.x+=3
            bunnyl.nextFrame()
            bunnyl.draw()
    if bunnyr.collidedWith(thorn3) or bunnyl.collidedWith(thorn3):
        if keys.Pressed[K_RIGHT]:
            bunnyl.x-=3
            bunnyl.visible = False
            bunnyr.visible = True
            bunnyr.x-=3
            bunnyr.nextFrame()
            bunnyr.draw()
        if keys.Pressed[K_LEFT]:
            bunnyr.x+=3
            bunnyr.visible = False
            bunnyl.visible = True
            bunnyl.x+=3
            bunnyl.nextFrame()
            bunnyl.draw()
    if bunnyr.collidedWith(thorn2) or bunnyl.collidedWith(thorn2):
        if keys.Pressed[K_RIGHT]:
            bunnyl.x-=2
            bunnyl.visible = False
            bunnyr.visible = True
            bunnyr.x-=2
            bunnyr.nextFrame()
            bunnyr.draw()
        if keys.Pressed[K_LEFT]:
            bunnyr.x+=2
            bunnyr.visible = False
            bunnyl.visible = True
            bunnyl.x+=2
            bunnyl.nextFrame()
            bunnyl.draw()
    if bunnyr.y< 725 or bunnyl.y< 725 and not landed:
        landed = False#not landed
    else:
        landed = True
    
    if jumping:
        bunnyr.y -=24*factor
        bunnyl.y -=24*factor
        #make the character go up. factor creates a slowing effect 
        factor*=.95


    
        landed = False

        if factor < .18:
            jumping = False
            factor = 1

    if not landed:#is jumping

        bunnyr.y +=5
        bunnyl.y +=5
        bunnyr.nextFrame()
        bunnyl.nextFrame()
        carrot.draw()

    if ammo.collidedWith(mushroom):
        explosion.moveTo(mushroom.x,mushroom.y)
        explosion.visible = True
        mushroom.visible = False
        ammo.visible = False
        mushroom.moveTo(game.width+150,710)
        mushroom.visible = True
        x = randint(1,10)
        mushroom.setSpeed(x,90)

    if landed and bunnyr.collidedWith(mushroom) or bunnyr.collidedWith(mushroom):
        mushroom.visible = False
        explosion.moveTo(mushroom.x,mushroom.y)
        mushroom.moveTo(game.width+150,710)
        explosion.visible = True
        heartcount-=1
        x = randint(1,10)
        mushroom.setSpeed(x,90)
        mushroom.visible = True

    if wolf.collidedWith(bunnyr) or wolf.collidedWith(bunnyl):
        wolf.moveTo(game.width+300,690)
        heartcount-=2
    if keys.Pressed[K_SPACE] and carrotcount>0:
        ammo.moveTo(bunnyr.x+150,bunnyr.y)
        ammo.setSpeed(50,-90)
        ammo.visible = True
        launcher.visible = True
    else:
        launcher.visible = False

    if ammo.collidedWith(wolf):#
        wolfhealth-=1
        ammo.visible = False
        hit = True
        explosion.moveTo(wolf.x,wolf.y)
        wolf.moveTo(game.width+300,690)
    if hit:
        carrotcount-=1
        hit = False
    if wolfhealth<1:
        explosion.visible = True
        wolfhealth = 3

    if bunnyr.isOffScreen("right") or bunnyl.isOffScreen("right"):
        game.over = True

    if heartcount <1:
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)

    if bunnyr.collidedWith(cactus):
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()
            
    if bunnyl.collidedWith(cactus):
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()
            
    if bunnyr.collidedWith(door) or bunnyl.collidedWith(door):
        game.over = True
        heartcount = 8
        
    if keys.Pressed[K_RIGHT] and bunnyr.collidedWith(cactus) or bunnyl.collidedWith(cactus):
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()
            
    if keys.Pressed[K_LEFT] and bunnyr.collidedWith(cactus) or bunnyl.collidedWith(cactus):
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        bunnyr.moveTo(-100000000,-10000000)
        bunnyl.moveTo(-100000000,-10000000)
        cactus.moveTo(bunnyr.x,bunnyr.y)
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()




    game.update(60)


#third game loop
x = randint(1,10)
mushroom.setSpeed(x,90)
portal.moveTo(-500,-500)
game.over = False
bunnyr.moveTo(600,680)
bunnyl.moveTo(600,680)
wolfhealth = 3
wolf.moveTo(game.width+300,690)
mushroom.moveTo(game.width+50,690)
while not game.over and heartcount>1:
#bunny movements
#mushrooms
    
    game.processInput()
    forest.draw()
    explosion.draw(False)
    bunnyr.draw()
    bunnyl.draw()
    mushroom.move()
    wolf.move()
    carrot.draw()
    tiger.draw()
    ammo.move()
    launcher.draw()
    launcher.moveTo(bunnyr.x+80,bunnyr.y)
    light.draw(False)
    light.move()

    if keys.Pressed[K_RIGHT]:
        bunnyl.x+=4
        bunnyl.visible = False
        bunnyr.visible = True
        bunnyr.x+=4
        bunnyr.nextFrame()
        bunnyr.draw()
    if keys.Pressed[K_LEFT]:
        bunnyr.x-=4
        bunnyr.visible = False
        bunnyl.visible = True
        bunnyl.x-=4
        bunnyl.nextFrame()
        bunnyl.draw()

    for index in range(heartcount):
        heart[index].draw()

    for index in range(th):
        tigerhealth[index].draw()
        

    if bunnyr.y< 725 or bunnyl.y< 725:
        landed = False#not landed

    

    
    else:
        landed = True

    if wolf.isOffScreen("left"):
        wolf.moveTo(game.width+300,690)    
    if keys.Pressed[K_UP] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True
    if wolf.collidedWith(bunnyr) or wolf.collidedWith(bunnyl):
        wolf.moveTo(game.width+300,690)
        heartcount-=2   
    if landed and bunnyr.collidedWith(mushroom) or bunnyr.collidedWith(mushroom):
        mushroom.visible = False
        explosion.moveTo(mushroom.x,mushroom.y)
        mushroom.moveTo(game.width+50,690)
        explosion.visible = True
        heartcount-=1
        x = randint(1,10)
        mushroom.setSpeed(x,90)
        mushroom.visible = True


        
    if jumping:
        bunnyr.y -=24*factor
        bunnyl.y -=24*factor
        #make the character go up. factor creates a slowing effect 
        factor*=.95
        bunnyr.nextFrame()
        bunnyl.nextFrame()
        launcher.draw()
        carrot.draw()
            
        
    
        landed = False

        if factor < .18:
            jumping = False
            factor = 1

    if not landed:#is jumping

        bunnyr.y +=5
        bunnyl.y +=5
        bunnyr.nextFrame()
        bunnyl.nextFrame()
        carrot.draw()
        launcher.draw()
        if bunnyr.collidedWith(mushroom) or bunnyl.collidedWith(mushroom):
            explosion.moveTo(mushroom.x,mushroom.y)
            explosion.visible = True
            mushroom.visible = False
            mushroom.moveTo(game.width+50,690)
            mushroom.visible = True
            carrotcount+=1
            x = randint(1,10)
            mushroom.setSpeed(x,90)

    if keys.Pressed[K_SPACE] and carrotcount>0:
        ammo.moveTo(bunnyr.x+150,bunnyr.y)
        ammo.setSpeed(50,-90)
        ammo.visible = True
        launcher.visible = True
    else:
        launcher.visible = False
        

    if bunnyr.collidedWith(light) or bunnyl.collidedWith(light):
        light.visible = False
        heartcount -= 2

    if bunnyr.collidedWith(tiger) or bunnyl.collidedWith(tiger):
        heartcount -=8

    if ammo.collidedWith(light) or ammo.collidedWith(light):
        ammo.visible = False
        light.visible = False
        carrotcount-=1
        light.moveTo(tiger.x-75,tiger.y)

    if ammo.collidedWith(mushroom) or ammo.collidedWith(mushroom):
        ammo.visible = False
        explosion.moveTo(mushroom.x,mushroom.y)
        explosion.visible = True
        mushroom.moveTo(game.width+100,mushroom.y)
        x = randint(1,10)
        mushroom.setSpeed(x,90)

    if ammo.collidedWith(wolf):#
        wolfhealth-=1
        ammo.visible = False
        hit = True
        explosion.moveTo(wolf.x,wolf.y)
        wolf.moveTo(game.width+300,690)
    if hit:
        carrotcount-=1
        hit = False
    if wolfhealth<1:
        explosion.visible = True
        wolfhealth = 3
        
    if ammo.collidedWith(tiger) or ammo.collidedWith(tiger):
        ammo.visible = False
        carrotcount-=1
        th-=1
        light.visible = True
        light.moveTo(tiger.x-75,tiger.y)
        light.setSpeed(60,-270)

    if th<1:
        mushroom.visible = False
        portal.moveTo(game.width/2, 500)
        portal.draw()
        portal.rotateTo(50)
        tiger.visible = False
        end.draw()
        esc.draw()

    if th<1 and ammo.collidedWith(tiger):
        explosion.resizeBy(70)
        explosion.visible= True
    if mushroom.isOffScreen("left"):
        x = randint(1,10)
        mushroom.setSpeed(x,90)
        mushroom.moveTo(game.width+100,690)
    if heartcount <1:
        over.draw()
        death.draw()
        gameover.move()
        esc2.draw()
        if gameover.isOffScreen("left"):
            gameover.moveTo(1600,700)
        if keys.Pressed[K_ESCAPE]:
            game.quit()

    if bunnyr.collidedWith(portal) or bunnyl.collidedWith(portal):
        game.over = True

    game.drawText("Carrots: " + str(carrotcount),200,800)
    game.update(60)









        
#winning screen
game.over = False
while not game.over and heartcount>1:
    game.processInput()
    winner.draw()
    win.draw()
    bye.draw()
    en.moveTo(game.width/2,400)
    en.draw()
    for index in range(20):
        firework[index].draw()
    for index in range(20):
        firework1[index].draw()
    for index in range(20):
        firework2[index].draw()
    if keys.Pressed[K_ESCAPE]:
            game.quit()


    
    


    game.update(30)



game.quit()

