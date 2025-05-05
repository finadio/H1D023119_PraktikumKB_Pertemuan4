import tkinter as tk
from tkinter import messagebox

class TampilHasil:
    def tampilkan(self, root, hasil, kembali_callback):
        self.clear_frame(root)
        
        main_frame = tk.Frame(root, bg="#f0f8ff", padx=40, pady=40)
        main_frame.pack(expand=True, fill="both")
        
        # Header
        tk.Label(
            main_frame,
            text="HASIL DIAGNOSA PENYAKIT PADI",
            font=("Arial", 18, "bold"),
            fg="#2e7d32",
            bg="#f0f8ff"
        ).pack(pady=(0, 30))
        
        # Diagnosis result
        diagnosa_frame = tk.Frame(main_frame, bg="#e8f5e9", padx=20, pady=20)
        diagnosa_frame.pack(fill="x", pady=10)
        
        tk.Label(
            diagnosa_frame,
            text=f"⛑️ HASIL: {hasil['penyakit']}",
            font=("Arial", 14, "bold"),
            bg="#e8f5e9",
            fg="#2e7d32"
        ).pack(anchor="w")
        
        # Solution
        solusi_frame = tk.Frame(main_frame, bg="white", padx=20, pady=20)
        solusi_frame.pack(fill="both", expand=True)
        
        tk.Label(
            solusi_frame,
            text="📌 REKOMENDASI PENANGANAN:",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#2e7d32"
        ).pack(anchor="w", pady=(0, 10))
        
        solusi_text = tk.Text(
            solusi_frame,
            wrap="word",
            font=("Arial", 11),
            bg="white",
            padx=10,
            pady=10,
            height=10,
            relief="flat"
        )
        solusi_text.insert("1.0", hasil["solusi"])
        solusi_text.config(state="disabled")
        solusi_text.pack(fill="both", expand=True)
        
        # Action buttons
        button_frame = tk.Frame(main_frame, bg="#f0f8ff", pady=30)
        button_frame.pack(fill="x")
        
        tk.Button(
            button_frame,
            text="🔄 DIAGNOSA ULANG",
            command=kembali_callback,
            bg="#388e3c",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=25,
            pady=5,
            cursor="hand2"
        ).pack(side="left", padx=10)
        
        tk.Button(
            button_frame,
            text="❌ KELUAR",
            command=root.quit,
            bg="#d32f2f",
            fg="white",
            font=("Arial", 12),
            padx=25,
            pady=5,
            cursor="hand2"
        ).pack(side="right", padx=10)
    
    def clear_frame(self, root):
        for widget in root.winfo_children():
            widget.destroy()