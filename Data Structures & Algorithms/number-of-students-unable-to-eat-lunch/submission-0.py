class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while  len(sandwiches)>0 and sandwiches[0] in students:
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
            else: 
                element = students.pop(0)
                students.append(element)
            
            print(students)
            print(sandwiches)

        return len(students)
            
        