import load_image
import numpy
import matplotlib.pyplot as plt


def rotate(tab: numpy.ndarray) -> numpy.ndarray:
    squeezed = numpy.squeeze(tab)
    rows, cols = squeezed.shape
    result = numpy.zeros((cols, rows), dtype=numpy.uint8)
    for i in range(rows):
        for j in range(cols):
            result[j][i] = squeezed[i][j]
    return result


if __name__ == "__main__":
    try:
        tab = load_image.ft_load("animal.jpeg")
        print(tab)
        sliced = tab[100:500, 450:850, 1:2]
        print(f"New shape after Transpose: ", end="")
        transposed = rotate(sliced)
        print(transposed.shape)
        print(transposed)
        plt.imshow(transposed, cmap="gray")
        plt.axis('on')
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
