class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten.append((r, c))

        minutes = 0
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        while rotten and fresh:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in DIRS:
                    nr, nc = dr+r, dc+c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotten.append((nr,nc))
            minutes += 1

        return minutes if fresh == 0 else -1


        