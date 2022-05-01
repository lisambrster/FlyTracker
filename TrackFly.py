

# Need to detect the fly
# (w,h) 608x600
# < 200 is the ruler
# start at frame 200
# start point is here: (273,61)

# threshold of 100
# connected components
# biggest one
import cv2
import numpy as np

for iframe in range(200,401):
    num_str = '%d' % iframe
    fname = 'Frames/frame' + num_str + '.jpg'
    image = cv2.imread(fname,0)
    #print('image loaded ',image.shape)
    # need to crop
    gray = image[30:, 230:]
    #cv2.imshow('Original image', gray)
    #cv2.waitKey(0)
    print('image cropped ', gray.shape)

    ind = np.where(gray < 110)
    thresh = np.zeros(gray.shape,dtype=np.uint8)
    thresh[ind] = 255

    #out_name =  'OutFrames/cropbinary_' + num_str + '.png'
    #cv2.imwrite(out_name,thresh)
    #cv2.imshow('thresh image', thresh)
    #cv2.waitKey(0)

    connectivity = 8
    # Perform the operation
    labels = np.zeros(gray.shape, dtype=np.uint16)
    cv2.connectedComponents(thresh, labels, connectivity, cv2.CV_16U) #

    unique, counts = np.unique(labels, return_counts=True)
    print(unique, counts)

    max_size_label = -1
    max_size = 0
    for ilabel in unique:
        area = counts[ilabel]
        ind = np.where(labels == ilabel)
        a = len(ind[0])
        print(ilabel,area,a)
        if (area > max_size) and (area < 3000):
            max_size = area
            max_size_label = ilabel
    print('max area ', max_size)
    print('at label ', max_size_label)
    # compute centroid from ind (or use cv2 cc with stats
    # print('with centroid ',centroids[ilabel])
    # make image with just this component
    ind = np.where(labels == max_size_label)
    a = len(ind[0])
    #print(a)
    out_img = np.zeros(labels.shape,dtype=np.uint8)
    out_img[ind] = 255

    # save it in sequence
    out_name =  'OutFrames/frame' + num_str + '.png'
    cv2.imwrite(out_name,out_img)



