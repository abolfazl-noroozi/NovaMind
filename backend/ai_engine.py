
"""
NovaMind - AI Engine
Handles AI assistant responses.
"""

class AIEngine:

    def __init__(self):
        self.name = "NovaMind AI"

    def generate_response(self, question: str) -> str:
        if not question.strip():
            return "Please enter a question."

        return (
            f"You asked: {question}\n"
            "NovaMind AI is ready to process your request."
        )


if __name__ == "__main__":
    ai = AIEngine()
    print(ai.generate_response("Hello NovaMind!"))
