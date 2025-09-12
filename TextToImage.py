#!/usr/bin/env python3
"""
Text-to-Image generation using Hugging Face InferenceClient
Fixed version with proper image handling
"""

import os
from dotenv import find_dotenv, load_dotenv
from huggingface_hub import InferenceClient
from PIL import Image
from datetime import datetime

# Load environment variables
load_dotenv(find_dotenv())

# Hugging Face API token
API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Available text-to-image models (free for inference API)
MODELS = {
    "1": "black-forest-labs/FLUX.1-schnell",  # Apache 2.0 license - fully free
    "2": "runwayml/stable-diffusion-v1-5",
    "3": "stabilityai/stable-diffusion-2-1", 
    "4": "CompVis/stable-diffusion-v1-4",
    "5": "prompthero/openjourney-v4",
    "6": "black-forest-labs/FLUX.1-dev"  # Non-commercial license
}

def generate_image(prompt, model_id="black-forest-labs/FLUX.1-schnell"):
    """
    Generate image using Hugging Face InferenceClient
    Simplified version with better error handling
    """
    try:
        print(f"🎨 Generating with model: {model_id}")
        print(f"📝 Prompt: '{prompt}'")
        print("⏳ Please wait...")
        
        # Initialize client for each request to avoid issues
        client = InferenceClient(api_key=API_TOKEN)
        
        # Use the simplest possible call
        image = client.text_to_image(prompt, model=model_id)
        
        print(f"✅ Generated image type: {type(image)}")
        
        # Save immediately to avoid conversion issues
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        clean_prompt = "".join(c for c in prompt[:20] if c.isalnum() or c in (' ', '-', '_')).strip()
        filename = f"img_{timestamp}_{clean_prompt.replace(' ', '_')}.png"
        
        # Direct save - let PIL handle the format
        image.save(filename)
        
        print(f"💾 Saved: {filename}")
        print(f"📏 Size: {image.size}")
        print(f"🎨 Mode: {image.mode}")
        
        return True
        
    except Exception as e:
        print(f"❌ Generation failed: {str(e)}")
        print(f"🔍 Error type: {type(e).__name__}")
        
        # Try alternative approach with different client initialization
        try:
            print("🔄 Trying alternative approach...")
            alt_client = InferenceClient()
            alt_client.token = API_TOKEN
            
            image = alt_client.text_to_image(prompt)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(OUTPUT_DIR, f"img_alt_{timestamp}.png")
            image.save(filename)
            
            print(f"✅ Alternative method worked! Saved: {filename}")
            return True
            
        except Exception as e2:
            print(f"❌ Alternative also failed: {str(e2)}")
            return False

def display_models():
    """Display available models with licensing info"""
    print("\n📋 Available Models:")
    print("=" * 60)
    for key, model in MODELS.items():
        license_info = ""
        if "schnell" in model:
            license_info = " (✅ Fully Free - Apache 2.0)"
        elif "FLUX.1-dev" in model:
            license_info = " (⚠️ Non-commercial license)"
        elif "stable-diffusion" in model:
            license_info = " (✅ Generally free)"
        elif "openjourney" in model:
            license_info = " (✅ Free for most uses)"
            
        print(f"{key}. {model}{license_info}")
    print("=" * 60)

def main():
    """Main text-to-image generation loop"""
    
    if not API_TOKEN:
        print("❌ Error: HUGGINGFACEHUB_API_TOKEN not found!")
        print("Please set your Hugging Face API token in your .env file")
        print("Get it from: https://huggingface.co/settings/tokens")
        return
    
    print("🎨 Simple Text-to-Image Generator")
    print("=" * 50)
    print("Commands: 'models', 'examples', 'exit'")
    
    # Start with the most reliable free model
    current_model = MODELS["1"]  # FLUX.1-schnell
    generation_count = 0
    
    # Example prompts
    examples = [
        "a red sports car on a mountain road",
        "a cute robot in a garden",
        "a sunset over the ocean",
        "a cozy coffee shop",
        "a space astronaut floating",
        "a magical forest with glowing lights"
    ]
    
    while True:
        print(f"\n🤖 Current model: {current_model}")
        user_input = input("Enter prompt (or command): ").strip()
        
        if user_input.lower() == "exit":
            print(f"👋 Goodbye! Generated {generation_count} images.")
            break
            
        elif user_input.lower() == "models":
            display_models()
            choice = input("Select model (1-6): ").strip()
            if choice in MODELS:
                current_model = MODELS[choice]
                print(f"✅ Switched to: {current_model}")
            continue
            
        elif user_input.lower() == "examples":
            print("\n🌟 Example prompts:")
            for i, ex in enumerate(examples, 1):
                print(f"{i}. {ex}")
            
            try:
                choice = input("Select example (1-6) or Enter to skip: ").strip()
                if choice.isdigit() and 1 <= int(choice) <= 6:
                    user_input = examples[int(choice) - 1]
                    print(f"Selected: {user_input}")
                else:
                    continue
            except:
                continue
        
        if not user_input or user_input.lower() in ["models", "examples", "exit"]:
            continue
            
        # Generate image
        success = generate_image(user_input, current_model)
        if success:
            generation_count += 1
            print(f"🎉 Total generated: {generation_count}")
        else:
            print("💡 Try a different model or simpler prompt")

if __name__ == "__main__":
    print("📦 Required packages: huggingface_hub python-dotenv pillow")
    print("📄 Make sure you have a .env file with: HUGGINGFACEHUB_API_TOKEN=your_token")
    print()
    main()