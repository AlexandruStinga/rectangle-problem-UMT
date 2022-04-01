from Point import Point


def readPoints(nr, points):
    """
    Reads a given number of points
    :param points: the list in which to add the points that have been read
    :param nr: number of points
    """
    for i in range(nr):
        x = int(input("x = "))
        y = int(input("y = "))
        p = Point(x, y)
        points.append(p)


def solve(points):
    """
    Function to count the number of rectangles that can be made using the points in the list
    :param points: list that contains all the points
    :return: number of rectangles

    The algorithm takes every pair of points (x,y) and (a,b) and considers them to be the diagonal of some rectangle.
    When we consider them to be a diagonal, x != a and y != b. If there exist the points (x,b) and (a,y) in the list,
    we have a rectangle and increment the nrRectangles variable. As there are two diagonals for each rectangle, we have
    to divide the number we get by 2, thus getting the number of rectangles.

    """
    nrRectangles = 0
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            point1 = points[i]
            point2 = points[j]

            if point1.getX() != point2.getX() and point1.getY() != point2.getY():
                point3 = Point(point1.getX(), point2.getY())
                point4 = Point(point2.getX(), point1.getY())

                if pointExists(point3, points) and pointExists(point4, points):
                    nrRectangles += 1

    return nrRectangles // 2


def pointExists(p, points):
    """
    Function to check if a point already exists in the list of points
    :param points: the list of points to check if p exists in
    :param p: a point
    :return: true if the point exists in the list, false otherwise
    """
    for point in points:
        if point.getX() == p.getX() and point.getY() == p.getY():
            return True
    return False


def menu():
    while True:
        print("1.Run example 1")
        print("2.Run example 2")
        print("3.Run another example (read from keyboard) ")
        print("0.Exit")

        option = int(input("Option: "))
        if option == 1:
            points = [Point(1, 1), Point(1, 3), Point(2, 1), Point(2, 3), Point(3, 1), Point(3, 3)]
            print("Number of rectangles: ", solve(points))
        if option == 2:
            points = [Point(1, 1), Point(1, 3), Point(2, 1), Point(3, 1), Point(3, 3)]
            print("Number of rectangles: ", solve(points))
        if option == 3:
            points = []
            nrPoints = int(input("Number of points: "))
            readPoints(nrPoints, points)
            print("Number of rectangles: ", solve(points))
        if option == 0:
            break


if __name__ == '__main__':
    menu()
