import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, ttk
from threading import Thread
from app.downloader import download_audio


class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Variáveis de Interface
        self.url_entry = None
        self.save_dir_entry = None
        self.title_entry = None
        self.progress_bar = None
        self.progress_label = None

        # Layout
        self.setup_ui()

    def setup_ui(self):
        # URL do vídeo
        Label(self.root, text="URL do Vídeo do YouTube:", font=("Arial", 12)).pack(pady=10)
        self.url_entry = Entry(self.root, width=50, font=("Arial", 12))
        self.url_entry.pack(pady=5)

        # Diretório de Salvar
        Label(self.root, text="Diretório de Salvar:", font=("Arial", 12)).pack(pady=10)
        self.save_dir_entry = Entry(self.root, width=50, font=("Arial", 12))
        self.save_dir_entry.pack(pady=5)
        Button(self.root, text="Selecionar Diretório", command=self.select_directory, bg="orange", fg="white", font=("Arial", 10)).pack(pady=5)

        # Título Personalizado
        Label(self.root, text="Título Personalizado (Opcional):", font=("Arial", 12)).pack(pady=10)
        self.title_entry = Entry(self.root, width=50, font=("Arial", 12))
        self.title_entry.pack(pady=5)

        # Botão de Baixar
        Button(self.root, text="Baixar", command=self.start_download, bg="green", fg="white", font=("Arial", 14), height=2, width=15).pack(pady=10)

        # Barra de Progresso
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.pack(pady=10)

        # Label de Progresso
        self.progress_label = Label(self.root, text="Progresso: 0%", font=("Arial", 10))
        self.progress_label.pack(pady=5)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.save_dir_entry.delete(0, "end")
            self.save_dir_entry.insert(0, directory)

    def update_progress(self, progress, status="Baixando..."):
        self.progress_bar["value"] = progress
        self.progress_label.config(text=f"{status} {progress}%")
        self.root.update_idletasks()

    def start_download(self):
        video_url = self.url_entry.get()
        save_directory = self.save_dir_entry.get()
        title = self.title_entry.get()

        if not video_url or not save_directory:
            messagebox.showerror("Erro", "Insira a URL e o diretório de destino!")
            return

        Thread(target=self.execute_download, args=(video_url, save_directory, title)).start()

    def execute_download(self, video_url, save_directory, title):
        try:
            self.update_progress(0, "Iniciando...")
            download_audio(video_url, save_directory, title, self.update_progress)
            self.update_progress(100, "Concluído!")
            messagebox.showinfo("Sucesso", f"Áudio baixado com sucesso em: {save_directory}")
        except Exception as e:
            self.update_progress(0, "Erro")
            messagebox.showerror("Erro", f"Erro ao baixar o vídeo: {e}")
