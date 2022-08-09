
import random
import os
import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image

class Vet:
    def __init__(self, nome, instrumento, padrinho, fotos):
        self.nome = nome
        self.instrumento = instrumento
        self.padrinho = padrinho
        self.fotos = fotos
    
    def getNome(self):
        return self.nome
    
    def getInstrumento(self):
        return self.instrumento
    
    def getPadrinho(self):
        return self.padrinho
    
    def getFotos(self):
        return self.fotos

def importVeteranos():
    f = open("data/Veteranos.txt", "r", encoding="utf-8")
    vets = []

    for line in f:
        photos = []
        temp = line.split(",")

        for i in range(3, len(temp), 1):
            photos.append(temp[i].strip())

        v = Vet(temp[0], temp[1], temp[2], photos)
        vets.append(v)
    
    return vets  


def checkAnswer(button, correct, options):
    if button.cget('text') != correct.cget('text'):
        button.configure(bg='#ff0000', activeforeground='#ffffff', activebackground='#ff0000')
    correct.configure(bg='#00ff00',  activeforeground='#ffffff', activebackground='#00ff00')

    for o in options:    
        o.unbind('<ButtonRelease>')

def nextWindowNameQuiz(vets):
    clean_window()
    iterationName(vets)

def nextWindowInstrumentoQuiz(vets):
    clean_window()
    iterationInstrument(vets)

def nextWindowPadrinhoQuiz(vets):
    clean_window()
    iterationPadrinho(vets)

def clean_window():
    for widgets in window.winfo_children():
        widgets.destroy()

def backToHome(vets):
    clean_window()
    initialScreen(vets) 

def createNameQuizLayout(vet, vets, full):
    myFont = font.Font(family='Chaparral Pro', size=int(0.009*window.winfo_screenwidth()), weight='bold')

    frame1 = tk.Frame(window, width=0.625*window.winfo_screenwidth(), height=0.556*window.winfo_screenheight(), bg="#222426")
    frame1.pack()
    frame1.place(anchor='s', relx=0.5, rely=0.63)

    next_button_frame = tk.Frame(window, width=0.078*window.winfo_screenwidth(), height=0.167*window.winfo_screenheight(),  bd=0)
    next_button_frame.place(anchor='s', relx=0.77, rely=0.888)
    next_button_frame.pack_propagate(False)

    next_font=font.Font(family='Chaparral Pro',weight='bold',size=int(0.015*window.winfo_screenwidth()))
    next_button = tk.Button(next_button_frame, text='➔\nNEXT', font=next_font, width=100, height=100, wraplength=130, bg='#424649', fg="white", borderwidth=5)
    next_button.pack()

    menu_button_frame = tk.Frame(window, width=0.078*window.winfo_screenwidth(), height=0.102*window.winfo_screenheight(), bd=0)
    menu_button_frame.place(anchor='s', relx=0.05, rely=0.12)
    menu_button_frame.pack_propagate(False)

    menu_font=font.Font(family='Chaparral Pro', size=int(0.013*window.winfo_screenwidth()),weight='bold')
    menu_button = tk.Button(menu_button_frame, text='◄\nMENU', font=menu_font, width=100, height=100, wraplength=130, bg='#424649', fg="white", borderwidth=5)
    menu_button.pack()
    

    options = tk.Frame(window, width=0.417*window.winfo_screenwidth(), height=0.185*window.winfo_screenheight(), bg='#222426')
    options.pack()
    options.place(anchor='s', relx=0.5, rely=0.9)

    options.grid_propagate(False)
    options.grid_columnconfigure(0, weight = 1)
    options.grid_columnconfigure(1, weight = 1)
    options.grid_rowconfigure(0, weight = 1)
    options.grid_rowconfigure(1, weight = 1)

    top_left_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    top_left_option.grid(column=0, row=0)
    top_left_option.pack_propagate(False)

    top_right_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    top_right_option.grid(column=1, row=0)
    top_right_option.pack_propagate(False)

    bottom_left_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    bottom_left_option.grid(column=0, row=1)
    bottom_left_option.pack_propagate(False)

    bottom_right_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    bottom_right_option.grid(column=1, row=1)
    bottom_right_option.pack_propagate(False)

    random.shuffle(vets)
    correct = ""

    option1 = tk.Button(top_left_option,text=vets[0],
                        font=myFont, wraplength=350, justify='center',
                        width=100, height=100, bd=0, bg='#424649', fg="white",
                        borderwidth=10)
    option1.pack()
    if option1.cget('text') == vet.getNome(): correct = option1

    option2 = tk.Button(top_right_option, text=vets[1],
                        font=myFont, wraplength=350, justify='center',
                        width=100, height=100,  bd=0,bg="#424649", fg="white",
                        borderwidth=10)
    option2.pack()
    if option2.cget('text') == vet.getNome(): correct = option2

    option3 = tk.Button(bottom_left_option,text=vets[2], 
                        font=myFont, wraplength=350, justify='center',
                        width=100,height=100,  bd=0,bg="#424649", fg="white",
                        borderwidth=10)
    option3.pack()
    if option3.cget('text') == vet.getNome(): correct = option3

    option4 = tk.Button(bottom_right_option, text=vets[3],
                        font=myFont, wraplength=350, justify='center', 
                        width=100,height=100, bd=0, bg="#424649", fg="white",
                        borderwidth=10)
    option4.pack()
    if option4.cget('text') == vet.getNome(): correct = option4

    options_list = [option1, option2, option3, option4]

    option1.bind('<ButtonRelease>', lambda event, a=option1, b=correct, c=options_list: checkAnswer(a, b, c))
    option2.bind('<ButtonRelease>', lambda event, a=option2, b=correct, c=options_list: checkAnswer(a, b, c))
    option3.bind('<ButtonRelease>', lambda event, a=option3, b=correct, c=options_list: checkAnswer(a, b, c))
    option4.bind('<ButtonRelease>', lambda event, a=option4, b=correct, c=options_list: checkAnswer(a, b, c))
    next_button.bind('<ButtonRelease>', lambda event, a=full: nextWindowNameQuiz(a))
    menu_button.bind('<ButtonRelease>', lambda event, a=full: backToHome(a))

    image = Image.open(vet.getFotos()[0])

    imwidth = int(frame1.winfo_reqheight()*(image.width/image.height))
    image = image.resize((imwidth,frame1.winfo_reqheight()))

    img = ImageTk.PhotoImage(image)

    label = tk.Label(frame1, image = img)
    label.image=img
    label.pack_propagate(False)
    label.pack()

def createInstrumentQuizLayout(vet, instruments, full):
    myFont = font.Font(family='Chaparral Pro', size=int(0.009*window.winfo_screenwidth()), weight='bold')

    frame1 = tk.Frame(window, width=0.625*window.winfo_screenwidth(), height=0.556*window.winfo_screenheight(), bg="#222426")
    frame1.pack()
    frame1.place(anchor='s', relx=0.5, rely=0.63)

    next_button_frame = tk.Frame(window, width=0.078*window.winfo_screenwidth(), height=0.167*window.winfo_screenheight(),  bd=0)
    next_button_frame.place(anchor='s', relx=0.77, rely=0.888)
    next_button_frame.pack_propagate(False)

    next_font=font.Font(family='Chaparral Pro',weight='bold',size=int(0.015*window.winfo_screenwidth()))
    next_button = tk.Button(next_button_frame, text='➔\nNEXT', font=next_font, width=100, height=100, wraplength=130, bg='#424649', fg="white", borderwidth=5)
    next_button.pack()

    menu_button_frame = tk.Frame(window, width=0.078*window.winfo_screenwidth(), height=0.102*window.winfo_screenheight(), bd=0)
    menu_button_frame.place(anchor='s', relx=0.05, rely=0.12)
    menu_button_frame.pack_propagate(False)

    menu_font=font.Font(family='Chaparral Pro', size=int(0.013*window.winfo_screenwidth()),weight='bold')
    menu_button = tk.Button(menu_button_frame, text='◄\nMENU', font=menu_font, width=100, height=100, wraplength=130, bg='#424649', fg="white", borderwidth=5)
    menu_button.pack()

    nome_frame = tk.Frame(window, width=0.4170*window.winfo_screenwidth(), height=0.074*window.winfo_screenheight(), bg='#222426')
    nome_frame.place(anchor='s', relx=0.5, rely=0.72)
    nome_frame.pack_propagate(False)

    nome_font=font.Font(family='Chaparral Pro',weight='bold',size=int(0.015*window.winfo_screenwidth()))
    nome = tk.Label(nome_frame, text=vet.getNome(), font=nome_font, justify='center', padx=0.5, pady=0.5, fg='white', bg='#222426')
    nome.pack()

    
    options = tk.Frame(window, width=0.417*window.winfo_screenwidth(), height=0.185*window.winfo_screenheight(), bg='#222426')
    options.pack()
    options.place(anchor='s', relx=0.5, rely=0.9)

    options.grid_propagate(False)
    options.grid_columnconfigure(0, weight = 1)
    options.grid_columnconfigure(1, weight = 1)
    options.grid_rowconfigure(0, weight = 1)
    options.grid_rowconfigure(1, weight = 1)

    top_left_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    top_left_option.grid(column=0, row=0)
    top_left_option.pack_propagate(False)

    top_right_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    top_right_option.grid(column=1, row=0)
    top_right_option.pack_propagate(False)

    bottom_left_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    bottom_left_option.grid(column=0, row=1)
    bottom_left_option.pack_propagate(False)

    bottom_right_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    bottom_right_option.grid(column=1, row=1)
    bottom_right_option.pack_propagate(False)

    random.shuffle(instruments)
    correct = ""

    option1 = tk.Button(top_left_option,text=instruments[0],
                        font=myFont, wraplength=350, justify='center',
                        width=100, height=100, bd=0, bg='#424649', fg="white",
                        borderwidth=10)
    option1.pack()
    if option1.cget('text') == vet.getInstrumento(): correct = option1

    option2 = tk.Button(top_right_option, text=instruments[1],
                        font=myFont, wraplength=350, justify='center',
                        width=100, height=100,  bd=0,bg="#424649", fg="white",
                        borderwidth=10)
    option2.pack()
    if option2.cget('text') == vet.getInstrumento(): correct = option2

    option3 = tk.Button(bottom_left_option,text=instruments[2], 
                        font=myFont, wraplength=350, justify='center',
                        width=100,height=100,  bd=0,bg="#424649", fg="white",
                        borderwidth=10)
    option3.pack()
    if option3.cget('text') == vet.getInstrumento(): correct = option3

    option4 = tk.Button(bottom_right_option, text=instruments[3],
                        font=myFont, wraplength=350, justify='center', 
                        width=100,height=100, bd=0, bg="#424649", fg="white",
                        borderwidth=10)
    option4.pack()
    if option4.cget('text') == vet.getInstrumento(): correct = option4

    options_list = [option1, option2, option3, option4]

    option1.bind('<ButtonRelease>', lambda event, a=option1, b=correct, c=options_list: checkAnswer(a, b, c))
    option2.bind('<ButtonRelease>', lambda event, a=option2, b=correct, c=options_list: checkAnswer(a, b, c))
    option3.bind('<ButtonRelease>', lambda event, a=option3, b=correct, c=options_list: checkAnswer(a, b, c))
    option4.bind('<ButtonRelease>', lambda event, a=option4, b=correct, c=options_list: checkAnswer(a, b, c))
    next_button.bind('<ButtonRelease>', lambda event, a=full: nextWindowInstrumentoQuiz(a))
    menu_button.bind('<ButtonRelease>', lambda event, a=full: backToHome(a))

    image = Image.open(vet.getFotos()[0])

    imwidth = int(frame1.winfo_reqheight()*(image.width/image.height))
    image = image.resize((imwidth,frame1.winfo_reqheight()))

    img = ImageTk.PhotoImage(image)

    label = tk.Label(frame1, image = img)
    label.image=img
    label.pack_propagate(False)
    label.pack()

def createPadrinhoQuizLayout(vet, vets, full):
    myFont = font.Font(family='Chaparral Pro', size=int(0.009*window.winfo_screenwidth()), weight='bold')

    frame1 = tk.Frame(window, width=0.625*window.winfo_screenwidth(), height=0.556*window.winfo_screenheight(), bg="#222426")
    frame1.pack()
    frame1.place(anchor='s', relx=0.5, rely=0.63)

    next_button_frame = tk.Frame(window, width=0.078*window.winfo_screenwidth(), height=0.167*window.winfo_screenheight(),  bd=0)
    next_button_frame.place(anchor='s', relx=0.77, rely=0.888)
    next_button_frame.pack_propagate(False)

    next_font=font.Font(family='Chaparral Pro',weight='bold',size=int(0.015*window.winfo_screenwidth()))
    next_button = tk.Button(next_button_frame, text='➔\nNEXT', font=next_font, width=100, height=100, wraplength=130, bg='#424649', fg="white", borderwidth=5)
    next_button.pack()

    menu_button_frame = tk.Frame(window, width=0.078*window.winfo_screenwidth(), height=0.102*window.winfo_screenheight(), bd=0)
    menu_button_frame.place(anchor='s', relx=0.05, rely=0.12)
    menu_button_frame.pack_propagate(False)

    menu_font=font.Font(family='Chaparral Pro', size=int(0.013*window.winfo_screenwidth()),weight='bold')
    menu_button = tk.Button(menu_button_frame, text='◄\nMENU', font=menu_font, width=100, height=100, wraplength=130, bg='#424649', fg="white", borderwidth=5)
    menu_button.pack()

    nome_frame = tk.Frame(window, width=0.4170*window.winfo_screenwidth(), height=0.074*window.winfo_screenheight(), bg='#222426')
    nome_frame.place(anchor='s', relx=0.5, rely=0.72)
    nome_frame.pack_propagate(False)

    nome_font=font.Font(family='Chaparral Pro',weight='bold',size=int(0.015*window.winfo_screenwidth()))
    nome = tk.Label(nome_frame, text=vet.getNome(), font=nome_font, justify='center', padx=0.5, pady=0.5, fg='white', bg='#222426')
    nome.pack()

    
    options = tk.Frame(window, width=0.417*window.winfo_screenwidth(), height=0.185*window.winfo_screenheight(), bg='#222426')
    options.pack()
    options.place(anchor='s', relx=0.5, rely=0.9)

    options.grid_propagate(False)
    options.grid_columnconfigure(0, weight = 1)
    options.grid_columnconfigure(1, weight = 1)
    options.grid_rowconfigure(0, weight = 1)
    options.grid_rowconfigure(1, weight = 1)

    top_left_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    top_left_option.grid(column=0, row=0)
    top_left_option.pack_propagate(False)

    top_right_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    top_right_option.grid(column=1, row=0)
    top_right_option.pack_propagate(False)

    bottom_left_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    bottom_left_option.grid(column=0, row=1)
    bottom_left_option.pack_propagate(False)

    bottom_right_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    bottom_right_option.grid(column=1, row=1)
    bottom_right_option.pack_propagate(False)

    random.shuffle(vets)
    correct = ""

    option1 = tk.Button(top_left_option,text=vets[0],
                        font=myFont, wraplength=350, justify='center',
                        width=100, height=100, bd=0, bg='#424649', fg="white",
                        borderwidth=10)
    option1.pack()
    if option1.cget('text') == vet.getPadrinho(): correct = option1

    option2 = tk.Button(top_right_option, text=vets[1],
                        font=myFont, wraplength=350, justify='center',
                        width=100, height=100,  bd=0,bg="#424649", fg="white",
                        borderwidth=10)
    option2.pack()
    if option2.cget('text') == vet.getPadrinho(): correct = option2

    option3 = tk.Button(bottom_left_option,text=vets[2], 
                        font=myFont, wraplength=350, justify='center',
                        width=100,height=100,  bd=0,bg="#424649", fg="white",
                        borderwidth=10)
    option3.pack()
    if option3.cget('text') == vet.getPadrinho(): correct = option3

    option4 = tk.Button(bottom_right_option, text=vets[3],
                        font=myFont, wraplength=350, justify='center', 
                        width=100,height=100, bd=0, bg="#424649", fg="white",
                        borderwidth=10)
    option4.pack()
    if option4.cget('text') == vet.getPadrinho(): correct = option4

    options_list = [option1, option2, option3, option4]

    option1.bind('<ButtonRelease>', lambda event, a=option1, b=correct, c=options_list: checkAnswer(a, b, c))
    option2.bind('<ButtonRelease>', lambda event, a=option2, b=correct, c=options_list: checkAnswer(a, b, c))
    option3.bind('<ButtonRelease>', lambda event, a=option3, b=correct, c=options_list: checkAnswer(a, b, c))
    option4.bind('<ButtonRelease>', lambda event, a=option4, b=correct, c=options_list: checkAnswer(a, b, c))
    next_button.bind('<ButtonRelease>', lambda event, a=full: nextWindowPadrinhoQuiz(a))
    menu_button.bind('<ButtonRelease>', lambda event, a=full: backToHome(a))

    image = Image.open(vet.getFotos()[0])

    imwidth = int(frame1.winfo_reqheight()*(image.width/image.height))
    image = image.resize((imwidth,frame1.winfo_reqheight()))

    img = ImageTk.PhotoImage(image)

    label = tk.Label(frame1, image = img)
    label.image=img
    label.pack_propagate(False)
    label.pack()

def iterationPadrinho(vets):
    options = []
    v = random.choice(vets)
    options.append(v.getPadrinho())
    i = 1
    while i < 4:
        temp = random.choice(vets)
        if temp.getPadrinho() not in options:
            if temp.getPadrinho() != v.getNome():
                options.append(temp.getPadrinho())
                i += 1
    
    createPadrinhoQuizLayout(v, options, vets)

def iterationInstrument(vets):
    instruments = ["Outro", "Viola", "Pandeireta", "Bandolim", "Cavaquinho", "Percussão", "Acordeão", "Violino", "Contrabaixo", "Flauta Transversal"]
    options = []
    v = random.choice(vets)
    options.append(v.getInstrumento())
    i = 1
    while i < 4:
        temp = random.choice(instruments)
        if temp not in options:
            options.append(temp)
            i += 1
    
    createInstrumentQuizLayout(v, options, vets)

def iterationName(vets):
    options = []
    v = random.choice(vets)
    options.append(v.getNome())
    i = 1
    while i < 4:
        temp = random.choice(vets)
        if temp.getNome() not in options:
            options.append(temp.getNome())
            i += 1
    
    createNameQuizLayout(v, options, vets)

def initialScreen(vets):
    myFont = font.Font(family='Chaparral Pro', size=int(0.009*window.winfo_screenwidth()), weight='bold')
    logo = tk.Frame(window, width=0.13*window.winfo_screenwidth(), height=0.231*window.winfo_screenheight())
    logo.pack()
    logo.place(anchor='n', relx=0.5, rely=0.02)

    image_path=os.path.join(base_folder, 'data/logo.png')
    image = Image.open(image_path)
    imwidth = int(logo.winfo_reqheight()*(image.width/image.height))
    image = image.resize((imwidth,logo.winfo_reqheight()))
    img = ImageTk.PhotoImage(image)

    label = tk.Label(logo, image = img,borderwidth=0, highlightthickness=0 )
    label.image=img
    label.pack_propagate(False)
    label.pack()

    options = tk.Frame(window, width=0.167*window.winfo_screenwidth(), height=0.648*window.winfo_screenheight(), bg="#222426")
    options.pack()
    options.place(anchor='n', relx=0.5, rely=0.27)

    options.grid_propagate(False)
    options.grid_columnconfigure(0, weight = 1)
    options.grid_rowconfigure(0, weight = 1)
    options.grid_rowconfigure(1, weight = 1)
    options.grid_rowconfigure(2, weight = 1)
    options.grid_rowconfigure(3, weight = 1)
    options.grid_rowconfigure(4, weight = 1)
    options.grid_rowconfigure(5, weight = 1)

    first_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    first_option.grid(column=0, row=0)
    first_option.pack_propagate(False)

    second_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    second_option.grid(column=0, row=1)
    second_option.pack_propagate(False)

    third_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    third_option.grid(column=0, row=2)
    third_option.pack_propagate(False)

    fourth_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    fourth_option.grid(column=0, row=3)
    fourth_option.pack_propagate(False)

    fifth_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    fifth_option.grid(column=0, row=4)
    fifth_option.pack_propagate(False)

    sixth_option = tk.Frame(options,width=0.198*window.winfo_screenwidth(), height=0.083*window.winfo_screenheight(), bg="#222426")
    sixth_option.grid(column=0, row=5)
    sixth_option.pack_propagate(False)

    option1 = tk.Button(first_option,text="NOMES E ALCUNHAS",
                        font=myFont, wraplength=0.198*window.winfo_screenwidth(), justify='center',
                        width=100, height=100, bd=0, bg='#424649', fg="white",
                        borderwidth=10)
    option1.pack()
    option2 = tk.Button(second_option, text="INSTRUMENTOS",
                        font=myFont, wraplength=0.198*window.winfo_screenwidth(), justify='center',
                        width=100, height=100,  bd=0,bg="#424649", fg="white",
                        borderwidth=10)
    option2.pack()
    option3 = tk.Button(third_option,text="PADRINHOS", 
                        font=myFont, wraplength=0.198*window.winfo_screenwidth(), justify='center',
                        width=100,height=100,  bd=0,bg="#424649", fg="white",
                        borderwidth=10)
    option3.pack()
    option4 = tk.Button(fourth_option, text="Coming Soon...",
                        font=myFont, wraplength=0.198*window.winfo_screenwidth(), justify='center', 
                        width=100,height=100, bd=0, bg="#424649", fg="white",
                        borderwidth=10)
    option4.pack()
    option5 = tk.Button(fifth_option,text="Coming Soon...", 
                        font=myFont, wraplength=0.198*window.winfo_screenwidth(), justify='center',
                        width=100,height=100,  bd=0,bg="#424649", fg="white",
                        borderwidth=10)
    option5.pack()
    option6 = tk.Button(sixth_option, text="Coming Soon...",
                        font=myFont, wraplength=0.198*window.winfo_screenwidth(), justify='center', 
                        width=100,height=100, bd=0, bg="#424649", fg="white",
                        borderwidth=10)
    option6.pack()

    option1.bind('<ButtonRelease>', lambda event, a=vets: nextWindowNameQuiz(a))
    option2.bind('<ButtonRelease>', lambda event, a=vets: nextWindowInstrumentoQuiz(a))
    option3.bind('<ButtonRelease>', lambda event, a=vets: nextWindowPadrinhoQuiz(a))


vets = importVeteranos()
base_folder = os.path.dirname(__file__)

window = tk.Tk()
window.title("Who is that Veterano?")
window.configure(width=window.winfo_screenwidth(), height=window.winfo_screenheight(), bg='#222426')

initialScreen(vets)

window.mainloop()