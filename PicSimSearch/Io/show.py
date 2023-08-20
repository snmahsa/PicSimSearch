from ..dependencies import *
from ..variables import *
from ..color import to_rgb

def result(result, query):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    # تصویر اول
    axes[0].imshow(cv2.cvtColor(query, cv2.COLOR_BGR2RGB))
    axes[0].axis('off')
    axes[0].set_title('query')
    
    # تصویر دوم
    result_image = cv2.imread(result)
    axes[1].imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
    axes[1].axis('off')
    axes[1].set_title('result')
    
    plt.tight_layout()
    plt.show()
