**Task 1: Asynchronous Notification**
   - This tasks shows how to send notifications in the background using Flask and Python threading.
   - When we update a task using an API, a notification is sent. 
   - But the API does not wait for the notification to finish and it sends it in the background.

  **How it works**
    - User send a POST request to /update_task with a task_id.
    - A new thread starts to send a notification.
    - The API responds immediately, without waiting for the notification.

  **Why threading**
    - threading makes the API faster.
    - The user does not need to wait for the notification.
    - It helps to handle next upcoming requests quickly.

  **Commands to run app.py**
    python -m venv env
    env\Scripts\activate
    pip install Flask
    python app.py
    Send a POST request using Postman
        - curl -X POST http://127.0.0.1:5000/update_task -H "Content-Type: application/json" -d "{\"task_id\": 101}"
    
    You will see a message immediately.
    After 5 seconds, the cmd will print a notification message.
    
