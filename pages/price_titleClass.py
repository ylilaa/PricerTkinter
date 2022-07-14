import tkinter as tk
import customtkinter
from utils import *
from tkinter import filedialog

from pandastable import Table

#Forms inherited from pydantic
from models.titleModel import titleInputForm

# ----------------------------------------  CONTAINER ------------------------------------------------------------------------

class Price_title(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        # ============ create two frames ============
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                width=180,
                                                corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)


        # ============ LEFT FRAME ============

        # configure grid layout (1x11)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)

        # Title left grid
        self.leftTitle = customtkinter.CTkLabel(master=self.frame_left,
                                            text="Pricer Titres",
                                            text_font=("Roboto Medium", -16))  # font name and size in px
        self.leftTitle.grid(row=1, column=0, pady=10, padx=10)

        # Champs à remplir modèle excel


        self.entryCode = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="Code ISIN ou Maroclear")
        self.entryCode.grid(row=2, column=0, pady=10, padx=20, sticky="w")
              
        
        self.entryDateValo = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="Date de valorisation")
        self.entryDateValo.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.entryCourbe = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="Date Courbe")
        self.entryCourbe.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.InputTitleForm = titleInputForm()
        def store_title_input():
            
            self.InputTitleForm.code = self.entryCode.get()
            self.InputTitleForm.dateValo = self.entryDateValo.get()
            self.InputTitleForm.dateCourbe = self.entryCourbe.get()
            print(colored('Title parameters registered Successfully','green'))

        def open_popup():
            top= Toplevel(self)
            top.geometry("300x150")
            top.title("Choix d'un Fichier courbe personnalisé")
            Entry(top).grid()
            Button(top, text="Parcourir", command=donothing).grid()
            Button(top, text="ok", command=donothing).grid()


        def browseFiles():
                filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
                print(filename)
                return filename
    
        self.buttonImportCurve = customtkinter.CTkButton(master=self.frame_left,
                                                    text="Importer une courbe",
                                                    command=browseFiles)
        self.buttonImportCurve.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        

        self.buttonValidate = customtkinter.CTkButton(master=self.frame_left,
                                                    text="Valider",
                                                    command=store_title_input)
        self.buttonValidate.grid(row=6, column=0, pady=10, padx=20, sticky="w")


        # ====================RIGHT FRAME ===========================

        
    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        # Menu
        
        actionmenu = Menu(menubar, tearoff=0, relief=RAISED)
        actionmenu.add_command(label="Pricer un Fonds", command=lambda: parent.show_frame(parent.Price_fund))
        actionmenu.add_separator()
        actionmenu.add_command(label="Exit", command=parent.quit)
        menubar.add_cascade(label="Actions", menu=actionmenu)

        querymenu = Menu(menubar, tearoff=0, relief=RAISED)
        querymenu.add_command(
            label="Actualiser les données depuis Manar", command=donothing)
        querymenu.add_command(
            label="Actualiser les données depuis fichier", command=donothing)
        menubar.add_cascade(label="Requêtes", menu=querymenu)

        helpmenu = Menu(menubar, tearoff=0, relief=RAISED)
        helpmenu.add_command(label="Documentation", command=lambda: parent.show_frame(parent.docsClass))
        menubar.add_cascade(label="Aide", menu=helpmenu)
        return menubar
