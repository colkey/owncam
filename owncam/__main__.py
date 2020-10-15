import cv2


def main():
    capture = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    while(True):
        ret, frame = capture.read()
        cv2.imshow('ownCam', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
