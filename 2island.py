class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        grid = [ [True if c =='1' else False for c in s] for s in grid ]

        islandCount = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    
                    islandCount +=1

                    s = [(y,x)]
                    grid[y][x] = False

                    while s:
                        #print s
                        nexty,nextx = s.pop()

                        if nextx<len(grid[0])-1 and grid[nexty][nextx+1]: 
                            grid[nexty][nextx+1] = False
                            s.append((nexty,nextx+1))
                        if nexty<len(grid)-1 and grid[nexty+1][nextx]:
                            grid[nexty+1][nextx] = False
                            s.append((nexty+1,nextx))

                        if nextx>0 and grid[nexty][nextx-1]: 
                            grid[nexty][nextx-1] = False
                            s.append((nexty,nextx-1))
                        if nexty>0 and grid[nexty-1][nextx]:
                            grid[nexty-1][nextx] = False
                            s.append((nexty-1,nextx))
                    #print "-------------------------------"

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

grid = ["111","010","111"]

x = Solution()

print x.numIslands(grid)