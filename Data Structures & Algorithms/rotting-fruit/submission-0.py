class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0
        minutes = 0

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 2:
                    rotten.append((row, column))
                    print(rotten)
                elif grid[row][column] == 1:
                    fresh += 1

        directions = [
            [-1, 0],  # up
            [1, 0],   # down
            [0, -1],  # left
            [0, 1]    # right
        ]

        while rotten and fresh > 0:

            # Everything currently in the queue
            # represents fruit rotten at THIS minute
            for i in range(len(rotten)):
                foundRow, foundColumn = rotten.popleft()

                for dr, dc in directions:
                    row = foundRow + dr
                    column = foundColumn + dc

                    if (
                        row >= 0
                        and row < len(grid)
                        and column >= 0
                        and column < len(grid[0])
                        and grid[row][column] == 1
                    ):
                        grid[row][column] = 2
                        fresh -= 1
                        rotten.append((row, column))

            minutes += 1

        if fresh > 0:
            return -1

        return minutes