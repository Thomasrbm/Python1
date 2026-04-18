import load_image
import numpy
import matplotlib.pyplot as plt


def rotate(tab: numpy.ndarray) -> numpy.ndarray:
    squeezed = numpy.squeeze(tab)
    result = numpy.transpose(squeezed)
    return result


if __name__ == "__main__":
    try:
        tab = load_image.ft_load("animal.jpeg")
        print(tab)
        sliced = tab[100:500, 450:850, 1:2]
        # garde 400 par 400 pixel, canal au hasard, osef
        print("New shape after Transpose: ", end="")
        transposed = rotate(sliced)
        print(transposed.shape)
        print(transposed)
        plt.imshow(transposed, cmap="gray")
        plt.axis('on')
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
