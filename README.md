# ⚡ FocusFlow - Smart Productivity App

A beautiful, AI-powered productivity app built with Streamlit. Track tasks, manage your energy levels, monitor your mood, and let smart algorithms decide what to work on next.

## ✨ Features

- **Smart Task Picker**: AI-powered task recommendations based on your energy level and priorities
- **Mood Tracker**: Track your daily mood with beautiful visualizations
- **Analytics Dashboard**: Deep insights into your productivity patterns
- **Priority Management**: Organize tasks by priority and energy requirements
- **Completion Tracking**: See your productivity streaks and completed tasks
- **Beautiful UI**: Modern, gradient-based design with smooth interactions

## 🚀 Quick Start

### Local Development

1. **Clone or download this repository**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run app.py
```

4. **Open your browser**
The app will automatically open at `http://localhost:8501`

## ☁️ Deploy to Streamlit Cloud (FREE)

1. **Push to GitHub**
   - Create a new repository on GitHub
   - Push this code to your repository

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository, branch (main), and file (app.py)
   - Click "Deploy"

3. **Your app will be live in minutes!**
   - You'll get a URL like: `https://your-app-name.streamlit.app`

## 🐳 Deploy with Docker

1. **Build the image**
```bash
docker build -t focusflow .
```

2. **Run the container**
```bash
docker run -p 8501:8501 focusflow
```

## 📦 Deploy to Other Platforms

### Heroku
```bash
# Install Heroku CLI, then:
heroku create your-app-name
git push heroku main
```

### Railway.app
- Connect your GitHub repo
- Railway will auto-detect Streamlit
- Click Deploy

### Render.com
- Connect your GitHub repo
- Select "Web Service"
- Build Command: `pip install -r requirements.txt`
- Start Command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

## 📁 File Structure

```
focusflow/
├── app.py                 # Main application
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── tasks.json            # Task storage (auto-created)
├── mood.json             # Mood data (auto-created)
└── stats.json            # Statistics (auto-created)
```

## 🎨 Features Breakdown

### Dashboard
- Quick overview of tasks, moods, and productivity
- Visual mood trends
- Recent task overview

### Task Management
- Add tasks with energy levels and priorities
- Filter and organize tasks
- Mark tasks as complete
- Track completion history

### Smart Picker
- Get AI-recommended tasks based on:
  - Current energy level
  - Available time
  - Task priorities
- Weighted random selection favoring high-priority items

### Mood Tracking
- Log daily moods (1-10 scale)
- Add optional notes
- View mood trends over time
- Calculate average mood

### Analytics
- Task distribution by priority
- Energy level distribution
- Completion trends
- Productivity streaks

## 🛠️ Customization

### Change Colors
Edit the CSS in `app.py` (lines 27-90) to customize:
- Primary colors
- Task card colors
- Background colors

### Add Features
The code is modular and well-commented. Easy areas to extend:
- Add categories/tags to tasks
- Implement task due dates
- Add notification reminders
- Export data to CSV
- Add team collaboration

## 📊 Data Storage

Data is stored in JSON files:
- `tasks.json` - Your task list
- `mood.json` - Mood tracking data
- `stats.json` - Completion statistics

**Note**: For production use with multiple users, consider upgrading to a database like PostgreSQL or MongoDB.

## 🔒 Privacy

All data is stored locally in JSON files. When deployed to Streamlit Cloud, each deployment has its own isolated file system. For multi-user applications, implement proper authentication and database storage.

## 🤝 Contributing

Feel free to fork, modify, and enhance! Some ideas:
- Add calendar integration
- Implement Pomodoro timer
- Add data export features
- Create mobile-responsive improvements
- Add dark mode

## 📝 License

MIT License - feel free to use this for personal or commercial projects!

## 🙏 Acknowledgments

Built with:
- [Streamlit](https://streamlit.io) - The fastest way to build data apps
- [Plotly](https://plotly.com) - Interactive visualizations
- [Pandas](https://pandas.pydata.org) - Data manipulation

---

**Made with ❤️ and Python**

If you find this useful, give it a ⭐ on GitHub!
