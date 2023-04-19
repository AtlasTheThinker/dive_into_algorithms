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
plt.plot(xs, ys)
plt.title('Trajectory')
plt.xlabel('X pos')
plt.ylabel('Y pos')
plt.axhline(y=0)
plt.show()
