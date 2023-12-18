import os
from tqdm import trange

def template(context, prompt):
    template = f"""Answer the question with context: <context>{context}<context> Question: <question>{prompt}<question>
    """
    return template

def GPT4(prompt, client):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        temperature=0,
        messages=[
            # {
            #     "role": "system",
            #     "content": ""
            # },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response

def removeNull(documents):
    for i in trange(len(documents)):
        documents[i].page_content = documents[i].page_content.replace("\x00", "\uFFFD")
    return documents

def printContext(context):
    for i in range(len(context)):
        print(f"##CONTEXT## {i+1}: {context[i].page_content}")

def removeDots(documents):
    for i in trange(len(documents)):
        documents[i].page_content = documents[i].page_content.replace("..................", ".")
    return documents