import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# --- KONFIGURASI WARNA ---
BG_COLOR = "#1e272e"
CARD_COLOR = "#ffffff"
BTN_PRIMARY = "#578CA9"
BTN_LOGOUT = "#87CEEB"
TEXT_COLOR = "#34495e"

# --- [FIX] MENENTUKAN LOKASI GAMBAR SECARA ABSOLUT ---
# Ini trik agar Python selalu mencari gambar di sebelah file .py ini
basedir = os.path.dirname(os.path.abspath(__file__))
LOGO_FILENAME = os.path.join(basedir, "logo.png")

class MenuUserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PIP Hospital Center - User Menu")
        self.root.geometry("450x700")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        # --- CONTAINER UTAMA ---
        self.main_frame = tk.Frame(self.root, bg=CARD_COLOR, width=380, height=650)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.main_frame.pack_propagate(False)

        # --- 1. LOGO GAMBAR ---
        # Debugging: Cetak lokasi gambar yang dicari Python ke terminal
        print(f"Mencari logo di: {LOGO_FILENAME}")

        if os.path.exists(LOGO_FILENAME):
            try:
                img_asli = Image.open(LOGO_FILENAME)
                img_resized = img_asli.resize((120, 100), Image.Resampling.LANCZOS)
                self.logo_image = ImageTk.PhotoImage(img_resized)
                
                tk.Label(self.main_frame, image=self.logo_image, bg=CARD_COLOR).pack(pady=(40, 10))
                print("-> Logo DITEMUKAN dan berhasil dimuat!")
            except Exception as e:
                print(f"-> Logo error: {e}")
                tk.Label(self.main_frame, text=f"Error Gambar:\n{e}", fg="red", bg=CARD_COLOR).pack(pady=(40, 10))
        else:
            print("-> Logo TIDAK ditemukan di jalur tersebut.")
            tk.Label(self.main_frame, text="[LOGO TIDAK DITEMUKAN]", fg="red", bg=CARD_COLOR).pack(pady=(40, 10))

        # --- 2. JUDUL ---
        tk.Label(self.main_frame, text="Selamat Datang di Pip Hospital", 
                 font=("Helvetica", 12, "bold"), bg=CARD_COLOR, fg=TEXT_COLOR).pack(pady=(5, 5))
        
        tk.Label(self.main_frame, text="Silakan Pilih Menu", 
                 font=("Helvetica", 10), bg=CARD_COLOR, fg="gray").pack(pady=(0, 30))

        # --- 3. TOMBOL MENU ---
        self.buat_tombol("Read Data Pasien", self.aksi_read_data)
        self.buat_tombol("Permohonan Kunjungan", self.aksi_permohonan)
        self.buat_tombol("Cek Status Kunjungan", self.aksi_cek_status)

        # --- 4. TOMBOL LOGOUT ---
        btn_logout = tk.Button(self.main_frame, text="Logout", font=("Arial", 11, "bold"),
                               bg=BTN_LOGOUT, fg="white", activebackground="#5eb6dd", activeforeground="white",
                               bd=0, padx=20, pady=10, width=25, cursor="hand2",
                               command=self.aksi_logout)
        btn_logout.pack(side="bottom", pady=(0, 50))

    def buat_tombol(self, text, command):
        btn = tk.Button(self.main_frame, text=text, font=("Arial", 11, "bold"),
                        bg=BTN_PRIMARY, fg="white", activebackground="#4a7a94", activeforeground="white",
                        bd=0, padx=20, pady=12, width=28, cursor="hand2",
                        command=command)
        btn.pack(pady=8)

    # --- FUNGSI AKSI ---
    def aksi_read_data(self):
        messagebox.showinfo("Info", "Membuka Data Pasien...")

    def aksi_permohonan(self):
        messagebox.showinfo("Info", "Membuka Form Permohonan...")

    def aksi_cek_status(self):
        messagebox.showinfo("Info", "Mengecek Status...")

    def aksi_logout(self):
        if messagebox.askyesno("Konfirmasi", "Yakin ingin keluar?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuUserApp(root)
    root.mainloop()