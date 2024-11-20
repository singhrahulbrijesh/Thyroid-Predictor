# 1. Use a Python 3.7 base image
FROM python:3.7-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements.txt file into the container
COPY requirements.txt .

# 4. Install the Python dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code into the container
COPY . .

# 6. Expose the port Streamlit will run on
EXPOSE 8501

# 7. Set the default command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
