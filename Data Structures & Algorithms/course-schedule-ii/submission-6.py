class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def checkPre(course, output):
            if course in visited:
                output.clear()
                return False
            if course in store:
                return True
            visited.add(course)
            pres = courses_dict.get(course, [])
            for pre in pres:
                if not checkPre(pre, output):
                    return False
            output.append(course)
            store.add(course)
            visited.remove(course)
            return True
            
        visited = set()
        store = set()
        output = []
        courses_dict = dict()
        for course in prerequisites:
            courses_dict.setdefault(course[0], []).append(course[1])
        for i in range(numCourses):
            checkPre(i, output)
            if not output:
                return []
        return output