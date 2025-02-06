import os
import google.generativeai as genai
import streamlit as st
from PIL import Image
import io

# Configure Gemini API with your API key
api_key = "AIzaSyACCREq1ZDeaPpTF_Rk9pyeMSgD5zhGCb0"  # Replace with your API key
genai.configure(api_key=api_key)

# Set up model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 500,
    "response_mime_type": "text/plain",
}

# Initialize the Gemini model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# Define prompt for the chatbot
prompt = """You are an assistant designed to help people with anything they ask"""

# Start chat session with initial prompt
chat_session = model.start_chat(
    history=[{"role": "model", "parts": prompt}]
)

# Initialize chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Function to display messages in the chat UI
def direct_chat(text, role):
    with st.chat_message(role):
        st.write(text)

# Chatbot function that runs the chat logic
def chatbot():
    st.header("Chatbot Interface")

    # If there's no prior conversation, bot starts with an initial message
    if len(st.session_state.chat_history) == 0:
        initial_message = "Hello! I'm ready to assist you. What do you need help with today?"
        st.session_state.chat_history.append({"role": "assistant", "text": initial_message})

    # Display all previous chat messages, excluding the prompt
    for message in st.session_state.chat_history:
        if message["role"] != "model":  # Make sure prompt is not displayed
            direct_chat(message["text"], role=message["role"])

    # Get user input
    user_input = st.chat_input("Type something about anything...")

    if user_input:
        # Save user's message to chat history
        st.session_state.chat_history.append({"role": "user", "text": user_input})

        # Send the message to the model and get the response
        response = chat_session.send_message(user_input)

        # Save the model's response to chat history
        st.session_state.chat_history.append({"role": "assistant", "text": response.text})

        # Display the new user input and model response
        direct_chat(user_input, role="user")
        direct_chat(response.text, role="assistant")

    # Add an image uploader widget for the user to upload an image
    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    # Input for the task to perform with the image
    task_input = st.text_input("What would you like to do with the image? (e.g., 'Classify this image', 'Describe the image')")

    if uploaded_image:
        # Open and display the image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Process the image based on the task provided by the user
        if task_input:
            # Here, you can implement your image processing based on the task input
            # For example, you can send the image to a model for classification or processing
            # Example: Classify the image (you can replace this with your specific task handling code)
            st.write(f"Processing the image to: {task_input}...")

            # Example of responding to the task (you can implement actual image processing)
            # For now, we will just mock a response
            mock_response = f"The image has been {task_input.lower()}."
            st.session_state.chat_history.append({"role": "assistant", "text": mock_response})

            # Display the mock response
            direct_chat(mock_response, role="assistant")

# Streamlit app layout
chatbot()  # Call the chatbot function directly without the index menu
