{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1d6d8486-3014-41ab-9e9f-564136daf5e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n",
      "  Downloading streamlit-1.32.2-py2.py3-none-any.whl.metadata (8.5 kB)\n",
      "Collecting altair<6,>=4.0 (from streamlit)\n",
      "  Downloading altair-5.2.0-py3-none-any.whl.metadata (8.7 kB)\n",
      "Collecting blinker<2,>=1.0.0 (from streamlit)\n",
      "  Downloading blinker-1.7.0-py3-none-any.whl.metadata (1.9 kB)\n",
      "Collecting cachetools<6,>=4.0 (from streamlit)\n",
      "  Downloading cachetools-5.3.3-py3-none-any.whl.metadata (5.3 kB)\n",
      "Requirement already satisfied: click<9,>=7.0 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (23.2)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (2.2.1)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (10.2.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from streamlit) (4.25.3)\n",
      "Collecting pyarrow>=7.0 (from streamlit)\n",
      "  Downloading pyarrow-15.0.2-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (3.0 kB)\n",
      "Requirement already satisfied: requests<3,>=2.27 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from streamlit) (13.7.1)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (8.2.3)\n",
      "Collecting toml<2,>=0.10.1 (from streamlit)\n",
      "  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (4.10.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (3.1.42)\n",
      "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
      "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl.metadata (3.9 kB)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (6.4)\n",
      "Collecting watchdog>=2.1.5 (from streamlit)\n",
      "  Downloading watchdog-4.0.0-py3-none-manylinux2014_x86_64.whl.metadata (37 kB)\n",
      "Requirement already satisfied: jinja2 in /home/codespace/.local/lib/python3.10/site-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in /home/codespace/.local/lib/python3.10/site-packages (from altair<6,>=4.0->streamlit) (4.21.1)\n",
      "Collecting toolz (from altair<6,>=4.0->streamlit)\n",
      "  Downloading toolz-0.12.1-py3-none-any.whl.metadata (5.1 kB)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in /home/codespace/.local/lib/python3.10/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /home/codespace/.local/lib/python3.10/site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in /home/codespace/.local/lib/python3.10/site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /home/codespace/.local/lib/python3.10/site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /home/codespace/.local/lib/python3.10/site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /home/codespace/.local/lib/python3.10/site-packages (from requests<3,>=2.27->streamlit) (3.6)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /home/codespace/.local/lib/python3.10/site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /home/codespace/.local/lib/python3.10/site-packages (from rich<14,>=10.14.0->streamlit) (2.17.2)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in /home/codespace/.local/lib/python3.10/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /home/codespace/.local/lib/python3.10/site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
      "Requirement already satisfied: attrs>=22.2.0 in /home/codespace/.local/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.2.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /home/codespace/.local/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in /home/codespace/.local/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.33.0)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in /home/codespace/.local/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
      "Requirement already satisfied: six>=1.5 in /home/codespace/.local/lib/python3.10/site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
      "Downloading streamlit-1.32.2-py2.py3-none-any.whl (8.1 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.1/8.1 MB\u001b[0m \u001b[31m59.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m:00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hDownloading altair-5.2.0-py3-none-any.whl (996 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m996.9/996.9 kB\u001b[0m \u001b[31m20.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hDownloading blinker-1.7.0-py3-none-any.whl (13 kB)\n",
      "Downloading cachetools-5.3.3-py3-none-any.whl (9.3 kB)\n",
      "Downloading pyarrow-15.0.2-cp310-cp310-manylinux_2_28_x86_64.whl (38.3 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m38.3/38.3 MB\u001b[0m \u001b[31m34.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m:00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hDownloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m51.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m:00:01\u001b[0m\n",
      "\u001b[?25hDownloading toml-0.10.2-py2.py3-none-any.whl (16 kB)\n",
      "Downloading watchdog-4.0.0-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m83.0/83.0 kB\u001b[0m \u001b[31m2.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading toolz-0.12.1-py3-none-any.whl (56 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m56.1/56.1 kB\u001b[0m \u001b[31m1.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hInstalling collected packages: watchdog, toolz, toml, pyarrow, cachetools, blinker, pydeck, altair, streamlit\n",
      "Successfully installed altair-5.2.0 blinker-1.7.0 cachetools-5.3.3 pyarrow-15.0.2 pydeck-0.8.1b0 streamlit-1.32.2 toml-0.10.2 toolz-0.12.1 watchdog-4.0.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a64b25d0-1818-4de7-ac33-7f9990de07dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1be2bd29-da09-48d3-b042-3716c11a5242",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-03-22 12:30:09.949 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /home/codespace/.local/lib/python3.10/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.set_page_config(page_title=\"Amazon Reviews Sentiment Analysis App\", page_icon=\"😊😟\")\n",
    "\n",
    "st.markdown(\"#😊😟 Sentiment Analysis\")\n",
    "st.markdown(\"### (Is the text Positive or Negative?)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c49df54-786a-47b0-ba57-909a984d789d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
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
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
