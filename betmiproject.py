import cv2

# read the image
def count_pasta(path):
    image = cv2.imread(path)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply binary thresholding
    ret, thresh = cv2.threshold(img_gray, 140, 255, cv2.THRESH_BINARY)

    # draw contours on the original image

    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    # initialize counters
    spaghettis = []
    pasta = []
    grains = []

    # for each contour detected, calculate contour perimeter and classify object
    for object in contours:
        arclen = cv2.arcLength(object, closed = False)
        if arclen > 200:
            spaghettis.append(object)
        elif arclen > 100:
            pasta.append(object)
        elif arclen > 10:
            grains.append(object)

    # make images, highlighting the desired pasta
    new = image.copy()
    cv2.drawContours(image=new, contours=spaghettis, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.imwrite('spaghettis.jpg', new)

    new = image.copy()
    cv2.drawContours(image=new, contours=pasta, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.imwrite('pasta.jpg', new)

    new = image.copy()
    cv2.drawContours(image=new, contours=grains, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.imwrite('grains.jpg', new)
    return (len(spaghettis), len(pasta), len(grains))

print(count_pasta("./OriginalImage.tif"))
