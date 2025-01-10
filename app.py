import streamlit as st
from langflow import load_flow
from langchain.schema import AIMessage, HumanMessage

# Load LangFlow workflow
def load_langflow_workflow(file_path):
    with open(file_path, 'r') as file:
        return load_flow(file.read())

# Initialize Streamlit app
st.title("LangFlow Workflow Hosting")

# Load your LangFlow file
workflow_path = "your_project.json"
flow = load_langflow_workflow(workflow_path)

# User input
user_input = st.text_input("Enter your message:")
if user_input:
    with st.spinner("Processing..."):
        # Run the flow
        result = flow.run(HumanMessage(content=user_input))
        st.success("Done!")
        st.write("**Response:**")
        st.write(result.content)
