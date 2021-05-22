class Player:
    def __init__(self,team):
        self.pieces=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        
        self.team=team
        self.initall()
    class Pawn:
        
        def __init__(self,pos,team):
            self.pos = pos
            self.originalpos = pos
            self.name="Pawn"
            self.team=team
            
        def get_moves(self,grid):
            a,b=self.pos
            avmoves=[]
            if self.team==1:
                if a+1<len(grid) and grid[a+1][b]=="":
                    avmoves.append((a+1,b))
                if self.pos==self.originalpos and grid[a+2][b]=="":
                    avmoves.append((a+2,b))
                if a+1<len(grid) and b+1<len(grid[0]) and grid[a+1][b+1]!="" and grid[a+1][b+1].team!=self.team:
                    avmoves.append((a+1,b+1))
                if a+1<len(grid) and b-1<len(grid[0]) and grid[a+1][b-1]!="" and grid[a+1][b-1].team!=self.team:
                    avmoves.append((a+1,b-1))
            else:
                if a-1>=0 and grid[a-1][b]=="":
                    avmoves.append((a-1,b))
                if self.pos==self.originalpos and grid[a-2][b]=="":
                    avmoves.append((a-2,b))
                if a-1>=0 and b+1<len(grid[0]) and grid[a-1][b+1]!="" and grid[a-1][b+1].team!=self.team:
                    avmoves.append((a+1,b+1))
                if a-1>=0 and b-1>=0 and grid[a-1][b-1]!="" and grid[a-1][b-1].team!=self.team:
                    avmoves.append((a+1,b-1))

            return avmoves

            
    class Rook:
        def __init__(self,pos,team):
            self.pos=pos
            self.name="Rook"
            self.team=team
        def get_moves(self,grid):
            a,b=self.pos
            avmoves=[]
            while a-1 >=0 and (grid[a-1][b]=="" or grid[a-1][b].team!=self.team):
                avmoves.append((a-1,b))
                a,b=a-1,b
            a,b=self.pos
            while a+1<len(grid) and (grid[a+1][b]=="" or grid[a+1][b].team!=self.team):
                avmoves.append((a+1,b))
                a,b=a+1,b
            a,b=self.pos
            while b-1>=0 and (grid[a][b-1]=="" or grid[a][b-1].team!=self.team):
                avmoves.append((a,b-1))
                a,b=a,b-1
            a,b=self.pos
            while b+1<len(grid[0]) and (grid[a][b+1]=="" or grid[a][b+1].team!=self.team):
                avmoves.append((a,b+1))
                a,b=a,b+1
            a,b=self.pos
            return avmoves
    class Knight:
        def __init__(self,pos,team):
            self.pos=pos
            self.name="Knight"
            self.team=team
        def get_moves(self,grid):
            y,x = self.pos
            avmoves=[]
            for a,b in [(y+2,x+1),(y+2,x-1),(y+1,x+2),(y+1,x-2),(y-2,x+1),(y-2,x-1),(y-1,x+2),(y-1,x-2)]:
                if a>0 and b>0 and a<len(grid) and b<len(grid[0]):
                    if grid[a][b]=="":
                        avmoves.append((a,b))
                    elif grid[a][b].team!=self.team:
                        avmoves.append((a,b))
            return avmoves
    class Bishop:
        def __init__(self,pos,team):
            self.pos = pos
            self.name="Bishop"
            self.team=team
        def get_moves(self,grid):
            a,b = self.pos
            avmoves=[]
            while a-1 >=0 and b-1>=0 and (grid[a-1][b-1]=="" or grid[a-1][b-1].team!=self.team):
                avmoves.append((a-1,b-1))
                if grid[a-1][b-1]!="":
                    break
                a,b  = a-1,b-1
            a,b=self.pos
            while a+1<len(grid) and b+1<len(grid[0]) and (grid[a+1][b+1]=="" or grid[a+1][b+1].team!=self.team):
                avmoves.append((a+1,b+1))
                if grid[a+1][b+1]!="":
                    break
                a,b=a+1,b+1
            a,b=self.pos
            while b-1>=0 and a+1<len(grid) and (grid[a+1][b-1]=="" or grid[a+1][b-1].team!=self.team):
                avmoves.append((a+1,b-1))
                if grid[a+1][b-1]!="":
                    break
                a,b=a+1,b-1
            a,b=self.pos
            while b+1<len(grid[0]) and a-1>=0 and (grid[a-1][b+1]=="" or grid[a-1][b+1].team!=self.team):
                avmoves.append((a-1,b+1))
                if grid[a-1][b+1]!="":
                    break
                a,b=a-1,b+1
            a,b=self.pos
            return avmoves
    class King:
        def __init__(self,pos,team):
            self.pos=pos
            self.name="King"
            self.team=team
        def get_moves(self,grid):
            y,x = self.pos
            avmoves=[]
            for a,b in [(y-1,x-1),(y,x-1),(y+1,x-1),(y-1,x+1),(y,x+1),(y+1,x+1),(y-1,x),(y+1,x)]:
                if a>0 and b>0 and a<len(grid) and b<len(grid[0]):
                    if grid[a][b]=="" or grid[a][b].team!=self.team:
                        avmoves.append((a,b))
            return avmoves

    class Queen:
        def __init__(self,pos,team):
            self.pos=pos
            self.name="Queen"
            self.team=team
        def get_moves(self,grid):
            a,b=self.pos
            avmoves=[]
            while a-1 >=0 and b-1>=0 and (grid[a-1][b-1]=="" or grid[a-1][b-1].team!=self.team):
                avmoves.append((a-1,b-1))
                a,b  = a-1,b-1
            a,b=self.pos
            while a+1<len(grid) and b+1<len(grid[0]) and (grid[a+1][b+1]=="" or grid[a+1][b+1].team!=self.team):
                avmoves.append((a+1,b+1))
                a,b=a+1,b+1
            a,b=self.pos
            while b-1>=0 and a+1<len(grid) and (grid[a+1][b-1]=="" or grid[a+1][b-1].team!=self.team):
                avmoves.append((a+1,b-1))
                a,b=a+1,b-1
            a,b=self.pos
            while b+1<len(grid[0]) and a-1>=0 and (grid[a-1][b+1]=="" or grid[a-1][b+1].team!=self.team):
                avmoves.append((a-1,b+1))
                a,b=a-1,b+1
            a,b=self.pos
            while a-1 >=0 and (grid[a-1][b]=="" or grid[a-1][b].team!=self.team):
                avmoves.append((a-1,b))
                a,b=a-1,b
            a,b=self.pos
            while a+1<len(grid) and (grid[a+1][b]=="" or grid[a+1][b].team!=self.team):
                avmoves.append((a+1,b))
                a,b=a+1,b
            a,b=self.pos
            while b-1>=0 and (grid[a][b-1]=="" or grid[a][b-1].team!=self.team):
                avmoves.append((a,b-1))
                a,b=a,b-1
            a,b=self.pos
            while b+1<len(grid[0]) and (grid[a][b+1]=="" or grid[a][b+1].team!=self.team):
                avmoves.append((a,b+1))
                a,b=a,b+1
            a,b=self.pos
            return avmoves

    def addpawns(self):
        a=1 if self.team==1 else 0
        h = 1 if self.team==1 else 6
        for i in range(8):
            p = self.Pawn(pos=(h,i),team=self.team)
            self.pieces[a][i]=p
    def addrooks(self):
        a=0 if self.team==1 else 1
        p = 0 if self.team==1 else 7
        for x in [0,7]:
            r = self.Rook(pos=(p,x),team=self.team)
            self.pieces[a][x]=r
    def addKnights(self):
        a=0 if self.team==1 else 1
        p = 0 if self.team==1 else 7
        for x in [1,6]:
            k=self.Knight(pos=(p,x),team=self.team)
            
            self.pieces[a][x]=k
    def addBishops(self):
        a=0 if self.team==1 else 1
        p = 0 if self.team==1 else 7
        for x in [2,5]:
            b=self.Bishop(pos=(p,x),team=self.team)

            self.pieces[a][x]=b
            
    
    def addKing(self):
        
        if self.team==1:
            k = self.King(pos=(0,4),team=self.team)
            self.pieces[0][4]=k
        else:
            k = self.King(pos=(7,4),team=self.team)
            self.pieces[-1][4]=k
    def addQueen(self):
        
        if self.team==1:
            q = self.Queen(pos=(0,3),team=self.team)
            self.pieces[0][3]=q
        else:
            q = self.Queen(pos=(7,3),team=self.team)
            self.pieces[-1][3]=q
    def initall(self):
        self.addpawns()
        self.addrooks()
        self.addKnights()
        self.addBishops()
        self.addKing()
        self.addQueen()

class Board:
    def __init__(self):
        self.board=[]
        player1 = Player(1)
        player2=Player(2)
        self.board+=player1.pieces
        for i in range(4):
            temp=[]
            for j in range(8):
                temp.append("")
            self.board.append(temp)
        self.board+=player2.pieces
    def move(self,piecepos,destinationpos):
        a,b=piecepos
        piece = self.board[a][b]
        print(piece.get_moves(self.board))
        if destinationpos in piece.get_moves(self.board):
            
            y,x=destinationpos
            if self.board[y][x]!="":
                pass
            self.board[y][x]=piece
            self.board[a][b]=""
            piece.pos = (y,x)



