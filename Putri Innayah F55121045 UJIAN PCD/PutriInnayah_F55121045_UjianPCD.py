from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

class ImageEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Putri Innayah F55121045 PROGRAM PERBAIKAN CITRA")
        self.master.resizable(False, False)
        
        # Membuat Elemen-elemen GUI
        self.original_image_label = Label(self.master, text="Original Image")
        self.original_image_label.grid(row=0, column=0)
        self.processed_image_label = Label(self.master, text="Processed Image")
        self.processed_image_label.grid(row=0, column=1)
        
        self.original_image_canvas = Canvas(self.master, width=400, height=400)
        self.original_image_canvas.grid(row=1, column=0)
        self.processed_image_canvas = Canvas(self.master, width=400, height=400)
        self.processed_image_canvas.grid(row=1, column=1)
        
        self.noise_reduction_button = Button(self.master, text="Noise Reduction", command=self.noise_reduction)
        self.noise_reduction_button.grid(row=2, column=0)
        self.sharpen_button = Button(self.master, text="Sharpen", command=self.sharpen)
        self.sharpen_button.grid(row=2, column=1)
        
        self.original_image = None
        self.processed_image = None
    
    def open_file(self):
        # Membuat Fungsi untuk menginput Image
        file_path = filedialog.askopenfilename(title="Open Image", filetypes=[("Image files", "*.jpg *.png *.bmp")])
        if file_path:
            # Fungsi Untuk menampilakn gambar yang dipilih
            self.original_image = Image.open(file_path).resize((400, 400))
            self.original_image_tk = ImageTk.PhotoImage(self.original_image)
            self.original_image_canvas.create_image(0, 0, anchor=NW, image=self.original_image_tk)
            
            self.processed_image_canvas.delete("all")
    
    def noise_reduction(self):
        # Membuat fungsi Noise Reduction
        if self.original_image:
            self.processed_image = self.original_image.filter(ImageFilter.MedianFilter())
            self.processed_image_tk = ImageTk.PhotoImage(self.processed_image)
            self.processed_image_canvas.create_image(0, 0, anchor=NW, image=self.processed_image_tk)
    
    def sharpen(self):
        # Membuat fungsi Sgarpen Image
        if self.original_image:
            self.processed_image = self.original_image.filter(ImageFilter.SHARPEN)
            self.processed_image_tk = ImageTk.PhotoImage(self.processed_image)
            self.processed_image_canvas.create_image(0, 0, anchor=NW, image=self.processed_image_tk)
    
root = Tk()
app = ImageEditor(root)

# Membuat Menu Bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=app.open_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.mainloop()

