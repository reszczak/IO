import cv2 as cv
import time

def downloadDataFromCameras(duration_seconds=86400, output_folder='./', i=0):

    cap = cv.VideoCapture(0)

    start_time = time.time()
    end_time = start_time + duration_seconds

    while time.time() < end_time:

        fourcc = cv.VideoWriter_fourcc(*'XVID')
        output_filename = f'{output_folder}/Day{i}.avi'
        out = cv.VideoWriter(output_filename, fourcc, 20.0, (640, 480))

        while time.time() < end_time:
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            # frame = cv.flip(frame, 0)

            out.write(frame)
            cv.imshow('frame', frame)


        out.release()



    cap.release()
    cv.destroyAllWindows()
