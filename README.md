# 🖼️ AI Image Caption Generator

An AI-powered desktop application that generates descriptive captions for images using cutting-edge deep learning models — all packed into a clean, intuitive interface built with Tkinter.

---

## ✨ Features

- 📷 Upload any image (`.jpg`, `.png`)
- 🧠 Generates captions using `ViT-GPT2` from Hugging Face Transformers
- 🪟 Simple and clean Tkinter GUI
- ⚡ Runs completely offline after dependencies are installed
- 📋 One-click copy to clipboard

---

## 📂 Folder Structure

<pre>
image-caption-generator/
├── caption_gui.py            # Main GUI code
├── caption_gui.spec          # PyInstaller build config
├── Sample_images/            # Folder with sample images
│   ├── Dog_demo.png
│   └── Man_demo.png
├── dist/                     # Contains generated executable
│   └── caption_gui.exe
├── build/                    # Auto-generated during build
├── requirements.txt          # Project dependencies
├── .gitignore                # Git ignored files/folders
└── README.md                 # Project overview and usage
</pre>

---
---

## 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/github/license/PseudoDs/image-caption-generator)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![HuggingFace Model](https://img.shields.io/badge/Model-ViT--GPT2-orange)
![Built with Tkinter](https://img.shields.io/badge/UI-Tkinter-blueviolet)

## 🚀 Getting Started

### 1. Clone this repo
```bash
git clone https://github.com/PseudoDs/image-caption-generator.git
cd image-caption-generator
```



2. Install dependencies

```bash
pip install -r requirements.txt
```



3. Run the app

```bash
python caption_gui.py
```
⏳ The model may take a few minutes to load the first time.



📦 Build Executable (Optional)
To create a standalone .exe (Windows only):

```bash
pip install pyinstaller
pyinstaller caption_gui.py --onefile --noconsole
```


🧠 Model Info
Uses ViT-GPT2 Image Captioning from Hugging Face 🤗



🛠️ Dependencies

- `transformers`
- `torch`
- `Pillow`
- `tkinter`


💖 Made with love by Daisy and Deepika ☕✨
“A picture is worth a thousand words, but sometimes it needs help finding them.”
