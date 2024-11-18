import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h
    
    def __lt__(self, other):
        return self.f < other.f

def a_star_algorithm(start, goal, grid, heuristic):
    open_set = []
    closed_set = set()
    
    start_node = Node(start, None, 0, heuristic(start, goal))
    goal_node = Node(goal, None)

    heapq.heappush(open_set, start_node)
    
    while open_set:
        current_node = heapq.heappop(open_set)
        
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        closed_set.add(current_node.position)
        
        for neighbor_pos in get_neighbors(current_node.position, grid):
            if neighbor_pos in closed_set:
                continue
            
            g = current_node.g + 1
            h = heuristic(neighbor_pos, goal)
            neighbor_node = Node(neighbor_pos, current_node, g, h)
            
            if not any(neighbor.position == neighbor_pos and neighbor.f < neighbor_node.f for neighbor in open_set):
                heapq.heappush(open_set, neighbor_node)
    
    return None

def get_neighbors(position, grid):
    x, y = position
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            neighbors.append((nx, ny))
    
    return neighbors

def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (4, 4)
    
    path = a_star_algorithm(start, goal, grid, manhattan_distance)
    
    if path: print("Path found:", path)
    else: print("No path found")