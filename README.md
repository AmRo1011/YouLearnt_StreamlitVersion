# AI Course Description Generator

<<<<<<< HEAD
A web application that generates professional course descriptions using AI. Built with Streamlit and Groq AI.
=======
A web application that generates professional course descriptions using AI. Built with Flask and Groq AI.
>>>>>>> origin/main

## Features

- Generate course descriptions based on title and category
- Support for multiple languages
- Clean and modern UI
- Real-time generation with loading indicators
- Error handling and validation

## Prerequisites

- Python 3.8 or higher
- Groq API key (get it from [Groq Console](https://console.groq.com/))
<<<<<<< HEAD
- Git (optional, for version control)

## Installation

### 1. Clone the repository (optional)
```bash
git clone https://github.com/AmRo1011/course_description_generator-You_Learnt-.git
cd course_description_generator-You_Learnt-
```

### 2. Set up Python Virtual Environment

#### Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate
```

#### macOS/Linux:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 3. Install dependencies
=======

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/course_description_generator.git
cd course_description_generator
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
>>>>>>> origin/main
```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
### 4. Set up environment variables

Create a `.env` file in the project root with the following variables:
=======
4. Create a `.env` file in the project root with the following variables:
>>>>>>> origin/main
```
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama3-8b-8192
TEMPERATURE=0.7
TIMEOUT=30
<<<<<<< HEAD
```

Replace `your_groq_api_key_here` with your actual Groq API key from [Groq Console](https://console.groq.com/).

## Running the Application

1. Make sure your virtual environment is activated (you should see `(venv)` at the start of your command prompt)

2. Start the Streamlit app:
```bash
streamlit run app.py
```

3. The app will automatically open in your default web browser at:
```
http://localhost:8501
```

If it doesn't open automatically, you can manually open the URL in your browser.

## Usage

1. Enter the course title (e.g., "Python for Beginners")
2. Enter the course category (e.g., "Programming")
3. Select the language from the dropdown
4. Click "Generate Description"
5. Wait for the AI to generate the description
6. The generated description will appear in the text area below

## Troubleshooting

### Common Issues

1. **Virtual Environment Not Activating**
   - Windows: Make sure you're running the command from the correct directory
   - macOS/Linux: Ensure the script has execute permissions

2. **Package Installation Errors**
   - Try upgrading pip: `python -m pip install --upgrade pip`
   - Make sure you're in the virtual environment (check for `(venv)` prefix)

3. **Streamlit Not Starting**
   - Check if all dependencies are installed correctly
   - Try running `streamlit --version` to verify installation

4. **API Key Issues**
   - Verify your Groq API key is correct
   - Check if the `.env` file is in the correct location
   - Make sure the `.env` file is properly formatted
=======
PORT=5000
DEBUG=True
ALLOWED_ORIGINS=*
```

## Usage

1. Start the Flask server:
```bash
python main.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter the course title and category, select a language, and click "Generate Description"
>>>>>>> origin/main

## Project Structure

```
course_description_generator/
<<<<<<< HEAD
├── app.py              # Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in git)
└── README.md          # Project documentation
=======
├── main.py              # Flask application
├── index.html           # Main HTML template
├── style.css            # CSS styles
├── script.js            # JavaScript functionality
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
>>>>>>> origin/main
```

## Technologies Used

<<<<<<< HEAD
- Streamlit (Python web framework)
- Groq AI (Language model)
- Python-dotenv (Environment management)
=======
- Flask (Python web framework)
- Groq AI (Language model)
- HTML5
- CSS3
- JavaScript (ES6+)
>>>>>>> origin/main

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 