# Social Media Analyzer

This project is a social media analyzer built using Streamlit, LangFlow, and LangChain. It allows users to analyze social media data and generate insights.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/social-media-analyzer.git
    cd social-media-analyzer
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Create a [.env](http://_vscodecontentref_/0) file in the root directory and add the following line:
    ```properties
    .venv
    ```

2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

3. Open your web browser and go to `http://localhost:8501` to access the app.

## Project Structure

- [app.py](http://_vscodecontentref_/1): Main application file that initializes the Streamlit app and loads the LangFlow workflow.
- [requirements.txt](http://_vscodecontentref_/2): List of dependencies required for the project.
- [.env](http://_vscodecontentref_/3): Environment file specifying the virtual environment.

## Dependencies

- `streamlit`
- `langflow`
- `langchain`
- `requests`
- `pydantic`
- `typing-extensions`

