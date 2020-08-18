#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3342/
#https://www.youtube.com/watch?v=0ACfAqs8mm0&t=148s

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def BFSUtil(self, v, color):
        queue = [];
        queue.append(v);
        color[v] = 0;
        while queue:
            current = queue.pop(0);
            for i in self.graph[current]:
                if color[current] == color[i]:
                    return False;
                if color[i] == -1:
                    queue.append(i);
                    color[i] = 1 - color[current]
        return True;
    def possibleBipartition(self, N: int, dislikes: [[int]]) -> bool:
        lrow = N;
        if lrow == 0:
            return True;
        color = [-1]*(N+1);
        for l in dislikes:
            self.graph[l[0]].append(l[1]);
            self.graph[l[1]].append(l[0]);
        for i in range(1, lrow):
            if color[i] == -1:
                if not self.BFSUtil(i, color):
                    return False;
        return True;