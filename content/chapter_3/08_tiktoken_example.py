# Needed lot of workaround because of ssl error
# https://stackoverflow.com/questions/76106366/how-to-use-tiktoken-in-offline-mode-computer#76107077

import tiktoken_ext.openai_public
import inspect
import tiktoken

print(dir(tiktoken_ext.openai_public))
# The encoder we want is cl100k_base, we see this as a possible function

print(inspect.getsource(tiktoken_ext.openai_public.cl100k_base))
# The URL should be in the 'load_tiktoken_bpe function call'

import hashlib

blobpath = "https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken"
cache_key = hashlib.sha1(blobpath.encode()).hexdigest()
print(cache_key)

import os

tiktoken_cache_dir = "C:/Users/wb164718/.cache/tiktoken"
os.environ["TIKTOKEN_CACHE_DIR"] = tiktoken_cache_dir

# validate
assert os.path.exists(os.path.join(tiktoken_cache_dir, cache_key))

encoding = tiktoken.get_encoding("cl100k_base")
encoding.encode("Hello, world")




# 2. Load an encoding with tiktoken.get_encoding()
encoding = tiktoken.get_encoding("cl100k_base")

# 3. Turn some text into tokens with encoding.encode()
print(encoding.encode("Learning how to use Tiktoken is fun!"))
print(encoding.decode([1061, 15009, 374, 264, 2294, 1648, 311, 4048, 922, 15592, 0]))

print(encoding.decode([48567, 1268, 311, 1005, 73842, 5963, 374, 2523, 0]))
print(encoding.decode([48567, 1855, 311, 1005, 73842, 5963, 374, 2523, 0]))


def count_tokens(text_string: str, encoding_name: str) -> int:
    """
    Returns the number of tokens in a text string using a given encoding.

    Args:
        text: The text string to be tokenized.
        encoding_name: The name of the encoding to be used for tokenization.

    Returns:
        The number of tokens in the text string.

    Raises:
        ValueError: If the encoding name is not recognized.
    """
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(text_string))
    return num_tokens


# 4. Use the function to count the number of tokens in a text string.
text_string = "Hello world! This is a test."
print(count_tokens(text_string, "cl100k_base"))


# Use this function to count the number of tokens in a list of messages:
def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
    """Return the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif "gpt-3.5-turbo" in model:
        print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
        return num_tokens_from_messages(messages, model="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens

