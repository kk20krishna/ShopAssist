# ShopAssist

ShopAssist is an AI-powered web application that helps users find the most suitable laptop based on their requirements. It uses OpenAI's GPT models to interact with users, ask targeted questions, and recommend laptops from a curated dataset. The app is built with Flask and features a modern chat interface.

---

## Features

- **Conversational AI**: Guides users through a series of questions to understand their laptop needs.
- **Smart Recommendations**: Suggests laptops based on GPU intensity, display quality, portability, multitasking, processing speed, and budget.
- **Moderation**: Filters inappropriate content using OpenAI's moderation API.
- **Persistent Conversation**: Maintains chat history during the session.
- **Modern UI**: Clean, responsive chat interface styled with CSS.
- **Easy Reset**: Users can end the conversation and start a new one at any time.

---

## Demo

![ShopAssist Chat UI Screenshot](static/send-icon.png) <!-- Replace with actual screenshot if available -->

---

## Getting Started

### Prerequisites

- Python 3.10+
- [pip](https://pip.pypa.io/en/stable/)
- OpenAI API Key

### Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/ShopAssist.git
    cd ShopAssist
    ```

2. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables**

    - Copy `.env_example` to `.env` and add your OpenAI API key:
      ```
      cp .env_example .env
      ```
      Edit [.env](http://_vscodecontentref_/0) and set:
      ```
      OPENAI_API_KEY=sk-...
      ```

4. **Run the application**
    ```sh
    python app.py
    ```
    The app will be available at `http://localhost:5000/` by default.

---

## Project Structure
├── app.py # Flask application entry point 
├── functions.py # Core logic: configs, OpenAI API, recommendation, moderation 
├── configs.yaml # Assistant configuration and prompt templates 
├── updated_laptop.csv # Laptop dataset with features and descriptions 
├── requirements.txt # Python dependencies 
├── static
    ├── CSS
        └── styles.css # Chat UI styles 
        └── send-icon.png # (Optional) UI asset 
├── templates
    └── shopAssist.html # Main chat interface template
└── .env_example # Example environment file


---

## How It Works

1. **User Interaction**: Users interact with the assistant via a chat interface.
2. **Requirement Gathering**: The assistant asks questions to clarify user needs.
3. **Recommendation Engine**: Once requirements are confirmed, the assistant calls the  function, which filters and scores laptops from the dataset.
4. **Result Presentation**: The assistant presents the top recommendations in plain language.
5. **Feedback Loop**: Users can refine their requirements or end the conversation.

---

## Customization

- **Laptop Dataset**: Update  to add or modify laptop options.
- **Assistant Behavior**: Edit  to change prompts, questions, or the system's workflow.
- **UI Styling**: Modify  for custom look and feel.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

---

## License

This project is licensed under the MIT License. See LICENSE for details.

---

## Acknowledgements

- [OpenAI](https://openai.com/) for the GPT API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Pandas](https://pandas.pydata.org/) for data handling

---

## Contact

For questions or support, please open an issue on GitHub or contact the maintainer.
