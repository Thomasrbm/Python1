import load_image
import numpy
import matplotlib.pyplot as plt


def print_corners(tab):
    first = tab[0, :3]
    last = tab[-1, -3:]
    fake = numpy.zeros_like(first[:1])
    stacked = numpy.concatenate([first, fake, last])[numpy.newaxis, ...]
    with numpy.printoptions(threshold=6, edgeitems=3):
        print(stacked)


def zoom(tab: numpy.ndarray):
    print_corners(tab)
    tab = tab[100:500, 400:800]
    tab = tab[:, :, 1:2]
    # si 3 cannaux cmap est ignored
    print(f"New shape after slicing: {tab.shape}")
    with numpy.printoptions(edgeitems=3, threshold=10):
        print(tab[:1])
    return tab


def main():
    try:
        img = load_image.ft_load("animal.jpeg")
        sliced = zoom(img)
        plt.imshow(sliced, cmap="gray")
        # load l objet AxesImage, dans la fenetre Figure
        plt.show()
    except KeyboardInterrupt:
        print("Ctrl + c interrupted")
    except Exception as e:
        print(f"error: {e}")


if __name__ == "__main__":
    main()
