import streamlit as st
import random
import json
import os
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="FocusFlow - Smart Productivity",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(120deg, #6366f1, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    
    .task-card {
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #6366f1;
        background-color: #f8fafc;
        margin-bottom: 0.8rem;
    }
    
    .task-card-high {
        border-left-color: #ef4444;
    }
    
    .task-card-medium {
        border-left-color: #f59e0b;
    }
    
    .task-card-low {
        border-left-color: #10b981;
    }
    
    .success-box {
        padding: 1rem;
        background-color: #d1fae5;
        border-left: 4px solid #10b981;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .info-box {
        padding: 1rem;
        background-color: #dbeafe;
        border-left: 4px solid #3b82f6;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------
# Constants
# -------------------------
TASK_FILE = "tasks.json"
MOOD_FILE = "mood.json"
STATS_FILE = "stats.json"

# -------------------------
# Helper Functions
# -------------------------
def load_data(file, default):
    """Load JSON data from file"""
    if os.path.exists(file):
        try:
            with open(file, "r") as f:
                return json.load(f)
        except:
            return default
    return default

def save_data(file, data):
    """Save data to JSON file"""
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def priority_weight(priority):
    """Return numerical weight for priority"""
    return {"Low": 1, "Medium": 3, "High": 5}[priority]

def get_priority_color(priority):
    """Return color for priority level"""
    colors = {"Low": "#10b981", "Medium": "#f59e0b", "High": "#ef4444"}
    return colors.get(priority, "#6366f1")

def complete_task(task_name):
    """Mark a task as completed and log stats"""
    stats = load_data(STATS_FILE, {"completed": [], "total_time": 0})
    stats["completed"].append({
        "name": task_name,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    save_data(STATS_FILE, stats)

# -------------------------
# Initialize Session State
# -------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = load_data(TASK_FILE, [])

if "moods" not in st.session_state:
    st.session_state.moods = load_data(MOOD_FILE, [])

if "stats" not in st.session_state:
    st.session_state.stats = load_data(STATS_FILE, {"completed": [], "total_time": 0})

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>⚡ FocusFlow</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b;'>Smart Productivity Assistant</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    page = st.radio(
        "Navigate",
        ["📊 Dashboard", "➕ Add Tasks", "🎯 Pick Task", "😊 Mood Tracker", "📈 Analytics"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Quick Stats
    st.markdown("### Quick Stats")
    st.metric("Active Tasks", len(st.session_state.tasks))
    st.metric("Completed Today", len([
        t for t in st.session_state.stats.get("completed", [])
        if datetime.strptime(t["date"], "%Y-%m-%d %H:%M").date() == datetime.now().date()
    ]))
    
    st.markdown("---")
    st.markdown("<small style='color: #64748b;'>Built with Streamlit & Python</small>", unsafe_allow_html=True)

# -------------------------
# Dashboard Page
# -------------------------
if page == "📊 Dashboard":
    st.markdown("<h1 class='main-header'>Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("Your productivity at a glance")
    
    st.markdown("---")
    
    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Tasks",
            len(st.session_state.tasks),
            delta=None
        )
    
    with col2:
        completed_count = len(st.session_state.stats.get("completed", []))
        st.metric(
            "Completed",
            completed_count,
            delta=None
        )
    
    with col3:
        if st.session_state.moods:
            avg_mood = round(sum(m["mood"] for m in st.session_state.moods) / len(st.session_state.moods), 1)
        else:
            avg_mood = 0
        st.metric(
            "Avg Mood",
            f"{avg_mood}/10",
            delta=None
        )
    
    with col4:
        high_priority = len([t for t in st.session_state.tasks if t["priority"] == "High"])
        st.metric(
            "High Priority",
            high_priority,
            delta=None
        )
    
    st.markdown("---")
    
    # Main Content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📋 Recent Tasks")
        
        if st.session_state.tasks:
            for i, task in enumerate(st.session_state.tasks[:5]):
                priority_class = f"task-card-{task['priority'].lower()}"
                
                st.markdown(f"""
                <div class='task-card {priority_class}'>
                    <strong>{task['name']}</strong><br>
                    <small>🔋 {task['category']} • ⏱️ {task['duration']} min • 🎯 {task['priority']} Priority</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No tasks yet. Add your first task to get started!")
    
    with col2:
        st.subheader("😊 Mood Overview")
        
        if st.session_state.moods:
            recent_moods = st.session_state.moods[-7:]
            df = pd.DataFrame(recent_moods)
            df["date"] = pd.to_datetime(df["date"])
            
            fig = px.line(
                df,
                x="date",
                y="mood",
                title="Last 7 Days",
                labels={"mood": "Mood", "date": "Date"}
            )
            fig.update_layout(
                height=250,
                showlegend=False,
                margin=dict(l=0, r=0, t=30, b=0)
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No mood data yet. Track your mood to see trends!")

# -------------------------
# Add Tasks Page
# -------------------------
elif page == "➕ Add Tasks":
    st.markdown("<h1 class='main-header'>Add Tasks</h1>", unsafe_allow_html=True)
    st.markdown("Create and manage your task list")
    
    st.markdown("---")
    
    # Add Task Form
    with st.form("add_task_form", clear_on_submit=True):
        st.subheader("Create New Task")
        
        task_name = st.text_input("Task Name *", placeholder="e.g., Write blog post")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            category = st.selectbox("Energy Level *", ["Low energy", "High energy"])
        
        with col2:
            priority = st.selectbox("Priority *", ["Low", "Medium", "High"])
        
        with col3:
            duration = st.number_input("Duration (min) *", 5, 300, 30, step=5)
        
        submitted = st.form_submit_button("✨ Add Task", use_container_width=True)
        
        if submitted:
            if task_name.strip():
                new_task = {
                    "name": task_name.strip(),
                    "category": category,
                    "priority": priority,
                    "duration": duration,
                    "created": datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                st.session_state.tasks.append(new_task)
                save_data(TASK_FILE, st.session_state.tasks)
                st.success("✅ Task added successfully!")
                st.rerun()
            else:
                st.error("Please enter a task name")
    
    st.markdown("---")
    
    # Display Tasks
    st.subheader("📝 Your Tasks")
    
    if st.session_state.tasks:
        # Filter options
        col1, col2 = st.columns([2, 1])
        with col1:
            filter_priority = st.multiselect(
                "Filter by Priority",
                ["Low", "Medium", "High"],
                default=["Low", "Medium", "High"]
            )
        with col2:
            filter_energy = st.selectbox(
                "Filter by Energy",
                ["All", "Low energy", "High energy"]
            )
        
        # Filter tasks
        filtered_tasks = [
            (i, t) for i, t in enumerate(st.session_state.tasks)
            if t["priority"] in filter_priority
            and (filter_energy == "All" or t["category"] == filter_energy)
        ]
        
        st.markdown(f"Showing {len(filtered_tasks)} of {len(st.session_state.tasks)} tasks")
        
        for i, task in filtered_tasks:
            col1, col2, col3 = st.columns([6, 1, 1])
            
            priority_class = f"task-card-{task['priority'].lower()}"
            
            with col1:
                st.markdown(f"""
                <div class='task-card {priority_class}'>
                    <strong style='font-size: 1.1rem;'>{task['name']}</strong><br>
                    <small>🔋 {task['category']} • ⏱️ {task['duration']} min • 🎯 {task['priority']} Priority</small>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                if st.button("✓", key=f"complete_{i}", help="Mark as complete"):
                    complete_task(task['name'])
                    st.session_state.tasks.pop(i)
                    save_data(TASK_FILE, st.session_state.tasks)
                    st.success("Task completed! 🎉")
                    st.rerun()
            
            with col3:
                if st.button("🗑️", key=f"delete_{i}", help="Delete task"):
                    st.session_state.tasks.pop(i)
                    save_data(TASK_FILE, st.session_state.tasks)
                    st.rerun()
    else:
        st.info("No tasks yet. Add your first task above!")

# -------------------------
# Pick Task Page
# -------------------------
elif page == "🎯 Pick Task":
    st.markdown("<h1 class='main-header'>Smart Task Picker</h1>", unsafe_allow_html=True)
    st.markdown("Let AI decide your next task based on your energy and priorities")
    
    st.markdown("---")
    
    if not st.session_state.tasks:
        st.warning("⚠️ No tasks available. Add some tasks first!")
    else:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            energy_filter = st.selectbox(
                "How's your energy level right now?",
                ["Any", "Low energy", "High energy"],
                help="Choose your current energy level for better task matching"
            )
        
        with col2:
            time_available = st.number_input(
                "Time available (min)",
                5, 300, 60, 15,
                help="How much time do you have?"
            )
        
        st.markdown("---")
        
        if st.button("🎲 Pick My Next Task", use_container_width=True, type="primary"):
            filtered_tasks = st.session_state.tasks
            
            # Filter by energy
            if energy_filter != "Any":
                filtered_tasks = [
                    t for t in filtered_tasks
                    if t["category"] == energy_filter
                ]
            
            # Filter by duration
            filtered_tasks = [
                t for t in filtered_tasks
                if t["duration"] <= time_available
            ]
            
            if filtered_tasks:
                # Weighted random choice based on priority
                weights = [priority_weight(t["priority"]) for t in filtered_tasks]
                chosen = random.choices(filtered_tasks, weights=weights, k=1)[0]
                
                st.markdown("<div class='success-box'>", unsafe_allow_html=True)
                st.markdown(f"## 🎯 Your Next Task:")
                st.markdown(f"### {chosen['name']}")
                st.markdown(f"**Duration:** {chosen['duration']} minutes")
                st.markdown(f"**Priority:** {chosen['priority']}")
                st.markdown(f"**Energy:** {chosen['category']}")
                st.markdown("</div>", unsafe_allow_html=True)
                
                if st.button("✅ Mark as Complete", type="primary"):
                    task_index = st.session_state.tasks.index(chosen)
                    complete_task(chosen['name'])
                    st.session_state.tasks.pop(task_index)
                    save_data(TASK_FILE, st.session_state.tasks)
                    st.balloons()
                    st.success("Great job! Task completed! 🎉")
                    st.rerun()
            else:
                st.warning("⚠️ No tasks match your current energy level and available time. Try adjusting your filters!")
        
        # Show available tasks
        st.markdown("---")
        st.subheader("Available Tasks")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            high_tasks = [t for t in st.session_state.tasks if t["priority"] == "High"]
            st.metric("High Priority", len(high_tasks))
        
        with col2:
            medium_tasks = [t for t in st.session_state.tasks if t["priority"] == "Medium"]
            st.metric("Medium Priority", len(medium_tasks))
        
        with col3:
            low_tasks = [t for t in st.session_state.tasks if t["priority"] == "Low"]
            st.metric("Low Priority", len(low_tasks))

# -------------------------
# Mood Tracker Page
# -------------------------
elif page == "😊 Mood Tracker":
    st.markdown("<h1 class='main-header'>Mood Tracker</h1>", unsafe_allow_html=True)
    st.markdown("Track your daily mood and see patterns over time")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Log Your Mood")
        
        mood_value = st.slider(
            "How are you feeling right now?",
            1, 10, 5,
            help="1 = Very Low, 10 = Excellent"
        )
        
        # Mood emoji
        mood_emoji = {
            range(1, 3): "😢",
            range(3, 5): "😕",
            range(5, 7): "😐",
            range(7, 9): "🙂",
            range(9, 11): "😄"
        }
        
        for mood_range, emoji in mood_emoji.items():
            if mood_value in mood_range:
                st.markdown(f"<h1 style='text-align: center;'>{emoji}</h1>", unsafe_allow_html=True)
        
        note = st.text_area("Add a note (optional)", placeholder="What's making you feel this way?")
        
        if st.button("💾 Log Mood", use_container_width=True, type="primary"):
            mood_entry = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "mood": mood_value,
                "note": note
            }
            st.session_state.moods.append(mood_entry)
            save_data(MOOD_FILE, st.session_state.moods)
            st.success("✅ Mood logged successfully!")
            st.rerun()
    
    with col2:
        st.subheader("Mood Insights")
        
        if st.session_state.moods:
            recent = st.session_state.moods[-1]
            avg_mood = round(sum(m["mood"] for m in st.session_state.moods) / len(st.session_state.moods), 1)
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Last Mood", f"{recent['mood']}/10")
            with col_b:
                st.metric("Average", f"{avg_mood}/10")
        else:
            st.info("No mood data yet")
    
    # Mood History
    if st.session_state.moods:
        st.markdown("---")
        st.subheader("📊 Mood History")
        
        df = pd.DataFrame(st.session_state.moods)
        df["date"] = pd.to_datetime(df["date"])
        
        # Plot
        fig = px.line(
            df,
            x="date",
            y="mood",
            title="Your Mood Over Time",
            labels={"mood": "Mood (1-10)", "date": "Date"},
            markers=True
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Recent entries
        st.subheader("Recent Entries")
        for mood in reversed(st.session_state.moods[-5:]):
            with st.expander(f"{mood['date']} - Mood: {mood['mood']}/10"):
                if mood.get('note'):
                    st.write(mood['note'])
                else:
                    st.write("No note")

# -------------------------
# Analytics Page
# -------------------------
elif page == "📈 Analytics":
    st.markdown("<h1 class='main-header'>Analytics</h1>", unsafe_allow_html=True)
    st.markdown("Deep dive into your productivity patterns")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Task Distribution")
        
        if st.session_state.tasks:
            # Priority distribution
            priority_counts = pd.DataFrame(st.session_state.tasks)['priority'].value_counts()
            
            fig = px.pie(
                values=priority_counts.values,
                names=priority_counts.index,
                title="Tasks by Priority",
                color_discrete_sequence=["#ef4444", "#f59e0b", "#10b981"]
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No tasks to analyze")
    
    with col2:
        st.subheader("Energy Distribution")
        
        if st.session_state.tasks:
            energy_counts = pd.DataFrame(st.session_state.tasks)['category'].value_counts()
            
            fig = px.bar(
                x=energy_counts.index,
                y=energy_counts.values,
                title="Tasks by Energy Level",
                labels={"x": "Energy Level", "y": "Count"},
                color_discrete_sequence=["#6366f1"]
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No tasks to analyze")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Completion Stats")
        completed = st.session_state.stats.get("completed", [])
        
        if completed:
            df = pd.DataFrame(completed)
            df["date"] = pd.to_datetime(df["date"]).dt.date
            daily_counts = df.groupby("date").size().reset_index(name='count')
            
            fig = px.bar(
                daily_counts,
                x="date",
                y="count",
                title="Tasks Completed Per Day",
                labels={"count": "Tasks", "date": "Date"}
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No completed tasks yet")
    
    with col2:
        st.subheader("Productivity Streak")
        
        if completed:
            dates = sorted(set(pd.to_datetime([c["date"] for c in completed]).date))
            
            if dates:
                today = datetime.now().date()
                current_streak = 0
                
                for i in range(len(dates) - 1, -1, -1):
                    expected_date = today - timedelta(days=current_streak)
                    if dates[i] == expected_date:
                        current_streak += 1
                    else:
                        break
                
                st.metric("Current Streak", f"{current_streak} days")
                st.metric("Total Completed", len(completed))
                st.metric("Best Day", max(pd.DataFrame(completed).groupby(
                    pd.to_datetime(pd.DataFrame(completed)["date"]).dt.date
                ).size()))
        else:
            st.info("Complete tasks to see your streak!")
