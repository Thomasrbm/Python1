import numpy
import matplotlib.pyplot as plt
import load_image


def ft_invert(array) -> numpy.ndarray:
    """Inverts the color of the image received."""
    result = 255 - array
    # ex sur rouge:
    # pixel rouge pur  [255,   0,   0]
    # 255 -            [  0, 255, 255]  → cyan  (opposé du rouge)

    # pixel blanc      [255, 255, 255]
    # 255 -            [  0,   0,   0]  → noir
    plt.figure("invert")
    plt.imshow(result)
    plt.show()
    return result


def ft_red(array) -> numpy.ndarray:
    """Keeps only the red channel of the image received."""
    plt.figure("red")
    result = array * numpy.array([1, 0, 0], dtype=numpy.uint8)
    plt.imshow(result)
    plt.show()
    return result


def ft_green(array) -> numpy.ndarray:
    """Keeps only the green channel of the image received."""
    plt.figure("green")
    result = array - array * numpy.array([1, 0, 1], dtype=numpy.uint8)
    plt.imshow(result)
    plt.show()
    return result


def ft_blue(array) -> numpy.ndarray:
    """Keeps only the blue channel of the image received."""
    plt.figure("blue")
    result = array * numpy.array([0, 0, 1])
    plt.imshow(result)
    plt.show()
    return result


def ft_grey(array) -> numpy.ndarray:
    """Converts the image received to greyscale."""
    plt.figure("grey")
    grey = array.mean(axis=2).astype(numpy.uint8)
    # array.shape  # (H, W, 3)
    #                       ^ axis=2
    # mean(axis=2)
    # [255, 255, 255]  → blanc  (R=G=B)
    # [0,   0,   0  ]  → noir   (R=G=B)
    # [128, 128, 128]  → gris moyen (R=G=B)

    # si tout a 128 on voit juste du gris. donc :
    # pixel clair  = [220, 200, 210]  → moyenne = 210  → gris clair
    # pixel sombre = [20,  30,  10]   → moyenne = 20   → gris foncé
    # pixel moyen  = [100, 80, 120]   → moyenne = 100  → gris moyen
    result = numpy.stack([grey, grey, grey], axis=2)
    plt.imshow(result)
    plt.show()
    return result


def main():
    try:
        tab = load_image.ft_load("landscape.jpg")

        options = {
            "invert": ft_invert,
            "red":    ft_red,
            "green":  ft_green,
            "blue":   ft_blue,
            "grey":   ft_grey,
        }

        choice = input("Que voulez-vous voir ? \
(invert/red/green/blue/grey/all) : ").strip().lower()

        if choice == "all":
            for name, func in options.items():
                print(f"\n--- {name} ---")
                func(tab)
        elif choice in options:
            options[choice](tab)
        else:
            print("Option invalide")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
