from .llm import llm
from .parsers import classification_parser, summary_parser, translation_parser
from src.prompts.prompts import classification_prompt, summary_prompt, translation_prompt, chat_prompt

# Classification Chain
classification_chain = classification_prompt | llm | classification_parser

# Summary Chain
summary_chain = summary_prompt | llm | summary_parser

# Translation Chain
translation_chain = translation_prompt | llm | translation_parser

# Chat Chain
chat_chain = chat_prompt | llm
