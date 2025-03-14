import pytest
from tkinter import Tk
from app.ui import YouTubeDownloaderApp
from unittest.mock import patch

@pytest.fixture
def app_root():
    root = Tk()
    yield root
    root.destroy()

def test_ui_initialization(app_root):
    app = YouTubeDownloaderApp(app_root)
    assert app.url_entry.get() == ""
    assert app.save_dir_entry.get() == ""
    assert app.title_entry.get() == ""

@patch("app.ui.filedialog.askdirectory")
def test_ui_select_directory(mock_askdirectory, app_root):
    app = YouTubeDownloaderApp(app_root)
    mock_askdirectory.return_value = "/mock/directory"
    app.select_directory()
    assert app.save_dir_entry.get() == "/mock/directory"

@patch("app.ui.messagebox.showerror")
def test_ui_download_with_missing_url(mock_showerror, app_root):
    app = YouTubeDownloaderApp(app_root)
    app.url_entry.delete(0, "end")
    app.url_entry.insert(0, "")  # Simula URL vazia
    app.download_video()
    mock_showerror.assert_called_with("Erro", "Por favor, insira a URL do vídeo!")

@patch("app.ui.messagebox.showerror")
def test_ui_download_with_missing_directory(mock_showerror, app_root):
    app = YouTubeDownloaderApp(app_root)
    app.url_entry.delete(0, "end")
    app.url_entry.insert(0, "https://www.youtube.com/watch?v=JL_M6ap2Yqs")
    app.save_dir_entry.delete(0, "end")  # Simula diretório vazio
    app.download_video()
    mock_showerror.assert_called_with("Erro", "Por favor, selecione o diretório de destino!")
