import pygame
# initialize pygame
pygame.init()
 
# define width of screen
width = 1000
# define height of screen
height = 600
screen_res = (width, height)
 
pygame.display.set_caption("GFG Bouncing game")
screen = pygame.display.set_mode(screen_res)

pygame.font.init()
font = pygame.font.Font(None, 36)
 
# define colors
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
 
# define ball
ball_obj = pygame.draw.circle(
    surface=screen, color=red, center=[screen.get_width()/2, screen.get_height()/2], radius=40)
# define speed of ball
# speed = [X direction speed, Y direction speed]
speed = [0, 0]

count = 0

playing = True
# game loop
while playing:
    # event loop
    for event in pygame.event.get():
        # check if a user wants to exit the game or not
        if event.type == pygame.QUIT:
            exit()
 
    # fill black color on screen
    screen.fill(black)
 
    # move the ball
    # Let center of the ball is (100,100)  and the speed is (1,1)
    ball_obj = ball_obj.move(speed)
    # Now center of the ball is (101,101)
    # In this way our wall will move
    if pygame.mouse.get_pressed()[0]:
        speed = [0, -1]
    # if ball goes out of screen then change direction of movement
    if ball_obj.top <= 0:
        speed[1] = -speed[1]
    if ball_obj.bottom >= height:
        speed[1] = 0
        playing = False

    # draw ball at new centers that are obtained after moving ball_obj
    pygame.draw.circle(surface=screen, color=red,
                       center=ball_obj.center, radius=40)


    if speed[1] == -1:
        count += 1          

    

    # update screen

    count_text = font.render(f'{count}', True, red)

    screen.blit(count_text, ((screen.get_width() - count_text.get_width())/2,
                (screen.get_height() - count_text.get_height())/2))




        
    pygame.display.flip()
