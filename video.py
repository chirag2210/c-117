import os
import cv2
path = 'C:/Users/sonud/Downloads/PRo-117/images'
Images = []

for file in os.listdir(path):
    name, extension = os.path.splitext(file)

    if extension.lower() == '.jpg':   
        file_name = os.path.join(path, file)   
        print(file_name)   
        Images.append(file_name)


count = len(Images)
frame = cv2.imread(Images[0])
height, width, channels = frame.shape
size = (width, height)

print(size)
 
video_name = 'Project.avi'
fourcc = cv2.VideoWriter_fourcc(*'MJPG') 
fps = 0.5
Size = size
out = cv2.VideoWriter(video_name, fourcc, fps, Size)
 
for i in range(count):

    img = cv2.imread(Images[i])
    out.write(img)

print("Done")

out.release()
