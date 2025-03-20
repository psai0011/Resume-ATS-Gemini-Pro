# Resume-ATS-Gemini-Pro

Resume-ATS-Gemini-Pro is a web application built using **Streamlit** that leverages **Google Generative AI (Gemini Pro)** for **Resume Analysis and ATS (Applicant Tracking System) Optimization**. It extracts text from PDF resumes, processes them, and provides insights based on AI analysis.

## Features

- Upload PDF resumes
- Convert PDF to images for processing
- Extract text from resumes
- Use **Google Generative AI (Gemini Pro)** to analyze and optimize resumes
- Display ATS-friendly recommendations
- Simple and interactive **Streamlit** UI

## Installation

### Prerequisites
Make sure you have **Python 3.10** installed on your system.

### Clone the Repository
```sh
git clone https://github.com/your-username/Resume-ATS-Gemini-Pro.git
cd Resume-ATS-Gemini-Pro
```

### Install Dependencies
Create a virtual environment (optional but recommended):
```sh
conda create -p venv python==3.10 -y
conda activate venv/
```
Install required Python packages:
```sh
pip install -r requirements.txt
```

### Environment Variables
Create a **.env** file in the root directory and add the following variables:
```sh
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage
Run the Streamlit application:
```sh
streamlit run app.py
```

## Dependencies
The following Python libraries are used in this project:
```sh
streamlit
google-generativeai
python-dotenv
pdf2image
```

## Contributing
Feel free to fork the repository and submit a pull request with any improvements.

## License
This project is licensed under the MIT License.
