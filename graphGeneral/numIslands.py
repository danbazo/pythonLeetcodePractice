def numIslands(grid):
        observed=set()
        islandCount=0
        m=len(grid)
        n=len(grid[0])
        directions=[(-1,0),(0,-1),(1,0),(0,1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='0' or (i,j) in observed: continue
                
                
                checking=[(i,j)]
                

                while checking:

                    iTemp,jTemp=checking.pop()
                    observed.add((iTemp,jTemp))
                    for direction in directions:
                        iTempTemp=iTemp+direction[0]
                        jTempTemp=jTemp+direction[1]
                        if 0<=iTempTemp<m and 0<=jTempTemp<n and (iTempTemp,jTempTemp) not in observed and grid[iTempTemp][jTempTemp]=="1":
                            checking.append((iTempTemp,jTempTemp))


                islandCount+=1

        return islandCount
