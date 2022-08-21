# Rock,Paper,scissors(tk)

import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from random import choice

class SampleApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Rock Paper Scissors')
        # self.columnconfigure(0,weight=1)
        # self.rowconfigure(0,weight=1)
        self.geometry('1200x650')
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)


        self._frame = None
        self.raise_frame(Front)

    def raise_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)
        self._frame.grid(row=0,column=0,sticky='NEWS')



class Front(tk.Frame):
    def __init__(self, master):
        super().__init__(master)



        Image_frame = tk.Frame(self,bg='black')
        Image_frame.columnconfigure((0,1),weight=1)
        Image_frame.grid(row=0,column=0,sticky='NSEW')

        Button_frame = tk.Frame(self, bg='black')
        Button_frame.columnconfigure(0, weight=1)
        Button_frame.grid(row=1, column=0, sticky='NSEW')


        image_intro = Image.open('RPS.png').resize((850, 390))
        photoimage_intro = ImageTk.PhotoImage(image_intro)
        panel = tk.Label(Image_frame, text='Rock.Paper.Scissors', image=photoimage_intro, bg='black')
        panel.configure(font=("Courier", 44))
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(0, weight=1)
        panel.img = photoimage_intro
        panel.grid(row=0, column=0, sticky='NSEW', padx=10, pady=20)

        enter_btn = tk.Button(Button_frame, text='Play', bg='cyan', command=lambda: master.raise_frame(Game_frame))
        enter_btn.grid(row=0, column=0, pady=10, ipady=20, ipadx=20)


        exit_btn = tk.Button(Button_frame, text='Exit', bg='red', command=master.destroy)
        exit_btn.grid(row=1, column=0, pady=20, ipady=20, ipadx=20)



class Game_frame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        Button_frame = tk.Frame(self,bg='black')
        Button_frame.columnconfigure((0,1,2),weight=1)
        Button_frame.rowconfigure((0,1,2),weight=1)
        Button_frame.grid(row=0,column=0,sticky='NEWS')

        Text_frame = tk.Frame(self,bg='grey')
        Text_frame.columnconfigure(0,weight=1)
        Text_frame.rowconfigure(0,weight=1)
        Text_frame.grid(row=1,column=0,sticky='NEWS')

        #Text_var = tk.StringVar()

        Text = tk.Text(Text_frame,bg='grey')
        Text.columnconfigure(0,weight=1)
        Text.rowconfigure(0,weight=1)
        Text.insert('1.0', "Welcome to RPS!\nLet's Play:\n")
        Text.insert("3.0", "Click your choice...\n")
        Text.grid(row=1,column=0,sticky='NEWS')


        Back_frame = tk.Frame(self,bg='purple')
        Back_frame.grid(row=0,column=1,sticky='NEWS')

        rock_btn = tk.Button(Button_frame,text='Rock',bg='brown',fg='white',command=lambda:rock('Rock'))
        rock_btn.grid(row=0,column=0,ipadx=20,ipady=20)

        sci_btn = tk.Button(Button_frame,text='Scissors',bg='blue',fg='white',command=lambda:scissors('Scissors'))
        sci_btn.grid(row=0,column=1,ipadx=20,ipady=20)

        pap_btn = tk.Button(Button_frame,text='Paper',bg='green',fg='white',command=lambda:paper('Paper'))
        pap_btn.grid(row=0,column=2,ipadx=20,ipady=20)

        play_again_btn = tk.Button(Button_frame,text='Play Again',bg='yellow')
        play_again_btn.grid(row=1,column=1,ipadx=25,ipady=25)

        back_btn = tk.Button(Back_frame,text='Back',bg='red',command=lambda:master.raise_frame(Front))
        back_btn.grid(row=0,column=0,padx=5,ipadx=8,ipady=8)


        def rock(text):
            user_choice = text
            start_game(user_choice)

        def scissors(text):
            user_choice = text
            start_game(user_choice)

        def paper(text):
            user_choice = text
            start_game(user_choice)


        def start_game(text):
            Text.delete('1.0', '10.0')

            while 1:
                i = 0
                Game_material = ['Rock','Paper','Scissors']
                AI_choice = choice(Game_material)


                user_choice = text

                if user_choice == 'Rock':
                    if AI_choice == 'Rock':
                        Text.insert(f"{i}.0",f"You choose {user_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0", f"A.I chooses {AI_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0","Round Draw..\n")
                        i += 2

                    elif AI_choice == 'Paper':
                        Text.insert(f"{i}.0", f"You choose {user_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0",f"A.I chooses {AI_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0","A.I won :(\n")
                        i += 2

                    else:
                        Text.insert(f"{i}.0", f"You choose {user_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0",f"A.I chooses {AI_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0",f"You win :)\n")
                        i += 2


                elif user_choice == 'Paper':
                    if AI_choice == 'Paper':
                        Text.insert(f"{i}.0", f"You choose {user_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0", f"A.I chooses {AI_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0", "Round Draw..\n")
                        i += 2

                    elif AI_choice == 'Scissors':
                        Text.insert(f"{i}.0", f"You choose {user_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0", f"A.I chooses {AI_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0", "A.I won :(\n")
                        i += 2

                    else:
                        Text.insert(f"{i}.0", f"You choose {user_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0", f"A.I chooses {AI_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0", f"You win :)\n")
                        i += 2

                else:
                    if AI_choice == 'Scissors':
                        if AI_choice == 'Paper':
                            Text.insert(f"{i}.0", f"You choose {user_choice}\n")
                            i += 2
                            Text.insert(f"{i}.0", f"A.I chooses {AI_choice}\n")
                            i += 2
                            Text.insert(f"{i}.0", "Round Draw..\n")
                            i += 2

                    elif AI_choice == 'Rock':
                        Text.insert(f"{i}.0", f"You choose {user_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0", f"A.I chooses {AI_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0", "A.I won :(\n")
                        i += 2

                    else:
                        Text.insert(f"{i}.0", f"You choose {user_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0", f"A.I chooses {AI_choice}\n")
                        i += 2
                        Text.insert(f"{i}.0", f"You win :)\n")
                        i += 2

                break


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
