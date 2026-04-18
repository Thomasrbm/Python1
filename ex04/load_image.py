# Import
import PIL.Image
import numpy


def ft_load(path: str) -> numpy.ndarray:
    img = PIL.Image.open(path)
    fmt = img.format
    if fmt not in ["JPEG"]:  # jpg et jpeg renvoit JPEG
        raise Exception("not the right format (jpeg expected)")
    img = img.convert("RGB")
    tab = numpy.array(img)
    print(f"The shape of image is: {tab.shape}")
    return tab
