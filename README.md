# LHL_final_project
## Squat Classification with 3DCNN

#### <ins>Project Overview</ins>:

Using video data of squats in 7 different classes: 
    - Good
    - Rounded Back
    - Warped Back
    - Collapsed Knees
    - Knees Forward
    - Head Tilted
    - Shallow

Utilize a 3D Convolutional Neural Network to classify videos from frame images.

Video dataset can be downloaded from [this link](http://hi.cs.waseda.ac.jp/~ogata/Dataset.html)

#### <ins>Packages/tools used</ins>:
  * Google Colab
  * Google Drive
  * tensorflow/keras 
  * os
  * cv2
  * numpy
  * pandas
  * sklearn
  * matplotlib

#### <ins>Directories</ins>:

Data:
 * Pose_Dataset: Annotated 3D pose vectors for each video, separated into classes


---


Functions: .py file containing helper functions for processing data
  * create_data(input_dir): takes input_dir as data path and parses videos within
  * frames_extraction(video_path): used inside create_data to generate frames
  * get_classes(test_values, predictions, class_names): gets class names for test and prediction data


---


Notebook: Colab Notebook used for data processing and model training


---

Presentation: Presentation slides for intended use-case and results


---


