'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths
would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

runtime: 48ms
'''
import random

class Solution:
    '''
    @param obstacle_grid:
    @type obstacle_grid:
    '''
    def unique_paths_with_obstacles(self, obstacle_grid):
        row = len(obstacle_grid)
        column = len(obstacle_grid[0])
        dp = [[0 for j in range(column)] for i in range(row)]

        for i in range(row):
            if obstacle_grid[i][0] == 0:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
                break

        for j in range(column):
            if obstacle_grid[0][j] == 0:
                dp[0][j] = 1
            else:
                dp[0][j] = 0
                break

        for i in range(1, row):
            for j in range(1, column):
                if obstacle_grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[row-1][column-1]

if __name__ == '__main__':
    s = Solution()

    def generate_grid(m, n, num_ones):
        row = random.randint(1, m)
        column = random.randint(1, n)
        matrix = [[0 for j in range(column)] for i in range(row)]
        # num_ones = random.randint(1, row * column)

        for i in range(num_ones):
            p = random.randrange(row)
            q = random.randrange(column)
            matrix[p][q] = 1

        return matrix

    result = []
    for i in range(10):
        obstacle_grid = generate_grid(10, 10, 2)
        result.append(s.unique_paths_with_obstacles(obstacle_grid))

    print(result)
