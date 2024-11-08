class DFS:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        
    def search(self, start, goal):
        # Convert start and goal to integers
        start = (int(start[0]), int(start[1]))
        goal = (int(goal[0]), int(goal[1]))
        
        visited = set()
        path = []
        
        def dfs(current):
            if current == goal:
                return True
            
            visited.add(current)
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            for dx, dy in directions:
                next_x = int(current[0] + dx)
                next_y = int(current[1] + dy)
                next_pos = (next_x, next_y)
                
                if (0 <= next_x < self.cols and 
                    0 <= next_y < self.rows and 
                    next_pos not in visited and 
                    self.grid[next_y][next_x] == 0):
                    path.append(next_pos)
                    if dfs(next_pos):
                        return True
                    path.pop()
            
            return False
        
        path.append(start)
        dfs(start)
        return path