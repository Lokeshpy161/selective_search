import cv2

# Load the image
image_path = 'photo-1438761681033-6461ffad8d80.jpeg'
image = cv2.imread(image_path)

# Create a Selective Search segmentation object
ss = cv2.ximgproc.segmentation. createSelectiveSearchSegmentation()

# Set the input image
ss.setBaseImage(image)

# Perform selective search
ss.switchToSelectiveSearchFast()
rects = ss.process()

# Display the top 'num_proposals' regions
num_proposals = 100
for i, rect in enumerate(rects[:num_proposals]):
    x, y, w, h = rect
    proposal = image[y:y+h, x:x+w]
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1)

# Display the image with regions highlighted
cv2.imshow('Selective Search', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
