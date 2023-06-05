class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        # Calculate the slope of the first line segment
        if x1 - x0 != 0:
            slope = (y1 - y0) / (x1 - x0)
        else:
            slope = float('inf')  # Handle vertical line case
        # Check the slopes of subsequent line segments
        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i] 
            # Calculate the slope of the current line segment
            if xi - x0 != 0:
                curr_slope = (yi - y0) / (xi - x0)
            else:
                curr_slope = float('inf')  # Handle vertical line case
            # If the slope of the current line segment is not equal to the initial slope, return False
            if curr_slope != slope:
                return False
        return True
