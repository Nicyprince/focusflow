# ⚡ FocusFlow

> A smart productivity assistant that helps you manage tasks based on your energy levels and priorities.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://focusflow-xbtppe9khfr43eyz4p78t4.streamlit.app/)

## 🎯 Overview

FocusFlow is an AI-powered productivity app that takes the decision fatigue out of task management. Instead of staring at your to-do list wondering what to work on next, let FocusFlow intelligently recommend tasks based on your current energy level, available time, and task priorities.

### ✨ Key Features

- **🎲 Smart Task Picker** - AI-weighted recommendations based on priority and energy levels
- **📊 Visual Analytics** - Track productivity patterns and completion streaks
- **😊 Mood Tracking** - Monitor emotional trends alongside productivity
- **⚡ Energy-Based Organization** - Match tasks to your current energy state
- **📈 Progress Insights** - Beautiful charts showing your productivity journey

## 🚀 Live Demo

**[Try FocusFlow Live →](https://focusflow-xbtppe9khfr43eyz4p78t4.streamlit.app/)**

## 💡 Why FocusFlow?

Traditional to-do lists don't account for your fluctuating energy levels throughout the day. FocusFlow solves this by:

- ✅ Matching tasks to your current energy state
- ✅ Prioritizing what matters most
- ✅ Removing decision paralysis
- ✅ Tracking your mood and productivity patterns
- ✅ Celebrating your wins with streak tracking

## 🛠️ Built With

- **[Streamlit](https://streamlit.io)** - Interactive web framework
- **[Plotly](https://plotly.com)** - Data visualization
- **[Pandas](https://pandas.pydata.org)** - Data manipulation
- **Python 3.11+**

## 🚀 Quick Start

### Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/focusflow.git
cd focusflow

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Visit `http://localhost:8501` to see the app.

### Deploy Your Own

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy in one click!

## 📊 How It Works

1. **Add Tasks** - Create tasks with energy requirements (high/low) and priorities
2. **Check Your Energy** - When ready to work, tell FocusFlow your current energy level
3. **Get Recommendations** - The smart picker suggests tasks using weighted randomization that favors:
   - High-priority items
   - Tasks matching your energy level
   - Work that fits your available time
4. **Track Progress** - Monitor completions, streaks, and mood patterns

## 🎨 Features

### Smart Task Selection Algorithm
```python
# Weighted random selection favoring high-priority tasks
weights = [priority_weight(task) for task in filtered_tasks]
# High Priority = 5x weight
# Medium Priority = 3x weight  
# Low Priority = 1x weight
```

### Energy-Based Filtering
Tasks are categorized by energy requirements:
- **High Energy** - Creative work, problem-solving, important decisions
- **Low Energy** - Routine tasks, organization, email responses

### Mood Correlation
Track your emotional state alongside productivity to identify:
- Optimal working patterns
- Energy level trends
- Work-life balance indicators

## 🗺️ Future Enhancements

- [ ] Pomodoro timer integration
- [ ] Calendar sync (Google Calendar, Outlook)
- [ ] Data export (CSV, PDF reports)
- [ ] Dark mode
- [ ] Task categories and tags
- [ ] Mobile app version

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests
- ⭐ Star the repository if you find it useful!

## 📝 License

MIT License - feel free to use this project for personal or commercial purposes.

## 👨‍💻 Author

**Your Name**
- LinkedIn: https://www.linkedin.com/in/nicy-prince12
- GitHub: https://github.com/Nicyprince

## 🙏 Acknowledgments

Inspired by productivity methodologies:
- Getting Things Done (GTD)
- Energy Management Principles
- Eisenhower Matrix

And… obviously:
- Claude (for brainstorming and problem-solving)
- ChatGPT (for explanations, debugging, and structuring ideas)
- My mental health struggles, which made me care about building tools like this
- My indecisiveness, which somehow still led to shipping this project

---

<div align="center">

**Made with ❤️, Python and a lot of overthinking**

If you find FocusFlow helpful, please give it a ⭐!

[Live Demo](https://focusflow-xbtppe9khfr43eyz4p78t4.streamlit.app/) • [Report Bug](https://github.com/Nicyprince/focusflow/issues) • [Request Feature](https://github.com/Nicyprince/focusflow/issues)

</div>
