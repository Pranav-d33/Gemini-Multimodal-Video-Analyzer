# Gemini Multimodal Video Analyzer

![Video Analyzer Banner](https://img.shields.io/badge/Gemini-2.0%20Flash-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Phi Framework](https://img.shields.io/badge/Phi-Framework-green)

A powerful AI-powered video analysis tool that allows users to upload videos and have natural language conversations about the content. Built with Gemini 2.0 Flash, Streamlit, and the Phi Agent framework.

## 🌟 Features

- **Video Analysis**: Upload and analyze videos in various formats (MP4, MOV, AVI)
- **Conversational Interface**: Ask questions and get insights about the video content
- **Web Research Integration**: Supplements video analysis with relevant web information via DuckDuckGo
- **Multimodal Understanding**: Processes both visual and audio content from videos
- **User-Friendly UI**: Clean Streamlit interface with intuitive controls

## 🛠️ Technologies Used

- **Google Gemini 2.0 Flash**: State-of-the-art multimodal AI model
- **Phi Framework**: For building agentic AI applications
- **Streamlit**: For the web interface
- **Python**: Core programming language
- **DuckDuckGo API**: For web search capabilities

## 📋 Prerequisites

- Python 3.9+
- Google API Key for Gemini access

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pranav-d33/Gemini-Multimodal-Video-Analyzer.git
   cd Gemini-Multimodal-Video-Analyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

## 🖥️ Usage

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the displayed URL (typically http://localhost:8501)

3. Upload a video file using the file uploader

4. Enter your question or specify what insights you're looking for

5. Click the "Analyze Video" button and wait for the AI to process your request

## 📝 Example Queries

- "Summarize the main points discussed in this video"
- "What emotions are displayed by the people in this clip?"
- "Explain the technical process demonstrated in this tutorial"
- "What are the key arguments presented in this debate?"
- "Identify the products shown in this commercial"

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- Google Gemini team for the powerful AI model
- Phi Framework developers
- Streamlit team for the excellent web app framework
