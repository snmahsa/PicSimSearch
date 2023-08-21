from .prepare import prepare_image
from .dependencies import *
from .variables import *
# FEAT_PATH = 'PicSimSearch/features/features.pkl'
# FEAT_FOLDER_PATH = 'PicSimSearch/features/'

def load_features(FEAT_PATH):
    print('[INFO] Loading Features...')
    KeypointDataset = pickle.loads(open(FEAT_PATH, 'rb').read())
    return KeypointDataset

def serialize_features(features,FEAT_PATH):
    print('[INFO] Serializing Features...')
    f = open(FEAT_PATH, 'wb')
    f.write(pickle.dumps(features))
    f.close()

def extract_features(image, orb):
    print("extract_features")
    _, descriptor = orb.detectAndCompute(image, None)
    return descriptor

def creat_features_dataset(dataset_path, orb,FEAT_PATH):
    features = {}
    is_exist = os.path.exists(FEAT_FOLDER_PATH)
    if not is_exist:
        os.mkdir(FEAT_FOLDER_PATH)  
    for imagepath in glob.iglob(dataset_path + '/**/*.jpg', recursive=True):
        try:
            image = cv2.imread(imagepath)
            prepared_image = prepare_image(image)
            features[imagepath] = extract_features(prepared_image, orb)
        except:
            pass
    serialize_features(features,FEAT_PATH)