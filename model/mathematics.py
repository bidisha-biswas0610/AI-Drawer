import anthropic

# Initialize the Anthropic client
client = anthropic.Anthropic(
    api_key="your-api-key",
)

# Prompt the user for a single input
user_input = input("Enter a prompt: ")

# Create a conversation with the user input
response = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": user_input}
    ]
)

# Extract the text from the response content
# If the response.content is a list, access the first element's text field
if isinstance(response.content, list) and len(response.content) > 0:
    content_text = response.content[0].text
    print(f"Response: {content_text}")
else:
    print("No response.")

print("Program has ended.")
