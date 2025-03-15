import React, { useState } from 'react';
import axios from 'axios';

export default function App() {
  const [inputText, setInputText] = useState('');
  const [imageUrl, setImageUrl] = useState('');

  async function generateImage(text) {
    try {
      const response = await axios.post('http://localhost:5000/generate', { text });
      setImageUrl(response.data.url);
    } catch (error) {
      console.error('生成图片失败：', error);
    }
  }

  return (
    <div className="container">
      <h1>DesignAI - 描述文字转图片</h1>
      <input
        type="text"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="输入描述文字..."
        style={{ width: '100%', height: '200px', padding: '10px' }}
      />
      <button
        onClick={() => generateImage(inputText)}
        className="generate-btn"
      >
        生成图片
      </button>
      {imageUrl && (
        <img src={imageUrl} alt="AI生成的图片" style={{ maxWidth: '100%', height: 'auto' }} />
      )}
    </div>
  );
}
