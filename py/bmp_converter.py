from PIL import Image
import array
import os


def rgb332(r, g, b):
    r = r >> 5
    g = g >> 5
    b = b >> 6
    c = r << 5 | g << 2 | b
    return c


def rgb565(r, g, b):
    r = r >> 3
    g = g >> 2
    b = b >> 3
    c = r << 11 | g << 5 | b
    return c


def convert(cvt, path, subpath):
    subpath = os.path.join(path, subpath)
    if not os.path.exists(subpath):
        os.mkdir(subpath)

    for _, _, filesnames in os.walk(path):
        for file in filesnames:
            if (os.path.splitext(file)[-1] != '.bmp'):
                continue
            im = Image.open(os.path.join(path, file))
            width, height = im.size
            v = [cvt(r, g, b) for (r, g, b) in im.getdata()]
            v = [width & 0xff, width >> 8, height & 0xff, height >> 8] + v
            v = array.array('B', v)
            f = open(os.path.join(subpath, file), "wb")
            f.write(v)
            f.close()
        break


convert(rgb332, 'bmp', 'rgb332')
