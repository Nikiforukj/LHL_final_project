#  Creating frames from videos
 
def frames_extraction(video_path):
    """
    Parse video file and create individual frame images

    Parameters
    ----------
    video_path : str
        The file location of the video

    Returns
    -------
    frames_list
        a list of images parsed from video
    """
    frames_list = []
     
    vidObj = cv2.VideoCapture(video_path)
    # Used as counter variable 
    count = 1
 
    while count <= seq_len: 
         
        success, image = vidObj.read() 
        if success:
            image = cv2.resize(image, (img_height, img_width))
            frames_list.append(image)
            count += 1
        else:
            print("Defected frame")
            break
 
            
    return frames_list
 
def create_data(input_dir):
    """
    Create vectorized feature and label data from videos

    Parameters
    ----------
    input_dir : str
        Directory path to data

    Returns
    -------
    X
        Array of image feature data
    Y
        Array of label data
    """  
    X = []
    Y = []
     
    classes_list = os.listdir(input_dir)
     
    for c in classes_list:
        print(c)
        files_list = os.listdir(os.path.join(input_dir, c))
        for f in files_list:
           frames = frames_extraction(os.path.join(os.path.join(input_dir, c), f))
           if len(frames) == seq_len:
                X.append(frames)
             
                y = [0]*len(classes)
                y[classes.index(c)] = 1
                Y.append(y)
     
    X = np.asarray(X)
    Y = np.asarray(Y)
    return X, Y


# generate labels for predictions
def get_classes(test_values, predictions):
    """
    Generate actual and predicted labels from model results

    Parameters
    ----------
    test_values : array
        array of actual test values
    predictions : array
        array of predicted values

    Returns
    -------
    actual
        a list of actual labels for each index
    predicted
        a list of predicted labels for each index
    """
    actual = []
    predicted = []
    for i in range(len(test_values)):
      v = classes[np.argmax(test_values[i])]
      actual.append(v)
    for i in range(len(predictions)):
      p = classes[np.argmax(predictions[i])]
      predicted.append(p)
    return actual, predicted