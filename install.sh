#!/bin/bash

# Font Installer Setup Script
echo "🎨 Setting up Font Installer..."
echo "================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is required but not installed."
    echo "Please install pip3 and try again."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Make the script executable
chmod +x src/install_fonts.py

echo "✅ Setup complete!"
echo ""
echo "To run the font installer:"
echo "1. Ensure you're in the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Run the installer:"
echo "   python src/install_fonts.py"
echo ""
echo "Happy font installing! 🎉" 