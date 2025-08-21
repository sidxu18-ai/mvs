# 🚀 Deployment Guide

## Quick Setup for Your Repository

### 1. Clone Your Repository
```bash
git clone https://github.com/sidxu18-ai/mvs.git
cd mvs
```

### 2. Setup Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure GitHub Token
```bash
# Copy the template
cp .env.template .env

# Edit .env and add your GitHub token:
# GITHUB_TOKEN=your_github_personal_access_token_here
```

### 4. Install FFmpeg
```bash
# Windows (using winget)
winget install Gyan.FFmpeg

# Or run the automated installer
python install_ffmpeg.py

# macOS
brew install ffmpeg

# Linux
sudo apt install ffmpeg
```

### 5. Run the Application
```bash
# Basic interface
streamlit run streamlit_app.py

# Advanced PDF interface
streamlit run integrated_pdf_app.py

# Direct selection interface
streamlit run direct_selection_app.py
```

## 🌐 Online Deployment Options

### Streamlit Cloud
1. Connect your GitHub repo to [Streamlit Cloud](https://streamlit.io/cloud)
2. Add your `GITHUB_TOKEN` in the secrets section
3. Deploy automatically

### Heroku
1. Add `Procfile`:
   ```
   web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
   ```
2. Add buildpacks for Python and FFmpeg
3. Set environment variables

### Docker
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install FFmpeg
RUN apt-get update && apt-get install -y ffmpeg

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.address", "0.0.0.0"]
```

## 📊 Usage Analytics

To track usage, you can add:
- Google Analytics
- Streamlit metrics
- Custom logging

## 🔒 Security Notes

- Keep your GitHub token secure
- Use environment variables for sensitive data
- Consider rate limiting for production use
