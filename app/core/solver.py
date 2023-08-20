def solver(jx, jy, goal):
    steps = 0
    # Status: each jar content and space
    j = Juggler(jx, jy, goal)

    if goal in (jx, jy):
        steps = steps + 1
        return steps



    while goal not in (jx, jy):
        pass


    print(j.jar_x, j.jar_y)
    j.fill(j.jar_x)  # llenas 5
    print(j.jar_x, j.jar_y)
    j.transfer(j.jar_x, j.jar_y)  # sacas 3 a jarra3
    print(j.jar_x, j.jar_y)
    j.empty(j.jar_y)  # vacias jarra3
    print(j.jar_x, j.jar_y)
    j.transfer(j.jar_x, j.jar_y)  # pasas 2 que  quedaban a j3
    print(j.jar_x, j.jar_y)
    j.fill(j.jar_x)  # llenas 5
    print(j.jar_x, j.jar_y)
    j.transfer(j.jar_x, j.jar_y)  # mandas j5 lo que entre a j3
    print(j.jar_x, j.jar_y)






if __name__ == '__main__':
    solver(5, 3, 4)