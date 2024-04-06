# Additional code for PyCharm
import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def image_to_matrix(image_path):
    A = imread(image_path)
    X = np.mean(A, -1)

    return X


def main():
    A = image_to_matrix('images/fisico.png')
    U, S, VT = np.linalg.svd(A)
    S = np.diag(S)

    j = 0
    inc = 3
    for r in range(4, 100, inc):
        f, axarr = plt.subplots(2, 2)

        Xapprox = U[:, :r] @ S[:r, :r] @ VT[:r, :]
        Xadd = U[:, r-inc:r] @ S[r-inc:r, r-inc:r] @ VT[r-inc:r, :]
        Xprev = U[:, :r-inc] @ S[0:r-inc, :r-inc] @ VT[:r-inc, :]

        axarr[0, 0].imshow(Xapprox).set_cmap('gray')
        axarr[0, 1].imshow(Xadd).set_cmap('gray')
        axarr[1, 0].imshow(Xprev).set_cmap('gray')

        axarr[0, 0].axis('off')
        axarr[0, 0].set_title(f'({r} layers) {r*2*400+r}/{400*400} values.')
        axarr[1, 0].axis('off')
        axarr[1, 0].set_title(f'Previous {r - inc} Layers')
        axarr[0, 1].axis('off')
        axarr[0, 1].set_title(f'Additional {inc} Layers')

        plt.show()
        print(r)


if __name__ == '__main__':
    main()
