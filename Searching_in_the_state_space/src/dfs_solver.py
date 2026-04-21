from src.core_logic import get_start_goal, get_neighbors as get_neighbors_logic, print_maze_with_path

def dfs(maze):
    start, goal = get_start_goal(maze)
    
    if not start or not goal:
        print("Không tìm thấy Start hoặc Goal trong bản đồ!")
        return None, set()
    
    stack = [(start, [start])]

    visited = set()
    visited.add(start)

    while stack:
        current, path = stack.pop()

        if current == goal:
            print_maze_with_path(maze, path, len(visited))
            return path, visited

        for neighbor in get_neighbors_logic(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))

    print(f"Không tìm thấy đích! Đã duyệt qua {len(visited)} ô")
    return None, visited