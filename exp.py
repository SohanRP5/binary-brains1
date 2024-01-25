
from profanity_check import predict

def detect_bad_message(message):
    # Use profanity-check to predict if the message contains profanity
    profanity_prediction = predict([message])

    # The prediction is a binary value (1 for profanity, 0 for no profanity)
    return profanity_prediction[0] == 1

# Get user input
user_input = input("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")

# Detect bad messages
try:
    if detect_bad_message(user_input):
        print("Bad Message Detected: This message contains profanity.")
    else:
        print("No Bad Message Detected: This message is okay.")

except Exception as e:
    print(f"An error occurred: {e}")
