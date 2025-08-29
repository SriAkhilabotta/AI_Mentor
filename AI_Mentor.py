import random

class PlacementMentorBot:
    def __init__(self, name="MentorBot"):
        self.name = name
        self.topics = {
            "Python Basics": {
                "What are Python data types?": "int, float, str, list, tuple, dict, set, bool",
                "Explain mutable vs immutable objects.": "Mutable can change after creation (list, dict), immutable cannot (str, tuple, int).",
                "Write a program to reverse a string.": "s[::-1]"
            }
        }
        self.hr_questions = [
            "Tell me about yourself.",
            "What are your strengths and weaknesses?",
            "Why should we hire you?",
            "Explain one project you have done.",
            "Tell me about certifications you completed."
        ]

    def greet(self):
        print(f"👋 Hi! I am {self.name}, your AI mentor for placement preparation.\n")

    def ask_topic_questions(self, topic):
        print(f"📘 Today’s topic: {topic}\n")
        for q, correct_ans in self.topics[topic].items():
            print(f"❓ {q}")
            ans = input("Your answer: ")
            if correct_ans.lower() in ans.lower():
                print("✅ Correct!\n")
            else:
                print(f"❌ Not accurate. Correct answer: {correct_ans}\n")

    def mock_interview(self):
        print("\n🎤 Starting mock interview...\n")
        for q in self.hr_questions:
            print(f"👔 {q}")
            ans = input("Your answer: ")

            # Simple vocabulary/grammar feedback
            if "good" in ans.lower():
                print("💡 Tip: Instead of 'good', use 'excellent', 'skilled', or 'outstanding'.")
            if "hardworking" in ans.lower():
                print("💡 Tip: You can say 'dedicated' or 'committed' to sound more professional.")
            if len(ans.split()) < 5:
                print("⚠️ Try to give longer, structured answers.\n")
            else:
                print("✅ Nice, detailed answer!\n")

        print("✨ Mock interview finished! Keep improving 🚀\n")


if __name__ == "__main__":
    bot = PlacementMentorBot("PrepMate")
    bot.greet()
    bot.ask_topic_questions("Python Basics")

    choice = input("Do you want a mock interview now? (yes/no): ")
    if choice.lower() == "yes":
        bot.mock_interview()
