from flask import Flask, request, render_template
import os
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications import imagenet_utils

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
model_path = 'models/resnet50.h5'

# 加载预训练模型
model = imagenet_utils.load_model(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    if not request.json:
        return jsonify({'status': 'error', 'message': '缺少请求体'}), 400
    text = request.json.get('text')
    
    try:
        # 加载图片并预测
        image_path = os.path.join(UPLOAD_FOLDER, 'temp.jpg')
        img = load_img(image_path)
        features = model.predict(img)[0]
        
        # 调用外部模型生成图片（此示例简化为生成固定路径）
        generated_url = f'https://example.com/api/v1/generate-image/{features}'
        return jsonify({'url': generated_url}), 200
    except Exception as e:
        print(f'生成图片失败：{str(e)}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
