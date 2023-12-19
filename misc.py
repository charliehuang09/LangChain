import os
from tqdm import trange

def get_context(context):
    out = []
    for i, obj in enumerate(context):
        # print(obj[0].page_content)
        out.append(f"Context: {i} <context> {obj[0].page_content} <context> ")
    out = "".join(out)
    return out

def template(context, prompt):
    context = get_context(context)
    template = f"""Answer the question with the following contexts: {context}\n Question: <question>{prompt}<question>
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