def canFinish(numCourses, prerequisites):
        prerequisitesDict={}
        confirmedCourses=set()
        for prerequisite in prerequisites:
            if prerequisite[0] in prerequisitesDict:
                prerequisitesDict[prerequisite[0]].add(prerequisite[1])
            else:
                prerequisitesDict[prerequisite[0]]=set([prerequisite[1]])
            
        def dfs(course,checked):
            if course not in prerequisitesDict or course in confirmedCourses:
                return True
            elif course in checked:
                return False
            else:
                checked.add(course)
                for prereq in prerequisitesDict[course]:
                    if not dfs(prereq,checked): return False
                checked.remove(course)
                confirmedCourses.add(course)
                return True
        
        for course in range(numCourses):
            if not dfs(course,set()): return False
            

        return True
