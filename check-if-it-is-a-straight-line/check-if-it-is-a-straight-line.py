class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # u_coordinates = set(coordinates)
        p1, p2 = coordinates[0], coordinates[-1]
        try:
            m = (p2[1] - p1[1]) / (p2[0] - p1[0])
            c = p1[1] - (m * p1[0])
            
            for x, y in coordinates:
                if not y == (m * x) + c:
                    return False
        except:
            x1 = p1[0]
            for x, _ in coordinates:
                if x1 != x:
                    return False 


        return True