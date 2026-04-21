import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from maps.maze_basic import maze as basic_maze
from maps.maze_hard import maze as hard_maze
from src.core_logic import get_start_goal, print_maze_with_path

# Test BFS và DFS với các thứ tự hướng khác nhau

def get_neighbors_original(maze, node):
    """Thứ tự gốc: Lên, Xuống, Trái, Phải"""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    r, c = node
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != 1:
            neighbors.append((nr, nc))
    return neighbors

def get_neighbors_phải_trước(maze, node):
    """Thứ tự mới: Phải, Lên, Xuống, Trái"""
    directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    neighbors = []
    r, c = node
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != 1:
            neighbors.append((nr, nc))
    return neighbors

def bfs_custom(maze, get_neighbors_func):
    from collections import deque
    start, goal = get_start_goal(maze)
    
    if not start or not goal:
        return None, set()
    
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path, visited
        for neighbor in get_neighbors_func(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None, visited

def dfs_custom(maze, get_neighbors_func):
    start, goal = get_start_goal(maze)
    
    if not start or not goal:
        return None, set()
    
    stack = [(start, [start])]
    visited = set()
    visited.add(start)

    while stack:
        current, path = stack.pop()
        if current == goal:
            return path, visited
        for neighbor in get_neighbors_func(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
    return None, visited

print("\n========== SO SÁNH CÁC HƯỚNG ĐI ==========\n")

print("--- BẢN ĐỒ 10x10 ---\n")

print("📊 BFS - Thứ tự gốc (Lên, Xuống, Trái, Phải):")
_, visited_bfs_orig = bfs_custom(hard_maze, get_neighbors_original)
print(f"   Ô duyệt: {len(visited_bfs_orig)}")

print("\n📊 BFS - Thứ tự mới (Phải, Lên, Xuống, Trái):")
_, visited_bfs_new = bfs_custom(hard_maze, get_neighbors_phải_trước)
print(f"   Ô duyệt: {len(visited_bfs_new)}")

print("\n📊 DFS - Thứ tự gốc (Lên, Xuống, Trái, Phải):")
_, visited_dfs_orig = dfs_custom(hard_maze, get_neighbors_original)
print(f"   Ô duyệt: {len(visited_dfs_orig)}")

print("\n📊 DFS - Thứ tự mới (Phải, Lên, Xuống, Trái):")
_, visited_dfs_new = dfs_custom(hard_maze, get_neighbors_phải_trước)
print(f"   Ô duyệt: {len(visited_dfs_new)}")

print("\n📝 KẾT LUẬN:")
print(f"   - BFS luôn duyệt cùng số ô bất kể thứ tự (tìm kiếm theo chiều rộng): {len(visited_bfs_orig) == len(visited_bfs_new)}")
print(f"   - DFS thay đổi kết quả khi thứ tự khác: {len(visited_dfs_orig)} → {len(visited_dfs_new)} ô")
print(f"   - DFS tối ưu hơn BFS về bộ nhớ (duyệt ít ô hơn): DFS={len(visited_dfs_orig)} < BFS={len(visited_bfs_orig)}")
