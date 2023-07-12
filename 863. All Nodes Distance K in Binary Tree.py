# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def d(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                d(cur.left, cur)
            if cur.right:
                d(cur.right, cur)
        d(root, None)
        
        ans = []
        visited = set([target.val])
        queue = deque([(target.val, 0)])
        while queue:
            curr, distance = queue.popleft()
            if distance == k:
                ans.append(curr)
                continue
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    queue.append((neighbor, distance +1))
                    visited.add(neighbor)
        return ans