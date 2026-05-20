class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def checkRoot(index):
            if index in visited:
                output[0] = False
                return
            visited.add(index)
            for root in courses.get(index, []):
                checkRoot(root)
            visited.remove(index)
        courses = dict()
        output = [True]
        visited = set()
        for course in prerequisites:
            courses.setdefault(course[0], []).append(course[1])
        
        for course_index in range(numCourses):
            visited = set()
            checkRoot(course_index)
            if not output[0]:
                return False
            visited.clear()
        return output[0]

         
