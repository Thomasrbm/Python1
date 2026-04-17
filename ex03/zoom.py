import load_image
import numpy
import matplotlib.pyplot as plt


def zoom(tab: numpy.ndarray) -> numpy.ndarray:
    y_center = tab.shape[0] // 2
    x_center = tab.shape[1] // 2
    sliced = tab[y_center-300:y_center+100, x_center-50:x_center+350, 1:2]
    print(f"New shape after slicing: {sliced.shape}")
    print(sliced)
    return sliced


if __name__ == "__main__":
    try:
        tab = load_image.ft_load("animal.jpeg")
        print(tab)
        sliced = zoom(tab)
        plt.imshow(numpy.squeeze(sliced), cmap="gray")
        plt.axis('on')
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
