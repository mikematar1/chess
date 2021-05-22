from backend import Board
import pygame,sys
pygame.init()
squaresize=50
width=height=squaresize*8
screen = pygame.display.set_mode((width,height))
Game = Board()
font=pygame.font.Font(None,50)
def drawgrid():

    for i in range(8):
        if i%2==0:
            n=0
        else:
            n=1
        for j in range(8):
            if n%2==0:
                pygame.draw.rect(screen,(255,255,255),((j*squaresize,i*squaresize),(squaresize,squaresize)))
            else:
                pygame.draw.rect(screen,(255,0,0),((j*squaresize,i*squaresize),(squaresize,squaresize)))
            n+=1
def drawboard():
    b=Game.board
    for i in range(8):
        for j in range(8):
            piece = b[j][i]
            try:
                if piece.team==1:
                    a = font.render(piece.name[0],1,(0,128,0))
                    screen.blit(a,(i*squaresize,j*squaresize))
                else:
                    a = font.render(piece.name[0],1,(0,0,0))
                    screen.blit(a,(i*squaresize,j*squaresize))
            except:
                pass
            
clicked=None
getdest=False
dest=None
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            y,x = event.pos
            if not clicked and Game.board[x//squaresize][y//squaresize]!="":
                clicked=(x//squaresize,y//squaresize)
                getdest=True
                print("YOU HAVE CHOSEN: ",Game.board[x//squaresize][y//squaresize].name)
                print("MOVES: ",Game.board[x//squaresize][y//squaresize].get_moves(Game.board))
            elif getdest:
                dest=(x//squaresize,y//squaresize)
                getdest=False
    if dest:
        Game.move(clicked,dest)
        dest=None
        clicked=None
            

            
    screen.fill("white")
    drawgrid()
    drawboard()
    pygame.display.update()