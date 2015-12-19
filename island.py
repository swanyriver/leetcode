class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        #grid = [ [ True if  x=='1' else False for x in s] for s in grid ]
        neighbors = []
        #for i in range(len(grid)): neighbors.append( [[]] * len(grid[0]))
        #for len(grid): neighbors.append([False] * len(grid[0]))

        islandCount = 0

        for y in range(len(grid)):
            neighbors.append([])
            for x in range(len(grid[0])):
                neighbors[y].append([])
                if grid[y][x] == '1':
                    if x>0 and grid[y][x-1] == '1': 
                        neighbors[y][x].append((y,x-1))
                    if x<len(grid[0])-1 and grid[y][x+1]=='1': 
                        neighbors[y][x].append((y,x+1))
                    if y>0 and grid[y-1][x]=='1':
                        neighbors[y][x].append((y-1,x))
                    if y<len(grid)-1 and grid[y+1][x] == '1':
                        neighbors[y][x].append((y+1,x))

                    #print y, x     
                    #neighbors[y][x].append(1)
                    if not neighbors[y][x]: 
                        islandCount +=1
                        #print "lonley island"
                

        #for row in neighbors: print row
        #return


        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if neighbors[y][x]:
                    #print neighbors
                    #print "---------------------"
                    islandCount+=1
                    while neighbors[y][x]:
                        #print neighbors[y][x]
                        nexty,nextx = neighbors[y][x].pop()
                        if nexty == y and nextx == x: continue
                        neighbors[y][x].extend(neighbors[nexty][nextx])
                        neighbors[nexty][nextx]=[]
                    #print "-----------------------"
                    #print "-----------------------"


        return islandCount

                        





grid = [
"11110",
"11010",
"11000",
"00000"
]

grid = [
"11000",
"11000",
"00100",
"00011"
]

x = Solution()

print x.numIslands(grid)