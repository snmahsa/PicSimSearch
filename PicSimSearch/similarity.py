from .dependencies import *
from .variables import *

def compute_similarity(matches):
    distances = [m.distance for m in matches]
    if len(distances) == 0:
      return 0
    distance = sum(distances) / len(distances)
    sim = 1 / (1 + distance)
    return sim

