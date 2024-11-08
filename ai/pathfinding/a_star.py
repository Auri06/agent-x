import heapq


class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.open_list = []
        self.closed_list = set()
        self.came_from = {}
        self.g_score = {}
        self.f_score = {}

    def heuristic(self, start, goal):
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    def get_neighbors(self, node):
        neighbors = []
        x, y = int(node[0]), int(node[1])  # Convert to integers
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < self.cols and 
                0 <= new_y < self.rows and 
                self.grid[new_y][new_x] == 0):
                neighbors.append((new_x, new_y))
        return neighbors

    def reconstruct_path(self, current):
        total_path = [current]
        while current in self.came_from:
            current = self.came_from[current]
            total_path.append(current)
        return total_path[::-1]

    def search(self, start, goal):
        # Convert start and goal to integers
        start = (int(start[0]), int(start[1]))
        goal = (int(goal[0]), int(goal[1]))
        
        # Reset internal state
        self.open_list = []
        self.closed_list = set()
        self.came_from = {}
        self.g_score = {}
        self.f_score = {}

        heapq.heappush(self.open_list, (0, start))
        self.g_score[start] = 0
        self.f_score[start] = self.heuristic(start, goal)

        while self.open_list:
            _, current = heapq.heappop(self.open_list)

            if current == goal:
                return self.reconstruct_path(current)

            self.closed_list.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in self.closed_list:
                    continue

                tentative_g_score = self.g_score[current] + 1

                if neighbor not in self.g_score or tentative_g_score < self.g_score[neighbor]:
                    self.came_from[neighbor] = current
                    self.g_score[neighbor] = tentative_g_score
                    self.f_score[neighbor] = tentative_g_score + \
                        self.heuristic(neighbor, goal)
                    heapq.heappush(
                        self.open_list, (self.f_score[neighbor], neighbor))

        return None
