def findOrder(numCourses, prerequisites):
    hasPrerequisites={}
    coursesSeen=set()
    
    courseOrder=[]

    for prerequisite in prerequisites:
        if prerequisite[0] in hasPrerequisites:
            hasPrerequisites[prerequisite[0]].add(prerequisite[1])
        else:
            hasPrerequisites[prerequisite[0]]=set([prerequisite[1]])
    
    def dfs(course, visiting):
        if course in coursesSeen:
            return True
        elif course in visiting:
            return False
        elif course in hasPrerequisites:
            visiting.add(course)
            for prerequisite in hasPrerequisites[course]:
                if not dfs(prerequisite,visiting): return False
                           
        courseOrder.append(course)
        coursesSeen.add(course)
        return True

    for course in range(numCourses):
        if not dfs(course, set()): return []
    return courseOrder
        

        
