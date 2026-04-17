import numpy
import matplotlib.pyplot as plt


def ft_invert(array) -> numpy.ndarray:
    """Inverts the color of the image received."""
    result = 255 - array
    plt.imshow(result)
    plt.show()
    return result


def ft_red(array) -> numpy.ndarray:
    """Keeps only the red channel of the image received."""
    result = array * numpy.array([1, 0, 0], dtype=numpy.uint8)
    plt.imshow(result)
    plt.show()
    return result


def ft_green(array) -> numpy.ndarray:
    """Keeps only the green channel of the image received."""
    result = array - array * numpy.array([1, 0, 1], dtype=numpy.uint8)
    plt.imshow(result)
    plt.show()
    return result


def ft_blue(array) -> numpy.ndarray:
    """Keeps only the blue channel of the image received."""
    result = numpy.zeros_like(array)
    result[:, :, 2] = array[:, :, 2]
    plt.imshow(result)
    plt.show()
    return result


def ft_grey(array) -> numpy.ndarray:
    """Converts the image received to greyscale."""
    grey = (array[:, :, 0] / 3 + array[:, :, 1] /
            3 + array[:, :, 2] / 3).astype(numpy.uint8)
    result = numpy.stack([grey, grey, grey], axis=2)
    plt.imshow(result)
    plt.show()
    return result
