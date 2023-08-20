from .dependencies import *
def set_dataset_path():
  
    #Hide tk window
    root = tk.Tk()
    root.withdraw()
    #Get dataset path of local 
    # file_path = filedialog.askopenfilename()
    #Select dataset path 
    directory = filedialog.askdirectory()
    #Check
    if len(directory) != 0 :
        return directory
    else:
        return None

