import cv2
import numpy as np


# Load image 
image = cv2.imread("C:/Users/osuno/Desktop/Open CV/Lesson 6/HW7.py")
h, w = image.shape[:2]

# Load YOLO model
weights_path = "yolov3.weights"        
config_path = "yolov3.cfg"             
names_path = "coco.names"

net = cv2.dnn.readNet(weights_path, config_path)  # (Yolo function)


# Load class names
with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Get output layer names
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]





# Create blob and forward pass

blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

# ---------------------------------------------
# Process detections
# ---------------------------------------------
class_ids = []
confidences = []
boxes = []

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.5:
            center_x = int(detection[0] * w)
            center_y = int(detection[1] * h)
            width = int(detection[2] * w)
            height = int(detection[3] * h)

            x = int(center_x - width / 2)
            y = int(center_y - height / 2)

            boxes.append([x, y, width, height])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Non-max suppression
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# ---------------------------------------------
# Draw boxes
# ---------------------------------------------
for i in indices.flatten():
    x, y, w_box, h_box = boxes[i]
    label = str(classes[class_ids[i]])
    confidence = confidences[i]

    cv2.rectangle(image, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)
    cv2.putText(image, f"{label} {confidence:.2f}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 0), 2)

# ---------------------------------------------
# Show result
# ---------------------------------------------
cv2.imshow("YOLO Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()