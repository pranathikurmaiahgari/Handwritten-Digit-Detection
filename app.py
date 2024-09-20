import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageOps
import numpy as np
from keras.models import load_model

# Load the pre-trained CNN model
model = load_model('cnn_model.h5')

# Initialize the GUI window
class DigitRecognizerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digit Recognizer")
        self.geometry("400x500")

        # Canvas for drawing digits
        self.canvas = tk.Canvas(self, width=280, height=280, bg="white", cursor="cross")
        self.canvas.pack(pady=20)

        # Create buttons for predict and clear
        button_frame = tk.Frame(self)
        button_frame.pack()

        self.clear_button = tk.Button(button_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side="left", padx=10)

        self.predict_button = tk.Button(button_frame, text="Predict", command=self.predict_digit)
        self.predict_button.pack(side="right", padx=10)

        # Label to display the result
        self.result_label = tk.Label(self, text="Draw a digit", font=("Helvetica", 18))
        self.result_label.pack(pady=20)

        # Set up drawing capabilities
        self.old_x, self.old_y = None, None
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Create a PIL Image to store the drawing
        self.image = Image.new("L", (280, 280), color=255)
        self.draw_image = ImageDraw.Draw(self.image)

    def draw(self, event):
        """Draw on the canvas and PIL image."""
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=10, fill="black", capstyle="round", smooth=True)
            self.draw_image.line([self.old_x, self.old_y, event.x, event.y], fill=0, width=10)

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        """Reset the line drawing coordinates."""
        self.old_x, self.old_y = None, None

    def clear_canvas(self):
        """Clear the canvas and reset the image."""
        self.canvas.delete("all")
        self.image = Image.new("L", (280, 280), color=255)
        self.draw_image = ImageDraw.Draw(self.image)
        self.result_label.config(text="Draw a digit")

    def predict_digit(self):
        """Predict the digit drawn on the canvas using the CNN model."""
        # Resize the image to 28x28 pixels as expected by the CNN model
        resized_image = self.image.resize((28, 28))
        resized_image = ImageOps.invert(resized_image)  # Invert colors: white background, black digit

        # Preprocess the image
        img_array = np.array(resized_image).astype('float32') / 255.0
        img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Get the model's prediction
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions[0])
        predicted_accuracy = np.max(predictions[0]) * 100  # Get highest probability as percentage

        # Display the result
        self.result_label.config(text=f"Predicted: {predicted_class} ({predicted_accuracy:.2f}% confidence)")

# Run the app
if __name__ == "__main__":
    app = DigitRecognizerApp()
    app.mainloop()
