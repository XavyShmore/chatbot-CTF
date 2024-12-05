# The guardian CTF Chatbot Challenge

Welcome to the Laval University CTF Chatbot Challenge! This project is designed as a friendly Capture the Flag (CTF) challenge where participants must interact with a chatbot to retrieve a secret code (the flag). 

---

## **Getting Started**

### **Prerequisites**
To run this project locally, you'll need:
1. An OpenAI API key.
2. Python (works on 3.12, probably on older versions too).
3. Docker (optional).

---

## **Run with Docker**
See [Run locally](#run-locally) if you don't want to use docker.

1. **Environment Variables**
   - Create a `.env` file in the root of the project and define the following variables:
     ```dotenv
     OPENAI_API_KEY=yourApiKey
     FLAG=ctf{yourFlagHere}
     ```
     - Replace `yourApiKey` with your OpenAI API key.
     - Replace `ctf{yourFlagHere}` with the flag participants need to find.


2. **Docker Deployment**
   - To run the app in a Docker container, use the included `docker-compose` configuration:
     ```bash
     docker compose up
     ```

---

## **Customization**

1. **Language Translation**
   - If you prefer a language other than French (used during the original competition), update the chatbot prompts in [`prompts.py`](./prompts.py). Modify the system prompt and initial messages to suit your language.

---

### **Run locally**
These instruction are to run the app locally to test or for development. The flag is in the files of the project so it as to be hosted in order to work for a CTF. 

1. **Environment Variables**
   - Create a `.env` file in the root of the project and define the following variables:
     ```dotenv
     OPENAI_API_KEY=yourApiKey
     FLAG=ctf{yourFlagHere}
     ```
     - Replace `yourApiKey` with your OpenAI API key.
     - Replace `ctf{yourFlagHere}` with the flag participants need to find.

2. **Install Dependencies**
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Initialize the Database**
   - Set up the database:
     ```bash
     python db.py
     ```

4. **Run the Application**
   - Start the application locally:
     ```bash
     python main.py
     ```
   - By default, the development server will start on [http://127.0.0.1:5000](http://127.0.0.1:5000).


