import streamlit as st
import random

def main():
    st.set_page_config(page_title="Gamified Onboarding", layout="wide")
    
    # Sidebar Navigation
    menu = ["Home", "Learning Modules", "Quizzes & Challenges", "Team Building", "Leaderboard", "Resources & Support"]
    choice = st.sidebar.selectbox("Navigation", menu)
    
    if choice == "Home":
        st.title("Welcome to Your Gamified Onboarding Experience! 🎉")
        st.write("This interactive onboarding platform ensures a fun and engaging experience for new remote employees.")
        st.image("data:image/jpeg;base64,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")
        st.subheader("Key Features:")
        st.write("✅ Interactive Learning Modules with AI-driven recommendations")
        st.write("✅ Scenario-Based Challenges to test real-world problem-solving")
        st.write("✅ Virtual Team Building activities for stronger connections")
        st.write("✅ AI-Powered Personalization based on progress and performance")
        st.write("✅ Leaderboards & Rewards to encourage engagement")
        st.write("✅ Dedicated Support & Resources for a seamless transition")
    
    elif choice == "Learning Modules":
        st.title("📖 Learning Modules")
        st.write("Select a module to get started:")
        modules = {
            "Company Culture": "Understand the core values and mission of our company.",
            "Role-Specific Training": "Gain hands-on knowledge tailored to your job role.",
            "HR Policies": "Learn about company policies, compliance, and benefits.",
            "Communication & Collaboration": "Master the tools and etiquette for effective remote teamwork.",
            "Cybersecurity Best Practices": "Stay informed about online security protocols and safe practices."
        }
        module = st.selectbox("Choose a module", list(modules.keys()))
        st.write(f"### {module}")
        st.write(modules[module])
        st.write("Complete this module to earn points and unlock new content!")
    
    elif choice == "Quizzes & Challenges":
        st.title("🧠 Quizzes & Challenges")
        st.write("Test your knowledge and earn rewards!")
        questions = {
            "What is the core value of our company?": ["Innovation", "Collaboration", "Integrity", "All of the above"],
            "Which tool is used for company-wide communication?": ["Slack", "Zoom", "Google Meet", "None of the above"],
            "What should you do if you receive a phishing email?": ["Report it", "Click on the link", "Ignore it", "Forward it to colleagues"]
        }
        question = random.choice(list(questions.keys()))
        options = questions[question]
        answer = st.radio(question, options)
        if st.button("Submit Answer"):
            if answer == "All of the above" or answer == "Slack" or answer == "Report it":
                st.success("Correct! 🎉 You earned 10 points.")
            else:
                st.error("Oops! Try again.")
    
    elif choice == "Team Building":
        st.title("🤝 Virtual Team Building")
        st.write("Engage in fun activities to bond with your team!")
        activities = ["🔹 Icebreaker Questions", "🔹 Virtual Escape Rooms", "🔹 Online Team Challenges", "🔹 Remote Coffee Chats"]
        for activity in activities:
            st.write(activity)
    
    elif choice == "Leaderboard":
        st.title("🏆 Leaderboard")
        st.write("Check out the top performers!")
        scores = {"Alice": 50, "Bob": 40, "Charlie": 30, "You": random.randint(20, 50)}
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for rank, (name, score) in enumerate(sorted_scores, start=1):
            st.write(f"{rank}. {name} - {score} points")
    
    elif choice == "Resources & Support":
        st.title("📚 Resources & Support")
        st.write("Find helpful materials and contact support when needed.")
        st.write("📌 **Company Handbook** - A comprehensive guide to all company policies and procedures.")
        st.write("📌 **FAQ Section** - Answers to common onboarding questions.")
        st.write("📌 **Help Desk** - Contact HR or IT for any assistance.")
        st.write("📌 **Employee Forum** - Connect with colleagues and share insights.")

if __name__ == "__main__":
    main()
