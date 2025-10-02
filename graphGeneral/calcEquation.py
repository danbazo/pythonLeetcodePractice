def calcEquation(equations, values, queries):
        calcDict={}
        for i in range(len(values)):
            if equations[i][0] in calcDict:
                calcDict[equations[i][0]][equations[i][1]]=values[i]
            else:
                calcDict[equations[i][0]]={equations[i][1]:values[i]}
            
            if equations[i][1] in calcDict:
                calcDict[equations[i][1]][equations[i][0]]=1/values[i]
            else:
                calcDict[equations[i][1]]={equations[i][0]:1/values[i]}
        def helper(query,visited):

            if query[0] in calcDict and query[0] not in visited:
                visited.add(query[0])
                if query[1] in calcDict[query[0]]:
                    return calcDict[query[0]][query[1]]
                else:
                    
                    for divitions in calcDict[query[0]]:
                        possibleVal=helper([divitions,query[1]],visited)
                        if possibleVal!=0: return calcDict[query[0]][divitions]*possibleVal
                    return -1.0
        
            else: return -1.0
        
        queryVals=[]
        for query in queries:
            queryVals.append(helper(query,set()))
        return queryVals
