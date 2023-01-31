import cv2
import numpy as np
import imutils
from pypylon import pylon
import math
from math import pi
import pyautogui
import pygetwindow
import time

def start_blaumowe():

    print("Program is starting...")


    #######################################       ABRIR VÍDEO        #######################################################


    logo = cv2.imread('PLACA/_placa.png')
    size= 150

    logo = cv2.resize(logo, (size, size))

    img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    ret, maskk = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)


    ##############################       DEFINIR TAMANHO DA FRAME DO VÍDEO        ##########################################


    def empty():

        pass


    ########       CRIAÇÃO DE FUNÇAO PARA OBTER CONTORNOS DE APENAS DOIS PONTOS CENTRAIS DOS DIGITOS          ##############


    def drawline(frame,pt1,pt2,color,thickness=1,style='dotted',gap=20):
        dist =((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**.5
        pts= []
        for i in  np.arange(0,dist,gap):
            r=i/dist
            x=int((pt1[0]*(1-r)+pt2[0]*r)+.5)
            y=int((pt1[1]*(1-r)+pt2[1]*r)+.5)
            p = (x,y)
            pts.append(p)

        if style=='dotted':
            s = pts[0]
            e = pts[0]
            i = 0
            for p in pts:
                s = e
                e = p
                if i % 2 == 1:
                    cv2.line(frame, s, e, color, thickness)
                i += 1

        else:
            for p in pts:
                cv2.line(frame, p, thickness, color, -1)

    def drawpoly(frame,pts,color,thickness=1,style='dotted'):
        s=pts[0]
        e=pts[0]
        pts.append(pts.pop(0))
        for p in pts:
            s=e
            e=p
            drawline(frame,s,e,color,thickness,style)

    def drawrect(frame,pt1,pt2,color,thickness=1,style='dotted'):
        pts = [pt1,(pt2[0],pt1[1]),pt2,(pt1[0],pt2[1])]
        drawpoly(frame,pts,color,thickness,style)


    def draw_text(frame, text,
              font=cv2.FONT_HERSHEY_PLAIN,
              pos=(10, 0),
              font_scale=1,
              font_thickness=2,
              text_color=(0, 0, 0),
              text_color_bg=(0, 255, 255)
              ):

        x, y = pos
        text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
        text_w, text_h = text_size
        cv2.rectangle(frame, pos, (x + text_w, y + text_h), text_color_bg, -1)
        cv2.putText(frame, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)

        return text_size


    def draw_text(frame, text,
              font=cv2.FONT_HERSHEY_PLAIN,
              pos=(10, 0),
              font_scale=1,
              font_thickness=2,
              text_color=(0, 0, 0),
              text_color_bg=(0, 255, 255)
              ):

        x, y = pos
        text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
        text_w, text_h = text_size
        cv2.rectangle(frame, pos, (x + text_w, y + text_h), text_color_bg, -1)
        cv2.putText(frame, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)

        return text_size


    def getContours(ROI_digitos, frame):

        global T

        contours, hierarchy = cv2.findContours(ROI_digitos, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        T = []

        cv2.putText(Box, "ANGULO = ", (10, 365), 1, 2.25, (192, 192, 192), 2)

        for cnt in contours:

                area = cv2.contourArea(cnt)

                AreaMin = 50 #cv2.getTrackbarPos("AreaMin", "Parameters")

                AreaMax = 200 #cv2.getTrackbarPos("AreaMax", "Parameters")

                peri = cv2.arcLength(cnt, True)
                peri = round(peri, 4)

                PeriMin = 20

                PeriMax = 40

                approx = cv2.approxPolyDP(cnt, 0.01 * peri, True)

                if (AreaMin < area < AreaMax) & (5 < len(approx) < 30) & (PeriMin < peri < PeriMax):

                    M = cv2.moments(cnt)

                    if M != 0:

                        cx = int(M["m10"] / M["m00"]) + 450
                        cy = int(M["m01"] / M["m00"]) + 50

                        #cv2.circle(frame, (cx, cy), 1, (255, 0, 0), -1)

                        T.append([cx, cy])
                        #print(T)

                        if len(T) == 2:

                            ponto_1 = T[0]
                            ponto_2 = T[1]


                            cv2.line(frame, ponto_1, ponto_2, (255, 255, 255), 2)

                            ponto_inicio_reta_h = [330, 547]
                            ponto_final_reta_h = [1086, 279]

                            if (ponto_2[0] != ponto_1[0]):

                                m1 = (ponto_final_reta_h[1] - ponto_inicio_reta_h[1]) / (ponto_final_reta_h[0] - ponto_inicio_reta_h[0])  # (289-557) / (1086-330)
                                m2 = (ponto_2[1] - ponto_1[1]) / (ponto_2[0] - ponto_1[0])

                                angle_rad = (math.atan((m1 - m2) / (1 + (m1 * m2))))  # (math.atan(m1)-math.atan(m2))
                                angle_deg = angle_rad * 180 / pi
                                #print(angle_deg)
                                cv2.putText(Box, "         {}".format(int(angle_deg)), (40, 365), 1, 2.25, (192, 192, 192), 2)

                                if -4 < angle_deg < -2:

                                    cv2.circle(Box, (135, 110), 33, (0, 255, 255), -2)

                                elif -2 < angle_deg < 2:

                                    cv2.circle(Box, (225, 110), 33, (0, 255, 0), -2)

                                elif 2 < angle_deg < 4:

                                    cv2.circle(Box, (135, 110), 33, (0, 255, 255), -2)

                                else:

                                    cv2.circle(Box, (45, 110), 33, (0, 0, 255), -2)

                            else:

                                print("A abcissa dos pontos detetados são iguais! O cálculo da inclinação não é possível!")

                        elif len(T) == 3:

                            ponto_1 = T[0]
                            ponto_2 = T[1]
                            ponto_3 = T[2]


                            cv2.line(frame, ponto_1, ponto_3, (255, 255, 255), 2)

                            ponto_inicio_reta_h = [330, 547]
                            ponto_final_reta_h = [1086, 279]

                            if (ponto_3[0] != ponto_1[0]):

                                m1 = (ponto_final_reta_h[1] - ponto_inicio_reta_h[1]) / (ponto_final_reta_h[0] - ponto_inicio_reta_h[0])
                                m2 = (ponto_3[1] - ponto_1[1]) / (ponto_3[0] - ponto_1[0])

                                angle_rad = (math.atan((m1 - m2) / (1 + (m1 * m2))))
                                angle_deg = angle_rad * 180 / pi
                                #print(angle_deg)

                                cv2.putText(Box, "         {}".format(int(angle_deg)), (40, 365), 1, 2.25, (192, 192, 192), 2)

                                if -4 < angle_deg < -2:

                                    cv2.circle(Box, (135, 110), 33, (0, 255, 255), -2)

                                elif -2 < angle_deg < 2:

                                    cv2.circle(Box, (225, 110), 33, (0, 255, 0), -2)

                                elif 2 < angle_deg < 2:

                                    cv2.circle(Box, (135, 110), 33, (0, 255, 255), -2)

                                else:

                                    cv2.circle(Box, (45, 110), 33, (0, 0, 255), -2)

                            else:

                                print("A abcissa dos pontos detetados são iguais! O cálculo da inclinação não é possível!")

                        elif len(T) == 4:

                            ponto_1 = T[0]
                            ponto_2 = T[1]
                            ponto_3 = T[2]
                            ponto_4 = T[3]


                            cv2.line(frame, ponto_1, ponto_4, (255, 255, 255), 2)

                            ponto_inicio_reta_h = [330, 547]
                            ponto_final_reta_h = [1086, 279]

                            if (ponto_4[0] != ponto_1[0]):

                                m1 = (ponto_final_reta_h[1] - ponto_inicio_reta_h[1]) / (ponto_final_reta_h[0] - ponto_inicio_reta_h[0])
                                m2 = (ponto_4[1] - ponto_1[1]) / (ponto_4[0] - ponto_1[0])

                                angle_rad = (math.atan((m1 - m2) / (1 + (m1 * m2))))
                                angle_deg = angle_rad * 180 / pi
                                #print(angle_deg)

                                cv2.putText(Box, "         {}".format(int(angle_deg)), (40, 365), 1, 2.25, (192, 192, 192), 2)

                                if -4 < angle_deg < -2:

                                    cv2.circle(Box, (135, 110), 33, (0, 255, 255), -2)

                                elif -2 < angle_deg < 2:

                                    cv2.circle(Box, (225, 110), 33, (0, 255, 0), -2)

                                elif 2 < angle_deg < 4:

                                    cv2.circle(Box, (135, 110), 33, (0, 255, 255), -2)

                                else:

                                    cv2.circle(Box, (45, 110), 33, (0, 0, 255), -2)

                            else:

                                print("A abcissa dos pontos detetados são iguais! O cálculo da inclinação não é possível!")

                        else:

                            print(len(T), "- Out of Range")

                    else:

                        cx = 0
                        cy = 0
                        T = 0


    #################                        ÍNICIO LOOP DO VIDEO                                       ####################


    # conecting to the first available camera

    camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

    # Grabing Continusely (video) with minimal delay

    camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    converter = pylon.ImageFormatConverter()

    # converting to opencv bgr format

    converter.OutputPixelFormat = pylon.PixelType_BGR8packed
    converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    T = []

    while camera.IsGrabbing():

        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        if grabResult.GrabSucceeded():

            image = converter.Convert(grabResult)
            img = image.GetArray()
            width = 1280
            height = 960

            dim = (width, height)

            frame = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


    ############                   DESENHO RETÂNGULO COM INFORMAÇÕES DO ALVO E DIGITOS                       ###############


            Box = cv2.rectangle(frame, (0, 0), (270, 320), (0, 0, 0), -1)
            cv2.putText(Box, 'Digitos:', (10, 50), 1, 3, (192, 192, 192), 2)
            cv2.putText(Box, 'Alvo:', (10, 200), 1, 3, (192, 192, 192), 2)


            Box = cv2.rectangle(frame, (0, 960), (335, 700), (192, 192, 192), -1)
            cv2.putText(Box, ' INDICACOES PARA ', (0, 735), 1, 2, (0, 0, 0), 2)
            cv2.putText(Box, ' MOVER PLACA LED: ', (0, 775), 1, 2, (0, 0, 0), 2)


            cv2.circle(frame, (225, 110), 35, (192, 192, 192), -2)
            cv2.circle(Box, (225, 260), 35, (192, 192, 192), -2)
            cv2.circle(frame, (225, 110), 35, (96, 96, 96), 4)
            cv2.circle(Box, (225, 260), 35, (96, 96, 96), 4)
            cv2.circle(Box, (45, 260), 35, (192, 192, 192), -2)
            cv2.circle(Box, (45, 110), 35, (192, 192, 192), -2)
            cv2.circle(Box, (135, 260), 35, (192, 192, 192), -2)
            cv2.circle(Box, (135, 110), 35, (192, 192, 192), -2)
            cv2.circle(Box, (45, 260), 35, (96, 96, 96), 4)
            cv2.circle(Box, (45, 110), 35, (96, 96, 96), 4)
            cv2.circle(Box, (135, 260), 35, (96, 96, 96), 4)
            cv2.circle(Box, (135, 110), 35, (96, 96, 96), 4)


        #################                    DESENHO ZONA LIMITE DE CENTRAGEM DO ALVO                   ####################

            zona_limite_posicionamento_amarelo = np.array([[679, 416], [664, 421], [669, 436], [684, 431]], np.int32)
            cv2.polylines(frame, [zona_limite_posicionamento_amarelo], True, (0, 255, 255))

            zona_limite_posicionamento_vermelho = np.array([[688, 397], [643, 411], [660, 455], [704, 440]], np.int32)
            cv2.polylines(frame, [zona_limite_posicionamento_vermelho], True, (0, 0, 255))


            #s = (450, 255)
            #e = (900, 550)
            #drawrect(frame, s, e, (255, 128, 0), 1, 'dotted')


        #################                   CONFIGURAÇÃO MÁSCARA PARA DETEÇÃO DE ALVO                   ####################

            mask_roi = np.zeros(frame.shape, dtype=np.uint8)
            x, y = 674, 506
            cv2.circle(mask_roi, (x, y), 225, (255, 255, 255), -1)

            ROI = cv2.bitwise_and(frame, mask_roi)

            mask_roi = cv2.cvtColor(mask_roi, cv2.COLOR_BGR2GRAY)
            x, y, w, h = cv2.boundingRect(mask_roi)
            result = ROI[y:y + h, x:x + w]
            mask_roi = mask_roi[y:y + h, x:x + w]
            result[mask_roi == 0] = (0, 0, 0)

            median = cv2.medianBlur(result, 1)
            hsv = cv2.cvtColor(median, cv2.COLOR_BGR2HSV)
            #cv2.imshow("hsv", hsv)

            lower_red = np.array([0, 0, 255]) # 0, 0, 255
            upper_red = np.array([180, 254, 255]) # 153, 153, 255

            mask_1 = cv2.inRange(hsv, lower_red, upper_red)
            #cv2.imshow("mask1",mask_1)
            mask_2 = cv2.dilate(mask_1, None, iterations=6)
            # cv2.imshow("mask2", mask_2)
            mask_3 = cv2.erode(mask_2, None, iterations=4)
            # cv2.imshow("mask_3", mask_3)
            #ROI = mask_3[250:600, 382:982]
            #cv2.imshow("ROI", ROI)


        ################                    RECOLHA DE CONTORNOS PRESENTES NA MÁSCARA                   ####################


            contornos_red = cv2.findContours(mask_3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contornos_red = imutils.grab_contours(contornos_red)


            if len(contornos_red) >0:


            ########                    RESTRIÇÃO PARA DETEÇÃO DO MAIOR CIRCULO PRESENTE NA MÁSCARA                #############


                red_area = max(contornos_red, key=cv2.contourArea)

                ((x, y), radius) = cv2.minEnclosingCircle(red_area)


            ####         DETERMINAÇÃO DO CENTRO DO MAIOR CIRCULO DETETADO E DAS SUAS COORDENADAS EM XX E YY            #########


                M = cv2.moments(red_area)

                if (M["m00"]) != 0:

                    cx = int(M["m10"] / M["m00"]) + 449
                    cy = int(M["m01"] / M["m00"]) + 281

                else:

                    cx = 0
                    cy = 0


            ########                RESTRIÇÃO PARA DETEÇÃO APENAS DO ALVO DO LASER ATRAVÉS DO SEU TAMANHO             ##########


                if 20 < radius < 27:

                    cv2.circle(frame, (cx, cy), 2, (0, 255, 0), -2)


            ###      CONJUNTO DE RESTRIÇÕES PARA DETETAR SE O ALVO SE ENCONTRA DENTRO DA ZONA LIMITE DE POSICIONAMENTO      ####

                    if cx < 674 and cy < 418:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (195, 825), (195, 785), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (125, 935), (125, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (247, 885), (320, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (15, 800), (80, 800), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)


                    elif cx < 674 and cy > 418:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (195, 785), (195, 825), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (125, 885), (125, 935), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (247, 885), (320, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (15, 800), (80, 800), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)


                    elif cx > 674 and cy < 418:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (195, 825), (195, 785), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (125, 935), (125, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (320, 885), (247, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (80, 800), (15, 800), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)


                    elif cx > 674 and cy > 418:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (195, 785), (195, 825), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (125, 885), (125, 935), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (320, 885), (247, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (80, 800), (15, 800), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)


                    elif cx > 674 and cy == 418:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (320, 885), (247, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (80, 800), (15, 800), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)

                    elif cx < 674 and cy == 418:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (247, 885), (320, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (15, 800), (80, 800), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)


                    elif cx == 674 and cy > 418:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (195, 785), (195, 825), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (125, 885), (125, 935), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)


                    elif cx == 674 and cy < 418:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (195, 825), (195, 785), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (125, 935), (125, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)


                    if cy < (-0.3157894737 * cx + 614):

                        cv2.circle(Box, (45, 260), 33, (0, 0, 255), -2)


                    elif cy < (2.666666667 * cx - 1438):

                        cv2.circle(Box, (45, 260), 33, (0, 0, 255), -2)


                    elif cy > (2.666666667 * cx - 1305):

                        cv2.circle(Box, (45, 260), 33, (0, 0, 255), -2)


                    elif cy > (-0.3157894737 * cx + 663):

                        cv2.circle(Box, (45, 260), 33, (0, 0, 255), -2)


                    elif (-0.3157894737 * cx + 614) < cy < (-0.3157894737 * cx + 631):

                        cv2.circle(Box, (135, 260), 33, (0, 255, 255), -2)


                    elif (2.666666667 * cx - 1438) < cy < (2.666666667 * cx - 1393):

                        cv2.circle(Box, (135, 260), 33, (0, 255, 255), -2)


                    elif (2.666666667 * cx - 1349) < cy < (2.666666667 * cx - 1305):

                        cv2.circle(Box, (135, 260), 33, (0, 255, 255), -2)


                    elif (-0.3157894737 * cx + 647) < cy < (-0.3157894737 * cx + 663):

                        cv2.circle(Box, (135, 260), 33, (0, 255, 255), -2)


                    else:

                        cv2.circle(frame, (225, 260), 33, (0, 255, 0), -2)
                        Box = cv2.rectangle(frame, (1280, 960), (530, 850), (0, 255, 255), -1)
                        draw_text(frame, " O ALVO ESTA CENTRADO E A COORDENADAS ", font_scale=2, pos=(540, 880), text_color_bg=(0, 255, 255))
                        draw_text(frame, " DO CENTRO SAO: x:{} , y:{} ".format(cx, cy), font_scale=2, pos=(540, 915), text_color_bg=(0, 255, 255))



                ######               CRIAÇÃO DA MÁSCARA PARA EXTRAÇÃO DOS CONTORNOS DOS PONTOS DOS DÍGITOS               ###############


            frameBlur = cv2.GaussianBlur(frame, (21, 21), 1)
            frameHSV = cv2.cvtColor(frameBlur, cv2.COLOR_BGR2HSV)

            threshold1 = 160 #cv2.getTrackbarPos("Threshold1", "Parameters")
            threshold2 = 80 #cv2.getTrackbarPos("Threshold2", "Parameters")

            frameCanny = cv2.Canny(frameHSV, threshold1, threshold2)
            frameDilate = cv2.dilate(frameCanny, None, iterations=2)
            frameErode = cv2.erode(frameDilate, None, iterations=2)

            ROI_digitos = frameErode[50:250, 450:900]


            #############           CALL-BACK DA FUNÇÃO PARA OBTER OS CONTORNOS DOS PONTOS DOS DÍGITOS            ##################


            getContours(ROI_digitos, frame)


            ################               DISPLAY DA FRAME COM TODAS AS ALTERAÇÕES APLICADAS                    ###################


            cv2.imshow("Video da centragem do laser", frame)


            ################         COMANDO PARA SE O BOTAO ESC FOR PRESSIONADO O PROGRAMA TERMINAR             ###################

            timestr = time.strftime('___%d %m %Y____%H %M %S')

            k = cv2.waitKey(5)
            if k == 13:

                titles = pygetwindow.getAllTitles()

                window = pygetwindow.getWindowsWithTitle('Video da centragem do laser')[0]
                left, top = window.topleft
                right, bottom = window.bottomright
                screenshot = pyautogui.screenshot()
                screenshot = screenshot.crop((left + 10, top + 31, right - 10, bottom - 10))
                screenshot.save('C:/Users/installation/Desktop/Print (56x)/Ajuste_do_Display_e_do_Recetor_COLIMADOR.png')

                break

        grabResult.Release()

    camera.StopGrabbing()
    cv2.destroyAllWindows()

