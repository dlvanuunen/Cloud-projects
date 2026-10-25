# 1. Base image: which image do you start from? (name:tag)
FROM python:3.13-slim-bookworm

# 2. Working directory inside the container
WORKDIR /app

# 3. Copy the requirements file in first (so the install step can be cached)
COPY requirements.txt .

# 4. Install the libraries
RUN pip install -r requirements.txt

# 5. Copy the rest of your code in
COPY . .
# 6. Command to run when the container starts
CMD ["python", "Test.py"]