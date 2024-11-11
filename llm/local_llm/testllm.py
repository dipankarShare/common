import streamlit as st
import ollama
# from langchain import Ollama

ollama_client = ollama.Client()
# ollama_client = Ollama()

st.title("LLM App based on Local Ollama")

# Function to list available models using Ollama
def get_available_models():
    try:
        models = ollama_client.list()
        model_names = [model['name'] for model in models['models']]

        # Debugging print message
        # st.write("Debugging my_variable:", model_names)

        return model_names
    except Exception as e:
        st.error(f"Error fetching models: {e}")
        return []
    
# Function to generate the response using Ollama
def gen_response(desiredModel: str, question: str):
    response = ollama.chat(model=desiredModel, 
                           messages=[{
                               'role': 'user',
                               'content': question,
                           }])

    st.info(response['message']['content'])

# Get the list of installed models
model_names = get_available_models()

if model_names:
    # Dropdown to select the model
    selected_model = st.selectbox("Select Model", model_names)
    detail_or_concise = st.selectbox("Detail/Concise", ['Concise', 'Detail'])
    # Create a Streamlit form for user input
    with st.form("dip_form"):
        input_text = st.text_area("Enter Text:", "Enter the question and press the Submit button.")
        submitted = st.form_submit_button("Submit")

        # Check if the form is submitted, then generate a response
        if submitted:
            gen_response(selected_model, input_text + f". Give a {detail_or_concise} answer.")
