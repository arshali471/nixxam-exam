from tkinter import *
import math
import clicked_from_exam_mode
from PIL import ImageTk, Image


class OnlineProtectAssissment:
    value_first = None
    value_second = None
    value_third = None
    value_fourth = None
    computer_id = None
    protocol = None
    checkbox = None
    check_true_false = True
    frame = None
    url_value = None

    def __init__(self, root):
        self.root = root
        self.scr_width = root.winfo_screenwidth()
        self.scr_height = root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (self.scr_width, self.scr_height))
        self.root.attributes('-fullscreen', True)  # open window in full screen mode
        # '''to come from full screen mode to normal mode press f11 or excape key'''
        # self.root.bind("<F11>",
        #                lambda event: self.root.attributes("-fullscreen",
        #                                                   not self.root.attributes("-fullscreen")))
        self.root.bind("<Escape>",
                       lambda event: self.root.attributes("-fullscreen",
                                                          False))

        self.mainframe = Frame(root, width=self.scr_width, height=self.scr_height, bg="white", bd=2)
        self.mainframe.place(x=0, y=0)
        self.exam_mode()
        self.title()

    # for getting server ip address from each sub net and restrict it to limit only 3 character in each sub net.
    def limit_size(self, *args):
        if self.value_first:
            value = self.value_first.get()
            if len(value) > 2 and "." not in value:
                self.value_first.set(value[:3])
            if "." in value:
                value = value.split(".")
                self.value_first.set(value[0])
                self.value_second.set(value[1])
                self.value_third.set(value[2])
                self.value_fourth.set(value[3])
        if self.value_second:
            value = self.value_second.get()
            if len(value) > 2:
                self.value_second.set(value[:3])
        if self.value_third:
            value = self.value_third.get()
            if len(value) > 2:
                self.value_third.set(value[:3])
        if self.value_fourth:
            value = self.value_fourth.get()
            if len(value) > 2:
                self.value_fourth.set(value[:3])
        # if computerId:
        #     cid = computerId.get()  # cid stores computer id
        
    def getBool(self, frame): # get rid of the event argument
        if not self.checkbox.get(): 
            frame = Frame(frame, width=self.scr_width / 2.7, height=self.scr_height / 16, bg="white")
            frame.place(x=self.scr_width / 7.76, y=self.scr_height / 4)
            
            serverip = Label(frame, text="Server IP Address ",
                            bg='white', font=("Arial", round(self.scr_width / 91), 'bold'), fg='#808080')
            serverip.place(x=0, y=0)
            
            first_server_subnet = Entry(
                frame, width=5, textvariable=self.value_first, bd=2, relief='sunken', font=("Arial",
                                                                                            round(self.scr_width / 105),
                                                                                            'bold'))
            first_server_subnet.place(x=self.scr_width / 6.55, y=0)
            first_server_subnet.focus()

            subnet_seperator_dot = Label(frame, text=".", bg='white', font=('Arial', round(self.scr_width / 68.3),
                                                                            'bold'))
            subnet_seperator_dot.place(x=self.scr_width / 5, y=0, 
                                    width=self.scr_width / 271)

            second_server_subnet = Entry(
                frame, width=5, textvariable=self.value_second, bd=2, relief='sunken',
                font=("Arial", round(self.scr_width / 105), 'bold'))
            second_server_subnet.place(x=self.scr_width / 4.8, y=0)

            subnet_seperator_dot1 = Label(frame, text=".", bg='white', font=('Arial', round(self.scr_width / 68.3),
                                                                            'bold'))
            subnet_seperator_dot1.place(x=self.scr_width / 3.9, y=0,
                                        width=self.scr_width / 271)

            third_server_subnet = Entry(
                frame, width=5, textvariable=self.value_third, bd=2, relief='sunken', font=("Arial",
                                                                                            round(self.scr_width / 105),
                                                                                            'bold'))
            third_server_subnet.place(x=self.scr_width / 3.8, y=0)

            subnet_seperator_dot2 = Label(frame, text=".", bg='white', font=('Arial', round(self.scr_width / 68.3),
                                                                            'bold'))
            subnet_seperator_dot2.place(x=self.scr_width / 3.22, y=0,
                                        width=self.scr_width / 271)

            four_server_subnet = Entry(
                frame, width=5, textvariable=self.value_fourth, bd=2, relief='sunken',
                font=("Arial", round(self.scr_width / 105), 'bold'))
            four_server_subnet.place(x=self.scr_width / 3.15, y=0)
        else: 
            self.url_value = StringVar()
            frame = Frame(frame, width=self.scr_width / 2.7, height=self.scr_height / 16, bg="white")
            frame.place(x=self.scr_width / 7.76, y=self.scr_height / 4)
            
            server_url = Label(frame, text="Server Url ",
                            bg='white', font=("Arial", round(self.scr_width / 91), 'bold'), fg='#808080')
            server_url.place(x=0, y=0)
            
            server_url_box = Entry(
                frame, width=28, textvariable=self.url_value, bd=2, relief='sunken', font=("Arial",
                                                                                            round(self.scr_width / 105),
                                                                                            'bold'))
            server_url_box.place(x=self.scr_width / 6.55, y=0)
            server_url_box.focus()
    
    # for getting server ip address and Computer Id from EXAM MODE and open isolated web browser with server ip address.
    def exam_mode(self):
        frame = Frame(self.root, width=self.scr_width / 1.5, height=self.scr_height / 1.5, bg="white", bd=10,
                      relief='groove')
        frame.place(x=self.scr_width / 6, y=self.scr_height / 6)

        button_frame = Frame(frame, width=(self.scr_width / 1.5) - 20, height=50, bg='white')
        button_frame.place(x=0, y=0)
        

        self.value_first = StringVar()
        self.value_first.trace('w', self.limit_size)
        self.value_second = StringVar()
        self.value_second.trace('w', self.limit_size)
        self.value_third = StringVar()
        self.value_third.trace('w', self.limit_size)
        self.value_fourth = StringVar()
        self.value_fourth.trace('w', self.limit_size)
        self.computer_id = StringVar()
        self.computer_id.trace("w", self.limit_size)
        self.protocol = StringVar()
        self.protocol.set("HTTP")
        
        # self.url_value.trace("w", lambda: url_value.get().strip())
        
        # Dropdown menu options
        options = [
            "HTTP",
            "HTTPS"
        ]
        
        self.checkbox = BooleanVar()
        self.checkbox.set(False)
        
        # self.checkbox.trace('w', lambda *_: print("The value was changed"))
        # print(checkbox.get())
        
        protocol_drop_val= Label(frame, text="Server Protocol ",
                         bg='white', font=("Arial", round(self.scr_width / 91), 'bold'), fg='#808080')
        protocol_drop_val.place(x=self.scr_width / 7.76, y=self.scr_height / 5.8)
        
        # Create Dropdown menu
        protocol_drop = OptionMenu( frame , self.protocol, *options )
        protocol_drop.place(x=math.floor(self.scr_width / 3.56), y=self.scr_height / 5.8)

        url_checkbox = Checkbutton(frame, bg = "white", font=("Arial", round(self.scr_width / 91)), text = "Select To Enter Server Url", variable = self.checkbox, command = lambda : self.getBool(frame))
        url_checkbox.place(x=math.floor(self.scr_width / 2.55), y=self.scr_height / 5.8)
        
        

        computerip = Label(frame, text="Computer ID ", bg='white', font=("Arial", round(self.scr_width / 91.06),
                                                                         'bold'), fg='#808080')
        computerip.place(x=self.scr_width / 7.73, y=self.scr_height / 3)

        computer_subnet = Entry(frame, width=28, textvariable=self.computer_id, bd=2,
                                relief='sunken', font=('Arial', round(self.scr_width / 105), 'bold'))
        computer_subnet.place(x=self.scr_width / 3.56, y=self.scr_height / 3)

        sbutton = Button(frame, text="Connect", padx=30, pady=5, font='bold',
                         command=lambda: clicked_from_exam_mode.clicked_from_exam_mode(self.value_first,
                                                                                       self.value_second,
                                                                                       self.value_third,
                                                                                       self.value_fourth,
                                                                                       self.computer_id, 
                                                                                       self.protocol, 
                                                                                       self.url_value, 
                                                                                       self.checkbox.get()))
        sbutton.place(x=self.scr_width / 3.38, y=self.scr_height / 2.5)
        self.top_button(button_frame, "#242D56", "#303C73")

        def enter_click(e):
            clicked_from_exam_mode.clicked_from_exam_mode(self.value_first, self.value_second,
                                                          self.value_third, self.value_fourth,
                                                          self.computer_id,
                                                          self.protocol,
                                                          self.url_value,
                                                          self.checkbox.get())

        self.root.bind("<Return>", enter_click)   
        self.getBool(frame)

    # For nav bar button.
    def top_button(self, frame, exam_mode_color="#303C73", lanscape_mode_color="#303C73"):
        exammode_button = Button(frame, text='EXAM MODE', font=("Helvetica", round(self.scr_width / 124.18), "bold"),
                                     width=round(self.scr_width / 26.78), height=2, bg=lanscape_mode_color, fg='white',
                                     activebackground='#242D56',
                                     activeforeground="white",
                                     bd=1,
                                    #  command=self.lanscape_mode
                                    )
        exammode_button.place(x=0, y=0, width=self.scr_width / 1.5, height=50)


    def title(self):
        main_title = Frame(self.root, width=self.scr_width / 1.5, height=self.scr_height / 9,
                                    bg="white", bd=10)
        main_title.place(x=self.scr_width / 6, y=self.scr_height / 30)

        # load image
        load = Image.open("./static/nixxam.png")
        resize = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(resize)
        img = Label(main_title, image=render, borderwidth=0, highlightthickness=0, background = 'white')
        img.image = render
        img.place(x=self.scr_width / 4.5, y=0)

        title = Label(main_title, text="NIXXAM", bg='white', font=("Arial", round(self.scr_width / 31.06),
                                                                         'bold'), fg='#242D56')
        title.place(x=self.scr_width / 3.5, y=0)


def main():
    root = Tk()
    root.title("Online Protected Assessment")
    OnlineProtectAssissment(root)
    root.mainloop()


if __name__ == "__main__":
    main()
