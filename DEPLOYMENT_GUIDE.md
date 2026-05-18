# Deployment Guide - Heart Disease Prediction Dashboard

## GitHub Repository
✅ **Successfully pushed to:** https://github.com/karlsxo/Data-Mining-_-Final-Project.git

---

## Deployment Options for Streamlit Apps

### **Option 1: Streamlit Cloud (RECOMMENDED) ⭐**
**Best for Streamlit apps - Free & Easy**

1. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
2. Click "Deploy an app"
3. Connect your GitHub account
4. Select the repository: `karlsxo/Data-Mining-_-Final-Project`
5. Branch: `master`
6. Main file path: `streamlit_app.py`
7. Click "Deploy"

**Advantages:**
- ✅ Streamlit optimized
- ✅ Free hosting
- ✅ Auto-deploys on git push
- ✅ Built-in sharing and security
- ✅ Easy to configure secrets

---

### **Option 2: Render (Alternative) 🚀**
**Good alternative with generous free tier**

1. Go to [render.com](https://render.com)
2. Click "New +"
3. Select "Web Service"
4. Connect GitHub repository
5. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run streamlit_app.py`
6. Deploy

**Advantages:**
- ✅ Free tier with good specs
- ✅ Works with Streamlit
- ✅ Auto-deploys on git push
- ✅ Easy environment variables

---

### **Option 3: Heroku (Legacy) 🔧**
**Works but requires more setup**

Create `Procfile` in root directory:
```
web: streamlit run --server.port=$PORT --server.address=0.0.0.0 streamlit_app.py
```

Then:
1. Install Heroku CLI
2. Run: `heroku login`
3. Run: `heroku create your-app-name`
4. Run: `git push heroku master`

---

### **Option 4: Docker on Vercel/Railway 🐳**
**Most flexible but requires Docker**

Create `Dockerfile`:
```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Then deploy Docker image to:
- Railway.app
- Replit
- DigitalOcean App Platform

---

## ⚠️ Important: Vercel + Streamlit

**Vercel is Node.js first and doesn't natively support Python Streamlit apps.**

If you must use Vercel specifically, you would need:
- A Python runtime environment (like Railway or Render instead)
- Or convert to a Next.js web app using Python API backend (complex)

**Recommendation:** Use **Streamlit Cloud** (Option 1) - it's the easiest and best-supported option.

---

## Quick Comparison Table

| Platform | Setup Time | Cost | Python Support | Auto-Deploy |
|----------|-----------|------|-----------------|------------|
| Streamlit Cloud | 2 min | Free | ✅ Native | ✅ Yes |
| Render | 5 min | Free tier | ✅ Yes | ✅ Yes |
| Heroku | 10 min | Paid ($7+) | ✅ Yes | ✅ Yes |
| Railway | 5 min | Free tier | ✅ Yes | ✅ Yes |
| **Vercel** | **N/A** | **N/A** | ❌ No | **N/A** |

---

## Environment Variables (if needed)

For any platform, you can set environment variables in the deployment settings.

Example for `.env` file (not committed):
```
PYTHONUNBUFFERED=1
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

---

## Deployment Checklist

- ✅ Code pushed to GitHub
- ✅ `.gitignore` configured
- ✅ `requirements.txt` present
- ✅ `.streamlit/config.toml` configured
- ⏭️ **Next:** Choose platform and deploy (recommend Streamlit Cloud)

---

## Next Steps

1. **Recommended:** Go to [streamlit.io/cloud](https://streamlit.io/cloud) and deploy in 2 minutes
2. Share your live dashboard with friends, colleagues, and stakeholders!
3. Monitor app performance from the cloud dashboard

Need help? Contact the Streamlit community on Discord!
