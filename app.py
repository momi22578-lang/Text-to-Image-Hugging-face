#!/usr/bin/env python3
"""
Streamlit Web UI for Text-to-Image Generation with Download Capability
"""

import streamlit as st
import os
import io
from datetime import datetime
from dotenv import load_dotenv
from TextToImage import ImageGenerator, MODELS, MODEL_INFO, validate_api_token, get_example_prompts

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="🎨 AI Image Generator",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .model-info {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        color:black;
    }
    
    .example-prompt {
        background-color: #e8f4f8;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.2rem 0;
        cursor: pointer;
        border: 1px solid #d1e7dd;
    }
    
    .success-message {
        color: #28a745;
        font-weight: bold;
    }
    
    .error-message {
        color: #dc3545;
        font-weight: bold;
    }
    
    .download-section {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #dee2e6;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'generated_images' not in st.session_state:
        st.session_state.generated_images = []
    if 'generation_count' not in st.session_state:
        st.session_state.generation_count = 0

def image_to_bytes(image, format="PNG"):
    """Convert PIL Image to bytes for download"""
    img_buffer = io.BytesIO()
    image.save(img_buffer, format=format)
    img_buffer.seek(0)
    return img_buffer.getvalue()

def generate_filename(prompt, model_name, timestamp=None):
    """Generate a clean filename for the image"""
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Clean the prompt for filename
    clean_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
    clean_prompt = clean_prompt.replace(' ', '_')
    
    # Clean model name
    clean_model = model_name.replace(' ', '_').replace('.', '_')
    
    return f"{clean_model}_{timestamp}_{clean_prompt}.png"

def main():
    """Main Streamlit application"""
    initialize_session_state()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎨 AI Image Generator</h1>
        <p>Generate stunning images from text using Hugging Face models</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Token input
        api_token = st.text_input(
            "🔑 Hugging Face API Token",
            type="password",
            value=os.getenv("HUGGINGFACEHUB_API_TOKEN", ""),
            help="Get your token from https://huggingface.co/settings/tokens"
        )
        
        if not validate_api_token(api_token):
            st.error("❌ Please enter a valid Hugging Face API token")
            st.info("💡 Get your token from [Hugging Face Settings](https://huggingface.co/settings/tokens)")
            return
        
        st.success("✅ API token configured")
        
        # Model selection
        st.subheader("🤖 Model Selection")
        selected_model_name = st.selectbox(
            "Choose a model:",
            options=list(MODELS.keys()),
            index=0  # Default to FLUX.1-schnell
        )
        
        selected_model_id = MODELS[selected_model_name]
        model_info = MODEL_INFO[selected_model_id]
        
        # Display model information
        st.markdown(f"""
        <div  class="model-info " >
            <strong>📋 Model Info:</strong><br>
            <strong>Status:</strong> {model_info['status']}<br>
            <strong>License:</strong> {model_info['license']}<br>
            <strong>Description:</strong> {model_info['description']}
        </div>
        """, unsafe_allow_html=True)
        
        # Output directory setting
        output_dir = st.text_input(
            "📁 Output Directory",
            value="./generated_images",
            help="Directory where generated images will be saved"
        )
        
        # Download preferences
        st.subheader("📥 Download Settings")
        download_format = st.selectbox(
            "Image Format",
            options=["PNG", "JPEG"],
            help="Choose the format for downloaded images"
        )
        
        # Statistics
        st.subheader("📊 Statistics")
        st.metric("Images Generated", st.session_state.generation_count)
        st.metric("Images in Session", len(st.session_state.generated_images))
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("✏️ Image Generation")
        
        # Text prompt input
        prompt = st.text_area(
            "Enter your image description:",
            height=100,
            placeholder="Describe the image you want to generate...",
            help="Be descriptive and specific for better results"
        )
        
        # Generation buttons
        col_gen1, col_gen2, col_gen3 = st.columns([2, 1, 1])
        
        with col_gen1:
            generate_btn = st.button("🎨 Generate Image", type="primary", use_container_width=True)
        
        with col_gen2:
            clear_prompt = st.button("🗑️ Clear", use_container_width=True)
        
        with col_gen3:
            if st.button("🎲 Random", use_container_width=True):
                examples = get_example_prompts()
                import random
                prompt = random.choice(examples)
                st.rerun()
        
        if clear_prompt:
            st.rerun()
        
        # Image generation logic
        if generate_btn:
            if not prompt.strip():
                st.error("❌ Please enter a prompt to generate an image")
            else:
                with st.spinner(f"🎨 Generating image with {selected_model_name}..."):
                    try:
                        # Initialize generator
                        generator = ImageGenerator(api_token, output_dir)
                        
                        # Generate image
                        success, message, image = generator.generate_image(prompt, selected_model_id)
                        
                        if success:
                            st.success(message)
                            
                            # Create timestamp for this generation
                            generation_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            
                            # Add to session state
                            st.session_state.generated_images.insert(0, {
                                'image': image,
                                'prompt': prompt,
                                'model': selected_model_name,
                                'timestamp': generation_timestamp,
                                'format': download_format
                            })
                            st.session_state.generation_count += 1
                            
                            # Display the generated image with download option
                            st.image(image, caption=f"Generated: {prompt}", use_column_width=True)
                            
                            # Download section for the newly generated image
                            st.markdown('<div class="download-section">', unsafe_allow_html=True)
                            st.write("📥 **Download Options**")
                            
                            col_dl1, col_dl2 = st.columns(2)
                            
                            with col_dl1:
                                # Generate filename
                                filename = generate_filename(prompt, selected_model_name, generation_timestamp)
                                
                                # Convert image to bytes
                                img_bytes = image_to_bytes(image, download_format)
                                
                                # Download button
                                st.download_button(
                                    label=f"⬇️ Download as {download_format}",
                                    data=img_bytes,
                                    file_name=filename,
                                    mime=f"image/{download_format.lower()}",
                                    use_container_width=True
                                )
                            
                            with col_dl2:
                                st.info(f"📁 **Filename:** {filename}")
                                st.info(f"📏 **Size:** {image.size[0]}×{image.size[1]}")
                            
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                        else:
                            st.error(message)
                            
                    except Exception as e:
                        st.error(f"❌ Unexpected error: {str(e)}")
    
    with col2:
        st.subheader("💡 Example Prompts")
        
        examples = get_example_prompts()
        
        for i, example in enumerate(examples):
            if st.button(f"📝 Use Example {i+1}", key=f"example_{i}", use_container_width=True):
                st.session_state.temp_prompt = example
                st.rerun()
            
            with st.expander(f"Preview {i+1}", expanded=False):
                st.write(example)
        
        # Handle example selection
        if 'temp_prompt' in st.session_state:
            prompt = st.session_state.temp_prompt
            del st.session_state.temp_prompt
    
    # Display generated images history
    if st.session_state.generated_images:
        st.subheader("🖼️ Generated Images History")
        
        # Controls for history section
        col_hist1, col_hist2, col_hist3 = st.columns([2, 1, 1])
        
        with col_hist1:
            st.write(f"**{len(st.session_state.generated_images)}** images in history")
        
        with col_hist2:
            if st.button("📦 Download All", help="Download all images as ZIP"):
                # Create a ZIP file with all images
                import zipfile
                import tempfile
                
                with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as tmp_file:
                    with zipfile.ZipFile(tmp_file, 'w') as zip_file:
                        for idx, img_data in enumerate(st.session_state.generated_images):
                            filename = generate_filename(
                                img_data['prompt'], 
                                img_data['model'], 
                                img_data.get('timestamp', f'img_{idx}')
                            )
                            img_bytes = image_to_bytes(img_data['image'], img_data.get('format', 'PNG'))
                            zip_file.writestr(filename, img_bytes)
                    
                    # Read the ZIP file
                    tmp_file.seek(0)
                    zip_bytes = tmp_file.read()
                
                # Offer ZIP download
                st.download_button(
                    label="⬇️ Download ZIP",
                    data=zip_bytes,
                    file_name=f"ai_generated_images_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
                    mime="application/zip",
                    use_container_width=True
                )
        
        with col_hist3:
            if st.button("🗑️ Clear History", use_container_width=True):
                st.session_state.generated_images = []
                st.rerun()
        
        # Display images in a grid with download buttons
        cols_per_row = 2
        for i in range(0, len(st.session_state.generated_images), cols_per_row):
            cols = st.columns(cols_per_row)
            
            for j, col in enumerate(cols):
                if i + j < len(st.session_state.generated_images):
                    img_data = st.session_state.generated_images[i + j]
                    
                    with col:
                        # Display image
                        st.image(img_data['image'], use_column_width=True)
                        
                        # Image info
                        st.caption(f"**Model:** {img_data['model']}")
                        st.caption(f"**Prompt:** {img_data['prompt'][:50]}...")
                        
                        # Individual download button
                        filename = generate_filename(
                            img_data['prompt'], 
                            img_data['model'], 
                            img_data.get('timestamp', f'img_{i+j}')
                        )
                        img_format = img_data.get('format', 'PNG')
                        img_bytes = image_to_bytes(img_data['image'], img_format)
                        
                        st.download_button(
                            label=f"⬇️ Download",
                            data=img_bytes,
                            file_name=filename,
                            mime=f"image/{img_format.lower()}",
                            key=f"download_{i+j}",
                            use_container_width=True
                        )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🎨 Built with Streamlit • Powered by Hugging Face 🤗</p>
        <p>Made for learning and experimentation 🚀</p>
        <p>✨ Now with download capabilities! ✨</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()