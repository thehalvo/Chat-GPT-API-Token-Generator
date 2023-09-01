import openai
import time
import os

# Initialize OpenAI API key
openai.api_key = "your-api-key-here"

def generate_story():
    prompt = '''Write a short story about a person who wakes up one morning with the ability to teleport
anywhere in the world. However, there is a catch – every time they teleport, they lose one year of their
life. Describe their journey as they grapple with the consequences of this extraordinary power.'''

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )

    generated_story = response.choices[0].text.strip()
    return generated_story

# Run the script indefinitely
while True:
    story = generate_story()
    print(story)

    # Wait for a while before running the script again
    time.sleep(5)

