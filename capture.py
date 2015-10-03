def edges(board):
    for x in range(len(board[0])):
        yield x,0
        yield x,len(board)-1
    for y in range(1,len(board)):
        yield 0,y 
        yield len(board[0])-1,y


def liberate(x,y,board, freeOs):

    toliberate = [(x,y)]

    while toliberate:
        nextO = toliberate.pop()
        freeOs.add(nextO)

        x,y = nextO
        #up neighbor
        if y<len(board)-1 and board[y+1][x] is 'O' and (x,y+1) not in freeOs: toliberate.append((x,y+1))
        #down neighbor
        if y>0 and board[y-1][x] is 'O' and (x,y-1) not in freeOs: toliberate.append((x,y-1))
        #left neighbor
        if x<len(board[0])-1 and board[y][x+1] is 'O' and (x+1,y) not in freeOs: toliberate.append((x+1,y))
        #right neighbor
        if x>0 and board[y][x-1] is 'O' and (x-1,y) not in freeOs: toliberate.append((x-1,y))


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        freeOs = set()

        for x,y in edges(board):
            print x,y
            if board[y][x] is 'O' and (x,y) not in freeOs:
                 liberate(x,y,board, freeOs)

        print freeOs

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] is 'O' and (x,y) not in freeOs:
                    board[y][x] = 'X'




board = ["XXX","XOX","XXX"]
board = [list(x) for x in board]
print board
print "-------------"
x = Solution()
x.solve(board)
print board
