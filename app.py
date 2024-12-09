from flask import Flask, render_template, request, send_file
from youtube_transcript_api import YouTubeTranscriptApi
import re
import io

app = Flask(__name__)

def get_video_id(url):
    # Lấy video ID từ URL YouTube
    video_id = None
    if 'youtube.com' in url:
        video_id = re.search(r'v=([^&]+)', url).group(1)
    elif 'youtu.be' in url:
        video_id = url.split('/')[-1]
    return video_id

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            url = request.form['url']
            format_type = request.form['format']  # Lấy định dạng được chọn
            video_id = get_video_id(url)
            
            if not video_id:
                return "URL không hợp lệ", 400
            
            # Lấy phụ đề
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            
            if format_type == 'srt':
                # Tạo nội dung SRT
                content = ""
                for idx, line in enumerate(transcript, 1):
                    start = line['start']
                    duration = line['duration']
                    end = start + duration
                    
                    start_time = f"{int(start//3600):02d}:{int((start%3600)//60):02d}:{int(start%60):02d},{int((start%1)*1000):03d}"
                    end_time = f"{int(end//3600):02d}:{int((end%3600)//60):02d}:{int(end%60):02d},{int((end%1)*1000):03d}"
                    
                    content += f"{idx}\n{start_time} --> {end_time}\n{line['text']}\n\n"
                
                filename = 'subtitle.srt'
            else:
                # Tạo nội dung TXT
                content = ""
                for line in transcript:
                    content += f"{line['text']}\n"
                
                filename = 'subtitle.txt'
            
            # Tạo file để download
            buffer = io.BytesIO()
            buffer.write(content.encode('utf-8'))
            buffer.seek(0)
            
            return send_file(
                buffer,
                as_attachment=True,
                download_name=filename,
                mimetype='text/plain'
            )
            
        except Exception as e:
            return f"Có lỗi xảy ra: {str(e)}", 400
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)