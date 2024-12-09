# YouTube Subtitle Downloader

A simple web application to download subtitles from YouTube videos in two formats: SRT and TXT.

## Features

- Download subtitles from YouTube videos via URL
- Support two file formats:
  - SRT (SubRip Subtitle): standard subtitle format with timestamps
  - TXT: plain text content only
- Simple and user-friendly interface

## System Requirements

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/NDuyToan/youtube-subtitle-downloader.git
cd youtube-subtitle-downloader
```

2. Install required libraries:

```bash
pip install flask youtube_transcript_api
```

## Directory Structure

```
youtube-subtitle-downloader/
│
├── app.py
├── templates/
│   └── index.html
└── README.md
```

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:

   ```
   http://localhost:5000
   ```

3. Enter the YouTube video URL and select the desired file format (SRT or TXT)

4. Click "Download Subtitles" to download the file

## Notes

- Only works with videos that have subtitles
- Internet connection required
- Some videos may be restricted and subtitles cannot be downloaded
- Downloads English subtitles by default (if available)

## Common Errors

1. "Invalid URL": Check the YouTube video URL
2. "Transcript not available": Video doesn't have subtitles
3. "Video unavailable": Video doesn't exist or has been deleted

## Future Development

- [ ] Add option to select subtitle language
- [ ] Add subtitle preview before downloading
- [ ] Support more subtitle formats
- [ ] Improve user interface

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or create an Issue.

## License

[MIT License](LICENSE)

## Author

[Nguyen Duy Toan]

## Contact

- Email: [nguyenduytoanbkdn@gmail.com]
- GitHub: [https://github.com/NDuyToan]
