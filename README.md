# Web Search Integration in DeepSeek


DeepSeek has developed several notable models in the field of artificial intelligence:

DeepSeek-R1: Released in January 2025, this model offers performance comparable to leading AI systems like OpenAI's GPT-4, but at a fraction of the development cost. Its efficiency and open-source nature have made it a significant player in the AI community. 
EN.WIKIPEDIA.ORG

DeepSeek-V3: Introduced in December 2024, DeepSeek-V3 is a Mixture-of-Experts (MoE) language model with a total of 671 billion parameters, of which 37 billion are activated per token. It features innovations such as Multi-head Latent Attention (MLA) and the DeepSeekMoE architecture, enhancing both performance and efficiency. 
GITHUB.COM

DeepSeek-V2: Launched in May 2024, this model also employs a Mixture-of-Experts architecture and was trained on a diverse dataset of 8.1 trillion tokens. It supports a context length of up to 128,000 tokens and has been recognized for its economical training and efficient inference capabilities. 
ARXIV.ORG

These models reflect DeepSeek's commitment to advancing AI technology through innovative architectures and open-source collaboration


## Prerequisite 

You need SerXNG that can be used to find the relevant content to user's query.

Refer to https://github.com/ishan3350/SearXNG on installation guide

## Installation


```bash
git clone https://github.com/ishan3350/SearchWebDeepSeek
```

Change the Serxng endpoint URL with your IP in search.py file

```bash
def searxng_search(query, searxng_url="http://yourip:8080/search"):
    params = {
        'q': query,        # The search query
        'format': 'json'   # Request JSON formatted results
    }
```
If you are using a different model then change the model in test.py file
```bash
response = chat(
    # change the model name here accordingly
    model='deepseek-r1:8b',
    messages=[
        {'role': 'user', 'content': prompt}
    ]
)
```


## License

[MIT](https://choosealicense.com/licenses/mit/)