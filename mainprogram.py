import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageOps, ImageTk, ImageFilter

def main():
    parent = tk.Tk()
    parent.title("ImageEditor")
    parent.geometry("1000x800")
    parent.config(bg="white")


    def addImage():
        global file_path
        file_path = filedialog.askopenfilename()
        
        image = Image.open(file_path)

        # get the dimensions of canvas 
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        # calculate the scale factor to fit image within the canvas 
        width_ratio = canvas_width/image.width
        height_ratio = canvas_height/image.height
        scale_factor = min(width_ratio, height_ratio)

        # resize the image while maintaining its aspect ratio 
        new_width = int(image.width * scale_factor)
        new_height = int(image.height * scale_factor)
        image = image.resize((new_width, new_height), Image.LANCZOS)

        # convert the PIL Image to a Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image)

        # update the displayed image on the canvas 
        canvas.create_image(canvas_width/2, canvas_height/2, image=photo, anchor="center")
        canvas.image = photo
        

    def apply_filter(filter):
        image = Image.open(file_path)

        # get the dimensions of canvas 
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        # calculate the scale factor to fit image within the canvas 
        width_ratio = canvas_width/image.width
        height_ratio = canvas_height/image.height
        scale_factor = min(width_ratio, height_ratio)

        # resize the image while maintaining its aspect ratio 
        new_width = int(image.width * scale_factor)
        new_height = int(image.height * scale_factor)
        image = image.resize((new_width, new_height), Image.LANCZOS)

        if filter == "B & W":
            image = ImageOps.grayscale(image)
        elif filter == "Blur":
            image = image.filter(ImageFilter.BLUR)
        elif filter == "Contour":
            image = image.filter(ImageFilter.CONTOUR)
        elif filter == "Detail":
            image = image.filter(ImageFilter.DETAIL)
        elif filter == "Edge Enhance":
            image == image.filter(ImageFilter.EDGE_ENHANCE)
        elif filter == "Emboss":
            image = image.filter(ImageFilter.EMBOSS)
        elif filter == "Sharpen":
            image = image.filter(ImageFilter.SHARPEN)
        elif filter == "Smooth":
            image = image.filter(ImageFilter.SMOOTH)

        # convert the PIL Image to a Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image)

        # update the displayed image on the canvas 
        canvas.create_image(canvas_width/2, canvas_height/2, image=photo, anchor="center")
        canvas.image = photo

    left_frame = tk.Frame(parent, width=200, height=400, bg="light gray")
    left_frame.pack(side="left", fill="y")

    canvas = tk.Canvas(parent, width=700, height=650, bg="white")
    canvas.pack()

    addImage_button = tk.Button(left_frame, text="Add Image", command=addImage)
    addImage_button.pack(pady=20)

    filter_label = tk.Label(left_frame, text="Select Filter", bg="white")
    filter_label.pack()
    filter_combobox = ttk.Combobox(left_frame, values=["B & W", "Blur", 
                                                    "Contour", "Detail", 
                                                    "Edge Enhance", "Emboss", 
                                                    "Sharpen", "Smooth"])
    filter_combobox.pack()
    filter_combobox.bind("<<ComboboxSelected>>",
                        lambda event: apply_filter(filter_combobox.get()))


    parent.mainloop()

if __name__ == "__main__":
    main()