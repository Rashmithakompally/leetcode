class Solution:
    def countCollisions(self, directions: str) -> int:
        collisions = 0
        
        # Convert string to list since we will mark cars stopped
        dirs = list(directions)
        n = len(dirs)
        
        # Remove leading L cars → they never collide
        i = 0
        while i < n and dirs[i] == 'L':
            i += 1
        
        # Remove trailing R cars → they never collide
        j = n - 1
        while j >= 0 and dirs[j] == 'R':
            j -= 1
        
        # Now all cars between i and j will eventually collide except stationary ones
        for k in range(i, j + 1):
            if dirs[k] != 'S':
                collisions += 1
        
        return collisions
