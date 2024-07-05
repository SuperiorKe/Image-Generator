import os
import torch
from torchvision import transforms
from flask import Flask, request, render_template, send_from_directory
from PIL import Image

app = Flask(__name__)

# Load the pre-trained CycleGAN model (e.g., apple2orange)
model = torch.hub.load('junyanz/pytorch-CycleGAN-and-pix2pix', 'cyclegan_apple2orange', pretrained=True)
model.eval()

def transform_image(image_path):
    input_image = Image.open(image_path).convert('RGB')
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ])
    return preprocess(input_image).unsqueeze(0)

def generate_image(input_image_path):
    input_tensor = transform_image(input_image_path)
    with torch.no_grad():
        output_tensor = model(input_tensor)
    output_image = (output_tensor.squeeze().cpu().numpy() + 1) / 2 * 255
    output_image = output_image.transpose(1, 2, 0).astype('uint8')
    return output_image

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        output_image = generate_image(file_path)
        result_path = os.path.join('results', f'generated_{file.filename}')
        Image.fromarray(output_image).save(result_path)

        return render_template('results.html', image=result_path)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

@app.route('/results/<filename>')
def result_file(filename):
    return send_from_directory('results', filename)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('results', exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
