import numpy as np
import imutils
import math
from math import pi
import pyautogui
import pygetwindow
import time
import cv2
from pypylon import pylon

def check_up_42():

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


    def getContours(frameDilate, frame):

        global T

        contours, hierarchy = cv2.findContours(ROI_digitos, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        T = []

        cv2.putText(Box, "ANGULO = ", (10, 365), 1, 2.25, (192, 192, 192), 2)

        for cnt in contours:

                area = cv2.contourArea(cnt)

                AreaMin = 100 #cv2.getTrackbarPos("AreaMin", "Parameters")

                AreaMax = 200 #cv2.getTrackbarPos("AreaMax", "Parameters")

                peri = cv2.arcLength(cnt, True)
                peri = round(peri, 4)

                PeriMin = 38

                PeriMax = 50

                approx = cv2.approxPolyDP(cnt, 0.01 * peri, True)

                if (AreaMin < area < AreaMax) & (5 < len(approx) < 15) & (PeriMin < peri < PeriMax):

                    M = cv2.moments(cnt)

                    if M != 0:

                        cx = int(M["m10"] / M["m00"]) + 375
                        cy = int(M["m01"] / M["m00"]) +20

                        #cv2.circle(frame, (cx, cy), 1, (255, 0, 0), -1)

                        T.append([cx, cy])
                        print(T)


                        if len(T) == 2:

                            ponto_1_2 = T[0]
                            ponto_2_2 = T[1]

                            # LINHA2 = np.array([[ponto_1], [ponto_2], ponto_3], np.int32)
                            # cv2.polylines(frame, [LINHA2], isClosed= False, color = (255, 255, 255), thickness = 2)

                            cv2.line(frame, ponto_1_2, ponto_2_2, (255, 255, 255), 2)

                            ponto_inicio_reta_h = [330, 547]
                            ponto_final_reta_h = [1086, 279]

                            if (ponto_2_2[0] != ponto_1_2[0]):

                                #LINHA3 = cv2.line(frame, ponto_inicio_reta_h, ponto_final_reta_h, (255, 255, 255), 1)

                                m1 = (ponto_final_reta_h[1] - ponto_inicio_reta_h[1]) / (ponto_final_reta_h[0] - ponto_inicio_reta_h[0])  # (289-557) / (1086-330)
                                m2 = (ponto_2_2[1] - ponto_1_2[1]) / (ponto_2_2[0] - ponto_1_2[0])

                                angle_rad = (math.atan((m1 - m2) / (1 + (m1 * m2))))  # (math.atan(m1)-math.atan(m2))
                                angle_deg = angle_rad * 180 / pi
                                #print(angle_deg)

                                if -4 < angle_deg < -2:

                                    cv2.circle(Box, (135, 110), 33, (0, 255, 255), -2)

                                elif -2 < angle_deg < 2:

                                    cv2.circle(Box, (225, 110), 33, (0, 255, 0), -2)

                                elif 2 < angle_deg < 4:

                                    cv2.circle(Box, (135, 110), 33, (0, 255, 255), -2)

                                else:

                                    cv2.circle(Box, (45, 110), 33, (0, 0, 255), -2)

                                cv2.putText(Box, "         {}".format(int(angle_deg)), (40, 365), 1, 2.25, (192, 192, 192), 2)

                            else:

                                print("A abcissa dos pontos detetados são iguais! O cálculo da inclinação não é possível!")

                        elif len(T) == 3:

                            ponto_1_3 = T[0]
                            ponto_2_3 = T[1]
                            ponto_3_3 = T[2]

                            # LINHA2 = np.array([[ponto_1], [ponto_2], ponto_3], np.int32)
                            # cv2.polylines(frame, [LINHA2], isClosed= False, color = (255, 255, 255), thickness = 2)

                            cv2.line(frame, ponto_1_3, ponto_2_3, (255, 255, 255), 2)
                            cv2.line(frame, ponto_2_3, ponto_3_3, (255, 255, 255), 2)

                            ponto_inicio_reta_h = [330, 547]
                            ponto_final_reta_h = [1086, 279]

                            if (ponto_3_3[0] != ponto_1_3[0]):

                                #LINHA3 = cv2.line(frame, ponto_inicio_reta_h, ponto_final_reta_h, (255, 255, 255), 1)

                                m1 = (ponto_final_reta_h[1] - ponto_inicio_reta_h[1]) / (ponto_final_reta_h[0] - ponto_inicio_reta_h[0])
                                m2 = (ponto_3_3[1] - ponto_1_3[1]) / (ponto_3_3[0] - ponto_1_3[0])

                                angle_rad = (math.atan((m1 - m2) / (1 + (m1 * m2))))
                                angle_deg = angle_rad * 180 / pi
                                #print(angle_deg)

                                if -4 < angle_deg < -2:

                                    cv2.circle(Box, (135, 110), 33, (0, 255, 255), -2)

                                elif -2 < angle_deg < 2:

                                    cv2.circle(Box, (225, 110), 33, (0, 255, 0), -2)

                                elif 2 < angle_deg < 4:

                                    cv2.circle(Box, (135, 110), 33, (0, 255, 255), -2)

                                else:

                                    cv2.circle(Box, (45, 110), 33, (0, 0, 255), -2)

                                cv2.putText(Box, "         {}".format(int(angle_deg)), (40, 365), 1, 2.25, (192, 192, 192), 2)

                            else:

                                print("A abcissa dos pontos detetados são iguais! O cálculo da inclinação não é possível!")

                        elif len(T) == 4:

                            ponto_1_4 = T[0]
                            ponto_2_4 = T[1]
                            ponto_3_4 = T[2]
                            ponto_4_4 = T[3]

                            # LINHA2 = np.array([[ponto_1], [ponto_2], ponto_3], np.int32)
                            # cv2.polylines(frame, [LINHA2], isClosed= False, color = (255, 255, 255), thickness = 2)

                            cv2.line(frame, ponto_1_4, ponto_2_4, (255, 255, 255), 2)
                            cv2.line(frame, ponto_2_4, ponto_3_4, (255, 255, 255), 2)
                            cv2.line(frame, ponto_3_4, ponto_4_4, (255, 255, 255), 2)

                            ponto_inicio_reta_h = [330, 547]
                            ponto_final_reta_h = [1086, 279]

                            #print(ponto_inicio_reta_h[0])
                            #print(ponto_inicio_reta_h[1])

                            if (ponto_4_4[0] != ponto_1_4[0]):

                                #LINHA3 = cv2.line(frame, ponto_inicio_reta_h, ponto_final_reta_h, (255, 255, 255), 1)

                                m1 = (ponto_final_reta_h[1] - ponto_inicio_reta_h[1]) / (ponto_final_reta_h[0] - ponto_inicio_reta_h[0])
                                m2 = (ponto_4_4[1] - ponto_1_4[1]) / (ponto_4_4[0] - ponto_1_4[0])

                                angle_rad = (math.atan((m1 - m2) / (1 + (m1 * m2))))
                                angle_deg = angle_rad * 180 / pi
                                #print(angle_deg)

                                if -4 < angle_deg < -2:

                                    cv2.circle(Box, (135, 110), 33, (0, 255, 255), -2)

                                elif -2 < angle_deg < 2:

                                    cv2.circle(Box, (225, 110), 33, (0, 255, 0), -2)

                                elif 2 < angle_deg < 4:

                                    cv2.circle(Box, (135, 110), 33, (0, 255, 255), -2)

                                else:

                                    cv2.circle(Box, (45, 110), 33, (0, 0, 255), -2)

                                cv2.putText(Box, "         {}".format(int(angle_deg)), (40, 365), 1, 2.25, (192, 192, 192), 2)

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


            #LINHA3 = cv2.line(frame, ponto_inicio_reta_h, ponto_final_reta_h, (255, 255, 255), 1)
            #ponto_inicio_reta_h = [330, 547]
            #ponto_final_reta_h = [1086, 279]
            #cv2.line(frame, [330, 547], [1086, 279], (255, 255, 255), 1)

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


            s = (450, 255)
            e = (900, 550)
            drawrect(frame, s, e, (255, 128, 0), 1, 'dotted')


        #################                   CONFIGURAÇÃO MÁSCARA PARA DETEÇÃO DE ALVO                   ####################


            median = cv2.medianBlur(frame, 1)
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
            ROI = mask_3[250:600, 382:982]
            #cv2.imshow("ROI", ROI)


        ################                    RECOLHA DE CONTORNOS PRESENTES NA MÁSCARA                   ####################


            contornos_red = cv2.findContours(ROI, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contornos_red = imutils.grab_contours(contornos_red)


            if len(contornos_red) >0:


            ########                    RESTRIÇÃO PARA DETEÇÃO DO MAIOR CIRCULO PRESENTE NA MÁSCARA                #############


                red_area = max(contornos_red, key=cv2.contourArea)

                ((x, y), radius) = cv2.minEnclosingCircle(red_area)
                #print(radius)


            ####         DETERMINAÇÃO DO CENTRO DO MAIOR CIRCULO DETETADO E DAS SUAS COORDENADAS EM XX E YY            #########


                M = cv2.moments(red_area)

                if (M["m00"]) != 0:

                    cx = int(M["m10"] / M["m00"]) + 382
                    cy = int(M["m01"] / M["m00"]) + 250

                else:

                    cx = 0
                    cy = 0


            ########                RESTRIÇÃO PARA DETEÇÃO APENAS DO ALVO DO LASER ATRAVÉS DO SEU TAMANHO             ##########


                if 20 < radius < 25:

                    cv2.circle(frame, (cx, cy), 2, (0, 255, 0), -2)



            ###      CONJUNTO DE RESTRIÇÕES PARA DETETAR SE O ALVO SE ENCONTRA DENTRO DA ZONA LIMITE DE POSICIONAMENTO      ####

                    if cx < 674 and cy < 426:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (195, 825), (195, 785), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # VERTICAL C
                        cv2.arrowedLine(frame, (125, 935), (125, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # VERTICAL B
                        cv2.arrowedLine(frame, (247, 885), (320, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # HORIZONTAL D
                        cv2.arrowedLine(frame, (15, 800), (80, 800), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # HORIZONTAL E


                    elif cx < 674 and cy > 426:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (195, 785), (195, 825), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # VERTICAL C
                        cv2.arrowedLine(frame, (125, 885), (125, 935), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # VERTICAL B
                        cv2.arrowedLine(frame, (247, 885), (320, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # HORIZONTAL D
                        cv2.arrowedLine(frame, (15, 800), (80, 800), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # HORIZONTAL E


                    elif cx > 674 and cy < 426:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (195, 825), (195, 785), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (125, 935), (125, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)
                        cv2.arrowedLine(frame, (320, 885), (247, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # HORIZONTAL D
                        cv2.arrowedLine(frame, (80, 800), (15, 800), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # HORIZONTAL E


                    elif cx > 674 and cy > 426:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (195, 785), (195, 825), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # VERTICAL C
                        cv2.arrowedLine(frame, (125, 885), (125, 935), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # VERTICAL B
                        cv2.arrowedLine(frame, (320, 885), (247, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # HORIZONTAL D
                        cv2.arrowedLine(frame, (80, 800), (15, 800), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # HORIZONTAL E


                    elif cx > 674 and cy == 426:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (320, 885), (247, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # HORIZONTAL D
                        cv2.arrowedLine(frame, (80, 800), (15, 800), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # HORIZONTAL E

                    elif cx < 674 and cy == 426:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (247, 885), (320, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # HORIZONTAL D
                        cv2.arrowedLine(frame, (15, 800), (80, 800), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # HORIZONTAL E


                    elif cx == 674 and cy > 426:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (195, 785), (195, 825), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # VERTICAL C
                        cv2.arrowedLine(frame, (125, 885), (125, 935), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # VERTICAL B


                    elif cx == 674 and cy < 426:

                        roi = frame[-size - 20:-20, -size - 1040:-1040]
                        roi[np.where(maskk)] = 0
                        roi += logo
                        cv2.arrowedLine(frame, (195, 825), (195, 785), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # VERTICAL C
                        cv2.arrowedLine(frame, (125, 935), (125, 885), (0, 0, 0), 3, cv2.LINE_AA, 0, 0.1)  # VERTICAL B


                    if cy < (-0.3157894737 * cx + 614):

                        cv2.circle(Box, (45, 260), 33, (0, 0, 255), -2)
                        # print("O alvo não está centrado.")


                    elif cy < (2.666666667 * cx - 1438):

                        cv2.circle(Box, (45, 260), 33, (0, 0, 255), -2)
                        # print("O alvo não está centrado.")


                    elif cy > (2.666666667 * cx - 1305):

                        cv2.circle(Box, (45, 260), 33, (0, 0, 255), -2)
                        # print("O alvo não está centrado.")


                    elif cy > (-0.3157894737 * cx + 663):

                        cv2.circle(Box, (45, 260), 33, (0, 0, 255), -2)
                        # print("O alvo não está centrado.")


                    elif (-0.3157894737 * cx + 614) < cy < (-0.3157894737 * cx + 631):

                        cv2.circle(Box, (135, 260), 33, (0, 255, 255), -2)
                        # print("O alvo não está centrado.")


                    elif (2.666666667 * cx - 1438) < cy < (2.666666667 * cx - 1393):

                        cv2.circle(Box, (135, 260), 33, (0, 255, 255), -2)
                        # print("O alvo não está centrado.")


                    elif (2.666666667 * cx - 1349) < cy < (2.666666667 * cx - 1305):

                        cv2.circle(Box, (135, 260), 33, (0, 255, 255), -2)
                        # print("O alvo não está centrado.")


                    elif (-0.3157894737 * cx + 647) < cy < (-0.3157894737 * cx + 663):

                        cv2.circle(Box, (135, 260), 33, (0, 255, 255), -2)
                        # print("O alvo não está centrado.")


                    else:

                        cv2.circle(frame, (225, 260), 33, (0, 255, 0), -2)
                        Box = cv2.rectangle(frame, (1280, 960), (530, 850), (0, 255, 255), -1)
                        draw_text(frame, " O ALVO ESTA CENTRADO E A COORDENADAS ", font_scale=2, pos=(540, 880),
                                      text_color_bg=(0, 255, 255))
                        draw_text(frame, " DO CENTRO SAO: x:{} , y:{} ".format(cx, cy), font_scale=2, pos=(540, 915),
                                      text_color_bg=(0, 255, 255))
                        # print("O alvo está centrado e as coordenadas do centro são: [x:{}, y:{}].".format(cx, cy))


                ######               CRIAÇÃO DA MÁSCARA PARA EXTRAÇÃO DOS CONTORNOS DOS PONTOS DOS DÍGITOS               ###############


            frameBlur = cv2.GaussianBlur(frame, (5, 5), 1)
            frameGray = cv2.cvtColor(frameBlur, cv2.COLOR_BGR2GRAY)

            threshold1 = 50 #cv2.getTrackbarPos("Threshold1", "Parameters")
            threshold2 = 150 #cv2.getTrackbarPos("Threshold2", "Parameters")

            frameCanny = cv2.Canny(frameGray, threshold1, threshold2)
            frameDilate = cv2.dilate(frameCanny, None, iterations=3)
            #cv2.imshow('dilate', frameDilate)

            ROI_digitos = frameDilate[20:250, 375:1000]
            #cv2.imshow("ROI_Digitos", ROI_digitos)


            #############           CALL-BACK DA FUNÇÃO PARA OBTER OS CONTORNOS DOS PONTOS DOS DÍGITOS            ##################


            getContours(ROI_digitos, frame)


            #####     CRIAÇÃO DA MÁSCARA PARA DETEÇÃO DAS LINHAS DO EIXO HORIZONTAL E DA UNIÃO DOS PONTOS DOS DÍGITOS       ########


            #convert = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            #lower_white = np.array([0, 0, 255])
            #upper_white = np.array([0, 0, 255])

            #convert_2 = cv2.inRange(convert, lower_white, upper_white)

            #threshold_1 = 126 #cv2.getTrackbarPos("Threshold_1", "Parametros")
            #threshold_2 = 240 #cv2.getTrackbarPos("Threshold_2", "Parametros")

            #convert_3 = cv2.Canny(convert_2, threshold_1, threshold_2)

            #convert_4 = cv2.dilate(convert_3, None, iterations = 3)


            ###########        DETEÇÃO DAS LINHAS DO EIXO HORIZONTAL E DA UNIÃO DOS PONTOS DOS DÍGITOS              ################


            #linesP = cv2.HoughLinesP(convert_4, 1, np.pi / 180, 120, None, 50, 1)

            #if linesP is not None:

            #    for i in range(0, len(linesP)):

            #        l = linesP[i][0]
            #        cv2.line(convert_4, (l[0], l[1]), (l[2], l[3]), (255, 0, 0), 1, cv2.LINE_AA)


            ################               DISPLAY DA FRAME COM TODAS AS ALTERAÇÕES APLICADAS                    ###################


            cv2.imshow("Video da centragem do laser", frame)


            ################         COMANDO PARA SE O BOTAO ESC FOR PRESSIONADO O PROGRAMA TERMINAR             ###################
            timestr = time.strftime('___%d %m %Y____%H %M %S')

            k = cv2.waitKey(5)
            if k == 13:

                break

        grabResult.Release()

    camera.StopGrabbing()
    cv2.destroyAllWindows()


    ##   COMANDOS PARA QUANDO LIGADO A CÂMARA LIVE FECHAR A TRANSMISSÃO DA CÂMARA APÓS PRESSIONADO BOTAO PARA TERMINAR    ##
