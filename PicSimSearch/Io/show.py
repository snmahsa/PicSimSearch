from ..dependencies import *
from ..variables import *
from ..color import to_rgb

# def result(result, query):
#     fig, axes = plt.subplots(1, 2, figsize=(9, 9))
#     query_image = to_rgb(query)
#     plt.axis('off')
#     plt.set_title('query')
#     plt.imshow()


#     for ax, img_title in zip(axes, ['Query Image', 'Result Image']):
#       img = cv2.imread(query)
#       ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#       ax.axis('off')
#       ax.set_title(img_title)
#     plt.show()


def result(result, query):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    # تصویر اول
    axes[0].imshow(query)
    axes[0].axis('off')
    axes[0].set_title('Image 1')
    
    # تصویر دوم
    axes[1].imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    axes[1].axis('off')
    axes[1].set_title('Image 2')
    
    plt.tight_layout()
    plt.show()
