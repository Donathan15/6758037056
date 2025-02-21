import tkinter as tk
import random

# Thai consonants and their pronunciations
thai_consonants = [
    ("ก", "Gor Kai"), ("ข", "Khor Khai"), ("ฃ", "Khor Khuat"),
    ("ค", "Khor Khwai"), ("ฅ", "Khor Khon"), ("ฆ", "Khor Rakhang"),
    ("ง", "Ngor Ngu"), ("จ", "Jor Jan"), ("ฉ", "Chor Ching"),
    ("ช", "Chor Chang"), ("ซ", "Sor So"), ("ฌ", "Chor Cher"),
]

class ThaiFlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.card_frame = tk.Frame(root, width=300, height=200, bg="white")
        self.card_frame.pack(pady=20)
        
        self.label = tk.Label(self.card_frame, text="", font=("Arial", 50), bg="white")
        self.label.pack(expand=True)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack()
        
        self.current_card = None
        self.is_flipped = False
        
        self.next_card()
    
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0])
        self.is_flipped = False
    
    def flip_card(self):
        if self.current_card and not self.is_flipped:
            self.label.config(text=self.current_card[1])
            self.is_flipped = True
        else:
            self.label.config(text=self.current_card[0])
            self.is_flipped = False

if __name__ == "__main__":
    root = tk.Tk()
    app = ThaiFlashcardGame(root)
    root.mainloop()
