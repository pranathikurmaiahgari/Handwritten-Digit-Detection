
# 🎨 Handwritten Digit Detection with CNN 🖥️✍️

Welcome to the **Handwritten Digit Detection** project! This application allows users to draw digits on a canvas and predicts the digit using a highly accurate **Convolutional Neural Network (CNN)** model. The app also displays the model's confidence score and includes options to clear the canvas and make new predictions.

## 🌟 Features
- **Draw Digits**: Use the canvas to draw digits from 0 to 9.
- **Clear & Redraw**: Press the "Clear" button to erase the canvas and draw again.
- **Predict**: Get the digit prediction and confidence score with the "Predict" button.
- **CNN Model**: A trained CNN model achieves a **Test Accuracy** of 99.17%!
- **GUI Built with Tkinter**: An easy-to-use graphical interface.

---

## 🛠️ Project Structure
```bash
├── cnn_model.py          # CNN model creation and training
├── cnn_model.h5          # Trained CNN model
├── app.py # Main GUI application code
├── README.md             # This colorful readme!
```

---

## 🚀 How to Run the Project

### 1️⃣ Prerequisites
Make sure you have the following installed:
- **Python 3.x**
- **TensorFlow/Keras**
- **Pillow** for image manipulation
- **Tkinter** (comes pre-installed with Python)
- **NumPy** for handling arrays

To install dependencies, run:
```bash
pip install tensorflow keras pillow numpy
```

### 2️⃣ Running the App
1. Clone or download this repository.
2. Ensure the files `cnn_model.py` and `cnn_model.h5` (your trained CNN model) are in the project directory.
3. Run the GUI by executing the Python script:
   ```bash
   python app.py
   ```
4. A window will pop up where you can start drawing digits!

---

## 🖌️ How It Works
1. **Draw a digit** on the canvas (e.g., 0-9).
2. Click on the **Predict** button.
   - The app will process the drawing and predict the digit using the trained CNN model.
   - The predicted digit and **confidence score** will be displayed.
3. To erase your drawing, simply press the **Clear** button.

---

## 🧠 CNN Model Architecture
- **Input**: 28x28 grayscale image (handwritten digit).
- **Layers**:
  - **Conv2D + ReLU**: Extracts spatial features from the input image.
  - **Batch Normalization**: Normalizes the activations to improve training.
  - **MaxPooling**: Reduces dimensionality while retaining important features.
  - **Dropout**: Prevents overfitting by randomly dropping some neurons.
  - **Dense Layers**: Fully connected layers for classification.
  - **Output Layer**: Softmax activation for digit classification (0-9).

---


**Model Performance**:
- **Test loss**: 0.0309
- **Test accuracy**: 99.17%

---


## 🤝 Contributing
Feel free to fork this repository, raise issues, or submit pull requests for enhancements!

---

## 🔗 Resources
- **TensorFlow/Keras Documentation**: [https://www.tensorflow.org/](https://www.tensorflow.org/)
- **Tkinter Documentation**: [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)

---

## 📝 License
This project is open-source and available under the **MIT License**.

---

Happy coding, and enjoy building your digit recognition app! 🚀😊

---

