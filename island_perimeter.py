class Solution(object):
    def islandPerimeter(self, grid):
        height = len(grid)
        width = len(grid[0])
        perimeter = 0

        for i in range(0, height):
            for j in range(0, width):
                if grid[i][j] == 1:
                    if i == 0:
                        perimeter += 1
                    elif grid[i - 1][j] == 0:
                        perimeter += 1

                    if i == height - 1:
                        perimeter += 1
                    elif grid[i + 1][j] == 0:
                        perimeter += 1

                    if j == 0:
                        perimeter += 1
                    elif grid[i][j - 1] == 0:
                        perimeter += 1

                    if j == width - 1:
                        perimeter += 1
                    elif grid[i][j + 1] == 0:
                        perimeter += 1

        return perimeter

print(Solution().islandPerimeter([[0, 1, 0, 0],
                                  [1, 1, 1, 0],
                                  [0, 1, 0, 0],
                                  [1, 1, 0, 0]]))
