class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        time, fresh =0, 0
        rotten = deque()

        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten.append([r, c])

        dirns = [[0,1],[0,-1],[1,0],[-1,0]]
    
        while rotten and fresh > 0:
            for i in range(len(rotten)):
                r, c = rotten.popleft()

                for dr, dc in dirns:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        rotten.append((row,col))
                        fresh  -= 1
            time += 1
        return time if fresh == 0 else -1
                



        