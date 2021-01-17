import cv2 as cv

image = cv.imread('Resources/Photos/cats_2.jpg')

rect1StartPos = (image.shape[1]//2-40,image.shape[0]//2-100)
rect1EndPos = (image.shape[1]//2+100,image.shape[0]//2+40)

cv.rectangle(
    image,
    rect1StartPos,
    rect1EndPos,
    (0,0,255),
    thickness=2
)
cv.putText(
    image,
    'Cat',
    tuple(x+10 for x in rect1EndPos),
    cv.FONT_HERSHEY_DUPLEX,
    0.5,
    (0,0,255),
    thickness=1
)

rect2StartPos = (image.shape[1]//2-160,image.shape[0]//2-140)
rect2EndPos = (image.shape[1]//2-20,image.shape[0]//2)

cv.rectangle(
    image,
    rect2StartPos,
    rect2EndPos,
    (0,0,255),
    thickness=2
)
cv.putText(
    image,
    'Cat',
    tuple(x+10 for x in rect2EndPos),
    cv.FONT_HERSHEY_DUPLEX,
    0.5,
    (0,0,255),
    thickness=1
)

print(image)

cv.imshow('Cats', image)

cv.waitKey(0)
