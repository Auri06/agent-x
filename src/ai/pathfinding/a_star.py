import heapq

class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.open_list = []
        self.closed_list = set()
        self.came_from = {}
        self.g_score = {}
        self.f_score = {}

    def heuristic(self, start, goal):
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    def get_neighbors(self, node):
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (node[0] + dx, node[1] + dy)
            if 0 <= neighbor[0] < len(self.grid) and 0 <= neighbor[1] < len(self.grid[0]) and self.grid[neighbor[0]][neighbor[1]] == 0:
                neighbors.append(neighbor)
        return neighbors

    def reconstruct_path(self, current):
        total_path = [current]
        while current in self.came_from:
            current = self.came_from[current]
            total_path.append(current)
        return total_path[::-1]

    def search(self, start, goal):
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
