# Image Generation with StyleGAN

This project is a Flask web application that uses a pre-trained StyleGAN model to generate a series of images based on an input image. The generated images are saved and returned as a response.

## Requirements

- Python 3.6+
- Flask
- Torch
- TorchVision
- PIL (Pillow)
- NumPy

## Setup

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Download the pre-trained model:**
    The code automatically downloads the pre-trained StyleGAN model from `torch.hub`.

## Usage

1. **Run the Flask application:**
    ```bash
    python app.py
    ```

2. **Access the web application:**
    Open your web browser and navigate to `http://0.0.0.0:5000/`.

3. **Generate images:**
    - Upload an image file using the web interface.
    - The application generates a series of images based on the uploaded image and returns their paths in the response.

## Project Structure

- `app.py`: The main Flask application file.
- `uploads/`: Directory to store uploaded images.
- `results/`: Directory to store generated images.
- `templates/index.html`: The home page for the web application (ensure this file exists with a form for uploading images).

## Endpoints

- `/`: Home page.
- `/generate` (POST): Endpoint to upload an image and generate new images.
    - Request: `multipart/form-data` with a file field named `file`.
    - Response: JSON containing paths to the generated images.

## Example

Here's an example of how to use the `/generate` endpoint with `curl`:

```bash
curl -X POST -F "file=@/path/to/your/image.jpg" http://0.0.0.0:5000/generate
```

## Notes

- Ensure that the `uploads` and `results` directories exist or are created automatically by the code.
- The generated images are saved in the `results` directory with filenames `generated_0.png`, `generated_1.png`, etc.

## License

This project is licensed under the MIT License.

---
