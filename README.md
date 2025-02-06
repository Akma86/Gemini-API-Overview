# 🚗 Fine-Grained Car Classification using Gemini 1.5 Flash and Gemini 2.0
## 📜 Project Overview
This project demonstrates how to utilize the Gemini 1.5 Flash API for solving a fine-grained car classification problem. The focus is on showcasing the capabilities of Gemini API in handling multimodal tasks, with an emphasis on speed, scalability, and versatility.

## ✨ Why Gemini 1.5 Flash?
Gemini 1.5 Flash is a powerful, lightweight multimodal model optimized for:

Speed and Cost-Efficiency: Ideal for tasks requiring quick results with minimal resource usage.
Massive Context Understanding: Supports inputs of up to 1 million tokens, making it versatile for complex scenarios.
Ease of Integration: Simple API calls enable seamless interaction with the model.

## 🚀 Use Cases of Gemini API
Image-Based Classification: Quickly classify images into categories, as demonstrated with the Cars dataset.
Multimodal Applications: Combine text, image, or other modalities in a single input for enriched predictions.
Scalable Solutions: Handle large-scale datasets or high-volume requests with efficiency.

## 🛠️ How to Use the Gemini API
  1️⃣ Get Your API Key
    Visit the Generative AI website and sign up for access.
    Generate your API key and save it securely.
  2️⃣ Set Up Your Environment
    ## ⚙️ Setup Environment
| Step | Command                                   | Description                         |
|------|-------------------------------------------|-------------------------------------|
| 1    | `pip install requests`                   | Install the necessary library       |
| 2    | `export GEMINI_API_KEY="your_api_key"`   | Save the Gemini API key as variable |

  3️⃣ Make Your First API Call
  ## 🚀 Generate Text from Text Image
    from genai.model import GenerativeModel
    from PIL import Image
    
    # Initialize the Gemini 1.5 Flash model
    model = GenerativeModel('gemini-1.5-flash')
    
    # Load and display an example image
    image = Image.open('/kaggle/input/stanford-cars-dataset/cars_train/cars_train/00001.jpg')
    response = model.generate_content(image)
    to_markdown(response.text)
  > A white Audi TT is parked on the street. It is in focus and the background is out of focus. There are other cars parked behind it. The sky is bright and sunny.


  
## 4️⃣ API Response
The API returns a JSON object with:

Predicted Class: The category assigned to the input image.
Confidence Scores: Probabilities for each category.
Processing Time: Time taken for the prediction.
## 📂 Dataset Details
The project uses the Stanford Cars Dataset, which contains 16,185 images across 196 car categories. Images are split into training and testing sets, and categories range from make and model to the year of manufacture.

## 💡 Key Features
Quick Integration: Easily adapt the API for other datasets or tasks.
Flexible Input: Supports images via URL or base64 encoding.
Scalable Deployment: Process thousands of images efficiently.
## 🌟 Benefits of Using Gemini API
No need for extensive training or fine-tuning.
Leverages state-of-the-art multimodal capabilities.
Suitable for a wide range of image-based applications.
## 🤝 Contributions
Have ideas to extend the project? Feel free to fork the repository, submit pull requests, or raise issues.

