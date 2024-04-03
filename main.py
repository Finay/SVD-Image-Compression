# Additional code for PyCharm
import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def svd(matrix):
    return None


def image_to_matrix(image_path):
    A = imread(image_path)
    X = np.mean(A, -1)

    return X


def show_from_matrix(matrix, path="compressed_images/output.png"):
    img = plt.imshow(matrix)
    img.set_cmap('gray')
    plt.axis('off')
    plt.show()


def main():
    A = image_to_matrix('images/fisico.png')
    U, S, VT = np.linalg.svd(A, full_matrices=False)
    S = np.diag(S)

    j = 0
    for r in (5, 20, 100):
        print(U.shape, S.shape, VT.shape)
        Xapprox = U[:, :r] @ S[0:r, :r] @ VT[:r, :]
        plt.figure(j+1)
        j += 1

        show_from_matrix(Xapprox)
        print(r)


if __name__ == '__main__':
    main()
