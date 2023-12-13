import tkinter as tk
from tkinter import ttk

import requests

class Dictionary_App :

    def __init__(self) :
        self.root = tk.Tk()
        
        self.root.title("Dictionary App")
        self.root.geometry("500x300")

        self.Tabs = ttk.Notebook(self.root)

        # Tab for the Dictionary that uses API
        self.api_dictionaryTab = ttk.Frame(self.Tabs)
        self.Tabs.add(self.api_dictionaryTab , text="Dictionary API")

        # Tab for the Dictionary that uses Local_dictionary 
        self.local_dictionaryTab = ttk.Frame(self.Tabs)
        self.Tabs.add(self.local_dictionaryTab , text="Dictionary Local")

        self.Tabs.pack(expand=1, fill="y")
        

        # Intializing the Functions
        self.Api_Dictionary_Layout()
        self.Local_Dictionary_Layout()


        # Local Dicionary for storing Words and their meanings
        self.local_dictionary = {
            "hello": "Used as a greeting or to begin a conversation.",
            "world": "The earth, together with all of its countries and peoples.",
            "python": "A high-level programming language.",
            "noun" : "A noun is the name of any thing , place and person"
            # You can add more words and meanings as want needed
        }

        self.root.mainloop()



    def search_word_api(self ,event=None):  #function responsible for the Searching Words Through API
        word = self.entry.get().lower()
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
        try:
            response = requests.get(url)
            data = response.json()
    
            if isinstance(data, list):
                meanings = data[0].get("meanings", [])
                if meanings:
                    meaning = meanings[0].get("definitions", ["Meaning not found"])[0].get("definition", "Meaning not found")
                    self.result_text_api.delete(1.0, tk.END)  # Clear previous content
                    self.result_text_api.insert(tk.END, f"The meaning of '{word}' is:\n{meaning}")
                else:
                    self.result_text_api.delete(1.0, tk.END)
                    self.result_text_api.insert(tk.END, f"Sorry, '{word}' not found in the dictionary.")
            else:
                self.result_text_api.delete(1.0, tk.END)
                self.result_text_api.insert(tk.END, f"Sorry, '{word}' not found in the dictionary.")
    
        except requests.exceptions.RequestException as e:
            self.result_text_api.delete(1.0, tk.END)
            self.result_text_api.insert(tk.END, f"Error fetching data from the dictionary API:\n{e}")



    def search_word_local(self, event=None):
        word = self.entry.get().lower()

        if word in self.local_dictionary:
            meaning = self.local_dictionary[word]
            self.result_text_local.delete(1.0, tk.END)
            self.result_text_local.insert(tk.END, f"The meaning of '{word}' is:\n{meaning}")
        else:
            self.result_text_local.delete(1.0, tk.END)
            self.result_text_local.insert(tk.END, f"Sorry, '{word}' not found in the local dictionary.")



    def Api_Dictionary_Layout(self): #function responsible for Creating UI of the Appliction

        self.frame_title = ttk.LabelFrame(self.api_dictionaryTab , text="Dictionary (Search Your Words)" )
        self.frame_title.grid(row=0 , column=0 ,padx=10)

       
        self.label_space_1 = ttk.Label(self.frame_title, text="")
        self.label_space_1.grid( row=1 , column=0 ,padx=5 ,pady=10 , sticky=tk.W)

        self.entry = ttk.Entry(self.frame_title , font=('Arial' , 10) )
        self.entry.grid( row=2 , column=0 ,padx=15,pady=5 ,sticky=tk.W+tk.E)

        self.search_button = ttk.Button(self.frame_title, text="Search", command=self.search_word_api)
        self.search_button.grid( row=3 , column=0 ,padx=15,pady=5, sticky=tk.W)


        self.label_space = ttk.Label(self.frame_title , text="")
        self.label_space.grid( row=4 , column=0 ,padx=15 ,sticky=tk.W)

        self.label_meaning = ttk.Label(self.frame_title, text="Meaning :" , font=('Arial', 12))
        self.label_meaning.grid( row=5 , column=0 ,padx=15,pady=5 ,sticky=tk.W)


        self.result_text_api = tk.Text(self.frame_title, height=5, width=60 , font=('Arial', 10))
        self.result_text_api.grid( row=6 , column=0 ,padx=15,pady=5 ,sticky=tk.W+tk.E)


        self.entry.bind("<Return>", self.search_word_api) #When you press Enter any time (search_word) will get triggered



    def Local_Dictionary_Layout(self): #function responsible for Creating UI of the Appliction

        self.frame_title = ttk.LabelFrame(self.local_dictionaryTab , text="Dictionary (Search Your Words)" )
        self.frame_title.grid(row=0 , column=0 ,padx=10)

       
        self.label_space_1 = ttk.Label(self.frame_title, text="")
        self.label_space_1.grid( row=1 , column=0 ,padx=5 ,pady=10 , sticky=tk.W)

        self.entry = ttk.Entry(self.frame_title , font=('Arial' , 10) )
        self.entry.grid( row=2 , column=0 ,padx=15,pady=5 ,sticky=tk.W+tk.E)

        self.search_button = ttk.Button(self.frame_title, text="Search", command=self.search_word_local)
        self.search_button.grid( row=3 , column=0 ,padx=15,pady=5, sticky=tk.W)


        self.label_space = ttk.Label(self.frame_title , text="")
        self.label_space.grid( row=4 , column=0 ,padx=15 ,sticky=tk.W)

        self.label_meaning = ttk.Label(self.frame_title, text="Meaning :" , font=('Arial', 12))
        self.label_meaning.grid( row=5 , column=0 ,padx=15,pady=5 ,sticky=tk.W)


        self.result_text_local = tk.Text(self.frame_title, height=5, width=60 , font=('Arial', 10))
        self.result_text_local.grid( row=6 , column=0 ,padx=15,pady=5 ,sticky=tk.W+tk.E)


        self.entry.bind("<Return>", self.search_word_local) #When you press Enter any time (search_word) will get triggered

Dictionary_App()
