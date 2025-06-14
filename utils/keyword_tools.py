import openai

def fetch_related_keywords(seed):
    prompt = f"Generate 25 SEO-related keywords for: {seed}. Group them by intent."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    text = response['choices'][0]['message']['content']
    keywords = [line.strip() for line in text.split('\n') if line]
    return keywords
