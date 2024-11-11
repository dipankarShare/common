## LAMA 3.1:8Billion
- Download and Install the mac version

  https://ollama.com/download
- Which model best?
    - ollama run llama3.2:latest
    - ollama run mistral
    - this one is old - ollama.com/library/llama3.1:8b
      - comparision
    https://www.youtube.com/watch?v=BkWTAS_MKno

## Init
```bash
cd ..../personal/tech/llm
python3 -m venv myllm
source myllm/bin/activate
# already installed 
# xcode-select --install 
pip install -r requirements.txt
pip list
streamlit run local_llm/testllm.py
ollama --version
```
