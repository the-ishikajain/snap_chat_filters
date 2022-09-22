import cv2
import cvzone
#bg = cv2.imread('jkr.png')
#filter = cv2.imread('beard.png',cv2.IMREAD_UNCHANGED)
#overlay=cvzone.overlayPNG(bg , filter , [100,100])
#cv2.imshow('snap dead', overlay )
#cv2.waitKey(0)
cap=cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
y=input("ENTER NAME OF FILTER YOU WANT TO USE : ")
if y=='p':
    overlay=cv2.imread('pirate.png',cv2.IMREAD_UNCHANGED)
    while True:
        _, frame=cap.read()
        grey_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=cascade.detectMultiScale(grey_scale)
        for(x , y, w, h) in faces:
            #cv2.rectangle(frame, ( x , y ) , ( x+w , y+h ) ,(0 , 255 , 0) , 2)
            #overlay_resize=cv2.resize(overlay, (w,h))
            overlay_resize = cv2.resize(overlay, (int(w * 1.5), int(1.5 * h)))
            #frame=cvzone.overlayPNG(frame,overlay_resize,[x, y])
            frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])
        cv2.imshow('SNAP DEAD',frame)
        if cv2.waitKey(10) == ord('q'):
            break
elif y=='st':
    overlay=cv2.imread('star.png',cv2.IMREAD_UNCHANGED)
    while True:
        _, frame=cap.read()
        grey_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=cascade.detectMultiScale(grey_scale)
        for(x , y, w, h) in faces:
            overlay_resize = cv2.resize(overlay, (w, h))
            frame = cvzone.overlayPNG(frame, overlay_resize, [x, y])
        cv2.imshow('SNAP DEAD',frame)
        if cv2.waitKey(10) == ord('q'):
            break
elif y=='sun':
    overlay=cv2.imread('sunglass.png',cv2.IMREAD_UNCHANGED)
    while True:
        _, frame=cap.read()
        grey_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=cascade.detectMultiScale(grey_scale)
        for(x , y, w, h) in faces:
            overlay_resize = cv2.resize(overlay, (w, h))
            frame = cvzone.overlayPNG(frame, overlay_resize, [x, y])
        cv2.imshow('SNAP DEAD',frame)
        if cv2.waitKey(10) == ord('q'):
            break
elif y=='n':
    overlay=cv2.imread('native.png',cv2.IMREAD_UNCHANGED)
    while True:
        _, frame=cap.read()
        grey_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=cascade.detectMultiScale(grey_scale)
        for(x , y, w, h) in faces:
            overlay_resize = cv2.resize(overlay, (int(w * 1.5), int(1.5 * h)))
            frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])
        cv2.imshow('SNAP DEAD',frame)
        if cv2.waitKey(10) == ord('q'):
            break
elif y=='b':
    overlay=cv2.imread('beard.png',cv2.IMREAD_UNCHANGED)
    while True:
        _, frame=cap.read()
        grey_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=cascade.detectMultiScale(grey_scale)
        for(x , y, w, h) in faces:
            overlay_resize = cv2.resize(overlay, (int(w * 1.5), int(1.5 * h)))
            frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])
        cv2.imshow('SNAP DEAD',frame)
        if cv2.waitKey(10) == ord('q'):
            break
else:
        overlay=cv2.imread('cool.png',cv2.IMREAD_UNCHANGED)
        while True:
             _, frame=cap.read()
             grey_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
             faces=cascade.detectMultiScale(grey_scale)
             for(x , y, w, h) in faces:
                 overlay_resize = cv2.resize(overlay, (int(w * 1.5), int(1.5 * h)))
                 frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])
             cv2.imshow('SNAP DEAD',frame)
             if cv2.waitKey(10) == ord('q'):
                 break