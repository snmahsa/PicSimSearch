# PicSimSearch

PicSimSearch is a Python package for image search based on keypoint-based feature extraction and matching. It allows you to search for similar images in a dataset using a query image.


## Installation

### Using pip
PicSimSearch can be installed using pip:

```shell
pip install PicSimSearch
```
### Using Poetry
PicSimSearch can be installed using poetry:

1. Install Poetry:

   ```shell
   pip install poetry
   ```
2. Navigate to the project directory:   
    ```shell
    cd path/to/your/project
    ```
3. Install the dependencies:
    ```shell
    poetry install
    ```
4. Install    
    ```shell
   poetry add PicSimSearch
        ```
## Usage
```python
from PicSimSearch import Io
from PicSimSearch import *
from PicSimSearch import engine
from PicSimSearch import dataset

```

```python
Io.upload.upload_image_of_local()
```
![Sample Image](https://github.com/snmahsa/myrep/blob/main/upload_image_of_local1.png)
![Sample Image](https://github.com/snmahsa/myrep/blob/main/upload_image_of_local2.png)

```python
image = Io.read.read_image_from_folder()
```
![Sample Image](https://github.com/snmahsa/myrep/blob/main/read_image_from_folder2.png)

![Sample Image](https://github.com/snmahsa/myrep/blob/main/hvij.png)

```python
Io.show.imshow(image)
```

```python
dataset_path = dataset.set_dataset_path()
num_keypoints = 3000
```
![Sample Image](https://github.com/snmahsa/myrep/blob/main/set_dataset_path.png)

```python
engine.search(image, num_keypoints, dataset_path)
```
initialize engine ...

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

extract_features

...

[INFO] Serializing Features...

[INFO] Loading Features...

Searching ...

Folder : O


![Sample Image](https://github.com/snmahsa/myrep/blob/main/result.png)

## Contributing

Contributions to PicSimSearch are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository: https://github.com/snmahsa/PicSimSearch.
License

This project is licensed under the MIT License. See the LICENSE file for more information.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.