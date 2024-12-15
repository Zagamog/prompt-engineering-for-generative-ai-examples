import os

# Change the working directory
os.chdir("D:/prompt-engineering-for-generative-ai-examples/content/chapter_3/")


with open("hubspot_blog_post.txt", "r") as f:
    text = f.read()

chunks = [text[i : i + 200] for i in range(0, len(text), 200)]

for chunk in chunks:
    print("-" * 20)
    print(chunk)
