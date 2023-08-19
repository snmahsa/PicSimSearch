from ..dependencies import *


def read_image(path, mode = -1):
    """
    0 : gray scale
    1 : colorfull
    -1 : same
    """
    return cv2.imread(path, mode)


def read_image_from_folder():
    default_folder_path = 'PicSimSearch/Images/'
    #Hide tk window
    root = tk.Tk()
    root.withdraw()
    #Get image path
    file_path = filedialog.askopenfilename(initialdir=default_folder_path)
    #read image
    if len(file_path) != 0 :
        image = cv2.imread(file_path)
        #check successfully
        if image is None:
            print("Unable to read image")
            return None
        else:
            return image
    else:
        return None    




# def read_image_from_folder():
#     default_folder_path = '../../Image/'
#     file_path = gr.inputs.Image(type="filepath", label="Select Image")
    
#     def read_image(file):
#         image = cv2.imread(file.name)
#         if image is None:
#             print("Unable to read image")
#             return None
#         else:
#             return image
    
#     interface = gr.Interface(fn=read_image, inputs=file_path, outputs=None)
#     interface.launch()

