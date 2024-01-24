# Make sure to install the openai module first by running: pip install openai
import openai

# Set your OpenAI API key
openai.api_key = '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'

# Prompt the model with a text input
text_input = input("Enter a social media post: ")

# Use the OpenAI GPT-3.5 model to generate output
try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text_input,
        max_tokens=50  # You can adjust the number of tokens based on your needs
    )

    # Extract the generated output from the model
    generated_output = response['choices'][0]['text']

    # Perform hate speech detection on the generated output
    # You might want to use a more sophisticated hate speech detection model in a real-world scenario.
    # For simplicity, we'll just check for the presence of certain keywords associated with hate speech.
    hate_keywords = ['hate', 'disgusting', 'offensive', 'violence']

    if any(keyword in generated_output.lower() for keyword in hate_keywords):
        result = 'Hate Speech Detected'
    else:
        result = 'No Hate Speech Detected'

    print(f"Generated Output: {generated_output}")
    print(f"Result: {result}")

except Exception as e:
    print(f"An error occurred: {e}")
