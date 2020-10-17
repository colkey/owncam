import cv2
import json

config = json.load(open('setting.json', 'r'))


def main():
    capture = cv2.VideoCapture(config['DEVICE_ID'], cv2.CAP_DSHOW)

    while(capture.isOpened()):
        ret, frame = processor(*capture.read())
        if ret:
            cv2.imshow('ownCam', frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


def processor(ret, frame):
    if not ret:
        return ret, frame

    FLIP_LR = 1
    frame = cv2.flip(frame, FLIP_LR)

    return ret, frame


if __name__ == "__main__":
    main()
