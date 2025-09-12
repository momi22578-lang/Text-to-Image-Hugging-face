# 🎨 Text-to-Image Generator with Hugging Face

A powerful text-to-image generation application that creates stunning images from text prompts using Hugging Face's free inference API and various state-of-the-art models including FLUX.1 and Stable Diffusion.

## 🌐 Try It Live!

**🚀 [Launch Web App](https://text-to-image-hugging-face-dwu7nyvrg9q2qgkmroozt8.streamlit.app/)**

Experience the magic of AI-powered image generation directly in your browser! No installation required - just enter your prompt and watch your ideas come to life.

---

## ✨ Features

- **🌐 Web Interface**: Beautiful, interactive Streamlit web application
- **🤖 Multiple AI Models**: Support for FLUX.1-schnell, FLUX.1-dev, Stable Diffusion variants, and OpenJourney
- **💰 Free to Use**: Utilizes Hugging Face's free inference API
- **📱 Responsive Design**: Works on desktop, tablet, and mobile devices
- **💾 Easy Download**: Generated images can be downloaded directly from the web interface
- **🔄 Model Switching**: Easy switching between different AI models
- **⚡ Fast Generation**: Optimized for quick image generation
- **📋 Example Gallery**: Pre-built example prompts to get you started
- **📄 License Information**: Clear indication of model licenses and usage rights

## 🚀 Quick Start Options

### Option 1: Use the Web App (Recommended)
Simply visit **[our live deployment](https://text-to-image-hugging-face-dwu7nyvrg9q2qgkmroozt8.streamlit.app/)** and start generating images immediately!

### Option 2: Run Locally

#### Prerequisites

- Python 3.9 or higher (excluding 3.9.7)
- Poetry (for dependency management)
- Hugging Face account and API token

#### Installation

1. **Clone or download the repository**
   ```bash
   git clone <your-repo-url>
   cd text-to-image-generator
   ```

2. **Install dependencies with Poetry**
   ```bash
   # Install dependencies
   poetry install
   
   # Activate the virtual environment
   poetry shell
   ```

3. **Alternative: Using pip with .venv**
   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate virtual environment
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

4. **Get your Hugging Face API token**
   - Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
   - Create a new token (read access is sufficient)
   - Copy the token

5. **Create environment file**
   Create a `.env` file in the project root:
   ```env
   HUGGINGFACEHUB_API_TOKEN=your_actual_token_here
   ```

6. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

## 📋 Dependencies

The project uses the following Python packages:

- `streamlit` - For the web interface
- `huggingface_hub` - For accessing Hugging Face's inference API
- `python-dotenv` - For loading environment variables from .env file
- `pillow` - For image processing and saving
- `langchain` & `langchain-community` - For advanced AI integrations

## 🎯 Usage

### Web App Usage

1. **Visit the live app**: [https://text-to-image-hugging-face-dwu7nyvrg9q2qgkmroozt8.streamlit.app/](https://text-to-image-hugging-face-dwu7nyvrg9q2qgkmroozt8.streamlit.app/)

2. **Choose your model**: Select from the dropdown menu in the sidebar

3. **Enter your prompt**: Type your image description in the text input field

4. **Generate**: Click the "Generate Image" button

5. **Download**: Use the download button to save your generated image

### Local App Usage

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser to the displayed URL (usually `http://localhost:8501`)

3. Use the interface to generate images with custom prompts

### Example Prompts

Try these creative prompts to get started:

- "a serene mountain landscape at sunset with purple clouds"
- "a futuristic robot in a neon-lit cyberpunk city"
- "a magical enchanted forest with glowing mushrooms and fireflies"
- "a cozy coffee shop interior with warm lighting and books"
- "an astronaut floating in space with Earth and stars in background"
- "a majestic dragon soaring over ancient castle ruins"
- "a vibrant underwater coral reef scene with tropical fish"

## 🤖 Available Models

### FLUX.1 Models (Black Forest Labs)

1. **FLUX.1-schnell** ✅ **Recommended**
   - License: Apache 2.0 (fully free for all uses)
   - Speed: Fast generation (~10-20 seconds)
   - Quality: High quality results
   - Best for: General use, commercial projects

2. **FLUX.1-dev** ⚠️ **Limited Use**
   - License: Non-commercial license
   - Speed: Slower but higher quality (~30-60 seconds)
   - Quality: Premium results
   - Best for: Personal projects, research

### Stable Diffusion Models

3. **stable-diffusion-v1-5** ✅ **Reliable**
   - License: CreativeML Open RAIL-M (generally free)
   - Most tested and stable model
   - Good balance of speed and quality

4. **stable-diffusion-v2-1** ✅ **Enhanced**
   - Improved version with better prompt understanding
   - Higher resolution support

5. **stable-diffusion-v1-4** ✅ **Classic**
   - Original stable diffusion model
   - Well-documented and reliable

### Specialty Models

6. **OpenJourney v4** 🎨 **Artistic**
   - Trained on artistic styles
   - Great for creative and stylized images

## 📁 Project Structure

```
text-to-image-generator/
├── app.py                   # Main Streamlit application
├── text_to_image.py         # Core image generation logic
├── .env                     # Environment variables (create this for local use)
├── .env.example            # Environment variables template
├── README.md               # This file
├── pyproject.toml          # Poetry configuration
├── requirements.txt        # Pip dependencies
├── .gitignore             # Git ignore file
└── generated_images/       # Folder for generated images (created automatically)
```

## 🌐 Deployment

This app is deployed on **Streamlit Cloud** and automatically updates when changes are pushed to the main branch.

### Deploy Your Own Version

1. Fork this repository
2. Create a Streamlit Cloud account at [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add your `HUGGINGFACEHUB_API_TOKEN` to Streamlit Cloud secrets
5. Deploy!

### Local Development

For local development with hot reload:
```bash
streamlit run app.py --server.runOnSave true
```

## ⚙️ Configuration

### Environment Variables

For local deployment, create a `.env` file with:

```env
# Required: Your Hugging Face API token
HUGGINGFACEHUB_API_TOKEN=hf_your_token_here

# Optional: Default model (if not specified, uses FLUX.1-schnell)
DEFAULT_MODEL=black-forest-labs/FLUX.1-schnell
```

### Streamlit Cloud Secrets

For deployment on Streamlit Cloud, add your secrets in the app settings:

```toml
HUGGINGFACEHUB_API_TOKEN = "hf_your_token_here"
```

## 🔧 Troubleshooting

### Common Issues

1. **"Please configure your Hugging Face API token"**
   - For local use: Create a `.env` file with your token
   - For deployed app: The token is configured on our end

2. **"Error generating image: Model not found"**
   - Some models might be temporarily unavailable
   - Try switching to a different model
   - FLUX.1-schnell is usually the most reliable

3. **"Rate limit exceeded"**
   - Hugging Face free tier has rate limits
   - Wait a few minutes before trying again
   - Consider upgrading to Hugging Face Pro for higher limits

4. **"Generation takes too long"**
   - Free inference API can be slow during peak hours
   - FLUX.1-schnell is typically faster than other models
   - Be patient, especially during first use (models need to "warm up")

5. **App not loading/crashing**
   - Try refreshing the page
   - Check if you have a stable internet connection
   - Clear your browser cache

### Performance Tips

- **Use FLUX.1-schnell** for fastest results
- **Keep prompts descriptive** but not overly complex
- **Be specific** about what you want to see
- **Try different models** if one isn't producing desired results
- **Use the example prompts** as inspiration

## 📱 Mobile Experience

The web app is fully responsive and works great on mobile devices:
- Touch-friendly interface
- Optimized image display
- Easy prompt entry
- Quick model switching

## 📄 License Information

### Application License
This project is open source. Feel free to modify and distribute.

### Model Licenses
- **FLUX.1-schnell**: Apache 2.0 License (fully free for all uses)
- **FLUX.1-dev**: Non-commercial license (personal use only)
- **Stable Diffusion models**: CreativeML Open RAIL-M License
- **OpenJourney**: CreativeML Open RAIL-M License

Always check the specific model's license on Hugging Face before commercial use.

## 🚀 What's Next?

Planned features for future releases:
- **Image-to-image generation** - Transform existing images with prompts
- **Style transfer** - Apply artistic styles to generated images
- **Batch generation** - Generate multiple variations at once
- **History** - Save and revisit your favorite generations
- **Advanced settings** - Control generation parameters
- **Community gallery** - Share your best creations

## 🤝 Contributing

We welcome contributions! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🤖 Add support for more models
- 📚 Improve documentation
- 🔧 Submit pull requests

## 📞 Support & Feedback

If you encounter issues or have suggestions:

1. Try the troubleshooting section above
2. Check [Hugging Face Status](https://status.huggingface.co/) for service issues
3. Open an issue on GitHub
4. Contact the developers

## 🔗 Useful Links

- **🌐 [Live Web App](https://text-to-image-hugging-face-dwu7nyvrg9q2qgkmroozt8.streamlit.app/)**
- [Hugging Face Hub](https://huggingface.co/)
- [Get API Token](https://huggingface.co/settings/tokens)
- [FLUX.1 Models](https://huggingface.co/black-forest-labs)
- [Stable Diffusion Models](https://huggingface.co/runwayml)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

**🎨 Start creating amazing AI-generated images today! ✨**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://text-to-image-hugging-face-dwu7nyvrg9q2qgkmroozt8.streamlit.app/)