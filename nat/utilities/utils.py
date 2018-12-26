def simple_moving_average(x, window=5):
    if window == 0:
        return x
    return x.rolling(window=window, center=False).mean()


def replace_ninf_to_min(x):
    if x.shape == (0L,):
        return x

    x[x == np.NINF] = None
    y_min = np.nanmin(x)
    x[np.isnan(x)] = y_min
    return x


def replace_pinf_to_max(x):
    if x.shape == (0L,):
        return x

    x[x == np.PINF] = None
    y_max = np.nanmax(x)
    x[np.isnan(x)] = y_max
    return x


def add_gaussian_noise(x, percentage):
    percentage = float(percentage)
    amplitude = np.amax(x) - np.amin(x)
    noise = np.random.normal(0, 1, len(x)) * amplitude * percentage / 100

    return x + noise
