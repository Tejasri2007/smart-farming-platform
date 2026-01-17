# Smart Farming Platform - Deployment Guide

## 🚀 Deploy to Streamlit Cloud (Recommended - FREE)

### Step 1: Prepare for Deployment
```bash
# Create streamlit config
mkdir .streamlit
```

### Step 2: Upload to GitHub
1. Create GitHub repository
2. Upload all project files
3. Ensure requirements.txt is included

### Step 3: Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file: `src/app.py`
6. Click "Deploy"

## 🔧 Alternative: Heroku (Free Tier Ended)

### Required Files:
- `Procfile`
- `setup.sh`
- Updated `requirements.txt`

## 🐳 Alternative: Railway/Render

### Railway:
1. Connect GitHub repo
2. Set start command: `streamlit run src/app.py --server.port $PORT`

### Render:
1. Connect GitHub repo  
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `streamlit run src/app.py --server.port $PORT --server.address 0.0.0.0`

## ⚠️ Important Notes:
- TensorFlow models are large (may exceed free limits)
- Consider using lightweight model or CPU-only version
- Weather API key needed for production