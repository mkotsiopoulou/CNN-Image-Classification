import os
import scipy.io
import matplotlib.pyplot as plt
from PIL import Image

annotaion_file = '/Users/marina/Python/CNN/show_annotation.m'

def show_annotation(imgfile, annotation_file):
    # Προβολή της εικόνας με βάση τα annotations
    IMTYPE = 'jpg'
    LARGEFONT = 28
    MEDFONT = 18
    BIG_WINDOW = plt.get_current_fig_manager().window
    SMALL_WINDOW = [100, 100, 512, 480]

    # Φόρτωση των συντεταγμένων του πλαισίου και των συντεταγμένων του αντικειμένου
    annotations = scipy.io.loadmat(annotation_file)
    box_coord = annotations['box_coord']
    obj_contour = annotations['obj_contour']

    # Διάβασμα και εμφάνιση της εικόνας
    image = Image.open(imgfile)
    plt.figure()
    plt.imshow(image)
    plt.axis('image')
    plt.axis('ij')
    plt.title(imgfile)
    plt.show()

    # Εμφάνιση του πλαισίου
    plt.figure()
    plt.imshow(image)
    plt.axis('image')
    plt.axis('ij')
    box_handle = plt.Rectangle(
        (box_coord[3], box_coord[1]),
        box_coord[4] - box_coord[3],
        box_coord[2] - box_coord[1],
        edgecolor='y',
        linewidth=5,
        fill=False,
    )
    plt.gca().add_patch(box_handle)

    # Εμφάνιση του περιγράμματος
    for cc in range(obj_contour.shape[1]):
        if cc < obj_contour.shape[1] - 1:
            plt.plot(
                obj_contour[0, cc] + box_coord[3],
                obj_contour[1, cc] + box_coord[1],
                'r',
                linewidth=4,
            )
        else:
            plt.plot(
                [obj_contour[0, cc], obj_contour[0, 0]] + box_coord[3],
                [obj_contour[1, cc], obj_contour[1, 0]] + box_coord[1],
                'r',
                linewidth=4,
            )

    plt.title(imgfile)
    plt.show()