from .dependencies import *
from .variables import *
from .feature import *
from .Io import *
from .similarity import compute_similarity
from .prepare import prepare_image

def set_engine(num_keypoints, dataset_path):
    """
    num_keypoints: is the number of key sets used for feature extraction and matching.
      You can change this number according to your needs. Note that increasing this number may lead to 
    increased complexity and runtime, so you should choose it carefully.
    """
    orb = cv2.ORB_create(num_keypoints)
    keypoint_dataset = {}

    if os.path.exists(FEAT_PATH):
        keypoint_dataset = load_features()
    else:
        creat_features_dataset(dataset_path, orb)
        keypoint_dataset = load_features()
    return keypoint_dataset



def search(query, num_keypoints, dataset_path):
    print('initialize engine ...')
    keypoint_dataset = set_engine(num_keypoints, dataset_path)
    print("Search ...")
    query_image = prepare_image(query)
    descriptor_query = extract_features(query_image)
    #operator
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    similarities = {}

    for image_path, descriptor_original in keypoint_dataset.items():
        #each descriptor_original , descriptor_query are list
        matches = matcher.match(descriptor_original, descriptor_query)
        similarity = compute_similarity(matches)
        similarities[image_path] = similarity

    similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    if similarities:
        result = next(iter(similarities))[0]
        print(result.split('/')[-2])
        Io.show.result(result, query)
    else:
      print("No similar images found.")
