import matplotlib.pyplot as plt

GRAV_ACC = -10


def ball_trajectory(x):
    horizontal_v = 0.99
    vertical_v = 9.9
    location = vertical_v/horizontal_v * x + \
        (GRAV_ACC * (x ** 2)/(2 * (horizontal_v ** 2)))
    return location


xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(x) for x in xs]
xs2 = [0.1, 2]
ys2 = [ball_trajectory(0.1), 0]
xs3 = [0.2, 2]
ys3 = [ball_trajectory(0.2), 0]
xs4 = [0.3, 2]
ys4 = [ball_trajectory(0.3), 0]
plt.plot(xs, ys, xs2, ys2, xs3, ys3, xs4, ys4)
plt.title('Trajectory with Lines of sight')
plt.xlabel('X pos')
plt.ylabel('Y pos')
plt.axhline(y=0)
plt.show()
