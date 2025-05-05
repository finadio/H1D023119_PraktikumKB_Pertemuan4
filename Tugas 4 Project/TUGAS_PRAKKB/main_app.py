import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Penyakit Padi")
        self.root.geometry("700x550")  # Smaller window size
        self.root.configure(bg="#f0f8ff")
        self.setup_ui()
    
    def setup_ui(self):
        self.show_welcome_screen()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar dari aplikasi?"):
            self.root.destroy()
            sys.exit()
    
    def show_welcome_screen(self):
        self.clear_frame()
        
        header_frame = tk.Frame(self.root, bg="#2e7d32", height=80)
        header_frame.pack(fill="x", pady=(0,10))
        
        tk.Label(
            header_frame,
            text="DIAGNOSA PENYAKIT PADI",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#2e7d32"
        ).pack(pady=15)
        
        content_frame = tk.Frame(self.root, bg="#f0f8ff", padx=20, pady=20)
        content_frame.pack(expand=True, fill="both")
        
        tk.Label(
            content_frame,
            text="Deteksi 4 Penyakit Padi Utama",
            font=("Arial", 14),
            bg="#f0f8ff"
        ).pack(pady=(0,10))
        
        tk.Label(
            content_frame,
            text="Pilih gejala yang teramati pada tanaman",
            font=("Arial", 11),
            bg="#f0f8ff"
        ).pack(pady=5)
        
        tk.Button(
            content_frame,
            text="MULAI DIAGNOSA",
            command=self.start_diagnosa,
            bg="#388e3c",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=8,
            cursor="hand2"
        ).pack(pady=20)
        
        footer_frame = tk.Frame(self.root, bg="#2e7d32", height=40)
        footer_frame.pack(fill="x", side="bottom")
        
        tk.Label(
            footer_frame,
            text="© 2023 Kelompok Tani Maju",
            font=("Arial", 9),
            fg="white",
            bg="#2e7d32"
        ).pack(pady=10)
    
    def start_diagnosa(self):
        from pertanyaan_padi import PertanyaanPadi
        from hasil_diagnosa import TampilHasil
        
        self.clear_frame()
        self.pertanyaan_padi = PertanyaanPadi(self.root, self.show_hasil)
        self.tampil_hasil = TampilHasil()
        self.pertanyaan_padi.tampilkan_pertanyaan()
    
    def show_hasil(self, jawaban):
        hasil = self.consult_prolog(jawaban)
        self.tampil_hasil.tampilkan(self.root, hasil, self.show_welcome_screen)
    
    def consult_prolog(self, jawaban):
        try:
            gejala_list = ",".join(str(g+1) for g in jawaban)
            cmd = [
                'swipl',
                '-l', 'basis_pengetahuan.pl',
                '-g', f'diagnosa([{gejala_list}],Penyakit,Solusi)',
                '-t', 'halt'
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0
            )
            
            if result.returncode == 0 and result.stdout.strip():
                lines = result.stdout.strip().split('\n')
                if len(lines) >= 2:
                    return {
                        "penyakit": lines[0],
                        "solusi": "\n".join(lines[1:])
                    }
                
                if len(lines) == 1 and any(disease in lines[0] for disease in [
                    "Hawar Daun Bakteri", "Blas", "Tungro", "Busuk Batang"
                ]):
                    return {
                        "penyakit": lines[0],
                        "solusi": "Lihat rekomendasi penanganan untuk penyakit ini"
                    }
        
        except Exception as e:
            print(f"Error: {str(e)}")
        
        return self.force_disease_detection(jawaban)
    
    def force_disease_detection(self, jawaban):
        diseases = {
            "Hawar Daun Bakteri": [0, 2, 8, 9],
            "Blas": [1, 2, 6, 7],
            "Tungro": [0, 1, 4, 5],
            "Busuk Batang": [5, 7, 8]
        }
        
        matches = {disease: len(set(jawaban) & set(symptoms)) 
                  for disease, symptoms in diseases.items()}
        best_match = max(matches.items(), key=lambda x: x[1])
        
        return {
            "penyakit": best_match[0],
            "solusi": self.get_solution_for_disease(best_match[0])
        }
    
    def get_solution_for_disease(self, disease_name):
        solutions = {
            "Hawar Daun Bakteri": (
                "1. Gunakan varietas tahan (Inpari 30)\n"
                "2. Semprot bakterisida Streptomycin 20%\n"
                "3. Kurangi pupuk nitrogen\n"
                "4. Rotasi tanaman dengan palawija"
            ),
            "Blas": (
                "1. Aplikasikan fungisida Tricyclazole\n"
                "2. Atur jarak tanam 30x30 cm\n"
                "3. Hindari pupuk nitrogen berlebihan\n"
                "4. Keringkan sawah periodik"
            ),
            "Tungro": (
                "1. Kendalikan wereng hijau (vektor)\n"
                "2. Tanam varietas tahan (Inpari 36)\n"
                "3. Tanam serempak di wilayah luas\n"
                "4. Cabut tanaman terinfeksi"
            ),
            "Busuk Batang": (
                "1. Berikan fungisida sistemik\n"
                "2. Perbaiki drainase sawah\n"
                "3. Gunakan pupuk kalium\n"
                "4. Hindari luka mekanis"
            )
        }
        return solutions.get(disease_name, "")
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()