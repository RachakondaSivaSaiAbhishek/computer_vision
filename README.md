# Basic Image, Video, and Webcam Processing in OpenCV (cv2)

This repository provides a collection of simple scripts and code snippets for performing basic image, video, and webcam processing using OpenCV (cv2) library in Python. OpenCV is a popular computer vision library that provides a wide range of tools and functions for image and video processing.

## Features

- **Image Processing**: Load and display images, perform basic operations such as resizing, cropping, rotating, and applying filters.
- **Video Processing**: Read and display videos, extract frames, and process each frame individually.
- **Webcam Processing**: Capture video from a webcam, apply real-time filters and effects, and display the output.


## Requirements

- Python 3.x
- OpenCV library
- NumPy library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/RachakondaSivaSaiAbhishek/computer_vision.git
```

2. Install the required libraries using pip:

```bash
pip install opencv-python numpy
```

## Usage

1. Update the `img` variable in the script with the path to your desired input image.
2. Run the script:

```bash
python functions.py
```

3. The processed images will be displayed in separate windows.

## Examples

Original Image             | Grayscale Image             | Blurred Image
:-------------------------:|:-------------------------:|:-------------------------:
![Original Image](https://github.com/RachakondaSivaSaiAbhishek/computer_vision/blob/main/car_functions/ori.png)  |  ![Grayscale Image](https://github.com/RachakondaSivaSaiAbhishek/computer_vision/blob/main/car_functions/grey.png)  | ![Blurred Image](https://github.com/RachakondaSivaSaiAbhishek/computer_vision/blob/main/car_functions/blur.png)


Edge-Detected Image             | Dilated Image             | Eroded Image
:-------------------------:|:-------------------------:|:-------------------------:
![Edge-Detected Image](https://github.com/RachakondaSivaSaiAbhishek/computer_vision/blob/main/car_functions/edg.png)  |  ![Dilated Image](https://github.com/RachakondaSivaSaiAbhishek/computer_vision/blob/main/car_functions/dil.png)  | ![Eroded Image](https://github.com/RachakondaSivaSaiAbhishek/computer_vision/blob/main/car_functions/eroded.png)


## License

This project is licensed under the [MIT License](LICENSE).

---

You can modify the paths and examples section to fit your specific use case and add more details if needed. Make sure to update the image paths and license information accordingly.

Feel free to customize it further to suit your project requirements!
