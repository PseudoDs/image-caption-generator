import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import threading
import os
import sys
from transformers import pipeline

class CaptionGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Image Caption Generator")
        self.root.geometry("650x700")
        self.root.resizable(False, False)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 11))
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        
        # Main container
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Image display
        self.image_frame = ttk.Frame(self.main_frame)
        self.image_frame.pack(pady=10)
        
        self.image_label = ttk.Label(self.image_frame)
        self.image_label.pack()
        
        # Controls
        self.controls_frame = ttk.Frame(self.main_frame)
        self.controls_frame.pack(pady=15)
        
        self.browse_btn = ttk.Button(
            self.controls_frame, 
            text="Browse Image", 
            command=self.load_image,
            style='TButton'
        )
        self.browse_btn.pack(side=tk.LEFT, padx=5)
        
        self.copy_btn = ttk.Button(
            self.controls_frame, 
            text="Copy Caption", 
            command=self.copy_caption,
            state=tk.DISABLED
        )
        self.copy_btn.pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready to load an image")
        self.status_bar = ttk.Label(
            self.main_frame, 
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, pady=(15,0))
        
        # Caption display
        self.caption_frame = ttk.Frame(self.main_frame)
        self.caption_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.caption_text = tk.Text(
            self.caption_frame,
            wrap=tk.WORD,
            font=('Arial', 11),
            height=6,
            padx=10,
            pady=10,
            state=tk.DISABLED
        )
        self.caption_text.pack(fill=tk.BOTH, expand=True)
        
        # Initialize model in background
        self.model = None
        threading.Thread(target=self.initialize_model, daemon=True).start()
    
    def initialize_model(self):
        self.status_var.set("Loading AI model (first time may take a few minutes)...")
        try:
            self.model = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
            self.status_var.set("Model loaded successfully! Ready to use.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load model:\n{str(e)}")
            self.status_var.set("Model failed to load")
    
    def load_image(self):
        filetypes = [
            ("Image files", "*.jpg *.jpeg *.png"),
            ("All files", "*.*")
        ]
        filepath = filedialog.askopenfilename(title="Select an image", filetypes=filetypes)
        
        if filepath:
            try:
                # Display image
                image = Image.open(filepath)
                image.thumbnail((550, 550))
                photo = ImageTk.PhotoImage(image)
                
                self.image_label.config(image=photo)
                self.image_label.image = photo
                self.status_var.set("Generating caption...")
                self.copy_btn.config(state=tk.DISABLED)
                
                # Generate caption in background
                threading.Thread(
                    target=self.generate_caption,
                    args=(image,),
                    daemon=True
                ).start()
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image:\n{str(e)}")
                self.status_var.set("Error loading image")
    
    def generate_caption(self, image):
        try:
            if not self.model:
                messagebox.showwarning("Warning", "Model is still loading, please wait")
                return
                
            result = self.model(image)
            caption = result[0]['generated_text']
            
            self.caption_text.config(state=tk.NORMAL)
            self.caption_text.delete(1.0, tk.END)
            self.caption_text.insert(tk.END, caption)
            self.caption_text.config(state=tk.DISABLED)
            
            self.copy_btn.config(state=tk.NORMAL)
            self.status_var.set("Caption generated successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Caption generation failed:\n{str(e)}")
            self.status_var.set("Caption generation failed")
    
    def copy_caption(self):
        caption = self.caption_text.get(1.0, tk.END).strip()
        if caption:
            self.root.clipboard_clear()
            self.root.clipboard_append(caption)
            self.status_var.set("Caption copied to clipboard!")
            self.root.after(2000, lambda: self.status_var.set("Ready to load another image"))

if __name__ == "__main__":
    root = tk.Tk()
    app = CaptionGeneratorApp(root)
    root.mainloop()