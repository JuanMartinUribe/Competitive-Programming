class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:

        course_prereqs = collections.defaultdict(set)
        is_prereq_of = collections.defaultdict(set)

        for course,prereq in prerequisites:
            course_prereqs[course].add(prereq)
            is_prereq_of[prereq].add(course)
        
        can_take = []
        topo_sort = []
        for course in range(num_courses):
            if not course_prereqs[course]:
                can_take.append(course)
        
        while can_take:
            cur_course = can_take.pop()
            topo_sort.append(cur_course)

            for course in is_prereq_of[cur_course]:
                course_prereqs[course].remove(cur_course)
                if not course_prereqs[course]:
                    can_take.append(course)
        
        return len(topo_sort)==num_courses







