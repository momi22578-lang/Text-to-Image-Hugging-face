# 🎨 Text-to-Image Generator with Hugging Face

A simple Python script that generates images from text prompts using Hugging Face's free inference API and various state-of-the-art models including FLUX.1 and Stable Diffusion.

## ✨ Features

- **Multiple AI Models**: Support for FLUX.1-schnell, FLUX.1-dev, Stable Diffusion variants, and OpenJourney
- **Free to Use**: Utilizes Hugging Face's free inference API
- **Interactive Interface**: Simple command-line interface with example prompts
- **Automatic Saving**: Generated images are automatically saved with timestamps
- **Model Switching**: Easy switching between different AI models
- **License Information**: Clear indication of model licenses and usage rights

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Poetry (for dependency management)
- Hugging Face account and API token

### Installation

1. **Clone or download the repository**
   ```bash
   git clone <your-repo-url>
   cd text-to-image-generator
   ```

2. **Set up Poetry virtual environment**
   ```bash
   # Initialize poetry if not already done
   poetry init
   
   # Install dependencies
   poetry add huggingface_hub python-dotenv pillow
   
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
   pip install huggingface_hub python-dotenv pillow
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

6. **Run the script**
   ```bash
   python text_to_image.py
   ```

## 📋 Dependencies

The project uses the following Python packages:

- `huggingface_hub` - For accessing Hugging Face's inference API
- `python-dotenv` - For loading environment variables from .env file
- `pillow` - For image processing and saving

## 🎯 Usage

### Basic Usage

1. Start the application:
   ```bash
   poetry run python text_to_image.py
   ```

2. Enter a text prompt when asked:
   ```
   Enter prompt (or command): a red sports car on a mountain road
   ```

3. The generated image will be saved automatically with a timestamp.

### Available Commands

- **`models`** - View and switch between available AI models
- **`examples`** - Browse and select from predefined example prompts
- **`exit`** - Quit the application

### Example Prompts

- "a serene mountain landscape at sunset"
- "a futuristic robot in a cyberpunk city"
- "a magical forest with glowing mushrooms"
- "a cozy coffee shop interior with warm lighting"
- "an astronaut floating in space with Earth in background"

## 🤖 Available Models

### FLUX.1 Models (Black Forest Labs)

1. **FLUX.1-schnell** ✅ **Recommended**
   - License: Apache 2.0 (fully free for all uses)
   - Speed: Fast generation
   - Quality: High quality results
   - Best for: General use, commercial projects

2. **FLUX.1-dev** ⚠️ **Limited Use**
   - License: Non-commercial license
   - Speed: Slower but higher quality
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
├── text_to_image.py          # Main application script
├── .env                      # Environment variables (create this)
├── .env.example             # Environment variables template
├── README.md                # This file
├── pyproject.toml           # Poetry configuration
├── .gitignore              # Git ignore file
└── generated_images/        # Folder for generated images (created automatically)
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with:

```env
# Required: Your Hugging Face API token
HUGGINGFACEHUB_API_TOKEN=hf_your_token_here

# Optional: Default model (if not specified, uses FLUX.1-schnell)
DEFAULT_MODEL=black-forest-labs/FLUX.1-schnell

# Optional: Output directory for images (defaults to current directory)
OUTPUT_DIR=./generated_images
```

### Poetry Configuration

Your `pyproject.toml` configuration:

```toml
[project]
name = "text-to-image-generator"
version = "0.1.0"
description = "AI-powered text-to-image generation using Hugging Face models"
authors = [
    {name = "sai venkat", email = "saisam346@gmail.com"}
]
readme = "README.md"
requires-python = ">=3.13,<4.0"
dependencies = [
    "langchain>=0.3.27,<0.4.0",
    "langchain-community>=0.3.29,<0.4.0",
    "pillow>=11.3.0,<12.0.0",
    "huggingface-hub>=0.34.4,<0.35.0",
    "python-dotenv>=1.1.1,<2.0.0"
]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

## 🔧 Troubleshooting

### Common Issues

1. **"HUGGINGFACEHUB_API_TOKEN not found!"**
   - Make sure you created the `.env` file
   - Check that your token is correctly copied
   - Ensure the `.env` file is in the same directory as the script

2. **"Error generating image: Model not found"**
   - Some models might be temporarily unavailable
   - Try switching to a different model using the `models` command
   - FLUX.1-schnell is usually the most reliable

3. **"Rate limit exceeded"**
   - Hugging Face free tier has rate limits
   - Wait a few minutes before trying again
   - Consider upgrading to Hugging Face Pro for higher limits

4. **"Generation takes too long"**
   - Free inference API can be slow during peak hours
   - FLUX.1-schnell is typically faster than other models
   - Be patient, especially on first use (models need to "warm up")

### Performance Tips

- **Use FLUX.1-schnell** for fastest results
- **Keep prompts concise** but descriptive
- **Avoid very complex prompts** that might confuse the model
- **Try different models** if one isn't working well

## 📄 License Information

### Script License
This project is open source. Feel free to modify and distribute.

### Model Licenses
- **FLUX.1-schnell**: Apache 2.0 License (fully free)
- **FLUX.1-dev**: Non-commercial license (personal use only)
- **Stable Diffusion models**: CreativeML Open RAIL-M License
- **OpenJourney**: CreativeML Open RAIL-M License

Always check the specific model's license on Hugging Face before commercial use.

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest new features
- Add support for more models
- Improve documentation
- Submit pull requests

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Verify your Hugging Face token is valid
3. Try different models
4. Check [Hugging Face Status](https://status.huggingface.co/) for service issues

## 🔗 Useful Links

- [Hugging Face Hub](https://huggingface.co/)
- [Get API Token](https://huggingface.co/settings/tokens)
- [FLUX.1 Models](https://huggingface.co/black-forest-labs)
- [Stable Diffusion Models](https://huggingface.co/runwayml)
- [Poetry Documentation](https://python-poetry.org/docs/)

---

**Happy generating! 🎨✨**