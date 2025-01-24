# Flask + Azure Cognitive Vision Services Caption Generator

This project demonstrates the integration of **Flask** with **Azure Cognitive Vision Services** to generate captions for uploaded images. The app showcases how Azure's AI capabilities can be used for image analysis in a scalable and cloud-based Python application.

---

## 🚀 Features

- **Caption Generation**: Upload an image and get a descriptive caption with a confidence score.
- **Flask Framework**: Lightweight Python backend for seamless API handling.
- **Azure Vision Integration**: Uses Azure's Vision API for powerful image captioning.
- **Cross-Origin Support**: Flask-CORS allows for cross-origin requests.

---

## 📋 Prerequisites

- **Python**: Version 3.8 or higher.
- **Azure Subscription**: Create an Azure Cognitive Vision resource and get:
  - API Endpoint
  - API Key
- **Environment Variables**: Add these to a `.env` file in your project root:
  
  ```bash
  VISION_ENDPOINT=<your-azure-endpoint>
  VISION_KEY=<your-azure-api-key>
