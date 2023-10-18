from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# 업로드된 파일이 저장될 디렉토리 설정
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)

        # 업로드한 데이터 파일을 Pandas로 읽음
        #data = pd.read_csv(file_path, encoding='utf-8',  errors='ignore')
        with open(file_path, 'r', errors='ignore') as f:
            data = pd.read_csv(f)
        

        # 데이터 분석 작업 수행 (예: 데이터 요약 통계)
        data_summary = data.describe()

        return render_template('analysis_result.html', tables=[data_summary.to_html(classes='data')], titles=data_summary.columns.values)
    else:
        return '파일을 선택하세요.'

if __name__ == '__main__':
    app.run(debug=True, port = 8081)
