class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        height = len(grid)
        width = len(grid[0])

        visited = [[False]* width for _ in range(height)]

        def dfs(x, y):
            visited[x][y] = True
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not(0 <= nx < height and 0 <= ny < width):
                    continue
                if visited[nx][ny]:
                    continue
                if grid[nx][ny] != '1':
                    continue
                dfs(nx, ny)

        count = 0
        for x in range(height):
            for y in range(width):
                if visited[x][y]:
                    continue
                if grid[x][y] != '1':
                    continue
                
                dfs(x, y)
                count += 1

        return count