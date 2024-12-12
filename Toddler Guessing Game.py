import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk, ImageSequence, ImageDraw, ImageFont

class ToddlerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Pick your Activities")
        self.master.geometry("600x500")

        # Create the background canvas
        self.bg_canvas = tk.Canvas(master, width=600, height=500)
        self.bg_canvas.pack(fill=tk.BOTH, expand=True)

        # Create frames for layout
        self.top_frame = tk.Frame(self.bg_canvas)
        self.top_frame.pack(pady=10)  # Add some padding at the top

        self.left_frame = tk.Frame(self.bg_canvas)
        self.left_frame.place(x=50, y=100, anchor="nw")

        self.center_frame = tk.Frame(self.bg_canvas)
        self.center_frame.place(x=300, y=100, anchor="n")

        self.right_frame = tk.Frame(self.bg_canvas)
        self.right_frame.place(x=550, y=100, anchor="ne")

        # Add the title at the top, centered using pack()
        self.caption_label = tk.Label(self.top_frame, text="What do we do before we go to bed?", font=("Arial", 18, "bold"))
        self.caption_label.pack()  # This will center the title within top_frame

        # Load default images/GIFs
        self.left_image_version = 1
        self.left_image_path = self.default_image_path_left = r"C:\Users\james\OneDrive\Desktop\Isaak Guessing Game\NoPictures.gif"
        self.left_caption = self.default_caption_left = "Reading a Book"
        self.start_image_left = self.load_image(self.left_image_path)
        self.image_label_left = tk.Label(self.left_frame)
        self.image_label_left.pack()
        self.caption_label_left = tk.Label(self.left_frame, text=self.left_caption, font=("Arial", 14, "bold"))
        self.caption_label_left.pack(pady=5)
        self.update_gif(self.image_label_left, self.start_image_left, 0)

        self.right_image_version = 1
        self.right_image_path = self.default_image_path_right = r"C:\Users\james\OneDrive\Desktop\Isaak Guessing Game\Playing.gif"
        self.right_caption = self.default_caption_right = "Playing with Mom and Dad"
        self.start_image_right = self.load_image(self.right_image_path)
        self.image_label_right = tk.Label(self.right_frame)
        self.image_label_right.pack()
        self.caption_label_right = tk.Label(self.right_frame, text=self.right_caption, font=("Arial", 14, "bold"))
        self.caption_label_right.pack(pady=5)
        self.update_gif(self.image_label_right, self.start_image_right, 0)

        # Button to upload custom image
        self.upload_button_left = tk.Button(self.left_frame, text="Upload Your Own Image", command=lambda: self.upload_image(self.image_label_left, self.caption_label_left, "left"))
        self.upload_button_left.pack()

        self.upload_button_right = tk.Button(self.right_frame, text="Upload Your Own Image", command=lambda: self.upload_image(self.image_label_right, self.caption_label_right, "right"))
        self.upload_button_right.pack()

        # New button to pick this option
        self.pick_button_left = tk.Button(self.left_frame, text="Pick this option", command=lambda: self.pick_option(self.left_caption, self.left_image_path, "left"))
        self.pick_button_left.pack(pady=5)

        self.pick_button_right = tk.Button(self.right_frame, text="Pick this option", command=lambda: self.pick_option(self.right_caption, self.right_image_path, "right"))
        self.pick_button_right.pack(pady=5)

        # Correct option configuration
        self.correct_option = "Reading a Book"  # This can be customized for each question

    def pick_option(self, caption, image_path, frame_side):
        """Handle the action for picking an activity option."""
        if caption == self.correct_option:
            self.show_toddler_popup("Correct!", "Yay! You picked the right one! 😊", "green", r"C:\Users\james\OneDrive\Desktop\Isaak Guessing Game\giraffe_heads1.png")  # Giraffe image path
        else:
            self.show_toddler_popup("Oops!", "Oops! Try again. 😟", "red", r"C:\Users\james\OneDrive\Desktop\Isaak Guessing Game\GrumpyCat.png")  # Giraffe image path)

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
            if img.is_animated:
                frames = []
                for frame in ImageSequence.Iterator(img):
                    frame = frame.resize((200, 200), resample=Image.BICUBIC)
                    frames.append(ImageTk.PhotoImage(frame))
                return frames
            else:
                img = img.resize((200, 200), resample=Image.BICUBIC)
                return ImageTk.PhotoImage(img)
        except (Exception) as e:
            messagebox.showerror("Image Load Error", f"Could not load image: {e}")
            # Fallback to a default image
            return ImageTk.PhotoImage(Image.new("RGB", (200, 200), (255, 255, 255)))

    def upload_image(self, image_label, caption_label, frame_side):
        """Open a file dialog to upload an image or GIF."""
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            try:
                custom_image = Image.open(file_path)
                if custom_image.is_animated:
                    frames = []
                    for frame in ImageSequence.Iterator(custom_image):
                        frame = frame.resize((200, 200), resample=Image.BICUBIC)
                        frames.append(ImageTk.PhotoImage(frame))
                    self.update_gif(image_label, frames, 0)
                else:
                    custom_image = custom_image.resize((200, 200), resample=Image.BICUBIC)
                    custom_image = ImageTk.PhotoImage(custom_image)
                    image_label.config(image=custom_image)
                    image_label.image = custom_image
                # Prompt user for a caption
                caption = tk.simpledialog.askstring("Caption", "Enter a caption for the image:")
                if caption:
                    caption_label.config(text=caption)
                    if frame_side == "left":
                        self.left_caption = caption
                        self.left_image_version += 1
                    else:
                        self.right_caption = caption
                        self.right_image_version += 1
                # Update the image and caption variables
                if frame_side == "left":
                    self.left_image_path = file_path
                else:
                    self.right_image_path = file_path
            except (Exception) as e:
                messagebox.showerror("Image Load Error", f"Could not load image: {e}")
        self.upload_button_right.pack()

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
