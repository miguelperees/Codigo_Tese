import os
import tkinter as tk
from tkinter import *
from pathlib import Path
import pyautogui
import os
import glob
import shutil
import time
import sys
import subprocess
import datetime
import fnmatch
from time import strftime
from PIL import ImageTk, Image
from tkinter import messagebox
from datetime import datetime
from MANTELMOWE_T import start_mantelmowe
from BLAUMÖWE_T import start_blaumowe
from MANTELMOWE_SERV_TECNICO_T import start_mantelmowe_serv_tecnico
from BLAUMÖWE_SERV_TECNICO_T import start_blaumowe_serv_tecnico
from CHECKUP_42_T import check_up_42
from CHECKUP_56_T import check_up_56

global logo


def master_pro_42():


    def voltar_inicial():

        inputtxt.delete(0, 'end')
        initial.forget()
        screen1.pack(fill=tk.BOTH, expand=True)


    def voltar_modelo_42():

        inputtxt.delete(0, 'end')
        initial.forget()
        selecionar.pack(fill=tk.BOTH, expand=True)
        label_imagem = tk.Label(selecionar, bg="black", anchor="nw", image=new_logo_2)
        label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


    def criar_pasta():

        root_folder = Path('C:/Users/installation/Desktop/Geovid Pro/(42x)')
        new_folder = Path(root_folder, inputtxt.get())
        new_folder.mkdir(parents=True, exist_ok=True)

        root_folder_2 = Path('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}'.format(inputtxt.get()))
        new_folder_2 = Path(root_folder_2, "Ajuste do Display e Recetor")
        new_folder_2.mkdir(parents=True, exist_ok=True)


    def iniciar_colimador():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                              AJUSTE DO COLIMADOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_colimador():


            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_colimador)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_colimador()


        def voltar_colimador():

            pasta = ('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))
            os.rmdir(pasta)

            pasta_2 = ('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}'.format(inputtxt.get()))
            os.rmdir(pasta_2)

            inputtxt.delete(0, 'end')

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar():


            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar():


            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run():

            global start

            start = datetime.now()

            disable_iniciar()
            able_registar()

            start_mantelmowe()


        def registar():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____COLIMADOR' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):

                    shutil.move(pngfile, dst_dir)

            second.forget()
            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o ajuste do\n colimador do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_colimador, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def criar_e_iniciar_colimador():

        criar_pasta()
        iniciar_colimador()


    def iniciar_colocar_anilha():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                         COLOCAÇÃO DE ANILHA", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_anilha():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_anilha)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_anilha()


        def voltar_anilha():

            inputtxt.delete(0, 'end')

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_anilha():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_anilha():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_anilha():

            global start

            start = datetime.now()

            disable_iniciar_anilha()
            able_registar_anilha()

            start_mantelmowe()


        def registar_anilha():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____COLOCACAO_ANILHA' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registada a colocação da \n anilha no prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_anilha, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_anilha, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_anilha, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_pos_estufa():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                       VERIFICAÇAO COLIMADOR APÓS ESTUFA", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_pos_estufa():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_pos_estufa)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_pos_estufa()


        def voltar_pos_estufa():

            inputtxt.delete(0, 'end')

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_pos_estufa():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_pos_estufa():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_pos_estufa():

            global start

            start = datetime.now()

            disable_iniciar_pos_estufa()
            able_registar_pos_estufa()

            start_mantelmowe()


        def registar_pos_estufa():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____POS_ESTUFA_COLIMADOR' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registada a verificação após estufa\n do colimador do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_pos_estufa, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_pos_estufa, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_pos_estufa, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_reajuste():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(second, text="                              REAJUSTE DO COLIMADOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='BLACK', fg='RED', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_reajuste():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_reajuste)

        font = ('times', 20, 'bold')

        l2 = tk.Label(second, font=font, bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_reajuste()


        def voltar_reajuste():

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            inputtxt.delete(0, 'end')


        def disable_iniciar_reajuste():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_reajuste():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_reajuste():

            global start_2

            start_2 = datetime.now()

            disable_iniciar_reajuste()
            able_registar_reajuste()

            global programa
            global p

            start_mantelmowe()

        def registar_reajuste():

            end_2 = datetime.now()

            global adjust_time_reajuste

            adjust_time_reajuste = (end_2 - start_2).total_seconds()

            adjust_time_reajuste_int = int(adjust_time_reajuste)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            path = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(path):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____REAJUSTE_DO_COLIMADOR' + timestr + '____' + str(adjust_time_reajuste_int) + '_seg''.png')
                old_name = path + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                check_existance = os.path.join(dst_dir, os.path.basename(new_name))

                if os.path.exists(check_existance):

                    os.remove(check_existance)

                else:

                    shutil.move(new_name, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do\n colimador do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_reajuste, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_reajuste, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_reajuste, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_display_e_recetor():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(second, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='BLACK', fg='RED', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_display_e_recetor():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_display_e_recetor)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_display_e_recetor()


        def voltar_display_e_recetor():

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            inputtxt.delete(0, 'end')


        def disable_iniciar_display_e_recetor():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_display_e_recetor():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_display_e_recetor():

            global start_1

            start_1 = datetime.now()

            disable_iniciar_display_e_recetor()
            able_registar_display_e_recetor()

            start_mantelmowe()


        def registar_display_e_recetor():

            end_1 = datetime.now()

            global adjust_time_display_e_recetor

            adjust_time_display_e_recetor = (end_1 - start_1).total_seconds()

            adjust_time_display_e_recetor_int = int(adjust_time_display_e_recetor)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            path = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(path):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____DISPLAY_E_RECETOR' + timestr + '_____' + str(adjust_time_display_e_recetor_int) + '_seg''.png')

                old_name = path + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                check_existance = os.path.join(dst_dir, os.path.basename(new_name))

                if os.path.exists(check_existance):

                    os.remove(check_existance)

                else:

                    shutil.move(new_name, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o ajuste do display\n e do recetor do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_display_e_recetor, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_display_e_recetor, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_display_e_recetor, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_reajuste_display_e_recetor():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(second, text="                          REAJUSTE DO DISPLAY E RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='BLACK', fg='RED', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_reajuste_display_e_recetor():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_reajuste_display_e_recetor)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_reajuste_display_e_recetor()


        def voltar_reajuste_display_e_recetor():

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            inputtxt.delete(0, 'end')


        def disable_iniciar_reajuste_display_e_recetor():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_reajuste_display_e_recetor():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_reajuste_display_e_recetor():

            global start_2

            start_2 = datetime.now()

            disable_iniciar_reajuste_display_e_recetor()
            able_registar_reajuste_display_e_recetor()

            global programa
            global p

            start_mantelmowe()


        def registar_reajuste_display_e_recetor():

            end_2 = datetime.now()

            global adjust_time_reajuste

            adjust_time_reajuste = (end_2 - start_2).total_seconds()

            adjust_time_reajuste_int = int(adjust_time_reajuste)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            path = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(path):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____REAJUSTE_DO_DISPLAY_E_RECETOR' + timestr + '____' + str(adjust_time_reajuste_int) + '_seg''.png')
                old_name = path + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                check_existance = os.path.join(dst_dir, os.path.basename(new_name))

                if os.path.exists(check_existance):

                    os.remove(check_existance)

                else:

                    shutil.move(new_name, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do display\n e do recetor do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_reajuste_display_e_recetor, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_reajuste_display_e_recetor, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_reajuste_display_e_recetor, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def verificação_pasta_criada():

        verificar = Path("C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            messagebox.showerror(title="", message="O colimador do prisma nº {} já foi ajustado!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        else:

            criar_e_iniciar_colimador()


    def verificacao_pasta_criada_anilha():

        verificar = Path("C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor/*_COLOCACAO_ANILHA___*'.format(inputtxt.get())):

                messagebox.showerror(title="", message="A colocação da anilha no\nprisma nº {} já foi realizada!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

            else:

                iniciar_colocar_anilha()

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_reajuste():

        verificar = Path('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                iniciar_reajuste()

            else:

                messagebox.showerror(title="", message="O prisma nº {} ainda não fez a verificação do colimador após estufa!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_pos_estufa():

        verificar = Path('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                messagebox.showerror(title="", message="A verificação do colimador após estufa\n do prisma nº {} já foi realizada!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

            else:

                iniciar_pos_estufa()

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_display_e_recetor():

        verificar = Path('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor/*_DISPLAY_E_RECETOR___*'.format(inputtxt.get())):

                    messagebox.showerror(title="", message="O display e recetor do\n prisma nº {} já foram ajustados!".format(inputtxt.get()))

                    inputtxt.delete(0, 'end')

                else:

                    iniciar_display_e_recetor()

            else:

                messagebox.showerror(title="", message="O prisma nº {} ainda não fez a verificação do colimador após estufa!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_reajuste_display_e_recetor():

        verificar = Path('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(42x)/{}/Ajuste do Display e Recetor/*_DISPLAY_E_RECETOR___*'.format(inputtxt.get())):

                    iniciar_reajuste_display_e_recetor()

                else:

                    messagebox.showerror(title="",message="O display e recetor do prisma nº {}\n ainda não foram ajustados!".format(inputtxt.get()))

                    inputtxt.delete(0, 'end')

            else:

                messagebox.showerror(title="",message="O prisma nº {} ainda não fez a verificação do colimador após estufa!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

        else:

            messagebox.showerror(title="",message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificar_input_texto():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada()


    def verificar_input_texto_anilha():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificacao_pasta_criada_anilha()


    def verificar_input_texto_reajuste():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_reajuste()


    def verificar_input_texto_pos_estufa():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_pos_estufa()


    def verificar_input_texto_display_e_recetor():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_display_e_recetor()


    def verificar_input_texto_reajuste_display_e_recetor():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_reajuste_display_e_recetor()


    def no_tab(event):

        return 'break'


    def no_enter(event):

        return 'break'


    def no_space(event):

        return 'break'


    selecionar.forget()

    global initial

    initial = tk.Canvas(screen, bg='#d9d9d9')
    initial.pack(fill=tk.BOTH, expand=True)

    frame_ = tk.Frame(initial, bg='#d9d9d9')
    frame_.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(initial, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_2 = tk.Frame(initial, bg='black')
    frame_2.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.7)

    frame_3 = tk.Frame(initial, bg='#8c8c8c')
    frame_3.place(relx=0.205, rely=0.21, relwidth=0.59, relheight=0.68)

    label_ = tk.Label(initial, text="  INSIRA O Nº DO PRISMA:", bg='#8c8c8c', fg='black', font=('Courier', 28, "bold"), anchor='w')
    label_.place(relx=0.35, rely=0.36, relwidth=0.3, relheight=0.08)

    global inputtxt

    v = StringVar()

    inputtxt = Entry(initial, width=19, font=('Courier', 27, "bold"), bg="white", textvariable=v)
    inputtxt.place(relx=0.36, rely=0.445, relwidth=0.275, relheight=0.04)

    inputtxt.bind('<Tab>', no_tab)

    inputtxt.bind('<Return>', no_enter)

    inputtxt.bind('<space>', no_space)


    def verificação_tamanho_numero_prisma(*arg):

        texto = inputtxt.get()

        breaks = texto.count('\n')

        charach_number = len(texto) - breaks

        if (charach_number > 24):

            inputtxt.delete((len(inputtxt.get()) - 1))


    def maiusculas(*arg):

        v.set(inputtxt.get().upper())


    v.trace('w', maiusculas)
    v.trace('w', verificação_tamanho_numero_prisma)

    button_iniciar = tk.Button(initial, text="1º - COLIMADOR", bg='GREEN', fg='WHITE', command=verificar_input_texto, font=('Courier', 18, "bold"))
    button_iniciar.place(relx=0.2875, rely=0.54, relwidth=0.125, relheight=0.09)


    button_pos_estufa = tk.Button(initial, text="2º - VERIFICAÇÃO\n     APÓS ESTUFA", bg='ORANGE', fg='WHITE', command=verificar_input_texto_pos_estufa, font=('Courier', 16, "bold"))
    button_pos_estufa.place(relx=0.4375, rely=0.54, relwidth=0.125, relheight=0.09)

    button_display_recetor = tk.Button(initial, text="3º - DISPLAY E\n   RECETOR", bg='BLUE', fg='WHITE', command=verificar_input_texto_display_e_recetor, font=('Courier', 16, "bold"))
    button_display_recetor.place(relx=0.5875, rely=0.54, relwidth=0.125, relheight=0.09)


    frame_retra = tk.Frame(initial, bg='black')
    frame_retra.place(relx=0.26175, rely=0.6775, relwidth=0.475, relheight=0.18)

    frame_retra2 = tk.Frame(initial, bg='#8c8c8c')
    frame_retra2.place(relx=0.2775, rely=0.7025, relwidth=0.445, relheight=0.13)

    label_ = tk.Label(initial, text="       RETRABALHOS",bg = 'BLACK', fg='WHITE', font=('Courier', 20, "bold"),anchor='w')
    label_.place(relx=0.3925, rely=0.6805, relwidth=0.3, relheight=0.02)


    button_anilha = tk.Button(initial, text="COLOCAÇÃO\nDE ANILHA", bg='#F1DA15', fg='BLACK', command=verificar_input_texto_anilha, font=('Courier', 16, "bold"))
    button_anilha.place(relx=0.2975, rely=0.7225, relwidth=0.105, relheight=0.09)

    button_readjust_colimador = tk.Button(initial, text="REAJUSTAR\nCOLIMADOR", bg='#F1DA15', fg='BLACK', command=verificar_input_texto_reajuste, font=('Courier', 16, "bold"))
    button_readjust_colimador.place(relx=0.4475, rely=0.7225, relwidth=0.105, relheight=0.09)

    button_readjust_display = tk.Button(initial, text="REAJUSTAR\nDISPLAY E\nRECETOR", bg='#F1DA15', fg='BLACK', command=verificar_input_texto_reajuste_display_e_recetor, font=('Courier', 16, "bold"))
    button_readjust_display.place(relx=0.5975, rely=0.7225, relwidth=0.105, relheight=0.09)

    button_mudar_modelo_42 = tk.Button(initial, text="MUDAR\nMODELO", bg='GREEN', fg='white', command=voltar_modelo_42, state=NORMAL, font=('Courier', 20, "bold"))
    button_mudar_modelo_42.place(relx=0.8, rely=0.005, relwidth=0.098, relheight=0.071)

    button_log_out = tk.Button(initial, text="TERMINAR\nSESSÃO", bg='RED', fg='white', command=voltar_inicial, state=NORMAL, font=('Courier', 20, "bold"))
    button_log_out.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    label_username = tk.Label(initial, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
    label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def tempo_master():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_master)


    l2 = tk.Label(screen, font=('times', 20, 'bold'), bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_master()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    global label_imagem

    label_imagem = tk.Label(initial, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


def master_com_42():


    def voltar_inicial():

        inputtxt.delete(0, 'end')
        initial.forget()
        screen1.pack(fill=tk.BOTH, expand=True)


    def voltar_modelo_42():

        inputtxt.delete(0, 'end')
        initial.forget()
        selecionar.pack(fill=tk.BOTH, expand=True)
        label_imagem = tk.Label(selecionar, bg="black", anchor="nw", image=new_logo_2)
        label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


    def criar_pasta():

        root_folder = Path('C:/Users/installation/Desktop/Geovid .COM/(42x)')
        new_folder = Path(root_folder, inputtxt.get())
        new_folder.mkdir(parents=True, exist_ok=True)

        root_folder_2 = Path('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}'.format(inputtxt.get()))
        new_folder_2 = Path(root_folder_2, "Ajuste do Display e Recetor")
        new_folder_2.mkdir(parents=True, exist_ok=True)


    def iniciar_colimador():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                              AJUSTE DO COLIMADOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_colimador():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_colimador)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_colimador()


        def voltar_colimador():

            pasta = ('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))
            os.rmdir(pasta)

            pasta_2 = ('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}'.format(inputtxt.get()))
            os.rmdir(pasta_2)

            inputtxt.delete(0, 'end')

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run():

            global start

            start = datetime.now()

            disable_iniciar()
            able_registar()

            start_mantelmowe()


        def registar():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____COLIMADOR' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()
            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o ajuste do\n colimador do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_colimador, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def criar_e_iniciar_colimador():

        criar_pasta()
        iniciar_colimador()


    def iniciar_colocar_anilha():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                         COLOCAÇÃO DE ANILHA", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_anilha():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_anilha)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_anilha()


        def voltar_anilha():

            inputtxt.delete(0, 'end')

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_anilha():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_anilha():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_anilha():

            global start

            start = datetime.now()

            disable_iniciar_anilha()
            able_registar_anilha()

            start_mantelmowe()


        def registar_anilha():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____COLOCACAO_ANILHA' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registada a colocação da \n anilha no prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_anilha, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_anilha, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_anilha, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_pos_estufa():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                       VERIFICAÇAO COLIMADOR APÓS ESTUFA", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_pos_estufa():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_pos_estufa)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_pos_estufa()


        def voltar_pos_estufa():

            inputtxt.delete(0, 'end')

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_pos_estufa():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_pos_estufa():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_pos_estufa():

            global start

            start = datetime.now()

            disable_iniciar_pos_estufa()
            able_registar_pos_estufa()

            start_mantelmowe()


        def registar_pos_estufa():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____POS_ESTUFA_COLIMADOR' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registada a verificação após estufa\n do colimador do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_pos_estufa, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_pos_estufa, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_pos_estufa, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_reajuste():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(second, text="                              REAJUSTE DO COLIMADOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='BLACK', fg='RED', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_reajuste():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_reajuste)

        font = ('times', 20, 'bold')

        l2 = tk.Label(second, font=font, bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_reajuste()


        def voltar_reajuste():

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            inputtxt.delete(0, 'end')


        def disable_iniciar_reajuste():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_reajuste():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_reajuste():

            global start_2

            start_2 = datetime.now()

            disable_iniciar_reajuste()
            able_registar_reajuste()

            global programa
            global p

            start_mantelmowe()

        def registar_reajuste():

            end_2 = datetime.now()

            global adjust_time_reajuste

            adjust_time_reajuste = (end_2 - start_2).total_seconds()

            adjust_time_reajuste_int = int(adjust_time_reajuste)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            path = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(path):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____REAJUSTE_DO_COLIMADOR' + timestr + '____' + str(adjust_time_reajuste_int) + '_seg''.png')
                old_name = path + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                check_existance = os.path.join(dst_dir, os.path.basename(new_name))

                if os.path.exists(check_existance):

                    os.remove(check_existance)

                else:

                    shutil.move(new_name, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do\n colimador do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_reajuste, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_reajuste, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_reajuste, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_display_e_recetor():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(second, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='BLACK', fg='RED', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_display_e_recetor():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_display_e_recetor)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_display_e_recetor()


        def voltar_display_e_recetor():

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            inputtxt.delete(0, 'end')


        def disable_iniciar_display_e_recetor():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_display_e_recetor():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_display_e_recetor():

            global start_1

            start_1 = datetime.now()

            disable_iniciar_display_e_recetor()
            able_registar_display_e_recetor()

            start_mantelmowe()


        def registar_display_e_recetor():

            end_1 = datetime.now()

            global adjust_time_display_e_recetor

            adjust_time_display_e_recetor = (end_1 - start_1).total_seconds()

            adjust_time_display_e_recetor_int = int(adjust_time_display_e_recetor)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            path = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(path):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____DISPLAY_E_RECETOR' + timestr + '_____' + str(adjust_time_display_e_recetor_int) + '_seg''.png')

                old_name = path + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                check_existance = os.path.join(dst_dir, os.path.basename(new_name))

                if os.path.exists(check_existance):

                    os.remove(check_existance)

                else:

                    shutil.move(new_name, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o ajuste do display\n e do recetor do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_display_e_recetor, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_display_e_recetor, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_display_e_recetor, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_reajuste_display_e_recetor():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(second, text="                          REAJUSTE DO DISPLAY E RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='BLACK', fg='RED', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_reajuste_display_e_recetor():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_reajuste_display_e_recetor)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_reajuste_display_e_recetor()


        def voltar_reajuste_display_e_recetor():

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            inputtxt.delete(0, 'end')


        def disable_iniciar_reajuste_display_e_recetor():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_reajuste_display_e_recetor():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_reajuste_display_e_recetor():

            global start_2

            start_2 = datetime.now()

            disable_iniciar_reajuste_display_e_recetor()
            able_registar_reajuste_display_e_recetor()

            global programa
            global p

            start_mantelmowe()


        def registar_reajuste_display_e_recetor():

            end_2 = datetime.now()

            global adjust_time_reajuste

            adjust_time_reajuste = (end_2 - start_2).total_seconds()

            adjust_time_reajuste_int = int(adjust_time_reajuste)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            path = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(path):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____REAJUSTE_DO_DISPLAY_E_RECETOR' + timestr + '____' + str(adjust_time_reajuste_int) + '_seg''.png')
                old_name = path + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                check_existance = os.path.join(dst_dir, os.path.basename(new_name))

                if os.path.exists(check_existance):

                    os.remove(check_existance)

                else:

                    shutil.move(new_name, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do display\n e do recetor do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_reajuste_display_e_recetor, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_reajuste_display_e_recetor, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_reajuste_display_e_recetor, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def verificação_pasta_criada():

        verificar = Path("C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            messagebox.showerror(title="", message="O colimador do prisma nº {} já foi ajustado!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        else:

            criar_e_iniciar_colimador()


    def verificacao_pasta_criada_anilha():

        verificar = Path("C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor/*_COLOCACAO_ANILHA___*'.format(inputtxt.get())):

                messagebox.showerror(title="", message="A colocação da anilha no\nprisma nº {} já foi realizada!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

            else:

                iniciar_colocar_anilha()

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_reajuste():

        verificar = Path('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                iniciar_reajuste()

            else:

                messagebox.showerror(title="", message="O prisma nº {} ainda não fez a verificação do colimador após estufa!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_pos_estufa():

        verificar = Path('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                messagebox.showerror(title="", message="A verificação do colimador após estufa\n do prisma nº {} já foi realizada!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

            else:

                iniciar_pos_estufa()

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_display_e_recetor():

        verificar = Path('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor/*_DISPLAY_E_RECETOR___*'.format(inputtxt.get())):

                    messagebox.showerror(title="", message="O display e recetor do\n prisma nº {} já foram ajustados!".format(inputtxt.get()))

                    inputtxt.delete(0, 'end')

                else:

                    iniciar_display_e_recetor()

            else:

                messagebox.showerror(title="", message="O prisma nº {} ainda não fez a verificação do colimador após estufa!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_reajuste_display_e_recetor():

        verificar = Path('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(42x)/{}/Ajuste do Display e Recetor/*_DISPLAY_E_RECETOR___*'.format(inputtxt.get())):

                    iniciar_reajuste_display_e_recetor()

                else:

                    messagebox.showerror(title="",message="O display e recetor do prisma nº {}\n ainda não foram ajustados!".format(inputtxt.get()))

                    inputtxt.delete(0, 'end')

            else:

                messagebox.showerror(title="",message="O prisma nº {} ainda não fez a verificação do colimador após estufa!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

        else:

            messagebox.showerror(title="",message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificar_input_texto():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada()


    def verificar_input_texto_anilha():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificacao_pasta_criada_anilha()


    def verificar_input_texto_reajuste():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_reajuste()


    def verificar_input_texto_pos_estufa():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_pos_estufa()


    def verificar_input_texto_display_e_recetor():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_display_e_recetor()


    def verificar_input_texto_reajuste_display_e_recetor():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_reajuste_display_e_recetor()


    def no_tab(event):

        return 'break'


    def no_enter(event):

        return 'break'


    def no_space(event):

        return 'break'


    selecionar.forget()

    global initial

    initial = tk.Canvas(screen, bg='#d9d9d9')
    initial.pack(fill=tk.BOTH, expand=True)

    frame_ = tk.Frame(initial, bg='#d9d9d9')
    frame_.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(initial, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_2 = tk.Frame(initial, bg='black')
    frame_2.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.7)

    frame_3 = tk.Frame(initial, bg='#8c8c8c')
    frame_3.place(relx=0.205, rely=0.21, relwidth=0.59, relheight=0.68)

    label_ = tk.Label(initial, text="  INSIRA O Nº DO PRISMA:", bg='#8c8c8c', fg='black', font=('Courier', 28, "bold"), anchor='w')
    label_.place(relx=0.35, rely=0.36, relwidth=0.3, relheight=0.08)

    global inputtxt

    v = StringVar()

    inputtxt = Entry(initial, width=19, font=('Courier', 27, "bold"), bg="white", textvariable=v)
    inputtxt.place(relx=0.36, rely=0.445, relwidth=0.275, relheight=0.04)

    inputtxt.bind('<Tab>', no_tab)

    inputtxt.bind('<Return>', no_enter)

    inputtxt.bind('<space>', no_space)


    def verificação_tamanho_numero_prisma(*arg):

        texto = inputtxt.get()

        breaks = texto.count('\n')

        charach_number = len(texto) - breaks

        if (charach_number > 24):

            inputtxt.delete((len(inputtxt.get()) - 1))


    def maiusculas(*arg):

        v.set(inputtxt.get().upper())


    v.trace('w', maiusculas)
    v.trace('w', verificação_tamanho_numero_prisma)

    button_iniciar = tk.Button(initial, text="1º - COLIMADOR", bg='GREEN', fg='WHITE', command=verificar_input_texto, font=('Courier', 18, "bold"))
    button_iniciar.place(relx=0.2875, rely=0.54, relwidth=0.125, relheight=0.09)

    button_pos_estufa = tk.Button(initial, text="2º - VERIFICAÇÃO\n     APÓS ESTUFA", bg='ORANGE', fg='WHITE', command=verificar_input_texto_pos_estufa, font=('Courier', 16, "bold"))
    button_pos_estufa.place(relx=0.4375, rely=0.54, relwidth=0.125, relheight=0.09)

    button_display_recetor = tk.Button(initial, text="3º - DISPLAY E\n   RECETOR", bg='BLUE', fg='WHITE', command=verificar_input_texto_display_e_recetor, font=('Courier', 16, "bold"))
    button_display_recetor.place(relx=0.5875, rely=0.54, relwidth=0.125, relheight=0.09)

    frame_retra = tk.Frame(initial, bg='black')
    frame_retra.place(relx=0.26175, rely=0.6775, relwidth=0.475, relheight=0.18)

    frame_retra2 = tk.Frame(initial, bg='#8c8c8c')
    frame_retra2.place(relx=0.2775, rely=0.7025, relwidth=0.445, relheight=0.13)

    label_ = tk.Label(initial, text="       RETRABALHOS", bg='BLACK', fg='WHITE', font=('Courier', 20, "bold"), anchor='w')
    label_.place(relx=0.3925, rely=0.6805, relwidth=0.3, relheight=0.02)

    button_anilha = tk.Button(initial, text="COLOCAÇÃO\nDE ANILHA", bg='#F1DA15', fg='BLACK', command=verificar_input_texto_anilha, font=('Courier', 16, "bold"))
    button_anilha.place(relx=0.2975, rely=0.7225, relwidth=0.105, relheight=0.09)

    button_readjust_colimador = tk.Button(initial, text="REAJUSTAR\nCOLIMADOR", bg='#F1DA15', fg='BLACK', command=verificar_input_texto_reajuste, font=('Courier', 16, "bold"))
    button_readjust_colimador.place(relx=0.4475, rely=0.7225, relwidth=0.105, relheight=0.09)

    button_readjust_display = tk.Button(initial, text="REAJUSTAR\nDISPLAY E\nRECETOR", bg='#F1DA15', fg='BLACK', command=verificar_input_texto_reajuste_display_e_recetor, font=('Courier', 16, "bold"))
    button_readjust_display.place(relx=0.5975, rely=0.7225, relwidth=0.105, relheight=0.09)

    button_mudar_modelo_42 = tk.Button(initial, text="MUDAR\nMODELO", bg='GREEN', fg='white', command=voltar_modelo_42, state=NORMAL, font=('Courier', 20, "bold"))
    button_mudar_modelo_42.place(relx=0.8, rely=0.005, relwidth=0.098, relheight=0.071)

    button_log_out = tk.Button(initial, text="TERMINAR\nSESSÃO", bg='RED', fg='white', command=voltar_inicial, state=NORMAL, font=('Courier', 20, "bold"))
    button_log_out.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    label_username = tk.Label(initial, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
    label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def tempo_master():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_master)


    l2 = tk.Label(screen, font=('times', 20, 'bold'), bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_master()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    global label_imagem

    label_imagem = tk.Label(initial, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


def master_st_pro_42():


    def voltar_inicial():

        inputtxt.delete(0, 'end')
        initial.forget()
        screen1.pack(fill=tk.BOTH, expand=True)


    def voltar_modelo_42():

        inputtxt.delete(0, 'end')
        initial.forget()
        selecionar.pack(fill=tk.BOTH, expand=True)
        label_imagem = tk.Label(selecionar, bg="black", anchor="nw", image=new_logo_2)
        label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


    def criar_pasta_serv_tecnico():

        root_folder = Path('C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(42x)')
        new_folder = Path(root_folder, inputtxt.get())
        new_folder.mkdir(parents=True, exist_ok=True)

        root_folder_2 = Path('C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(42x)/{}'.format(inputtxt.get()))
        new_folder_2 = Path(root_folder_2, "Ajuste do Display e Recetor")
        new_folder_2.mkdir(parents=True, exist_ok=True)


    def iniciar_reajuste_serv_tecnico():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                            REAJUSTE SERVIÇO TÉCNICO", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" BINÓCULO nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_serv_tecnico():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_serv_tecnico)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_serv_tecnico()


        def voltar_serv_tecnico():

            path = ('C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

            dir = os.listdir(path)

            if len(dir) == 0:

                pasta = ('C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))
                os.rmdir(pasta)

                pasta_2 = ('C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(42x)/{}'.format(inputtxt.get()))
                os.rmdir(pasta_2)

                inputtxt.delete(0, 'end')

                second.forget()

                initial.pack(fill=tk.BOTH, expand=True)

            else:

                inputtxt.delete(0, 'end')

                second.forget()

                initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_serv_tecnico():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_serv_tecnico():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_serv_tecnico():

            global start

            start = datetime.now()

            disable_iniciar_serv_tecnico()
            able_registar_serv_tecnico()

            start_mantelmowe_serv_tecnico()


        def registar_serv_tecnico():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____REAJUSTE_SERVIÇO_TECNICO' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do serviço\n técnico do binóculo nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_serv_tecnico, state=NORMAL,font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_serv_tecnico, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_serv_tecnico, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def criar_e_iniciar_reajuste_serv_tecnico():

        criar_pasta_serv_tecnico()
        iniciar_reajuste_serv_tecnico()


    def verificacao_pasta_criada_serv_tecnico():

        verificar = Path("C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(42x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            iniciar_reajuste_serv_tecnico()

        else:

            criar_e_iniciar_reajuste_serv_tecnico()


    def verificar_input_texto_serv_tecnico():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do binóculo!")

        else:

            verificacao_pasta_criada_serv_tecnico()


    def no_tab(event):

        return 'break'


    def no_enter(event):

        return 'break'


    def no_space(event):

        return 'break'


    selecionar.forget()

    global initial

    initial = tk.Canvas(screen, bg='#d9d9d9')
    initial.pack(fill=tk.BOTH, expand=True)

    frame_ = tk.Frame(initial, bg='#d9d9d9')
    frame_.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(initial, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_2 = tk.Frame(initial, bg='black')
    frame_2.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.6)

    frame_3 = tk.Frame(initial, bg='#8c8c8c')
    frame_3.place(relx=0.255, rely=0.26, relwidth=0.49, relheight=0.58)

    label_ = tk.Label(initial, text=" INSIRA O Nº DO BINÓCULO:", bg='#8c8c8c', fg='black', font=('Courier', 28, "bold"), anchor='w')
    label_.place(relx=0.35, rely=0.45, relwidth=0.3, relheight=0.08)

    global inputtxt

    v = StringVar()

    inputtxt = Entry(initial, width=19, font=('Courier', 27, "bold"), bg="white", textvariable=v)
    inputtxt.place(relx=0.36, rely=0.56, relwidth=0.275, relheight=0.04)

    inputtxt.bind('<Tab>', no_tab)

    inputtxt.bind('<Return>', no_enter)

    inputtxt.bind('<space>', no_space)


    def verificação_tamanho_numero_prisma(*arg):

        texto = inputtxt.get()

        breaks = texto.count('\n')

        charach_number = len(texto) - breaks

        if (charach_number > 24):

            inputtxt.delete((len(inputtxt.get()) - 1))


    def maiusculas(*arg):

        v.set(inputtxt.get().upper())


    v.trace('w', maiusculas)
    v.trace('w', verificação_tamanho_numero_prisma)

    button_avancar = tk.Button(initial, text="AVANÇAR", bg='GREEN', fg='WHITE', command=verificar_input_texto_serv_tecnico, font=('Courier', 18, "bold"))
    button_avancar.place(relx=0.4375, rely=0.69, relwidth=0.125, relheight=0.09)

    button_mudar_modelo_42 = tk.Button(initial, text="MUDAR\nMODELO", bg='GREEN', fg='white', command=voltar_modelo_42, state=NORMAL, font=('Courier', 20, "bold"))
    button_mudar_modelo_42.place(relx=0.8, rely=0.005, relwidth=0.098, relheight=0.071)

    button_log_out = tk.Button(initial, text="TERMINAR\nSESSÃO", bg='RED', fg='white', command=voltar_inicial, state=NORMAL, font=('Courier', 20, "bold"))
    button_log_out.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    label_username = tk.Label(initial, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
    label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def tempo_master():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_master)


    l2 = tk.Label(screen, font=('times', 20, 'bold'), bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_master()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    global label_imagem

    label_imagem = tk.Label(initial, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


def master_st_com_42():


    def voltar_inicial():

        inputtxt.delete(0, 'end')
        initial.forget()
        screen1.pack(fill=tk.BOTH, expand=True)


    def voltar_modelo_42():

        inputtxt.delete(0, 'end')
        initial.forget()
        selecionar.pack(fill=tk.BOTH, expand=True)
        label_imagem = tk.Label(selecionar, bg="black", anchor="nw", image=new_logo_2)
        label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


    def criar_pasta_serv_tecnico():

        root_folder = Path('C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(42x)')
        new_folder = Path(root_folder, inputtxt.get())
        new_folder.mkdir(parents=True, exist_ok=True)

        root_folder_2 = Path('C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(42x)/{}'.format(inputtxt.get()))
        new_folder_2 = Path(root_folder_2, "Ajuste do Display e Recetor")
        new_folder_2.mkdir(parents=True, exist_ok=True)


    def iniciar_reajuste_serv_tecnico():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                            REAJUSTE SERVIÇO TÉCNICO", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" BINÓCULO nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_serv_tecnico():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_serv_tecnico)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_serv_tecnico()


        def voltar_serv_tecnico():

            path = ('C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

            dir = os.listdir(path)

            if len(dir) == 0:

                pasta = ('C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))
                os.rmdir(pasta)

                pasta_2 = ('C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(42x)/{}'.format(inputtxt.get()))
                os.rmdir(pasta_2)

                inputtxt.delete(0, 'end')

                second.forget()

                initial.pack(fill=tk.BOTH, expand=True)

            else:

                inputtxt.delete(0, 'end')

                second.forget()

                initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_serv_tecnico():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_serv_tecnico():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_serv_tecnico():

            global start

            start = datetime.now()

            disable_iniciar_serv_tecnico()
            able_registar_serv_tecnico()

            start_mantelmowe_serv_tecnico()


        def registar_serv_tecnico():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____REAJUSTE_SERVIÇO_TECNICO' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do serviço\n técnico do binóculo nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_serv_tecnico, state=NORMAL,font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_serv_tecnico, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_serv_tecnico, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def criar_e_iniciar_reajuste_serv_tecnico():

        criar_pasta_serv_tecnico()
        iniciar_reajuste_serv_tecnico()


    def verificacao_pasta_criada_serv_tecnico():

        verificar = Path("C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(42x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            iniciar_reajuste_serv_tecnico()

        else:

            criar_e_iniciar_reajuste_serv_tecnico()


    def verificar_input_texto_serv_tecnico():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do binóculo!")

        else:

            verificacao_pasta_criada_serv_tecnico()


    def no_tab(event):

        return 'break'


    def no_enter(event):

        return 'break'


    def no_space(event):

        return 'break'


    selecionar.forget()

    global initial

    initial = tk.Canvas(screen, bg='#d9d9d9')
    initial.pack(fill=tk.BOTH, expand=True)

    frame_ = tk.Frame(initial, bg='#d9d9d9')
    frame_.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(initial, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_2 = tk.Frame(initial, bg='black')
    frame_2.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.6)

    frame_3 = tk.Frame(initial, bg='#8c8c8c')
    frame_3.place(relx=0.255, rely=0.26, relwidth=0.49, relheight=0.58)

    label_ = tk.Label(initial, text=" INSIRA O Nº DO BINÓCULO:", bg='#8c8c8c', fg='black', font=('Courier', 28, "bold"), anchor='w')
    label_.place(relx=0.35, rely=0.45, relwidth=0.3, relheight=0.08)

    global inputtxt

    v = StringVar()

    inputtxt = Entry(initial, width=19, font=('Courier', 27, "bold"), bg="white", textvariable=v)
    inputtxt.place(relx=0.36, rely=0.56, relwidth=0.275, relheight=0.04)

    inputtxt.bind('<Tab>', no_tab)

    inputtxt.bind('<Return>', no_enter)

    inputtxt.bind('<space>', no_space)


    def verificação_tamanho_numero_prisma(*arg):

        texto = inputtxt.get()

        breaks = texto.count('\n')

        charach_number = len(texto) - breaks

        if (charach_number > 24):

            inputtxt.delete((len(inputtxt.get()) - 1))


    def maiusculas(*arg):

        v.set(inputtxt.get().upper())


    v.trace('w', maiusculas)
    v.trace('w', verificação_tamanho_numero_prisma)

    button_avancar = tk.Button(initial, text="AVANÇAR", bg='GREEN', fg='WHITE', command=verificar_input_texto_serv_tecnico, font=('Courier', 18, "bold"))
    button_avancar.place(relx=0.4375, rely=0.69, relwidth=0.125, relheight=0.09)

    button_mudar_modelo_42 = tk.Button(initial, text="MUDAR\nMODELO", bg='GREEN', fg='white', command=voltar_modelo_42, state=NORMAL, font=('Courier', 20, "bold"))
    button_mudar_modelo_42.place(relx=0.8, rely=0.005, relwidth=0.098, relheight=0.071)

    button_log_out = tk.Button(initial, text="TERMINAR\nSESSÃO", bg='RED', fg='white', command=voltar_inicial, state=NORMAL, font=('Courier', 20, "bold"))
    button_log_out.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    label_username = tk.Label(initial, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
    label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def tempo_master():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_master)


    l2 = tk.Label(screen, font=('times', 20, 'bold'), bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_master()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    global label_imagem

    label_imagem = tk.Label(initial, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


def master_st_hdr_42():


    def voltar_inicial():

        inputtxt.delete(0, 'end')
        initial.forget()
        screen1.pack(fill=tk.BOTH, expand=True)


    def voltar_modelo_42():

        inputtxt.delete(0, 'end')
        initial.forget()
        selecionar.pack(fill=tk.BOTH, expand=True)
        label_imagem = tk.Label(selecionar, bg="black", anchor="nw", image=new_logo_2)
        label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


    def criar_pasta_serv_tecnico():

        root_folder = Path('C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(42x)')
        new_folder = Path(root_folder, inputtxt.get())
        new_folder.mkdir(parents=True, exist_ok=True)

        root_folder_2 = Path('C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(42x)/{}'.format(inputtxt.get()))
        new_folder_2 = Path(root_folder_2, "Ajuste do Display e Recetor")
        new_folder_2.mkdir(parents=True, exist_ok=True)


    def iniciar_reajuste_serv_tecnico():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                            REAJUSTE SERVIÇO TÉCNICO", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" BINÓCULO nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_serv_tecnico():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_serv_tecnico)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_serv_tecnico()


        def voltar_serv_tecnico():

            path = ('C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

            dir = os.listdir(path)

            if len(dir) == 0:

                pasta = ('C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))
                os.rmdir(pasta)

                pasta_2 = ('C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(42x)/{}'.format(inputtxt.get()))
                os.rmdir(pasta_2)

                inputtxt.delete(0, 'end')

                second.forget()

                initial.pack(fill=tk.BOTH, expand=True)

            else:

                inputtxt.delete(0, 'end')

                second.forget()

                initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_serv_tecnico():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_serv_tecnico():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_serv_tecnico():

            global start

            start = datetime.now()

            disable_iniciar_serv_tecnico()
            able_registar_serv_tecnico()

            start_mantelmowe_serv_tecnico()


        def registar_serv_tecnico():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (42x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (42x)/' + username1 + '____REAJUSTE_SERVIÇO_TECNICO' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (42x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(42x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do serviço\n técnico do binóculo nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_serv_tecnico, state=NORMAL,font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_serv_tecnico, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_serv_tecnico, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def criar_e_iniciar_reajuste_serv_tecnico():

        criar_pasta_serv_tecnico()
        iniciar_reajuste_serv_tecnico()


    def verificacao_pasta_criada_serv_tecnico():

        verificar = Path("C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(42x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            iniciar_reajuste_serv_tecnico()

        else:

            criar_e_iniciar_reajuste_serv_tecnico()


    def verificar_input_texto_serv_tecnico():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do binóculo!")

        else:

            verificacao_pasta_criada_serv_tecnico()


    def no_tab(event):

        return 'break'


    def no_enter(event):

        return 'break'


    def no_space(event):

        return 'break'


    selecionar.forget()

    global initial

    initial = tk.Canvas(screen, bg='#d9d9d9')
    initial.pack(fill=tk.BOTH, expand=True)

    frame_ = tk.Frame(initial, bg='#d9d9d9')
    frame_.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(initial, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_2 = tk.Frame(initial, bg='black')
    frame_2.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.6)

    frame_3 = tk.Frame(initial, bg='#8c8c8c')
    frame_3.place(relx=0.255, rely=0.26, relwidth=0.49, relheight=0.58)

    label_ = tk.Label(initial, text=" INSIRA O Nº DO BINÓCULO:", bg='#8c8c8c', fg='black', font=('Courier', 28, "bold"), anchor='w')
    label_.place(relx=0.35, rely=0.45, relwidth=0.3, relheight=0.08)

    global inputtxt

    v = StringVar()

    inputtxt = Entry(initial, width=19, font=('Courier', 27, "bold"), bg="white", textvariable=v)
    inputtxt.place(relx=0.36, rely=0.56, relwidth=0.275, relheight=0.04)

    inputtxt.bind('<Tab>', no_tab)

    inputtxt.bind('<Return>', no_enter)

    inputtxt.bind('<space>', no_space)


    def verificação_tamanho_numero_prisma(*arg):

        texto = inputtxt.get()

        breaks = texto.count('\n')

        charach_number = len(texto) - breaks

        if (charach_number > 24):

            inputtxt.delete((len(inputtxt.get()) - 1))


    def maiusculas(*arg):

        v.set(inputtxt.get().upper())


    v.trace('w', maiusculas)
    v.trace('w', verificação_tamanho_numero_prisma)

    button_avancar = tk.Button(initial, text="AVANÇAR", bg='GREEN', fg='WHITE', command=verificar_input_texto_serv_tecnico, font=('Courier', 18, "bold"))
    button_avancar.place(relx=0.4375, rely=0.69, relwidth=0.125, relheight=0.09)

    button_mudar_modelo_42 = tk.Button(initial, text="MUDAR\nMODELO", bg='GREEN', fg='white', command=voltar_modelo_42, state=NORMAL, font=('Courier', 20, "bold"))
    button_mudar_modelo_42.place(relx=0.8, rely=0.005, relwidth=0.098, relheight=0.071)

    button_log_out = tk.Button(initial, text="TERMINAR\nSESSÃO", bg='RED', fg='white', command=voltar_inicial, state=NORMAL, font=('Courier', 20, "bold"))
    button_log_out.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    label_username = tk.Label(initial, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
    label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def tempo_master():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_master)


    l2 = tk.Label(screen, font=('times', 20, 'bold'), bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_master()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    global label_imagem

    label_imagem = tk.Label(initial, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


def button_text_pro_42():

    label_modelo_pro_42 = tk.Label(initial, text=pro_42, bg='#8c8c8c', fg='WHITE', font=('Courier', 41, "bold"), anchor='w')
    label_modelo_pro_42.place(relx=0.36, rely=0.25, relwidth=0.3, relheight=0.09)


def button_text_com_42():

    label_modelo_pro_42 = tk.Label(initial, text=com_42, bg='#8c8c8c', fg='WHITE', font=('Courier', 41, "bold"), anchor='w')
    label_modelo_pro_42.place(relx=0.36, rely=0.25, relwidth=0.3, relheight=0.09)


def button_text_pro_42_st():

    label_modelo_pro_42 = tk.Label(initial, text=pro_42_st, bg='#8c8c8c', fg='WHITE', font=('Courier', 41, "bold"), anchor='w')
    label_modelo_pro_42.place(relx=0.36, rely=0.28, relwidth=0.3, relheight=0.09)


def button_text_com_42_st():

    label_modelo_pro_42 = tk.Label(initial, text=com_42_st, bg='#8c8c8c', fg='WHITE', font=('Courier', 41, "bold"), anchor='w')
    label_modelo_pro_42.place(relx=0.36, rely=0.28, relwidth=0.3, relheight=0.09)


def button_text_hdr_42_st():

    label_modelo_pro_42 = tk.Label(initial, text=hdr_42_st, bg='#8c8c8c', fg='WHITE', font=('Courier', 41, "bold"), anchor='w')
    label_modelo_pro_42.place(relx=0.36, rely=0.28, relwidth=0.3, relheight=0.09)




































def master_2_pro_56():


    def voltar_inicial():

        inputtxt.delete(0, 'end')
        initial.forget()
        screen1.pack(fill=tk.BOTH, expand=True)


    def voltar_modelo_56():

        inputtxt.delete(0, 'end')
        initial.forget()
        selecionar.pack(fill=tk.BOTH, expand=True)
        label_imagem = tk.Label(selecionar, bg="black", anchor="nw", image=new_logo_2)
        label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


    def criar_pasta():

        root_folder = Path('C:/Users/installation/Desktop/Geovid Pro/(56x)')
        new_folder = Path(root_folder, inputtxt.get())
        new_folder.mkdir(parents=True, exist_ok=True)

        root_folder_2 = Path('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}'.format(inputtxt.get()))
        new_folder_2 = Path(root_folder_2, "Ajuste do Display e Recetor")
        new_folder_2.mkdir(parents=True, exist_ok=True)


    def iniciar_colimador():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                              AJUSTE DO COLIMADOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_colimador():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_colimador)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_colimador()


        def voltar_colimador():

            pasta = ('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))
            os.rmdir(pasta)

            pasta_2 = ('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}'.format(inputtxt.get()))
            os.rmdir(pasta_2)

            inputtxt.delete(0, 'end')

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL

        def able_registar():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED

        def run():

            global start

            start = datetime.now()

            disable_iniciar()
            able_registar()

            start_blaumowe()

        def registar():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____COLIMADOR' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()
            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o ajuste do\n colimador do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_colimador, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def criar_e_iniciar_colimador():

        criar_pasta()
        iniciar_colimador()


    def iniciar_colocar_anilha():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                         COLOCAÇÃO DE ANILHA", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_anilha():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_anilha)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_anilha()


        def voltar_anilha():

            inputtxt.delete(0, 'end')

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_anilha():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_anilha():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_anilha():

            global start

            start = datetime.now()

            disable_iniciar_anilha()
            able_registar_anilha()

            start_blaumowe()


        def registar_anilha():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____COLOCACAO_ANILHA' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registada a colocação da \n anilha no prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_anilha, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_anilha, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_anilha, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_pos_estufa():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                       VERIFICAÇAO COLIMADOR APÓS ESTUFA", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_pos_estufa():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_pos_estufa)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_pos_estufa()


        def voltar_pos_estufa():

            inputtxt.delete(0, 'end')

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_pos_estufa():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_pos_estufa():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_pos_estufa():

            global start

            start = datetime.now()

            disable_iniciar_pos_estufa()
            able_registar_pos_estufa()

            start_blaumowe()


        def registar_pos_estufa():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____POS_ESTUFA_COLIMADOR' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registada a verificação após estufa\n do colimador do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_pos_estufa, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_pos_estufa, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_pos_estufa, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_reajuste():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(second, text="                              REAJUSTE DO COLIMADOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='BLACK', fg='RED', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_reajuste():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_reajuste)

        font = ('times', 20, 'bold')

        l2 = tk.Label(second, font=font, bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_reajuste()


        def voltar_reajuste():

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            inputtxt.delete(0, 'end')


        def disable_iniciar_reajuste():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_reajuste():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_reajuste():

            global start_2

            start_2 = datetime.now()

            disable_iniciar_reajuste()
            able_registar_reajuste()

            global programa
            global p

            start_blaumowe()


        def registar_reajuste():

            end_2 = datetime.now()

            global adjust_time_reajuste

            adjust_time_reajuste = (end_2 - start_2).total_seconds()

            adjust_time_reajuste_int = int(adjust_time_reajuste)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            path = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(path):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____REAJUSTE_DO_COLIMADOR' + timestr + '____' + str(adjust_time_reajuste_int) + '_seg''.png')
                old_name = path + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                check_existance = os.path.join(dst_dir, os.path.basename(new_name))

                if os.path.exists(check_existance):

                    os.remove(check_existance)

                else:

                    shutil.move(new_name, dst_dir)

            second.forget()
            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do\n colimador do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_reajuste, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_reajuste, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_reajuste, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_display_e_recetor():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(second, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='BLACK', fg='RED', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_display_e_recetor():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_display_e_recetor)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_display_e_recetor()


        def voltar_display_e_recetor():

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            inputtxt.delete(0, 'end')


        def disable_iniciar_display_e_recetor():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_display_e_recetor():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_display_e_recetor():

            global start_1

            start_1 = datetime.now()

            disable_iniciar_display_e_recetor()
            able_registar_display_e_recetor()

            start_blaumowe()


        def registar_display_e_recetor():

            end_1 = datetime.now()

            global adjust_time_display_e_recetor

            adjust_time_display_e_recetor = (end_1 - start_1).total_seconds()

            adjust_time_display_e_recetor_int = int(adjust_time_display_e_recetor)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            path = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(path):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____DISPLAY_E_RECETOR' + timestr + '_____' + str(adjust_time_display_e_recetor_int) + '_seg''.png')

                old_name = path + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                check_existance = os.path.join(dst_dir, os.path.basename(new_name))

                if os.path.exists(check_existance):

                    os.remove(check_existance)

                else:

                    shutil.move(new_name, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o ajuste do display\n e do recetor do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_display_e_recetor, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_display_e_recetor, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_display_e_recetor, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_reajuste_display_e_recetor():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(second, text="                          REAJUSTE DO DISPLAY E RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='BLACK', fg='RED', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_reajuste_display_e_recetor():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_reajuste_display_e_recetor)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_reajuste_display_e_recetor()


        def voltar_reajuste_display_e_recetor():

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            inputtxt.delete(0, 'end')


        def disable_iniciar_reajuste_display_e_recetor():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_reajuste_display_e_recetor():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_reajuste_display_e_recetor():

            global start_2

            start_2 = datetime.now()

            disable_iniciar_reajuste_display_e_recetor()
            able_registar_reajuste_display_e_recetor()

            global programa
            global p

            start_blaumowe()


        def registar_reajuste_display_e_recetor():

            end_2 = datetime.now()

            global adjust_time_reajuste

            adjust_time_reajuste = (end_2 - start_2).total_seconds()

            adjust_time_reajuste_int = int(adjust_time_reajuste)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            path = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(path):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____REAJUSTE_DO_DISPLAY_E_RECETOR' + timestr + '____' + str(adjust_time_reajuste_int) + '_seg''.png')
                old_name = path + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                check_existance = os.path.join(dst_dir, os.path.basename(new_name))

                if os.path.exists(check_existance):

                    os.remove(check_existance)

                else:

                    shutil.move(new_name, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do display\n e do recetor do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_reajuste_display_e_recetor, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_reajuste_display_e_recetor, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_reajuste_display_e_recetor, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def verificação_pasta_criada():

        verificar = Path("C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            messagebox.showerror(title="", message="O colimador do prisma nº {} já foi ajustado!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        else:

            criar_e_iniciar_colimador()


    def verificacao_pasta_criada_anilha():

        verificar = Path("C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor/*_COLOCACAO_ANILHA___*'.format(inputtxt.get())):

                messagebox.showerror(title="", message="A colocação da anilha no\nprisma nº {} já foi realizada!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

            else:

                iniciar_colocar_anilha()

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_reajuste():

        verificar = Path('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                iniciar_reajuste()

            else:

                messagebox.showerror(title="", message="O prisma nº {} ainda não fez a verificação do colimador após estufa!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_pos_estufa():

        verificar = Path('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                messagebox.showerror(title="", message="A verificação do colimador após estufa\n do prisma nº {} já foi realizada!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

            else:

                iniciar_pos_estufa()

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_display_e_recetor():

        verificar = Path('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor/*_DISPLAY_E_RECETOR___*'.format(inputtxt.get())):

                    messagebox.showerror(title="", message="O display e recetor do\n prisma nº {} já foram ajustados!".format(inputtxt.get()))

                    inputtxt.delete(0, 'end')

                else:

                    iniciar_display_e_recetor()

            else:

                messagebox.showerror(title="", message="O prisma nº {} ainda não fez a verificação do colimador após estufa!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_reajuste_display_e_recetor():

        verificar = Path('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                if glob.glob('C:/Users/installation/Desktop/Geovid Pro/(56x)/{}/Ajuste do Display e Recetor/*_DISPLAY_E_RECETOR___*'.format(inputtxt.get())):

                    iniciar_reajuste_display_e_recetor()

                else:

                    messagebox.showerror(title="", message="O display e recetor do prisma nº {}\n ainda não foram ajustados!".format(inputtxt.get()))

                    inputtxt.delete(0, 'end')

            else:

                messagebox.showerror(title="", message="O prisma nº {} ainda não fez a verificação do colimador após estufa!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificar_input_texto():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada()


    def verificar_input_texto_anilha():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificacao_pasta_criada_anilha()


    def verificar_input_texto_reajuste():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_reajuste()


    def verificar_input_texto_pos_estufa():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_pos_estufa()


    def verificar_input_texto_display_e_recetor():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_display_e_recetor()


    def verificar_input_texto_reajuste_display_e_recetor():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_reajuste_display_e_recetor()


    def no_tab(event):

        return 'break'


    def no_enter(event):

        return 'break'


    def no_space(event):

        return 'break'


    selecionar.forget()

    global initial

    initial = tk.Canvas(screen, bg='#d9d9d9')
    initial.pack(fill=tk.BOTH, expand=True)

    frame_ = tk.Frame(initial, bg='#d9d9d9')
    frame_.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(initial, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_2 = tk.Frame(initial, bg='black')
    frame_2.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.7)

    frame_3 = tk.Frame(initial, bg='#8c8c8c')
    frame_3.place(relx=0.205, rely=0.21, relwidth=0.59, relheight=0.68)

    label_ = tk.Label(initial, text="  INSIRA O Nº DO PRISMA:", bg='#8c8c8c', fg='black', font=('Courier', 28, "bold"), anchor='w')
    label_.place(relx=0.35, rely=0.36, relwidth=0.3, relheight=0.08)

    global inputtxt

    v = StringVar()

    inputtxt = Entry(initial, width=19, font=('Courier', 27, "bold"), bg="white", textvariable=v)
    inputtxt.place(relx=0.36, rely=0.445, relwidth=0.275, relheight=0.04)

    inputtxt.bind('<Tab>', no_tab)

    inputtxt.bind('<Return>', no_enter)

    inputtxt.bind('<space>', no_space)


    def verificação_tamanho_numero_prisma(*arg):

        texto = inputtxt.get()

        breaks = texto.count('\n')

        charach_number = len(texto) - breaks

        if (charach_number > 24):

            inputtxt.delete((len(inputtxt.get()) - 1))


    def maiusculas(*arg):

        v.set(inputtxt.get().upper())


    v.trace('w', maiusculas)
    v.trace('w', verificação_tamanho_numero_prisma)

    button_iniciar = tk.Button(initial, text="1º - COLIMADOR", bg='GREEN', fg='WHITE', command=verificar_input_texto, font=('Courier', 18, "bold"))
    button_iniciar.place(relx=0.2875, rely=0.54, relwidth=0.125, relheight=0.09)

    button_pos_estufa = tk.Button(initial, text="2º - VERIFICAÇÃO\n     APÓS ESTUFA", bg='ORANGE', fg='WHITE', command=verificar_input_texto_pos_estufa, font=('Courier', 16, "bold"))
    button_pos_estufa.place(relx=0.4375, rely=0.54, relwidth=0.125, relheight=0.09)

    button_display_recetor = tk.Button(initial, text="3º - DISPLAY E\n   RECETOR", bg='BLUE', fg='WHITE', command=verificar_input_texto_display_e_recetor, font=('Courier', 16, "bold"))
    button_display_recetor.place(relx=0.5875, rely=0.54, relwidth=0.125, relheight=0.09)

    frame_retra = tk.Frame(initial, bg='black')
    frame_retra.place(relx=0.26175, rely=0.6775, relwidth=0.475, relheight=0.18)

    frame_retra2 = tk.Frame(initial, bg='#8c8c8c')
    frame_retra2.place(relx=0.2775, rely=0.7025, relwidth=0.445, relheight=0.13)

    label_ = tk.Label(initial, text="       RETRABALHOS", bg='BLACK', fg='WHITE', font=('Courier', 20, "bold"), anchor='w')
    label_.place(relx=0.3925, rely=0.6805, relwidth=0.3, relheight=0.02)

    button_anilha = tk.Button(initial, text="COLOCAÇÃO\nDE ANILHA", bg='#F1DA15', fg='BLACK', command=verificar_input_texto_anilha, font=('Courier', 16, "bold"))
    button_anilha.place(relx=0.2975, rely=0.7225, relwidth=0.105, relheight=0.09)

    button_readjust_colimador = tk.Button(initial, text="REAJUSTAR\nCOLIMADOR", bg='#F1DA15', fg='BLACK', command=verificar_input_texto_reajuste, font=('Courier', 16, "bold"))
    button_readjust_colimador.place(relx=0.4475, rely=0.7225, relwidth=0.105, relheight=0.09)

    button_readjust_display = tk.Button(initial, text="REAJUSTAR\nDISPLAY E\nRECETOR", bg='#F1DA15', fg='BLACK', command=verificar_input_texto_reajuste_display_e_recetor, font=('Courier', 16, "bold"))
    button_readjust_display.place(relx=0.5975, rely=0.7225, relwidth=0.105, relheight=0.09)

    button_mudar_modelo = tk.Button(initial, text="MUDAR\nMODELO", bg='GREEN', fg='white', command=voltar_modelo_56, state=NORMAL, font=('Courier', 20, "bold"))
    button_mudar_modelo.place(relx=0.8, rely=0.005, relwidth=0.098, relheight=0.071)

    button_log_out = tk.Button(initial, text="TERMINAR\nSESSÃO", bg='#FE001B', fg='white', command=voltar_inicial, state=NORMAL, font=('Courier', 20, "bold"))
    button_log_out.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    label_username = tk.Label(initial, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
    label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def tempo_master2():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_master2)


    font = ('times', 20, 'bold')
    l2 = tk.Label(screen, font=font, bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_master2()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    label_imagem = tk.Label(initial, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


def master_2_com_56():


    def voltar_inicial():

        inputtxt.delete(0, 'end')
        initial.forget()
        screen1.pack(fill=tk.BOTH, expand=True)


    def voltar_modelo_56():

        inputtxt.delete(0, 'end')
        initial.forget()
        selecionar.pack(fill=tk.BOTH, expand=True)
        label_imagem = tk.Label(selecionar, bg="black", anchor="nw", image=new_logo_2)
        label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


    def criar_pasta():

        root_folder = Path('C:/Users/installation/Desktop/Geovid .COM/(56x)')
        new_folder = Path(root_folder, inputtxt.get())
        new_folder.mkdir(parents=True, exist_ok=True)

        root_folder_2 = Path('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}'.format(inputtxt.get()))
        new_folder_2 = Path(root_folder_2, "Ajuste do Display e Recetor")
        new_folder_2.mkdir(parents=True, exist_ok=True)


    def iniciar_colimador():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                              AJUSTE DO COLIMADOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_colimador():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_colimador)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_colimador()

        def voltar_colimador():

            pasta = ('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))
            os.rmdir(pasta)

            pasta_2 = ('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}'.format(inputtxt.get()))
            os.rmdir(pasta_2)

            inputtxt.delete(0, 'end')

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED

        def run():

            global start

            start = datetime.now()

            disable_iniciar()
            able_registar()

            start_blaumowe()


        def registar():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____COLIMADOR' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()
            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o ajuste do\n colimador do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_colimador, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def criar_e_iniciar_colimador():

        criar_pasta()
        iniciar_colimador()


    def iniciar_colocar_anilha():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                         COLOCAÇÃO DE ANILHA", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_anilha():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_anilha)


        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_anilha()


        def voltar_anilha():

            inputtxt.delete(0, 'end')

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_anilha():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_anilha():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_anilha():

            global start

            start = datetime.now()

            disable_iniciar_anilha()
            able_registar_anilha()

            start_blaumowe()


        def registar_anilha():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____COLOCACAO_ANILHA' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registada a colocação da \n anilha no prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_anilha, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_anilha, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_anilha, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_pos_estufa():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                       VERIFICAÇAO COLIMADOR APÓS ESTUFA", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_pos_estufa():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_pos_estufa)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_pos_estufa()


        def voltar_pos_estufa():

            inputtxt.delete(0, 'end')

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_pos_estufa():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_pos_estufa():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_pos_estufa():

            global start

            start = datetime.now()

            disable_iniciar_pos_estufa()
            able_registar_pos_estufa()

            start_blaumowe()


        def registar_pos_estufa():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____POS_ESTUFA_COLIMADOR' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registada a verificação após estufa\n do colimador do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_pos_estufa, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_pos_estufa, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_pos_estufa, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_reajuste():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(second, text="                              REAJUSTE DO COLIMADOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='BLACK', fg='RED', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_reajuste():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_reajuste)

        font = ('times', 20, 'bold')

        l2 = tk.Label(second, font=font, bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_reajuste()


        def voltar_reajuste():

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            inputtxt.delete(0, 'end')


        def disable_iniciar_reajuste():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_reajuste():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_reajuste():

            global start_2

            start_2 = datetime.now()

            disable_iniciar_reajuste()
            able_registar_reajuste()

            global programa
            global p

            start_blaumowe()


        def registar_reajuste():

            end_2 = datetime.now()

            global adjust_time_reajuste

            adjust_time_reajuste = (end_2 - start_2).total_seconds()

            adjust_time_reajuste_int = int(adjust_time_reajuste)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            path = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(path):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____REAJUSTE_DO_COLIMADOR' + timestr + '____' + str(adjust_time_reajuste_int) + '_seg''.png')
                old_name = path + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                check_existance = os.path.join(dst_dir, os.path.basename(new_name))

                if os.path.exists(check_existance):

                    os.remove(check_existance)

                else:

                    shutil.move(new_name, dst_dir)

            second.forget()
            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do\n colimador do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_reajuste, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_reajuste, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_reajuste, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_display_e_recetor():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(second, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='BLACK', fg='RED', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_display_e_recetor():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_display_e_recetor)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_display_e_recetor()


        def voltar_display_e_recetor():

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            inputtxt.delete(0, 'end')


        def disable_iniciar_display_e_recetor():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_display_e_recetor():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_display_e_recetor():

            global start_1

            start_1 = datetime.now()

            disable_iniciar_display_e_recetor()
            able_registar_display_e_recetor()

            start_blaumowe()


        def registar_display_e_recetor():

            end_1 = datetime.now()

            global adjust_time_display_e_recetor

            adjust_time_display_e_recetor = (end_1 - start_1).total_seconds()

            adjust_time_display_e_recetor_int = int(adjust_time_display_e_recetor)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            path = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(path):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____DISPLAY_E_RECETOR' + timestr + '_____' + str(adjust_time_display_e_recetor_int) + '_seg''.png')

                old_name = path + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                check_existance = os.path.join(dst_dir, os.path.basename(new_name))

                if os.path.exists(check_existance):

                    os.remove(check_existance)

                else:

                    shutil.move(new_name, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o ajuste do display\n e do recetor do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_display_e_recetor, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_display_e_recetor, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_display_e_recetor, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def iniciar_reajuste_display_e_recetor():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(second, text="                          REAJUSTE DO DISPLAY E RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" PRISMA nº {}".format(inputtxt.get()), bg='BLACK', fg='RED', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_reajuste_display_e_recetor():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_reajuste_display_e_recetor)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_reajuste_display_e_recetor()


        def voltar_reajuste_display_e_recetor():

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            inputtxt.delete(0, 'end')


        def disable_iniciar_reajuste_display_e_recetor():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_reajuste_display_e_recetor():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_reajuste_display_e_recetor():

            global start_2

            start_2 = datetime.now()

            disable_iniciar_reajuste_display_e_recetor()
            able_registar_reajuste_display_e_recetor()

            global programa
            global p

            start_blaumowe()


        def registar_reajuste_display_e_recetor():

            end_2 = datetime.now()

            global adjust_time_reajuste

            adjust_time_reajuste = (end_2 - start_2).total_seconds()

            adjust_time_reajuste_int = int(adjust_time_reajuste)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            path = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(path):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____REAJUSTE_DO_DISPLAY_E_RECETOR' + timestr + '____' + str(adjust_time_reajuste_int) + '_seg''.png')
                old_name = path + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                check_existance = os.path.join(dst_dir, os.path.basename(new_name))

                if os.path.exists(check_existance):

                    os.remove(check_existance)

                else:

                    shutil.move(new_name, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do display\n e do recetor do prisma nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_reajuste_display_e_recetor, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_reajuste_display_e_recetor, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_reajuste_display_e_recetor, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def verificação_pasta_criada():

        verificar = Path("C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            messagebox.showerror(title="", message="O colimador do prisma nº {} já foi ajustado!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        else:

            criar_e_iniciar_colimador()


    def verificacao_pasta_criada_anilha():

        verificar = Path("C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor/*_COLOCACAO_ANILHA___*'.format(inputtxt.get())):

                messagebox.showerror(title="", message="A colocação da anilha no\nprisma nº {} já foi realizada!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

            else:

                iniciar_colocar_anilha()

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_reajuste():

        verificar = Path('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                iniciar_reajuste()

            else:

                messagebox.showerror(title="", message="O prisma nº {} ainda não fez a verificação do colimador após estufa!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_pos_estufa():

        verificar = Path('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                messagebox.showerror(title="", message="A verificação do colimador após estufa\n do prisma nº {} já foi realizada!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

            else:

                iniciar_pos_estufa()

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_display_e_recetor():

        verificar = Path('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor/*_DISPLAY_E_RECETOR___*'.format(inputtxt.get())):

                    messagebox.showerror(title="", message="O display e recetor do\n prisma nº {} já foram ajustados!".format(inputtxt.get()))

                    inputtxt.delete(0, 'end')

                else:

                    iniciar_display_e_recetor()

            else:

                messagebox.showerror(title="", message="O prisma nº {} ainda não fez a verificação do colimador após estufa!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificação_pasta_criada_reajuste_display_e_recetor():

        verificar = Path('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

        if verificar.exists():

            if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor/*_POS_ESTUFA_COLIMADOR___*'.format(inputtxt.get())):

                if glob.glob('C:/Users/installation/Desktop/Geovid .COM/(56x)/{}/Ajuste do Display e Recetor/*_DISPLAY_E_RECETOR___*'.format(inputtxt.get())):

                    iniciar_reajuste_display_e_recetor()

                else:

                    messagebox.showerror(title="", message="O display e recetor do prisma nº {}\n ainda não foram ajustados!".format(inputtxt.get()))

                    inputtxt.delete(0, 'end')

            else:

                messagebox.showerror(title="", message="O prisma nº {} ainda não fez a verificação do colimador após estufa!".format(inputtxt.get()))

                inputtxt.delete(0, 'end')

        else:

            messagebox.showerror(title="", message="O prisma nº {} ainda não tem registo!\nPor favor inicie um novo registo!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')


    def verificar_input_texto():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada()


    def verificar_input_texto_anilha():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificacao_pasta_criada_anilha()


    def verificar_input_texto_reajuste():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_reajuste()


    def verificar_input_texto_pos_estufa():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_pos_estufa()


    def verificar_input_texto_display_e_recetor():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_display_e_recetor()


    def verificar_input_texto_reajuste_display_e_recetor():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do prisma!")

        else:

            verificação_pasta_criada_reajuste_display_e_recetor()


    def no_tab(event):

        return 'break'


    def no_enter(event):

        return 'break'


    def no_space(event):

        return 'break'


    selecionar.forget()

    global initial

    initial = tk.Canvas(screen, bg='#d9d9d9')
    initial.pack(fill=tk.BOTH, expand=True)

    frame_ = tk.Frame(initial, bg='#d9d9d9')
    frame_.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(initial, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_2 = tk.Frame(initial, bg='black')
    frame_2.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.7)

    frame_3 = tk.Frame(initial, bg='#8c8c8c')
    frame_3.place(relx=0.205, rely=0.21, relwidth=0.59, relheight=0.68)

    label_ = tk.Label(initial, text="  INSIRA O Nº DO PRISMA:", bg='#8c8c8c', fg='black', font=('Courier', 28, "bold"), anchor='w')
    label_.place(relx=0.35, rely=0.36, relwidth=0.3, relheight=0.08)

    global inputtxt

    v = StringVar()

    inputtxt = Entry(initial, width=19, font=('Courier', 27, "bold"), bg="white", textvariable=v)
    inputtxt.place(relx=0.36, rely=0.445, relwidth=0.275, relheight=0.04)

    inputtxt.bind('<Tab>', no_tab)

    inputtxt.bind('<Return>', no_enter)

    inputtxt.bind('<space>', no_space)


    def verificação_tamanho_numero_prisma(*arg):

        texto = inputtxt.get()

        breaks = texto.count('\n')

        charach_number = len(texto) - breaks

        if (charach_number > 24):

            inputtxt.delete((len(inputtxt.get()) - 1))


    def maiusculas(*arg):

        v.set(inputtxt.get().upper())

    v.trace('w', maiusculas)
    v.trace('w', verificação_tamanho_numero_prisma)

    button_iniciar = tk.Button(initial, text="1º - COLIMADOR", bg='GREEN', fg='WHITE', command=verificar_input_texto, font=('Courier', 18, "bold"))
    button_iniciar.place(relx=0.2875, rely=0.54, relwidth=0.125, relheight=0.09)

    button_pos_estufa = tk.Button(initial, text="2º - VERIFICAÇÃO\n     APÓS ESTUFA", bg='ORANGE', fg='WHITE', command=verificar_input_texto_pos_estufa, font=('Courier', 16, "bold"))
    button_pos_estufa.place(relx=0.4375, rely=0.54, relwidth=0.125, relheight=0.09)

    button_display_recetor = tk.Button(initial, text="3º - DISPLAY E\n   RECETOR", bg='BLUE', fg='WHITE', command=verificar_input_texto_display_e_recetor, font=('Courier', 16, "bold"))
    button_display_recetor.place(relx=0.5875, rely=0.54, relwidth=0.125, relheight=0.09)

    frame_retra = tk.Frame(initial, bg='black')
    frame_retra.place(relx=0.26175, rely=0.6775, relwidth=0.475, relheight=0.18)

    frame_retra2 = tk.Frame(initial, bg='#8c8c8c')
    frame_retra2.place(relx=0.2775, rely=0.7025, relwidth=0.445, relheight=0.13)

    label_ = tk.Label(initial, text="       RETRABALHOS", bg='BLACK', fg='WHITE', font=('Courier', 20, "bold"), anchor='w')
    label_.place(relx=0.3925, rely=0.6805, relwidth=0.3, relheight=0.02)

    button_anilha = tk.Button(initial, text="COLOCAÇÃO\nDE ANILHA", bg='#F1DA15', fg='BLACK', command=verificar_input_texto_anilha, font=('Courier', 16, "bold"))
    button_anilha.place(relx=0.2975, rely=0.7225, relwidth=0.105, relheight=0.09)

    button_readjust_colimador = tk.Button(initial, text="REAJUSTAR\nCOLIMADOR", bg='#F1DA15', fg='BLACK', command=verificar_input_texto_reajuste, font=('Courier', 16, "bold"))
    button_readjust_colimador.place(relx=0.4475, rely=0.7225, relwidth=0.105, relheight=0.09)

    button_readjust_display = tk.Button(initial, text="REAJUSTAR\nDISPLAY E\nRECETOR", bg='#F1DA15', fg='BLACK', command=verificar_input_texto_reajuste_display_e_recetor, font=('Courier', 16, "bold"))
    button_readjust_display.place(relx=0.5975, rely=0.7225, relwidth=0.105, relheight=0.09)

    button_mudar_modelo = tk.Button(initial, text="MUDAR\nMODELO", bg='GREEN', fg='white', command=voltar_modelo_56, state=NORMAL, font=('Courier', 20, "bold"))
    button_mudar_modelo.place(relx=0.8, rely=0.005, relwidth=0.098, relheight=0.071)

    button_log_out = tk.Button(initial, text="TERMINAR\nSESSÃO", bg='#FE001B', fg='white', command=voltar_inicial, state=NORMAL, font=('Courier', 20, "bold"))
    button_log_out.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    label_username = tk.Label(initial, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
    label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def tempo_master2():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_master2)

    font = ('times', 20, 'bold')
    l2 = tk.Label(screen, font=font, bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_master2()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    label_imagem = tk.Label(initial, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


def master_2_st_pro_56():

    def voltar_inicial():

        inputtxt.delete(0, 'end')
        initial.forget()
        screen1.pack(fill=tk.BOTH, expand=True)


    def voltar_modelo_56():

        inputtxt.delete(0, 'end')
        initial.forget()
        selecionar.pack(fill=tk.BOTH, expand=True)
        label_imagem = tk.Label(selecionar, bg="black", anchor="nw", image=new_logo_2)
        label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


    def criar_pasta_serv_tecnico_56():

        root_folder = Path('C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(56x)')
        new_folder = Path(root_folder, inputtxt.get())
        new_folder.mkdir(parents=True, exist_ok=True)

        root_folder_2 = Path('C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(56x)/{}'.format(inputtxt.get()))
        new_folder_2 = Path(root_folder_2, "Ajuste do Display e Recetor")
        new_folder_2.mkdir(parents=True, exist_ok=True)


    def iniciar_reajuste_serv_tecnico_56():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                            REAJUSTE SERVIÇO TÉCNICO", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" BINÓCULO nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_serv_tecnico():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_serv_tecnico)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_serv_tecnico()


        def voltar_serv_tecnico():

            path = ('C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

            dir = os.listdir(path)

            if len(dir) == 0:

                pasta = ('C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))
                os.rmdir(pasta)

                pasta_2 = ('C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(56x)/{}'.format(inputtxt.get()))
                os.rmdir(pasta_2)

                inputtxt.delete(0, 'end')

                second.forget()

                initial.pack(fill=tk.BOTH, expand=True)

            else:

                inputtxt.delete(0, 'end')

                second.forget()

                initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_serv_tecnico():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_serv_tecnico():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_serv_tecnico():

            global start

            start = datetime.now()

            disable_iniciar_serv_tecnico()
            able_registar_serv_tecnico()

            start_blaumowe_serv_tecnico()


        def registar_serv_tecnico():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____REAJUSTE_SERVIÇO_TECNICO' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do serviço\n técnico do binóculo nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_serv_tecnico, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_serv_tecnico, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_serv_tecnico, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def criar_e_iniciar_reajuste_serv_tecnico_56():

        criar_pasta_serv_tecnico_56()
        iniciar_reajuste_serv_tecnico_56()


    def verificacao_pasta_criada_serv_tecnico_56():

        verificar = Path("C:/Users/installation/Desktop/Geovid Pro/Servico Tecnico/(56x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            iniciar_reajuste_serv_tecnico_56()

        else:

            criar_e_iniciar_reajuste_serv_tecnico_56()


    def verificar_input_texto_serv_tecnico():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do binóculo!")

        else:

            verificacao_pasta_criada_serv_tecnico_56()


    def no_tab(event):

        return 'break'


    def no_enter(event):

        return 'break'


    def no_space(event):

        return 'break'

    selecionar.forget()

    global initial

    initial = tk.Canvas(screen, bg='#d9d9d9')
    initial.pack(fill=tk.BOTH, expand=True)

    frame_ = tk.Frame(initial, bg='#d9d9d9')
    frame_.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(initial, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_2 = tk.Frame(initial, bg='black')
    frame_2.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.6)

    frame_3 = tk.Frame(initial, bg='#8c8c8c')
    frame_3.place(relx=0.255, rely=0.26, relwidth=0.49, relheight=0.58)

    label_ = tk.Label(initial, text=" INSIRA O Nº DO BINÓCULO:", bg='#8c8c8c', fg='black', font=('Courier', 28, "bold"), anchor='w')
    label_.place(relx=0.35, rely=0.45, relwidth=0.3, relheight=0.08)

    global inputtxt

    v = StringVar()

    inputtxt = Entry(initial, width=19, font=('Courier', 27, "bold"), bg="white", textvariable=v)
    inputtxt.place(relx=0.36, rely=0.56, relwidth=0.275, relheight=0.04)

    inputtxt.bind('<Tab>', no_tab)

    inputtxt.bind('<Return>', no_enter)

    inputtxt.bind('<space>', no_space)


    def verificação_tamanho_numero_prisma(*arg):

        texto = inputtxt.get()

        breaks = texto.count('\n')

        charach_number = len(texto) - breaks

        if (charach_number > 24):

            inputtxt.delete((len(inputtxt.get()) - 1))


    def maiusculas(*arg):

        v.set(inputtxt.get().upper())

    v.trace('w', maiusculas)
    v.trace('w', verificação_tamanho_numero_prisma)

    button_avancar = tk.Button(initial, text="AVANÇAR", bg='GREEN', fg='WHITE', command=verificar_input_texto_serv_tecnico, font=('Courier', 18, "bold"))
    button_avancar.place(relx=0.4375, rely=0.69, relwidth=0.125, relheight=0.09)

    button_mudar_modelo_56 = tk.Button(initial, text="MUDAR\nMODELO", bg='GREEN', fg='white', command=voltar_modelo_56, state=NORMAL, font=('Courier', 20, "bold"))
    button_mudar_modelo_56.place(relx=0.8, rely=0.005, relwidth=0.098, relheight=0.071)

    button_log_out = tk.Button(initial, text="TERMINAR\nSESSÃO", bg='RED', fg='white', command=voltar_inicial, state=NORMAL, font=('Courier', 20, "bold"))
    button_log_out.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    label_username = tk.Label(initial, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
    label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def tempo_master():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_master)

    l2 = tk.Label(screen, font=('times', 20, 'bold'), bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_master()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    global label_imagem

    label_imagem = tk.Label(initial, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


def master_2_st_com_56():

    def voltar_inicial():

        inputtxt.delete(0, 'end')
        initial.forget()
        screen1.pack(fill=tk.BOTH, expand=True)


    def voltar_modelo_56():

        inputtxt.delete(0, 'end')
        initial.forget()
        selecionar.pack(fill=tk.BOTH, expand=True)
        label_imagem = tk.Label(selecionar, bg="black", anchor="nw", image=new_logo_2)
        label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


    def criar_pasta_serv_tecnico_56():

        root_folder = Path('C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(56x)')
        new_folder = Path(root_folder, inputtxt.get())
        new_folder.mkdir(parents=True, exist_ok=True)

        root_folder_2 = Path('C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(56x)/{}'.format(inputtxt.get()))
        new_folder_2 = Path(root_folder_2, "Ajuste do Display e Recetor")
        new_folder_2.mkdir(parents=True, exist_ok=True)


    def iniciar_reajuste_serv_tecnico_56():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                            REAJUSTE SERVIÇO TÉCNICO", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" BINÓCULO nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_serv_tecnico():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_serv_tecnico)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_serv_tecnico()


        def voltar_serv_tecnico():

            path = ('C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

            dir = os.listdir(path)

            if len(dir) == 0:

                pasta = ('C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))
                os.rmdir(pasta)

                pasta_2 = ('C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(56x)/{}'.format(inputtxt.get()))
                os.rmdir(pasta_2)

                inputtxt.delete(0, 'end')

                second.forget()

                initial.pack(fill=tk.BOTH, expand=True)

            else:

                inputtxt.delete(0, 'end')

                second.forget()

                initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_serv_tecnico():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_serv_tecnico():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_serv_tecnico():

            global start

            start = datetime.now()

            disable_iniciar_serv_tecnico()
            able_registar_serv_tecnico()

            start_blaumowe_serv_tecnico()


        def registar_serv_tecnico():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____REAJUSTE_SERVIÇO_TECNICO' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do serviço\n técnico do binóculo nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_serv_tecnico, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_serv_tecnico, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_serv_tecnico, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def criar_e_iniciar_reajuste_serv_tecnico_56():

        criar_pasta_serv_tecnico_56()
        iniciar_reajuste_serv_tecnico_56()


    def verificacao_pasta_criada_serv_tecnico_56():

        verificar = Path("C:/Users/installation/Desktop/Geovid .COM/Servico Tecnico/(56x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            iniciar_reajuste_serv_tecnico_56()

        else:

            criar_e_iniciar_reajuste_serv_tecnico_56()


    def verificar_input_texto_serv_tecnico():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do binóculo!")

        else:

            verificacao_pasta_criada_serv_tecnico_56()


    def no_tab(event):

        return 'break'


    def no_enter(event):

        return 'break'


    def no_space(event):

        return 'break'

    selecionar.forget()

    global initial

    initial = tk.Canvas(screen, bg='#d9d9d9')
    initial.pack(fill=tk.BOTH, expand=True)

    frame_ = tk.Frame(initial, bg='#d9d9d9')
    frame_.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(initial, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_2 = tk.Frame(initial, bg='black')
    frame_2.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.6)

    frame_3 = tk.Frame(initial, bg='#8c8c8c')
    frame_3.place(relx=0.255, rely=0.26, relwidth=0.49, relheight=0.58)

    label_ = tk.Label(initial, text=" INSIRA O Nº DO BINÓCULO:", bg='#8c8c8c', fg='black', font=('Courier', 28, "bold"), anchor='w')
    label_.place(relx=0.35, rely=0.45, relwidth=0.3, relheight=0.08)

    global inputtxt

    v = StringVar()

    inputtxt = Entry(initial, width=19, font=('Courier', 27, "bold"), bg="white", textvariable=v)
    inputtxt.place(relx=0.36, rely=0.56, relwidth=0.275, relheight=0.04)

    inputtxt.bind('<Tab>', no_tab)

    inputtxt.bind('<Return>', no_enter)

    inputtxt.bind('<space>', no_space)


    def verificação_tamanho_numero_prisma(*arg):

        texto = inputtxt.get()

        breaks = texto.count('\n')

        charach_number = len(texto) - breaks

        if (charach_number > 24):

            inputtxt.delete((len(inputtxt.get()) - 1))


    def maiusculas(*arg):

        v.set(inputtxt.get().upper())

    v.trace('w', maiusculas)
    v.trace('w', verificação_tamanho_numero_prisma)

    button_avancar = tk.Button(initial, text="AVANÇAR", bg='GREEN', fg='WHITE', command=verificar_input_texto_serv_tecnico, font=('Courier', 18, "bold"))
    button_avancar.place(relx=0.4375, rely=0.69, relwidth=0.125, relheight=0.09)

    button_mudar_modelo_56 = tk.Button(initial, text="MUDAR\nMODELO", bg='GREEN', fg='white', command=voltar_modelo_56, state=NORMAL, font=('Courier', 20, "bold"))
    button_mudar_modelo_56.place(relx=0.8, rely=0.005, relwidth=0.098, relheight=0.071)

    button_log_out = tk.Button(initial, text="TERMINAR\nSESSÃO", bg='RED', fg='white', command=voltar_inicial, state=NORMAL, font=('Courier', 20, "bold"))
    button_log_out.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    label_username = tk.Label(initial, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
    label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def tempo_master():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_master)

    l2 = tk.Label(screen, font=('times', 20, 'bold'), bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_master()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    global label_imagem

    label_imagem = tk.Label(initial, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


def master_2_st_hdr_56():

    def voltar_inicial():

        inputtxt.delete(0, 'end')
        initial.forget()
        screen1.pack(fill=tk.BOTH, expand=True)


    def voltar_modelo_56():

        inputtxt.delete(0, 'end')
        initial.forget()
        selecionar.pack(fill=tk.BOTH, expand=True)
        label_imagem = tk.Label(selecionar, bg="black", anchor="nw", image=new_logo_2)
        label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


    def criar_pasta_serv_tecnico_56():

        root_folder = Path('C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(56x)')
        new_folder = Path(root_folder, inputtxt.get())
        new_folder.mkdir(parents=True, exist_ok=True)

        root_folder_2 = Path('C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(56x)/{}'.format(inputtxt.get()))
        new_folder_2 = Path(root_folder_2, "Ajuste do Display e Recetor")
        new_folder_2.mkdir(parents=True, exist_ok=True)


    def iniciar_reajuste_serv_tecnico_56():

        initial.forget()

        second = tk.Canvas(screen, bg='#d9d9d9')
        second.pack(fill=tk.BOTH, expand=True)
        second.update()

        label = tk.Label(second, text="                            REAJUSTE SERVIÇO TÉCNICO", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
        label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        label_info = tk.Label(second, text=" BINÓCULO nº {}".format(inputtxt.get()), bg='black', fg='red', font=('Courier', 18, "bold"), anchor='w')
        label_info.place(relx=0.002, rely=0.005, relwidth=0.275, relheight=0.071)


        def tempo_serv_tecnico():

            time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
            l2.config(text=time_string)
            l2.after(1000, tempo_serv_tecnico)

        l2 = tk.Label(second, font=('times', 20, 'bold'), bg='#d9d9d9')
        l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

        tempo_serv_tecnico()


        def voltar_serv_tecnico():

            path = ('C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

            dir = os.listdir(path)

            if len(dir) == 0:

                pasta = ('C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))
                os.rmdir(pasta)

                pasta_2 = ('C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(56x)/{}'.format(inputtxt.get()))
                os.rmdir(pasta_2)

                inputtxt.delete(0, 'end')

                second.forget()

                initial.pack(fill=tk.BOTH, expand=True)

            else:

                inputtxt.delete(0, 'end')

                second.forget()

                initial.pack(fill=tk.BOTH, expand=True)


        def disable_iniciar_serv_tecnico():

            if (button_start['state'] == tk.NORMAL):

                button_start['state'] = tk.DISABLED
                button_back['state'] = tk.DISABLED

            else:

                button_start['state'] = tk.NORMAL
                button_back['state'] = tk.NORMAL


        def able_registar_serv_tecnico():

            if (button_regist['state'] == tk.DISABLED):

                button_regist['state'] = tk.NORMAL

            else:

                button_regist['state'] = tk.DISABLED


        def run_serv_tecnico():

            global start

            start = datetime.now()

            disable_iniciar_serv_tecnico()
            able_registar_serv_tecnico()

            start_blaumowe_serv_tecnico()


        def registar_serv_tecnico():

            end = datetime.now()

            global adjust_time_colimador

            adjust_time_colimador = (end - start).total_seconds()

            adjust_time_colimador_int = int(adjust_time_colimador)

            timestr = time.strftime('____%d %m %Y____%H %M %S')

            LOC = 'C:/Users/installation/Desktop/Print (56x)/'

            for filename in os.listdir(LOC):

                new_name = ('C:/Users/installation/Desktop/Print (56x)/' + username1 + '____REAJUSTE_SERVIÇO_TECNICO' + timestr + '____' + str(adjust_time_colimador_int) + '_seg''.png')

                old_name = LOC + filename

                os.rename(old_name, new_name)

                src_dir = ('C:/Users/installation/Desktop/Print (56x)')
                dst_dir = ('C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(56x)/{}/Ajuste do Display e Recetor'.format(inputtxt.get()))

                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)

            second.forget()

            initial.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Foi registado o reajuste do serviço\n técnico do binóculo nº {}!".format(inputtxt.get()))

            inputtxt.delete(0, 'end')

        button_start = tk.Button(second, text="INICIAR", bg='green', fg='white', command=run_serv_tecnico, state=NORMAL, font=('Courier', 30, "bold"))
        button_start.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.30)

        button_regist = tk.Button(second, text="REGISTAR", bg='blue', fg='white', command=registar_serv_tecnico, state=DISABLED, font=('Courier', 30, "bold"))
        button_regist.place(relx=0.725, rely=0.55, relwidth=0.2, relheight=0.30)

        button_back = tk.Button(second, text="VOLTAR", bg='RED', fg='white', command=voltar_serv_tecnico, state=NORMAL, font=('Courier', 20, "bold"))
        button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

        label_username = tk.Label(second, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
        label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def criar_e_iniciar_reajuste_serv_tecnico_56():

        criar_pasta_serv_tecnico_56()
        iniciar_reajuste_serv_tecnico_56()


    def verificacao_pasta_criada_serv_tecnico_56():

        verificar = Path("C:/Users/installation/Desktop/Geovid HD-R/Servico Tecnico/(56x)/{}/".format(inputtxt.get()))

        if verificar.exists():

            iniciar_reajuste_serv_tecnico_56()

        else:

            criar_e_iniciar_reajuste_serv_tecnico_56()


    def verificar_input_texto_serv_tecnico():

        TEXTO = inputtxt.get()

        if str(inputtxt.get()) == "":

            messagebox.showerror(title="", message="Insira o nº do binóculo!")

        else:

            verificacao_pasta_criada_serv_tecnico_56()


    def no_tab(event):

        return 'break'


    def no_enter(event):

        return 'break'


    def no_space(event):

        return 'break'

    selecionar.forget()

    global initial

    initial = tk.Canvas(screen, bg='#d9d9d9')
    initial.pack(fill=tk.BOTH, expand=True)

    frame_ = tk.Frame(initial, bg='#d9d9d9')
    frame_.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(initial, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_2 = tk.Frame(initial, bg='black')
    frame_2.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.6)

    frame_3 = tk.Frame(initial, bg='#8c8c8c')
    frame_3.place(relx=0.255, rely=0.26, relwidth=0.49, relheight=0.58)

    label_ = tk.Label(initial, text=" INSIRA O Nº DO BINÓCULO:", bg='#8c8c8c', fg='black', font=('Courier', 28, "bold"), anchor='w')
    label_.place(relx=0.35, rely=0.45, relwidth=0.3, relheight=0.08)

    global inputtxt

    v = StringVar()

    inputtxt = Entry(initial, width=19, font=('Courier', 27, "bold"), bg="white", textvariable=v)
    inputtxt.place(relx=0.36, rely=0.56, relwidth=0.275, relheight=0.04)

    inputtxt.bind('<Tab>', no_tab)

    inputtxt.bind('<Return>', no_enter)

    inputtxt.bind('<space>', no_space)


    def verificação_tamanho_numero_prisma(*arg):

        texto = inputtxt.get()

        breaks = texto.count('\n')

        charach_number = len(texto) - breaks

        if (charach_number > 24):

            inputtxt.delete((len(inputtxt.get()) - 1))


    def maiusculas(*arg):

        v.set(inputtxt.get().upper())

    v.trace('w', maiusculas)
    v.trace('w', verificação_tamanho_numero_prisma)

    button_avancar = tk.Button(initial, text="AVANÇAR", bg='GREEN', fg='WHITE', command=verificar_input_texto_serv_tecnico, font=('Courier', 18, "bold"))
    button_avancar.place(relx=0.4375, rely=0.69, relwidth=0.125, relheight=0.09)

    button_mudar_modelo_56 = tk.Button(initial, text="MUDAR\nMODELO", bg='GREEN', fg='white', command=voltar_modelo_56, state=NORMAL, font=('Courier', 20, "bold"))
    button_mudar_modelo_56.place(relx=0.8, rely=0.005, relwidth=0.098, relheight=0.071)

    button_log_out = tk.Button(initial, text="TERMINAR\nSESSÃO", bg='RED', fg='white', command=voltar_inicial, state=NORMAL, font=('Courier', 20, "bold"))
    button_log_out.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    label_username = tk.Label(initial, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
    label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


    def tempo_master():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_master)

    l2 = tk.Label(screen, font=('times', 20, 'bold'), bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_master()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    global label_imagem

    label_imagem = tk.Label(initial, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


def button_text_pro_56():

    label_modelo_pro_42 = tk.Label(initial, text=pro_56, bg='#8c8c8c', fg='WHITE', font=('Courier', 41, "bold"), anchor='w')
    label_modelo_pro_42.place(relx=0.36, rely=0.25, relwidth=0.3, relheight=0.09)


def button_text_com_56():

    label_modelo_pro_42 = tk.Label(initial, text=com_56, bg='#8c8c8c', fg='WHITE', font=('Courier', 41, "bold"), anchor='w')
    label_modelo_pro_42.place(relx=0.36, rely=0.25, relwidth=0.3, relheight=0.09)


def button_text_pro_56_st():

    label_modelo_pro_42 = tk.Label(initial, text=pro_56_st, bg='#8c8c8c', fg='WHITE', font=('Courier', 41, "bold"), anchor='w')
    label_modelo_pro_42.place(relx=0.36, rely=0.28, relwidth=0.3, relheight=0.09)


def button_text_com_56_st():

    label_modelo_pro_42 = tk.Label(initial, text=com_56_st, bg='#8c8c8c', fg='WHITE', font=('Courier', 41, "bold"), anchor='w')
    label_modelo_pro_42.place(relx=0.36, rely=0.28, relwidth=0.3, relheight=0.09)


def button_text_hdr_56_st():

    label_modelo_pro_42 = tk.Label(initial, text=hdr_56_st, bg='#8c8c8c', fg='WHITE', font=('Courier', 41, "bold"), anchor='w')
    label_modelo_pro_42.place(relx=0.36, rely=0.28, relwidth=0.3, relheight=0.09)


def check_up_42_f():


    def voltar_inicio_42():
        screen4.forget()
        selecionar.pack(fill=tk.BOTH, expand=True)


    def tempo_check_42():
        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_check_42)


    def visualizar_42():
        check_up_42()


    selecionar.forget()

    screen4 = tk.Canvas(screen, bg='#d9d9d9')
    screen4.pack(fill=tk.BOTH, expand=True)
    screen4.update()

    label_screen1 = tk.Label(screen4, text="                              CHECK-UP PRISMA (42x)", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label_screen1.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    Button_Back = tk.Button(screen4, text="VOLTAR", bg='#FE001B', fg="white", command=voltar_inicio_42, font=('Courier', 20, "bold"))
    Button_Back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    Button_Visualisar_42 = tk.Button(screen4, text="ABRIR", bg='GREEN', fg="white", command=visualizar_42, font=('Courier', 20, "bold"))
    Button_Visualisar_42.place(relx=0.002, rely=0.005, relwidth=0.098, relheight=0.071)

    l2 = tk.Label(screen4, font=font, bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_check_42()


def check_up_56_f():


    def voltar_inicio_56():
        screen4.forget()
        selecionar.pack(fill=tk.BOTH, expand=True)


    def tempo_check_56():
        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_check_56)


    def visualizar_56():

        check_up_56()


    selecionar.forget()

    screen4 = tk.Canvas(screen, bg='#d9d9d9')
    screen4.pack(fill=tk.BOTH, expand=True)
    screen4.update()

    label_screen1 = tk.Label(screen4, text="                              CHECK-UP PRISMA (56x)", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label_screen1.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    Button_Back = tk.Button(screen4, text="VOLTAR", bg='#FE001B', fg="white", command=voltar_inicio_56, font=('Courier', 20, "bold"))
    Button_Back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    Button_Visualisar_42 = tk.Button(screen4, text="ABRIR", bg='GREEN', fg="white", command=visualizar_56, font=('Courier', 20, "bold"))
    Button_Visualisar_42.place(relx=0.002, rely=0.005, relwidth=0.098, relheight=0.071)

    l2 = tk.Label(screen4, font=font, bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_check_56()


def selecionar_modelo():


    def tempo_modelo():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_modelo)


    def voltar_inicial_modelo():

        selecionar.forget()
        screen1 .pack(fill=tk.BOTH, expand=True)


    screen2.forget()

    global selecionar

    selecionar = tk.Canvas(screen, bg='#d9d9d9')
    selecionar.pack(fill=tk.BOTH, expand=True)

    _frame_ = tk.Frame(selecionar, bg='#d9d9d9')
    _frame_.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(selecionar, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    global pro_42
    global pro_56
    global com_42
    global com_56

    pro_42 = "GEOVID PRO (42x)"
    pro_56 = "GEOVID PRO (56x)"
    com_42 = "GEOVID .COM (42x)"
    com_56 = "GEOVID .COM (56x)"

    label_modelo = tk.Label(selecionar, text="ESCOLHA O MODELO:", bg="#d9d9d9", fg="black", font=('Courier', 50, "bold"), anchor="center")
    label_modelo.place(relx=0.32, rely=0.17, relwidth=0.36, relheight=0.05)

    button_silber_42 = tk.Button(selecionar, text=pro_42, bg='GREEN', fg='WHITE', command=lambda: [master_pro_42(), button_text_pro_42()], font=('Courier', 40, "bold"))
    button_silber_42.place(relx=0.15, rely=0.32, relwidth=0.30, relheight=0.25)

    button_silber_56 = tk.Button(selecionar, text=pro_56, bg='BLUE', fg='WHITE', command=lambda: [master_2_pro_56(), button_text_pro_56()], font=('Courier', 40, "bold"))
    button_silber_56.place(relx=0.55, rely=0.32, relwidth=0.30, relheight=0.25)

    button_mantel_42 = tk.Button(selecionar, text=com_42, bg='GREEN', fg='WHITE', command=lambda: [master_com_42(), button_text_com_42()], font=('Courier', 40, "bold"))
    button_mantel_42.place(relx=0.15, rely=0.62, relwidth=0.30, relheight=0.25)

    button_mantel_56 = tk.Button(selecionar, text=com_56, bg='BLUE', fg='WHITE', command=lambda: [master_2_com_56(), button_text_com_56()], font=('Courier', 40, "bold"))
    button_mantel_56.place(relx=0.55, rely=0.62, relwidth=0.30, relheight=0.25)

    button_back = tk.Button(selecionar, text="TERMINAR\nSESSÃO", bg='#FE001B', fg='white', command=voltar_inicial_modelo, state=NORMAL, font=('Courier', 20, "bold"))
    button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    l2 = tk.Label(selecionar, font=font, bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_modelo()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    label_imagem = tk.Label(selecionar, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)

    label_username = tk.Label(selecionar, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
    label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)

    Button_Check_Up_42 = tk.Button(selecionar, text="CHECK-UP (42x)", bg='GREEN', fg="#FFFFFF", command=check_up_42_f, font=('Courier', 18, "bold"))
    Button_Check_Up_42.place(relx=0.0015, rely=0.082, relwidth=0.11, relheight=0.06)

    Button_Check_Up_56 = tk.Button(selecionar, text="CHECK-UP (56x)", bg='BLUE', fg="#FFFFFF", command=check_up_56_f, font=('Courier', 18, "bold"))
    Button_Check_Up_56.place(relx=0.0015, rely=0.144, relwidth=0.11, relheight=0.06)


def selecionar_modelo_tecnico_f():

    def tempo_modelo_tecnico():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_modelo_tecnico)

    def voltar_inicial_modelo_tecnico():

        selecionar.forget()
        screen1.pack(fill=tk.BOTH, expand=True)

    screen5.forget()

    global selecionar

    selecionar = tk.Canvas(screen, bg='#d9d9d9')
    selecionar.pack(fill=tk.BOTH, expand=True)

    _frame_modelo_tecnico = tk.Frame(selecionar, bg='#d9d9d9')
    _frame_modelo_tecnico.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(selecionar, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    label_modelo = tk.Label(selecionar, text="ESCOLHA O MODELO:", bg="#d9d9d9", fg="black", font=('Courier', 50, "bold"), anchor="center")
    label_modelo.place(relx=0.32, rely=0.17, relwidth=0.36, relheight=0.05)

    global pro_42_st
    global pro_56_st
    global com_42_st
    global com_56_st
    global hdr_42_st
    global hdr_56_st

    pro_42_st = "GEOVID PRO (42x)"
    pro_56_st = "GEOVID PRO (56x)"
    com_42_st = "GEOVID .COM (42x)"
    com_56_st = "GEOVID .COM (56x)"
    hdr_42_st = "GEOVID HD-R (42x)"
    hdr_56_st = "GEOVID HD-R (56x)"


    button_silber_42 = tk.Button(selecionar, text=pro_42_st, bg='GREEN', fg='WHITE', command=lambda: [master_st_pro_42(), button_text_pro_42_st()], font=('Courier', 40, "bold"))
    button_silber_42.place(relx=0.15, rely=0.32, relwidth=0.30, relheight=0.15)

    button_silber_56 = tk.Button(selecionar, text=pro_56_st, bg='BLUE', fg='WHITE', command=lambda: [master_2_st_pro_56(), button_text_pro_56_st()], font=('Courier', 40, "bold"))
    button_silber_56.place(relx=0.55, rely=0.32, relwidth=0.30, relheight=0.15)

    button_mantel_42 = tk.Button(selecionar, text=com_42_st, bg='GREEN', fg='WHITE', command=lambda: [master_st_com_42(), button_text_com_42_st()], font=('Courier', 40, "bold"))
    button_mantel_42.place(relx=0.15, rely=0.52, relwidth=0.30, relheight=0.15)

    button_mantel_56 = tk.Button(selecionar, text=com_56_st, bg='BLUE', fg='WHITE', command=lambda: [master_2_st_com_56(), button_text_com_56_st()], font=('Courier', 40, "bold"))
    button_mantel_56.place(relx=0.55, rely=0.52, relwidth=0.30, relheight=0.15)

    button_blaumowe_42 = tk.Button(selecionar, text=hdr_42_st, bg='GREEN', fg='WHITE', command=lambda: [master_st_hdr_42(), button_text_hdr_42_st()], font=('Courier', 40, "bold"))
    button_blaumowe_42.place(relx=0.15, rely=0.72, relwidth=0.30, relheight=0.15)

    button_blaumowe_56 = tk.Button(selecionar, text=hdr_56_st, bg='BLUE', fg='WHITE', command=lambda: [master_2_st_hdr_56(), button_text_hdr_56_st()], font=('Courier', 40, "bold"))
    button_blaumowe_56.place(relx=0.55, rely=0.72, relwidth=0.30, relheight=0.15)

    button_back = tk.Button(selecionar, text="TERMINAR\nSESSÃO", bg='#FE001B', fg='white', command=voltar_inicial_modelo_tecnico, state=NORMAL, font=('Courier', 20, "bold"))
    button_back.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    l2 = tk.Label(selecionar, font=font, bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_modelo_tecnico()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    label_imagem = tk.Label(selecionar, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)

    label_username = tk.Label(selecionar, text=" USER : {}".format(username1), bg='#d9d9d9', fg='RED', font=('Lucida', 25, "bold"), anchor='w')
    label_username.place(relx=0, rely=0.95, relwidth=0.30, relheight=0.05)


def tempo_geral():

    time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
    l2.config(text=time_string)
    l2.after(1000, tempo_geral)


def login():

    def login_verify():

        global username1

        username1 = username_verify.get()
        password1 = password_verify.get()

        username_entry1.delete(0, END)
        password_entry1.delete(0, END)

        list_of_files = os.listdir()

        if not username1 and not password1:

            messagebox.showerror(title="", message="Preencha ambos os campos.")

        elif not username1:

            password_entry1.delete(0, END)

            messagebox.showerror(title="", message="Preencha ambos os campos.")

        elif not password1:

            username_entry1.delete(0, END)

            messagebox.showerror(title="", message="Preencha ambos os campos.")

        elif not username1.isdigit():

            messagebox.showerror(title="", message="O username é apenas constituído por números.")

            username_entry1.delete(0, END)

            password_entry1.delete(0, END)

        else:

            if username1 in list_of_files:

                file1 = open(username1, "r")
                verify = file1.read().splitlines()

                if password1 in verify:

                    screen2.forget()
                    selecionar_modelo()
                    messagebox.showinfo(title="", message="Bem-vindo(a).")

                else:

                    password_entry1.delete(0, END)
                    messagebox.showerror(title="", message="A password está incorreta.")
                    username_entry1.delete(0, END)

            else:

                screen2.forget()
                screen1.pack(fill=tk.BOTH, expand=True)

                messagebox.showerror(title="", message="O username ainda não tem registo!\nPor favor registe-se.")

                username_entry1.delete(0, END)
                password_entry1.delete(0, END)

    screen1.forget()

    global screen2

    screen2 = tk.Canvas(screen, bg='#d9d9d9')
    screen2.pack(fill=tk.BOTH, expand=True)

    label_screen2 = tk.Label(screen2, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label_screen2.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_dados = tk.Label(screen2, bg='#ee1721')
    frame_dados.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.55)

    label_dados = tk.Label(screen2, text="INSIRA OS SEUS DADOS:", bg='#ee1721', fg="#FFFFFF", font=('Courier', 30, "bold"))
    label_dados.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.05)

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    def length_username(self, *args):

        if len(username_verify.get()) > 5:
            username_verify.set(username_verify.get()[:-1])

    username_verify.trace('w', length_username)

    label_username = tk.Label(screen2, text="USERNAME:", bg='#ee1721', fg="#FFFFFF", font=('Courier', 24, "bold"))
    label_username.place(relx=0.25, rely=0.425, relwidth=0.13, relheight=0.05)

    global username_entry1
    global password_entry1

    username_entry1 = tk.Entry(screen2, textvariable=username_verify, font=('Courier', 35, "bold"))
    username_entry1.place(relx=0.375, rely=0.425, relwidth=0.25, relheight=0.05)

    label_password = tk.Label(screen2, text="PASSWORD:", bg='#ee1721', fg="#FFFFFF", font=('Courier', 24, "bold"))
    label_password.place(relx=0.25, rely=0.55, relwidth=0.13, relheight=0.05)

    password_entry1 = tk.Entry(screen2, textvariable=password_verify, font=('Courier', 35, "bold"), show="*")
    password_entry1.place(relx=0.375, rely=0.55, relwidth=0.25, relheight=0.05)

    Button_Login_Access = tk.Button(screen2, text="LOGIN", bg='grey', fg="#FFFFFF", font=('Courier', 24, "bold"), command=login_verify)
    Button_Login_Access.place(relx=0.425, rely=0.675, relwidth=0.15, relheight=0.05)

    def tempo_login():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_login)

    l2 = tk.Label(screen2, font=font, bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_login()

    def voltar_inicio_login():

        username_entry1.delete(0, END)
        password_entry1.delete(0, END)
        screen2.forget()
        screen1.pack(fill=tk.BOTH, expand=True)

    button_voltar_primeira_pagina = tk.Button(screen2, text="VOLTAR", bg='RED', fg='white', command=voltar_inicio_login, state=NORMAL, font=('Courier', 20, "bold"))
    button_voltar_primeira_pagina.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    label_imagem = tk.Label(screen2, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)


def register():

    def register_user():

        username_info = username.get()
        password_info = password.get()

        if not username.get() and not password.get():

            messagebox.showerror(title="", message="Preencha ambos os campos.")

        elif not username.get():

            password_entry.delete(0, END)

            messagebox.showerror(title="", message="Preencha ambos os campos.")

        elif not password.get():

            username_entry.delete(0, END)

            messagebox.showerror(title="", message="Preencha ambos os campos.")

        elif not username.get().isdigit():

            username_entry.delete(0, END)
            password_entry.delete(0, END)

            messagebox.showerror(title="", message="O username só pode ser constituído por números.")

        elif os.path.exists(username_info):

            username_entry.delete(0, END)
            password_entry.delete(0, END)

            messagebox.showerror(title="", message="Username já se encontra registado.")

        else:

            file = open(username_info, "w")
            file.write(username_info + "\n")
            file.write(password_info)
            file.close()

            username_entry.delete(0, END)
            password_entry.delete(0, END)

            screen2.forget()
            screen1.pack(fill=tk.BOTH, expand=True)

            messagebox.showinfo(title="", message="Registo realizado com sucesso.")

    global screen2

    screen2 = tk.Canvas(screen, bg='#d9d9d9')
    screen2.pack(fill=tk.BOTH, expand=True)

    label_screen2 = tk.Label(screen2, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label_screen2.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_dados = tk.Label(screen2, bg='#333333')
    frame_dados.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.55)

    label_dados = tk.Label(screen2, text="REGISTE OS SEUS DADOS:", bg='#333333', fg="#FFFFFF", font=('Courier', 30, "bold"))
    label_dados.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.05)

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    def length_username_(self, *args):

        if len(username.get()) > 5:
            username.set(username.get()[:-1])

    username.trace('w', length_username_)

    label_username_registar = tk.Label(screen2, text="USERNAME:", bg='#333333', fg="#FFFFFF", font=('Courier', 24, "bold"))
    label_username_registar.place(relx=0.25, rely=0.425, relwidth=0.13, relheight=0.05)

    global username_entry
    global password_entry

    username_entry = tk.Entry(screen2, textvariable=username, font=('Courier', 35, "bold"))
    username_entry.place(relx=0.375, rely=0.425, relwidth=0.25, relheight=0.05)

    label_password = tk.Label(screen2, text="PASSWORD:", bg='#333333', fg="#FFFFFF", font=('Courier', 24, "bold"))
    label_password.place(relx=0.25, rely=0.55, relwidth=0.13, relheight=0.05)

    password_entry = tk.Entry(screen2, textvariable=password, font=('Courier', 35, "bold"), show="*")
    password_entry.place(relx=0.375, rely=0.55, relwidth=0.25, relheight=0.05)

    Button_Registar_Confirm = tk.Button(screen2, text="REGISTAR", bg='grey', fg="#FFFFFF", font=('Courier', 24, "bold"), command=register_user)
    Button_Registar_Confirm.place(relx=0.425, rely=0.675, relwidth=0.15, relheight=0.05)

    def tempo_register():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_register)

    l2 = tk.Label(screen2, font=font, bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_register()

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    label_imagem = tk.Label(screen2, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)

    def voltar_inicio_register():

        username_entry.delete(0, END)
        password_entry.delete(0, END)

        screen2.forget()

        screen1.pack(fill=tk.BOTH, expand=True)

    button_voltar_primeira_pagina = tk.Button(screen2, text="VOLTAR", bg='RED', fg='white', command=voltar_inicio_register, state=NORMAL, font=('Courier', 20, "bold"))
    button_voltar_primeira_pagina.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)


def verify():

    def master_verify():

        username = "11034"
        password = "1223"

        if username_entry_ver.get() == username and password_entry_ver.get() == password:

            messagebox.showinfo(title="", message="Autenticação com sucesso.")

            screen3.forget()

            register()

        else:

            messagebox.showerror(title="", message="Autenticação incorreta.")

            username_entry_ver.delete(0, END)
            password_entry_ver.delete(0, END)

    screen1.forget()
    global screen3

    screen3 = tk.Canvas(screen, bg='#d9d9d9')
    screen3.pack(fill=tk.BOTH, expand=True)

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    label_imagem = tk.Label(screen3, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)

    label_screen3 = tk.Label(screen3, text="             AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label_screen3.place(relx=0.15, rely=0, relwidth=0.85, relheight=0.08)

    frame_dados_3 = tk.Label(screen3, bg='#333333')
    frame_dados_3.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.55)

    label_dados_3 = tk.Label(screen3, text="AUTENTICAÇÃO DE DADOS:", bg='#333333', fg="#FFFFFF", font=('Courier', 30, "bold"))
    label_dados_3.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.05)

    global username_ver
    global password_ver
    global username_entry_ver
    global password_entry_ver

    username_ver = StringVar()
    password_ver = StringVar()

    def length_username_ver(self, *args):

        if len(username_ver.get()) > 5:
            username_ver.set(username_ver.get()[:-1])

    username_ver.trace('w', length_username_ver)

    label_username_registar_ver = tk.Label(screen3, text="USERNAME:", bg='#333333', fg="#FFFFFF", font=('Courier', 24, "bold"))
    label_username_registar_ver.place(relx=0.25, rely=0.425, relwidth=0.13, relheight=0.05)

    global username_entry_ver
    global password_entry_ver

    username_entry_ver = tk.Entry(screen3, textvariable=username_ver, font=('Courier', 35, "bold"))
    username_entry_ver.place(relx=0.375, rely=0.425, relwidth=0.25, relheight=0.05)

    label_password_ver = tk.Label(screen3, text="PASSWORD:", bg='#333333', fg="#FFFFFF", font=('Courier', 24, "bold"))
    label_password_ver.place(relx=0.25, rely=0.55, relwidth=0.13, relheight=0.05)

    password_entry_ver = tk.Entry(screen3, textvariable=password_ver, font=('Courier', 35, "bold"), show="*")
    password_entry_ver.place(relx=0.375, rely=0.55, relwidth=0.25, relheight=0.05)

    Button_Avançar = tk.Button(screen3, text="AVANÇAR", bg='grey', fg="#FFFFFF", font=('Courier', 24, "bold"), command=master_verify)
    Button_Avançar.place(relx=0.425, rely=0.675, relwidth=0.15, relheight=0.05)

    def voltar_inicio_verify():

        username_entry_ver.delete(0, END)
        password_entry_ver.delete(0, END)

        screen3.forget()

        screen1.pack(fill=tk.BOTH, expand=True)

    button_voltar_primeira_pagina_verify = tk.Button(screen3, text="VOLTAR", bg='RED', fg='white', command=voltar_inicio_verify, state=NORMAL, font=('Courier', 20, "bold"))
    button_voltar_primeira_pagina_verify.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

    def tempo_verify():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_verify)

    l2 = tk.Label(screen3, font=font, bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_verify()


def login_serv_tecnico():

    def login_verify_serv_tecnico():

        global username1

        username1 = username_verify.get()
        password1 = password_verify.get()

        username_entry1.delete(0, END)
        password_entry1.delete(0, END)

        list_of_files = os.listdir()

        if not username1 and not password1:

            messagebox.showerror(title="", message="Preencha ambos os campos.")

        elif not username1:

            password_entry1.delete(0, END)

            messagebox.showerror(title="", message="Preencha ambos os campos.")

        elif not password1:

            username_entry1.delete(0, END)

            messagebox.showerror(title="", message="Preencha ambos os campos.")

        elif not username1.isdigit():

            messagebox.showerror(title="", message="O username é apenas constituído por números.")

            username_entry1.delete(0, END)

            password_entry1.delete(0, END)

        else:

            if username1 in list_of_files:

                file1 = open(username1, "r")
                verify = file1.read().splitlines()

                if password1 in verify:

                    screen5.forget()
                    selecionar_modelo_tecnico_f()
                    messagebox.showinfo(title="", message="Bem-vindo(a).")

                else:

                    password_entry1.delete(0, END)
                    messagebox.showerror(title="", message="A password está incorreta.")
                    username_entry1.delete(0, END)

            else:

                screen5.forget()
                screen1.pack(fill=tk.BOTH, expand=True)

                messagebox.showerror(title="", message="O username ainda não tem registo!\nPor favor registe-se.")

                username_entry1.delete(0, END)
                password_entry1.delete(0, END)


    def length_username(self, *args):

        if len(username_verify.get()) > 5:
            username_verify.set(username_verify.get()[:-1])


    def tempo_login_serv_tecnico():

        time_string = strftime('  %H:%M:%S \n %d/%m/%Y')
        l2.config(text=time_string)
        l2.after(1000, tempo_login_serv_tecnico)


    def voltar_inicio_serv_tecnico():

        username_entry1.delete(0, END)
        password_entry1.delete(0, END)
        screen5.forget()
        screen1.pack(fill=tk.BOTH, expand=True)


    screen1.forget()

    global screen5

    screen5 = tk.Canvas(screen, bg='#d9d9d9')
    screen5.pack(fill=tk.BOTH, expand=True)
    screen5.update()

    label_screen5 = tk.Label(screen5, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
    label_screen5.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    frame_dados = tk.Label(screen5, bg='#ee1721')
    frame_dados.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.55)

    label_dados = tk.Label(screen5, text="INSIRA OS SEUS DADOS:", bg='#ee1721', fg="#FFFFFF", font=('Courier', 30, "bold"))
    label_dados.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.05)

    global logo_2
    global new_logo_2

    logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
    new_logo_2 = ImageTk.PhotoImage(logo_2)

    label_imagem = tk.Label(screen5, bg="black", anchor="nw", image=new_logo_2)
    label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)

    l2 = tk.Label(screen5, font=font, bg='#d9d9d9')
    l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

    tempo_login_serv_tecnico()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    username_verify.trace('w', length_username)

    label_username = tk.Label(screen5, text="USERNAME:", bg='#ee1721', fg="#FFFFFF", font=('Courier', 24, "bold"))
    label_username.place(relx=0.25, rely=0.425, relwidth=0.13, relheight=0.05)

    global username_entry1
    global password_entry1

    username_entry1 = tk.Entry(screen5, textvariable=username_verify, font=('Courier', 35, "bold"))
    username_entry1.place(relx=0.375, rely=0.425, relwidth=0.25, relheight=0.05)

    label_password = tk.Label(screen5, text="PASSWORD:", bg='#ee1721', fg="#FFFFFF", font=('Courier', 24, "bold"))
    label_password.place(relx=0.25, rely=0.55, relwidth=0.13, relheight=0.05)

    password_entry1 = tk.Entry(screen5, textvariable=password_verify, font=('Courier', 35, "bold"), show="*")
    password_entry1.place(relx=0.375, rely=0.55, relwidth=0.25, relheight=0.05)

    Button_Login_Access = tk.Button(screen5, text="LOGIN", bg='grey', fg="#FFFFFF", command=login_verify_serv_tecnico, font=('Courier', 24, "bold"))
    Button_Login_Access.place(relx=0.425, rely=0.675, relwidth=0.15, relheight=0.05)

    button_voltar_primeira_pagina_serv_tecnico = tk.Button(screen5, text="VOLTAR", bg='RED', fg='white', command=voltar_inicio_serv_tecnico, state=NORMAL, font=('Courier', 20, "bold"))
    button_voltar_primeira_pagina_serv_tecnico.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)


def close():

    [f.unlink() for f in Path('C:/Users/installation/Desktop/Print (42x)').glob("*") if f.is_file()]
    [f.unlink() for f in Path('C:/Users/installation/Desktop/Print (56x)').glob("*") if f.is_file()]

    screen.destroy()


screen = tk.Tk()
screen.attributes('-fullscreen', True)
screen.title("Centragem do alvo e ajuste da placa dos dígitos")

global screen1

screen1 = tk.Canvas(screen, bg='#d9d9d9')
screen1.pack(fill=tk.BOTH, expand=True)

logo_2 = Image.open("LEICA/leica.png").resize((120, 95))
new_logo_2 = ImageTk.PhotoImage(logo_2)

label_imagem = tk.Label(screen, bg="black", anchor="nw", image=new_logo_2)
label_imagem.place(relx=0, rely=0, relwidth=0.15, relheight=0.08)

label_imagem_image = new_logo_2

logo = ImageTk.PhotoImage(Image.open('LEICA/leica.png'))

screen1.create_image(960, 600, anchor=CENTER, image=logo)

label_screen1 = tk.Label(screen1, text="                         AJUSTE DO DISPLAY E DO RECETOR", bg='black', fg='white', font=('Courier', 30, "bold"), anchor='w')
label_screen1.place(relx=0, rely=0, relwidth=1, relheight=0.08)

Button_Login = tk.Button(screen1, text="LOGIN", bg='grey', fg="#FFFFFF", command=login, font=('Courier', 18, "bold"))
Button_Login.place(relx=0.435, rely=0.71, relwidth=0.13, relheight=0.06)

Button_Registar = tk.Button(screen1, text="REGISTAR", bg='grey', fg="#FFFFFF", command=verify, font=('Courier', 18, "bold"))
Button_Registar.place(relx=0.435, rely=0.80, relwidth=0.13, relheight=0.06)

Button_Servico_Tecnico = tk.Button(screen1, text="SERVIÇO TÉCNICO", bg='ORANGE', fg="#FFFFFF", command=login_serv_tecnico, font=('Courier', 18, "bold"))
Button_Servico_Tecnico.place(relx=0.001, rely=0.938, relwidth=0.13, relheight=0.06)

Button_Sair = tk.Button(screen1, text="FECHAR", bg='#FE001B', fg="white", font=('Courier', 20, "bold"), command=close)
Button_Sair.place(relx=0.9, rely=0.005, relwidth=0.098, relheight=0.071)

font = ('times', 20, 'bold')

l2 = tk.Label(screen1, font=font, bg='#d9d9d9')
l2.place(relx=0.92, rely=0.93, relwidth=0.075, relheight=0.065)

tempo_geral()

screen.bind('<Escape>', lambda e: close())
screen.mainloop()
