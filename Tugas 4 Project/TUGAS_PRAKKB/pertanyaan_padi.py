import tkinter as tk
from tkinter import messagebox

class PertanyaanPadi:
    def __init__(self, root, callback_hasil):
        self.root = root
        self.callback_hasil = callback_hasil
        self.current_index = 0
        self.jawaban = []
        self.gejala = self.load_gejala()
    
    def load_gejala(self):
        return [
            "terdapat bercak daun berwarna coklat dengan pusat abu-abu",
            "daun menguning dari ujung kemudian layu",
            "terlihat bercak memanjang berwarna coklat pada daun",
            "ada bintik-bintik kecil berwarna kuning pada daun",
            "daun memiliki lapisan putih seperti tepung",
            "tanaman padi kerdil dan pertumbuhan terhambat",
            "daun menggulung dan berwarna kuning-oranye",
            "malai tidak keluar atau hampa",
            "akar berwarna hitam dan busuk",
            "terdapat bercak daun dengan tepi kuning"
        ]
    
    def tampilkan_pertanyaan(self):
        self.clear_frame()
        
        main_frame = tk.Frame(self.root, bg="#f0f8ff", padx=30, pady=30)
        main_frame.pack(expand=True, fill="both")
        
        # Question number
        tk.Label(
            main_frame,
            text=f"Pertanyaan {self.current_index+1}/{len(self.gejala)}",
            font=("Arial", 14, "bold"),
            bg="#f0f8ff",
            fg="#2e7d32"
        ).pack(pady=(0, 20))
        
        # Question frame
        question_frame = tk.Frame(main_frame, bg="#e8f5e9", padx=20, pady=20)
        question_frame.pack(fill="x", pady=10)
        
        tk.Label(
            question_frame,
            text=f"Apakah {self.gejala[self.current_index]}?",
            font=("Arial", 12),
            bg="#e8f5e9",
            wraplength=700,
            justify="left"
        ).pack(anchor="w")
        
        # Radio buttons
        self.var = tk.IntVar(value=-1)
        
        radio_frame = tk.Frame(main_frame, bg="#f0f8ff")
        radio_frame.pack(pady=15)
        
        tk.Radiobutton(
            radio_frame,
            text="Ya",
            variable=self.var,
            value=1,
            font=("Arial", 12),
            bg="#f0f8ff",
            activebackground="#f0f8ff",
            selectcolor="#c8e6c9"
        ).pack(side="left", padx=20)
        
        tk.Radiobutton(
            radio_frame,
            text="Tidak",
            variable=self.var,
            value=0,
            font=("Arial", 12),
            bg="#f0f8ff",
            activebackground="#f0f8ff",
            selectcolor="#c8e6c9"
        ).pack(side="left", padx=20)
        
        # Navigation buttons
        button_frame = tk.Frame(main_frame, bg="#f0f8ff", pady=30)
        button_frame.pack(fill="x")
        
        if self.current_index > 0:
            tk.Button(
                button_frame,
                text="Kembali",
                command=self.prev_question,
                bg="#ff9800",
                fg="white",
                font=("Arial", 12),
                padx=25,
                pady=5,
                cursor="hand2"
            ).pack(side="left", padx=10)
        
        tk.Button(
            button_frame,
            text="Selesai" if self.current_index == len(self.gejala)-1 else "Lanjut",
            command=self.next_question,
            bg="#388e3c",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=25,
            pady=5,
            cursor="hand2"
        ).pack(side="right", padx=10)
    
    def next_question(self):
        if self.var.get() == -1:
            messagebox.showwarning("Peringatan", "Harap pilih jawaban Ya atau Tidak")
            return
        
        if self.var.get() == 1:
            self.jawaban.append(self.current_index)
        
        self.current_index += 1
        
        if self.current_index >= len(self.gejala):
            self.callback_hasil(self.jawaban)
        else:
            self.tampilkan_pertanyaan()
    
    def prev_question(self):
        if self.current_index > 0:
            if (self.current_index-1) in self.jawaban:
                self.jawaban.remove(self.current_index-1)
            self.current_index -= 1
            self.tampilkan_pertanyaan()
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()