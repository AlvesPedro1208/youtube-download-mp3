import os
import pytest
from app.downloader import download_audio

@pytest.fixture
def mock_video_url():
    return "https://www.youtube.com/watch?v=JL_M6ap2Yqs"

@pytest.fixture
def mock_save_directory(tmpdir):
    return str(tmpdir)

def test_download_audio_with_valid_url_and_directory(mock_video_url, mock_save_directory):
    try:
        download_audio(mock_video_url, mock_save_directory, title="Test Title")
        # Verifica se o arquivo foi baixado com o título esperado
        downloaded_file = os.path.join(mock_save_directory, "Test Title.mp3")
        assert os.path.exists(downloaded_file)
    finally:
        # Remove o arquivo baixado
        if os.path.exists(downloaded_file):
            os.remove(downloaded_file)

def test_download_audio_without_title(mock_video_url, mock_save_directory):
    try:
        download_audio(mock_video_url, mock_save_directory, title="")
        # Verifica se o arquivo foi baixado com o título padrão
        downloaded_files = [f for f in os.listdir(mock_save_directory) if f.endswith(".mp3")]
        assert len(downloaded_files) == 1
    finally:
        # Limpa arquivos baixados
        for file in os.listdir(mock_save_directory):
            os.remove(os.path.join(mock_save_directory, file))

def test_download_audio_invalid_url():
    with pytest.raises(Exception):
        download_audio("https://invalid.url", "/invalid/directory", title="Invalid Test")
