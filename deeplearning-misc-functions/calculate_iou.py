# Simple and tested function created from Simplified_SingleBoundingBox Mentor Session 
def IOU(y_true, y_pred):
	"""
    Calculate Intersection over Union (IoU) between two ground truth and predicted values for bounding boxes.
    
    Parameters:
        y_true : The cordinates of boxes that is ground truth
        y_pred : The cordinates of boxes that is predicted value
        	
    Returns:
        float: Intersection over Union (IoU) score.
    """

    intersections = 0
    unions = 0
    # set the types so we are sure what type we are using

    gt = y_true
    pred = y_pred
    
    # Compute interection of predicted (pred) and ground truth (gt) bounding boxes
    diff_width = np.minimum(gt[:,0] + gt[:,2], pred[:,0] + pred[:,2]) - np.maximum(gt[:,0], pred[:,0])
    diff_height = np.minimum(gt[:,1] + gt[:,3], pred[:,1] + pred[:,3]) - np.maximum(gt[:,1], pred[:,1])
    intersection = diff_width * diff_height

    # Compute union
    area_gt = gt[:,2] * gt[:,3]
    area_pred = pred[:,2] * pred[:,3]
    union = area_gt + area_pred - intersection

    # Compute intersection and union over multiple boxes
    for j, _ in enumerate(union):
        if union[j] > 0 and intersection[j] > 0 and union[j] >= intersection[j]:
            intersections += intersection[j]
            unions += union[j]

    # Compute IOU. Use epsilon to prevent division by zero
    iou = np.round(intersections / (unions + tensorflow.keras.backend.epsilon()), 4)
    # This must match the type used in py_func
    iou = iou.astype(np.float32)
    
    return iou

# will integrate it to the compiler to check the iou score at every epoch
def IoU(y_true, y_pred):
    iou = tensorflow.py_function(IOU, [y_true, y_pred], Tout=tensorflow.float32)
    return iou

# Compile the model
import tensorflow
model.compile(loss="mean_squared_error", optimizer="adam", metrics=[IoU]) # Regression loss is MSE

# Use earlystopping
callback = tensorflow.keras.callbacks.EarlyStopping(monitor='val_IoU', patience=5, min_delta=0.01)

# Fit the model
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32, callbacks=[callback])

# ------------------------------------------------------------------------------------------------------------

# Simple and untested function created from chatgpt 
def calculate_iou(box1, box2):
    """
    Calculate Intersection over Union (IoU) between two bounding boxes.

    Parameters:
        box1 (tuple): Tuple containing (x1, y1, x2, y2) coordinates of the first bounding box.
        box2 (tuple): Tuple containing (x1, y1, x2, y2) coordinates of the second bounding box.
		
		Bounding Box 1 (box1):

					   It is represented by a tuple containing four values: (x1, y1, x2, y2).
					   (x1, y1) represents the coordinates of the top-left corner of the bounding box.
					   (x2, y2) represents the coordinates of the bottom-right corner of the bounding box.
					   This box contains information about the position and size of an object in an image.
		
    Returns:
        float: Intersection over Union (IoU) score.
    """
    # Extract coordinates of each bounding box
    x1_1, y1_1, x2_1, y2_1 = box1
    x1_2, y1_2, x2_2, y2_2 = box2

    # Calculate the coordinates of the intersection rectangle
    x_left = max(x1_1, x1_2)
    y_top = max(y1_1, y1_2)
    x_right = min(x2_1, x2_2)
    y_bottom = min(y2_1, y2_2)

    # If the boxes do not intersect, return 0
    if x_right < x_left or y_bottom < y_top:
        return 0.0

    # Calculate intersection area
    intersection_area = (x_right - x_left) * (y_bottom - y_top)

    # Calculate area of each bounding box
    box1_area = (x2_1 - x1_1) * (y2_1 - y1_1)
    box2_area = (x2_2 - x1_2) * (y2_2 - y1_2)

    # Calculate Union area
    union_area = box1_area + box2_area - intersection_area

    # Calculate IoU
    iou = intersection_area / union_area

    return iou

box1 = (10, 10, 50, 50)
box2 = (30, 30, 70, 70)

iou_score = calculate_iou(box1, box2)
print("Intersection over Union (IoU) score:", iou_score)
