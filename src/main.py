from sprites import *

## initialize pg and create window
pg.init()
pg.mixer.init()  ## For sound (maybe later)
pg.display.set_caption("<Your game>")
clock = pg.time.Clock()     ## For syncing the FPS

player1 = Player(100, 100)

## Game loop
running = True
while running:
    # here is the main game loop for anyone unfamiliar - the order of the game loop is-
    # work out which events have occured in since the last frame eg keyboard presses
    # update the relevant opjects positions and states
    # draw relevant objects onto the screen
    
     
    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pg.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pg.QUIT:
            running = False

    #2 Update
    player1.update()

    #3 Draw/render
    screen.fill(BLACK)
    
    player1.draw()

    ## Done after drawing everything to the screen
    pg.display.flip()       

pg.quit()