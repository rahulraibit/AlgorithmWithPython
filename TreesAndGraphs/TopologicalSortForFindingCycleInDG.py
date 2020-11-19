
from collections import defaultdict
#https://leetcode.com/problems/course-schedule/submissions/

class Solution:
    def __init__(self):
        self.graph = {}
        
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        for l in prerequisites:
            if not l[0] in self.graph:
                self.graph[l[0]] = [];
            self.graph[l[0]].append(l[1]);
        
        l = len(self.graph);
        visited = {}
        recStack = {}
        def isCyclic(node):  
            visited[node] = True 
            recStack[node] = True
            if node in self.graph:
                for next_node in self.graph[node]:
                    if not next_node in visited:
                        if isCyclic(next_node):
                            return True;
                    elif recStack[next_node]:
                            return True;
            recStack[node] = False
            return False
        for i in self.graph:
                if not i in visited and isCyclic(i):
                    return False
        return True