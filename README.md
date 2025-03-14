# YouTube Downloader - Baixe Vídeos e Converta para MP3 🎵

## 📝 Descrição
Este é um aplicativo simples para baixar vídeos do YouTube e convertê-los em arquivos de áudio MP3, utilizando `yt-dlp` e `ffmpeg`. O projeto possui uma interface gráfica amigável desenvolvida com `Tkinter`.

## 🚀 Funcionalidades
- Baixar vídeos do YouTube no formato de áudio (MP3).  
- Escolher o diretório de destino para salvar os arquivos.  
- Definir um nome personalizado para o arquivo de saída.  
- Barra de progresso para acompanhar o status do download.  
- Validação de URL e diretório para evitar erros comuns.  
- Testes automatizados para garantir a estabilidade da aplicação.

## 🛠️ Tecnologias Utilizadas
- **Python 3.9+**
- **yt-dlp** (para baixar vídeos do YouTube)
- **ffmpeg** (para conversão de áudio)
- **Tkinter** (para interface gráfica)
- **Pytest** (para testes automatizados)

## 📋 Pré-requisitos
Antes de rodar o projeto, certifique-se de que possui os seguintes pacotes instalados:

- **Python 3.8 ou superior**
- **FFmpeg** (certifique-se de que o caminho do `ffmpeg` está configurado corretamente no `config.py`)
- **yt-dlp** (pode ser instalado com `pip install yt-dlp`)
- **Outros pacotes** necessários podem ser instalados com:

```bash
pip install -r requirements.txt
```
## ⚙️ Executando a Aplicação
Após instalar as dependências, execute o aplicativo com:
```bash
python app/main.py
```
Isso abrirá a interface gráfica do YouTube Downloader.

## 🧪 Executando os Testes
O projeto inclui testes automatizados para garantir a funcionalidade correta. Para rodá-los, utilize:
```bash
pytest tests/
```
Os testes cobrem a interface gráfica (ui.py) e a lógica de download (downloader.py).

## 📂 Estrutura do Projeto
```bash
📂 app
│── __init__.py
│── config.py        # Configuração do caminho do FFmpeg
│── downloader.py    # Lógica de download e conversão para MP3
│── ui.py            # Interface gráfica do aplicativo
│── utils.py         # Funções auxiliares para validação
│── main.py          # Arquivo principal para iniciar a aplicação
│
📂 tests
│── __init__.py
│── test_downloader.py  # Testes para o módulo de download
│── teste_ui.py         # Testes para a interface gráfica
│
.gitignore
requirements.txt        # Dependências do projeto
```
## 🤝 Contribuição
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Basta fazer um fork do repositório e abrir um pull request!

### 📜 Licença
Este projeto está licenciado sob a MIT License.






