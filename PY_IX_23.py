def are_collinear(point1, point2, point3):
    area = 0.5 * (
        (point2[0] - point1[0]) * (point3[1] - point1[1])
        - (point3[0] - point1[0]) * (point2[1] - point1[1])
    )
    return area == 0


def find_non_collinear_points(points):
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if not are_collinear(points[i], points[j], points[k]):
                    return i + 1, j + 1, k + 1
    return None


with open("INPUT.TXT", "r") as file:
    lines = file.readlines()
    n = int(lines[0])
    points = [tuple(map(int, line.strip().split())) for line in lines[1:]]

non_collinear_points = find_non_collinear_points(points)

with open("OUTPUT.TXT", "w") as output_file:
    if non_collinear_points:
        output_file.write("Yes\n")
        output_file.write(" ".join(map(str, non_collinear_points)))
    else:
        output_file.write("No")
