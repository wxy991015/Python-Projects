def countPoints(points: list[list[int]], queries: list[list[int]]) -> list[int]:
    answer = []
    for query in queries:
        points_inside = 0
        xCentre, yCentre, radius = query
        for point in points:
            xCoordinate, yCoordinate = point
            if ((xCentre-xCoordinate)**2 + (yCentre-yCoordinate)**2) ** (1/2) <= radius:
                points_inside += 1
        answer.append(points_inside)
    return answer

points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]
print(f"Output: {countPoints(points, queries)}")