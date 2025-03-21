import cv2
import mediapipe as mp


video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    if not check:
        print("não capturou a camera")
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks
    h,w,_ = img.shape
    pontos = []
    if handsPoints:
        for points in handsPoints:
            mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS)
            for id, cord in enumerate(points.landmark):
                cx,cy = int(cord.x * w), int(cord.y * h)
                pontos.append((cx,cy))
        
        fingers = [8,12,16,20]
        contador = 0
        if points:
            if pontos[4] < pontos[2]:
                contador+=1
            for x in fingers:
                if pontos[x][1] < pontos[x-2][1]:
                    contador+=1
                    
        cv2.putText(img, str(contador), (200,100), cv2.FONT_HERSHEY_SIMPLEX,4,(255,0,0),5)

    
    cv2.imshow("Imagem", img)
    cv2.waitKey(1)