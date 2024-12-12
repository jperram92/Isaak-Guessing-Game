import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk, ImageSequence, ImageDraw, ImageFont

class ToddlerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Pick your Activities")
        self.master.geometry("900x850")  # Adjusted height and width for better layout

        # Create the background canvas with a light blue background
        self.bg_canvas = tk.Canvas(master, width=900, height=850, bg="#ADD8E6")  # Light Blue Color
        self.bg_canvas.pack(fill=tk.BOTH, expand=True)

        # Create frames for layout
        self.top_frame = tk.Frame(self.bg_canvas, bg="#ADD8E6")  # Same light blue color as background
        self.top_frame.pack(pady=10)  # Add some padding at the top

        # Create frames for top options (left and right)
        self.left_frame = tk.Frame(self.bg_canvas, bg="#ADD8E6")
        self.left_frame.place(x=300, y=100, anchor="n")  # Centered on the left side (300px space)

        self.right_frame = tk.Frame(self.bg_canvas, bg="#ADD8E6")
        self.right_frame.place(x=600, y=100, anchor="n")  # Centered on the right side (300px space)

        # Add the title at the top, centered using pack()
        self.caption_label = tk.Label(self.top_frame, text="What do we do before we go to bed?", font=("Arial", 18, "bold"), bg="#ADD8E6")
        self.caption_label.pack()  # This will center the title within top_frame

        # Load default images/GIFs (Top row options)
        self.left_image_version = 1
        self.left_image_path = self.default_image_path_left = r"C:\Users\james\OneDrive\Desktop\Isaak Guessing Game\NoPictures.gif"
        self.left_caption = self.default_caption_left = "Reading"
        self.start_image_left = self.load_image(self.left_image_path)
        self.image_label_left = tk.Label(self.left_frame)
        self.image_label_left.pack()
        self.caption_label_left = tk.Label(self.left_frame, text=self.left_caption, font=("Arial", 14, "bold"), bg="#ADD8E6")
        self.caption_label_left.pack(pady=5)
        self.update_gif(self.image_label_left, self.start_image_left, 0)

        self.right_image_version = 1
        self.right_image_path = self.default_image_path_right = r"C:\Users\james\OneDrive\Desktop\Isaak Guessing Game\Playing.gif"
        self.right_caption = self.default_caption_right = "Playing"
        self.start_image_right = self.load_image(self.right_image_path)
        self.image_label_right = tk.Label(self.right_frame)
        self.image_label_right.pack()
        self.caption_label_right = tk.Label(self.right_frame, text=self.right_caption, font=("Arial", 14, "bold"), bg="#ADD8E6")
        self.caption_label_right.pack(pady=5)
        self.update_gif(self.image_label_right, self.start_image_right, 0)

        # Bottom row frames for new options (evenly spaced)
        self.extra_left_frame = tk.Frame(self.bg_canvas, bg="#ADD8E6")  # Extra frame 1
        self.extra_left_frame.place(x=50, y=470, anchor="nw")

        self.extra_center_frame = tk.Frame(self.bg_canvas, bg="#ADD8E6")  # Extra frame 2
        self.extra_center_frame.place(x=350, y=470, anchor="nw")

        self.extra_right_frame = tk.Frame(self.bg_canvas, bg="#ADD8E6")  # Extra frame 3
        self.extra_right_frame.place(x=650, y=470, anchor="nw")

        # Load default images/GIFs (Bottom row options)
        self.extra_left_image_version = 1
        self.extra_left_image_path = r"C:\Users\james\OneDrive\Desktop\Isaak Guessing Game\BrushTeeth.gif"
        self.extra_left_caption = "Brushing"
        self.start_image_extra_left = self.load_image(self.extra_left_image_path)
        self.image_label_extra_left = tk.Label(self.extra_left_frame)
        self.image_label_extra_left.pack()
        self.caption_label_extra_left = tk.Label(self.extra_left_frame, text=self.extra_left_caption, font=("Arial", 14, "bold"), bg="#ADD8E6")
        self.caption_label_extra_left.pack(pady=5)
        self.update_gif(self.image_label_extra_left, self.start_image_extra_left, 0)

        self.extra_center_image_version = 1
        self.extra_center_image_path = r"C:\Users\james\OneDrive\Desktop\Isaak Guessing Game\Eating.gif"
        self.extra_center_caption = "Eating"
        self.start_image_extra_center = self.load_image(self.extra_center_image_path)
        self.image_label_extra_center = tk.Label(self.extra_center_frame)
        self.image_label_extra_center.pack()
        self.caption_label_extra_center = tk.Label(self.extra_center_frame, text=self.extra_center_caption, font=("Arial", 14, "bold"), bg="#ADD8E6")
        self.caption_label_extra_center.pack(pady=5)
        self.update_gif(self.image_label_extra_center, self.start_image_extra_center, 0)

        self.extra_right_image_version = 1
        self.extra_right_image_path = r"C:\Users\james\OneDrive\Desktop\Isaak Guessing Game\Kiss.gif"
        self.extra_right_caption = "Kiss"
        self.start_image_extra_right = self.load_image(self.extra_right_image_path)
        self.image_label_extra_right = tk.Label(self.extra_right_frame)
        self.image_label_extra_right.pack()
        self.caption_label_extra_right = tk.Label(self.extra_right_frame, text=self.extra_right_caption, font=("Arial", 14, "bold"), bg="#ADD8E6")
        self.caption_label_extra_right.pack(pady=5)
        self.update_gif(self.image_label_extra_right, self.start_image_extra_right, 0)

        # Upload buttons and pick buttons
        self.upload_button_left = tk.Button(self.left_frame, text="Upload Your Own Image", command=lambda: self.upload_image(self.image_label_left, self.caption_label_left, "left"), bg="#ADD8E6")
        self.upload_button_left.pack()

        self.upload_button_right = tk.Button(self.right_frame, text="Upload Your Own Image", command=lambda: self.upload_image(self.image_label_right, self.caption_label_right, "right"), bg="#ADD8E6")
        self.upload_button_right.pack()

        self.upload_button_extra_left = tk.Button(self.extra_left_frame, text="Upload Your Own Image", command=lambda: self.upload_image(self.image_label_extra_left, self.caption_label_extra_left, "left"), bg="#ADD8E6")
        self.upload_button_extra_left.pack()

        self.upload_button_extra_center = tk.Button(self.extra_center_frame, text="Upload Your Own Image", command=lambda: self.upload_image(self.image_label_extra_center, self.caption_label_extra_center, "center"), bg="#ADD8E6")
        self.upload_button_extra_center.pack()

        self.upload_button_extra_right = tk.Button(self.extra_right_frame, text="Upload Your Own Image", command=lambda: self.upload_image(self.image_label_extra_right, self.caption_label_extra_right, "right"), bg="#ADD8E6")
        self.upload_button_extra_right.pack()

        # Pick buttons to select option
        self.pick_button_left = tk.Button(self.left_frame, text="Pick this option", command=lambda: self.pick_option(self.left_caption, self.left_image_path, "left"), bg="#ADD8E6")
        self.pick_button_left.pack(pady=5)

        self.pick_button_right = tk.Button(self.right_frame, text="Pick this option", command=lambda: self.pick_option(self.right_caption, self.right_image_path, "right"), bg="#ADD8E6")
        self.pick_button_right.pack(pady=5)

        self.pick_button_extra_left = tk.Button(self.extra_left_frame, text="Pick this option", command=lambda: self.pick_option(self.extra_left_caption, self.extra_left_image_path, "left"), bg="#ADD8E6")
        self.pick_button_extra_left.pack(pady=5)

        self.pick_button_extra_center = tk.Button(self.extra_center_frame, text="Pick this option", command=lambda: self.pick_option(self.extra_center_caption, self.extra_center_image_path, "center"), bg="#ADD8E6")
        self.pick_button_extra_center.pack(pady=5)

        self.pick_button_extra_right = tk.Button(self.extra_right_frame, text="Pick this option", command=lambda: self.pick_option(self.extra_right_caption, self.extra_right_image_path, "right"), bg="#ADD8E6")
        self.pick_button_extra_right.pack(pady=5)

        # Correct option configuration (can be customized)
        self.correct_options = ["Brushing", "Reading", "Kiss"]  # Both options are correct

    def upload_image(self, image_label, caption_label, frame_side):
        """Open a file dialog to upload an image or GIF.""" 
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            try:
                custom_image = Image.open(file_path)
                # Resize image if necessary
                custom_image = custom_image.resize((200, 200), resample=Image.BICUBIC)
                
                # Check if it's animated GIF or static image
                if getattr(custom_image, "is_animated", False):  # Check for animated GIFs
                    frames = []
                    for frame in ImageSequence.Iterator(custom_image):
                        frame = frame.resize((200, 200), resample=Image.BICUBIC)
                        frames.append(ImageTk.PhotoImage(frame))
                    self.update_gif(image_label, frames, 0)
                else:
                    # For static images, update the label directly
                    custom_image = ImageTk.PhotoImage(custom_image)
                    image_label.config(image=custom_image)
                    image_label.image = custom_image  # Keep reference to avoid garbage collection
               
                # Prompt user for a caption
                caption = simpledialog.askstring("Caption", "Enter a caption for the image:")
                if caption:
                    caption_label.config(text=caption)
                    if frame_side == "left":
                        self.left_caption = caption
                    elif frame_side == "right":
                        self.right_caption = caption
                    elif frame_side == "center":
                        self.extra_center_caption = caption
                    # Update the image path for future use
                    if frame_side == "left":
                        self.left_image_path = file_path
                    elif frame_side == "right":
                        self.right_image_path = file_path
                    elif frame_side == "center":
                        self.extra_center_image_path = file_path
            except Exception as e:
                messagebox.showerror("Image Load Error", f"Could not load image: {e}")

    def pick_option(self, caption, image_path, frame_side):
        """Handle the action for picking an activity option.""" 
        if caption in self.correct_options:  # Check if the selected option is in the correct list
            self.show_toddler_popup("Correct!", "Yay! You picked the right one! 😊", "green", r"C:\Users\james\OneDrive\Desktop\Isaak Guessing Game\giraffe_heads1.png")  # Giraffe image path
        else:
            self.show_toddler_popup("Oops!", "Oops! Try again. 😟", "red", r"C:\Users\james\OneDrive\Desktop\Isaak Guessing Game\GrumpyCat.png")  # Giraffe image path

    def show_toddler_popup(self, title, message, color, image_path):
        """Create a toddler-friendly popup.""" 
        popup = tk.Toplevel(self.master)
        popup.title(title)
        popup.geometry("300x250")
        popup.configure(bg=color)

        title_label = tk.Label(popup, text=title, font=("Arial", 18, "bold"), bg=color)
        title_label.pack(pady=20)

        message_label = tk.Label(popup, text=message, font=("Arial", 14), bg=color)
        message_label.pack(pady=10)

        # Load and display the giraffe image if it's the correct option
        if image_path:
            giraffe_img = Image.open(image_path)
            giraffe_img = giraffe_img.resize((80, 80), Image.Resampling.LANCZOS)
            giraffe_img = ImageTk.PhotoImage(giraffe_img)
            img_label = tk.Label(popup, image=giraffe_img, bg=color)
            img_label.image = giraffe_img  # Keep a reference to the image
            img_label.pack(pady=10)

        ok_button = tk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack(pady=10)

    def load_image(self, image_path):
        """Load an image or GIF from a file path.""" 
        try:
            img = Image.open(image_path)
            if getattr(img, "is_animated", False):  # Check if the image is animated
                frames = []
                for frame in ImageSequence.Iterator(img):
                    frame = frame.resize((200, 200), resample=Image.BICUBIC)
                    frames.append(ImageTk.PhotoImage(frame))
                return frames
            else:
                img = img.resize((200, 200), resample=Image.BICUBIC)
                return ImageTk.PhotoImage(img)
        except Exception as e:
            messagebox.showerror("Image Load Error", f"Could not load image: {e}")
            # Fallback to a default image if there is an error
            return ImageTk.PhotoImage(Image.new("RGB", (200, 200), (255, 255, 255)))

    def update_gif(self, label, frames, index):
        """Update the GIF animation in the label.""" 
        label.config(image=frames[index])
        index += 1
        if index >= len(frames):
            index = 0
        label.after(50, self.update_gif, label, frames, index)

if __name__ == "__main__":
    root = tk.Tk()
    game = ToddlerGame(root)
    root.mainloop()
