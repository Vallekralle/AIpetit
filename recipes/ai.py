from openai import OpenAI
from environs import Env


class GeneriereRezept():
    env = Env()
    env.read_env()

    def __init__(self, input):
        self.input = input
        self.client = OpenAI(
            base_url="https://api.aimlapi.com/v1",

            api_key=self.env.str("AI_ML_API_KEY"),
        )

    def response(self) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """Generate a recipe based on the user's input, 1610 characters max""",
                },
                {
                    "role": "user",
                    "content": self.input
                },
            ],
        )

        return response.choices[0].message.content


# Hier teste ich die GeneriereRezept 
if __name__ == "__main__":
    input = """
        Ich möchte ein chinesisches Gericht und habe nur Nudeln, Ei und bisschen Gemüse
    """
    print(GeneriereRezept(input).response())