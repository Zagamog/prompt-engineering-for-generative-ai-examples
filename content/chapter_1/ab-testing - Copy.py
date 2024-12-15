{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  variant  ...                                           response\n",
      "0       A  ...  1. OmniFit Shoes\\n2. FlexiFit Footwear\\n3. Siz...\n",
      "1       A  ...  1. OmniFit Shoes\\n2. AdaptiFit Sneakers\\n3. Ve...\n",
      "2       A  ...  1. OmniFit Shoes\\n2. OneSizeFitAll Loafers\\n3....\n",
      "3       A  ...  1. AnyFit Shoes\\n2. Omni-Adapt Shoes\\n3. Flexi...\n",
      "4       A  ...  1. OmniStride Shoes\\n2. FlexFit Footwear\\n3. A...\n",
      "5       B  ...  AdaptaFit Shoes, FitFlex Footwear, OmniSize Sn...\n",
      "6       B  ...  AdaptaFit Shoes, OmniStep Shoes, CustomFit Foo...\n",
      "7       B  ...  OmniFit Shoes, AdaptiSole, FlexiFit Footwear, ...\n",
      "8       B  ...  OmniFit Shoes, AdaptiSole, PerfectFit Shoes, M...\n",
      "9       B  ...  AdaptaFit Shoes, OmniFit Sneakers, FlexiFit Fo...\n",
      "\n",
      "[10 rows x 3 columns]\n"
     ]
    }
   ],
   "source": [
    "# Define two variants of the prompt to test zero-shot\n",
    "# vs few-shot:\n",
    "prompt_A = \"\"\"Product description: A pair of shoes that can\n",
    "fit any foot size.\n",
    "Seed words: adaptable, fit, omni-fit.\n",
    "Product names:\"\"\"\n",
    "\n",
    "prompt_B = \"\"\"Product description: A home milkshake maker.\n",
    "Seed words: fast, healthy, compact.\n",
    "Product names: HomeShaker, Fit Shaker, QuickShake, Shake\n",
    "Maker\n",
    "\n",
    "Product description: A watch that can tell accurate time in\n",
    "space.\n",
    "Seed words: astronaut, space-hardened, eliptical orbit\n",
    "Product names: AstroTime, SpaceGuard, Orbit-Accurate,\n",
    "EliptoTime.\n",
    "\n",
    "Product description: A pair of shoes that can fit any foot\n",
    "size.\n",
    "Seed words: adaptable, fit, omni-fit.\n",
    "Product names:\"\"\"\n",
    "\n",
    "test_prompts = [prompt_A, prompt_B]\n",
    "\n",
    "import pandas as pd\n",
    "from openai import OpenAI\n",
    "import os\n",
    "\n",
    "# Change the working directory\n",
    "os.chdir(\"D:/prompt-engineering-for-generative-ai-examples/content/chapter_1\")\n",
    "\n",
    "# Set your OpenAI key as an environment variable\n",
    "\n",
    "# OpenAI API Key\n",
    "api_key = os.getenv(\"OPENAI_API_KEY\")\n",
    "client = OpenAI(\n",
    "  api_key=os.getenv(\"OPENAI_API_KEY\"),  # Default\n",
    ")\n",
    "\n",
    "\n",
    "def get_response(prompt):\n",
    "    response = client.chat.completions.create(\n",
    "        model=\"gpt-3.5-turbo\",\n",
    "        messages=[\n",
    "            {\n",
    "                \"role\": \"system\",\n",
    "                \"content\": \"You are a helpful assistant.\"\n",
    "            },\n",
    "            {\n",
    "                \"role\": \"user\",\n",
    "                \"content\": prompt\n",
    "            }\n",
    "        ]\n",
    "    )\n",
    "    return response.choices[0].message.content\n",
    "\n",
    "# Iterate through the prompts and get responses\n",
    "responses = []\n",
    "num_tests = 5\n",
    "\n",
    "for idx, prompt in enumerate(test_prompts):\n",
    "    # prompt number as a letter\n",
    "    var_name = chr(ord('A') + idx)\n",
    "\n",
    "    for i in range(num_tests):\n",
    "        # Get a response from the model\n",
    "        response = get_response(prompt)\n",
    "\n",
    "        data = {\n",
    "            \"variant\": var_name,\n",
    "            \"prompt\": prompt, \n",
    "            \"response\": response\n",
    "            }\n",
    "        responses.append(data)\n",
    "\n",
    "# Convert responses into a dataframe\n",
    "df = pd.DataFrame(responses)\n",
    "\n",
    "# Save the dataframe as a CSV file\n",
    "df.to_csv(\"responses.csv\", index=False)\n",
    "\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "277689943cf54f51a1cd6ea8d8aaa8cf",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HTML(value='<p>1. OmniFit Shoes\\n2. OneSizeFitAll Loafers\\n3. AdaptaStride Sneakers\\n4. FlexiFit Footwear\\n5. …"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "400ef49132164151bf6d8cd49dda4ed3",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(Button(description='👎', style=ButtonStyle()), Button(description='👍', style=ButtonStyle())))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1603f93dec3d48d6a83a0e9464531f6b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Label(value='Response: 1/10')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import ipywidgets as widgets\n",
    "from IPython.display import display\n",
    "import pandas as pd\n",
    "\n",
    "# load the responses.csv file\n",
    "df = pd.read_csv(\"responses.csv\")\n",
    "\n",
    "# Shuffle the dataframe\n",
    "df = df.sample(frac=1).reset_index(drop=True)\n",
    "\n",
    "# df is your dataframe and 'response' is the column with the \n",
    "# text you want to test\n",
    "response_index = 0\n",
    "# add a new column to store feedback\n",
    "df['feedback'] = pd.Series(dtype='str') \n",
    "\n",
    "def on_button_clicked(b):\n",
    "    global response_index\n",
    "    #  convert thumbs up / down to 1 / 0\n",
    "    user_feedback = 1 if b.description == \"\\U0001F44D\" else 0\n",
    "\n",
    "    # update the feedback column\n",
    "    df.at[response_index, 'feedback'] = user_feedback\n",
    "\n",
    "    response_index += 1\n",
    "    if response_index < len(df):\n",
    "        update_response()\n",
    "    else:\n",
    "        # save the feedback to a CSV file\n",
    "        df.to_csv(\"results.csv\", index=False)\n",
    "\n",
    "        print(\"A/B testing completed. Here's the results:\")\n",
    "        # Calculate score and num rows for each variant\n",
    "        summary_df = df.groupby('variant').agg(\n",
    "            count=('feedback', 'count'), \n",
    "            score=('feedback', 'mean')).reset_index()\n",
    "        print(summary_df)\n",
    "        \n",
    "def update_response():\n",
    "    new_response = df.iloc[response_index]['response']\n",
    "    if pd.notna(new_response):\n",
    "        new_response = \"<p>\" + new_response + \"</p>\"\n",
    "    else:\n",
    "        new_response = \"<p>No response</p>\"\n",
    "    response.value = new_response\n",
    "    count_label.value = f\"Response: {response_index + 1}\"\n",
    "    count_label.value += f\"/{len(df)}\"\n",
    "\n",
    "response = widgets.HTML()\n",
    "count_label = widgets.Label()\n",
    "\n",
    "update_response()\n",
    "\n",
    "thumbs_up_button = widgets.Button(description='\\U0001F44D')\n",
    "thumbs_up_button.on_click(on_button_clicked)\n",
    "\n",
    "thumbs_down_button = widgets.Button(\n",
    "    description='\\U0001F44E')\n",
    "thumbs_down_button.on_click(on_button_clicked)\n",
    "\n",
    "button_box = widgets.HBox([thumbs_down_button, \n",
    "thumbs_up_button])\n",
    "\n",
    "display(response, button_box, count_label)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (Spyder)",
   "language": "python3",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.21"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
