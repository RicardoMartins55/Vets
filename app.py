
import random
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


def checkNameAnswer(button, correct, options):
    if button.cget('text') != correct.cget('text'):
        button.configure(bg='#ff0000', activeforeground='#ffffff', activebackground='#ff0000')
    correct.configure(bg='#00ff00',  activeforeground='#ffffff', activebackground='#00ff00')

    for o in options:    
        o.unbind('<ButtonRelease>')


def clean_window(vets):
    for widgets in window.winfo_children():
        widgets.destroy()
    iteration(vets)

def createNameQuizLayout(vet, vets, full):
    window.title("Who is that Veterano?")
    window.configure(width=window.winfo_screenwidth(), height=window.winfo_screenheight(), bg='#222426')

    myFont = font.Font(family='Chaparral Pro', size=14, weight='bold')

    frame1 = tk.Frame(window, width=1200, height=600, bg="#222426")
    frame1.pack()
    frame1.place(anchor='s', relx=0.5, rely=0.63)

    next_button_frame = tk.Frame(window, width=150, height=150, highlightbackground='#ffffff', highlightthickness = 4, bd=0)
    next_button_frame.place(anchor='s', relx=0.75, rely=0.38)
    next_button_frame.pack_propagate(False)

    next_font=font.Font(size=60)
    next_button = tk.Button(next_button_frame, text='🡆', font=next_font, width=100, height=100, wraplength=130, bg='#424649', fg="white")
    next_button.pack()
    

    options = tk.Frame(window, width=800, height=200, bg='#222426')
    options.pack()
    options.place(anchor='s', relx=0.5, rely=0.9)

    options.grid_propagate(False)
    options.grid_columnconfigure(0, weight = 1)
    options.grid_columnconfigure(1, weight = 1)
    options.grid_rowconfigure(0, weight = 1)
    options.grid_rowconfigure(1, weight = 1)


    top_left_option = tk.Frame(options,width=380, height=90, bg="#222426")
    top_left_option.grid(column=0, row=0)
    top_left_option.pack_propagate(False)

    top_right_option = tk.Frame(options,width=380, height=90, bg="#222426")
    top_right_option.grid(column=1, row=0)
    top_right_option.pack_propagate(False)

    bottom_left_option = tk.Frame(options,width=380, height=90, bg="#222426")
    bottom_left_option.grid(column=0, row=1)
    bottom_left_option.pack_propagate(False)

    bottom_right_option = tk.Frame(options,width=380, height=90, bg="#222426")
    bottom_right_option.grid(column=1, row=1)
    bottom_right_option.pack_propagate(False)

    random.shuffle(vets)
    correct = ""



    option1 = tk.Button(top_left_option,text=vets[0],
                        font=myFont, wraplength=350, justify='center',
                        width=100, height=100, bd=0, bg='#424649', fg="white")
    option1.pack()
    if option1.cget('text') == vet.getNome(): correct = option1

    option2 = tk.Button(top_right_option, text=vets[1],
                        font=myFont, wraplength=350, justify='center',
                        width=100, height=100,  bd=0,bg="#424649", fg="white")
    option2.pack()
    if option2.cget('text') == vet.getNome(): correct = option2

    option3 = tk.Button(bottom_left_option,text=vets[2], 
                        font=myFont, wraplength=350, justify='center',
                        width=100,height=100,  bd=0,bg="#424649", fg="white")
    option3.pack()
    if option3.cget('text') == vet.getNome(): correct = option3

    option4 = tk.Button(bottom_right_option, text=vets[3],
                        font=myFont, wraplength=350, justify='center', 
                        width=100,height=100, bd=0, bg="#424649", fg="white")
    option4.pack()
    if option4.cget('text') == vet.getNome(): correct = option4

    options_list = [option1, option2, option3, option4]

    option1.bind('<ButtonRelease>', lambda event, a=option1, b=correct, c=options_list: checkNameAnswer(a, b, c))
    option2.bind('<ButtonRelease>', lambda event, a=option2, b=correct, c=options_list: checkNameAnswer(a, b, c))
    option3.bind('<ButtonRelease>', lambda event, a=option3, b=correct, c=options_list: checkNameAnswer(a, b, c))
    option4.bind('<ButtonRelease>', lambda event, a=option4, b=correct, c=options_list: checkNameAnswer(a, b, c))
    next_button.bind('<ButtonRelease>', lambda event, a=full: clean_window(a))

    image = Image.open(vet.getFotos()[0])

    imwidth = int(frame1.winfo_reqheight()*(image.width/image.height))
    image = image.resize((imwidth,frame1.winfo_reqheight()))

    img = ImageTk.PhotoImage(image)

    label = tk.Label(frame1, image = img)
    label.image=img
    label.pack_propagate(False)
    label.pack()

def iteration(vets):
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

vets = importVeteranos()

window = tk.Tk()

iteration(vets)

window.mainloop()