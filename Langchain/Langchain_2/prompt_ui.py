import json
from dotenv import load_dotenv
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Load the prompt template from JSON file
with open(r'C:\Users\jadit\OneDrive\Dokumente\Python\GEN-AI\Langchain\Langchain_3\template.json', 'r') as f:
    template_data = json.load(f)

# Create a LangChain PromptTemplate
prompt_template = PromptTemplate(
    template=template_data["template"],
    input_variables=template_data["input_variables"]
)

# Initialize LLM model
llm = ChatGroq(model="llama3-70b-8192")
model = llm

# Streamlit UI
st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name", 
    [
        "Attention Is All You Need", 
        "BERT: Pre-training of Deep Bidirectional Transformers", 
        "GPT-3: Language Models are Few-Shot Learners", 
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

if st.button('Summarize'):
    # Construct the final prompt
    final_prompt = prompt_template.format(
        paper_input=paper_input, 
        style_input=style_input, 
        length_input=length_input
    )
    
    # Generate response from the model
    result = model.invoke(final_prompt)
    
    # Display output
    st.write(result.content)