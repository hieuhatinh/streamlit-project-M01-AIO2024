# Streamlit Project - M01 - AIO 2024

## 1. Clone the repository: 
```
git clone https://github.com/hieuhatinh/streamlit-project-M01-AIO2024.git
```
## 2. Cài đặt thư viện ***streamlit***: 
```
pip install streamlit
```
## 3. Chạy dự án: 
Trong repo này có 3 dự án nhỏ dùng streamlit làm giao diện tương tác người dùng: 
* *Word Correction using Levenshtein Distance*
* *Oject Detection using DNN model*
* *Simple Chatbot using HugChat*

***(Option) Nếu sử dụng Anaconda, tạo môi trường mới và cài đặt các thư viện cần thiết cho từng dự án***
    
### 3.1 Word Correction using Levenshtein Distance:
- Sau khi clone project, mở 1 terminal/cmd mới
- Di chuyển đến thư mục chứa dự án Word Correction: 
```
cd ./word_correction
```
- Chạy dự án: 
```
streamlit run main.py
```
- Muốn thử nghiệm với data mới thì vào file `data/vocab.txt` để thêm hoặc tạo ra bộ từ mới

### 3.2. Oject Detection using DNN model: 
- Sau khi clone project, mở 1 terminal/cmd mới
- Di chuyển đến thư mục chứa dự án Object Detection: 
```
cd ./object_detection
```
- Chạy dự án: 
```
streamlit run main.py
```

### 3.3. Simple Chatbot using HugChat: 
- Truy cập [HugChat](https://huggingface.co/chat/) để tạo tài khoản hugchat
- Sau khi clone project và tạo tài khoản hugchat, mở 1 terminal/cmd mới
- Di chuyển đến thư mục chứa dự án Simple Chatbot: 
```
cd ./chatbot
```
- Chạy dự án: 
```
streamlit run main.py
```