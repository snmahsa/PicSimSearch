from ..dependencies import *
class Io:
    """
     upload  
    """
  
def upload_image_of_local():

        
    #Hide tk window
    root = tk.Tk()
    root.withdraw()
    #Get image path of local 
    file_path = filedialog.askopenfilename()
    #Select new path for saving
    dest_directory = filedialog.askdirectory()
    #Check
    if file_path and len(dest_directory) != 0 :
        #Read image
        image = cv2.imread(file_path)
        #Save
        file_name = os.path.basename(file_path)
        cv2.imwrite(os.path.join(dest_directory, file_name), image)
        # shutil.copy(file_path,dest_directory)
        # image = cv2.imread(file_path)
        # return file_name
    else:
        print("No file selected")


def upload_image_of_url(url):
    """
    return imagr name
    """
    url = url
    response = requests.get(url)
    image = PIL.Image.open(BytesIO(response.content))
    image = np.array(image)
    image = image.astype(float)

    #Select new path for saving
    dest_directory = filedialog.askdirectory()
    #Check
    if image.size > 0 and len(dest_directory) != 0 :
        #Save
        file_name = os.path.basename(url)
        cv2.imwrite(os.path.join(dest_directory, file_name), image)

        # return file_name
    else:
        print("No file selected")