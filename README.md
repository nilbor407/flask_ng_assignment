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
    



**Task 2: RxJS Integration (Conceptual)**

This task explains how the backend can send real-time updates to a frontend that uses RxJS.

In many applications, the frontend needs to update automatically when something changes (like when a task is updated). We can do this using technologies that push data from the server to the client.

We will discuss two main options: WebSockets and Server-Sent Events (SSE).



**Option 1: WebSockets (Two-way communication)**

WebSocket is a protocol that creates a live connection between the backend and the frontend. Both sides can send data at any time.

**Why WebSockets?**
- Best for real-time communication like chat apps, notifications, and dashboards.
- Works well with RxJS to receive a stream of updates.

**How it works:**
1. Frontend connects to a WebSocket endpoint (like `ws://server.com/updates`).
2. Backend uses `Flask-SocketIO` to send updates when a task changes.
3. RxJS listens to these events and updates the UI without refreshing.

**Example Event:**
{
  "event": "task_updated",
  "task_id": 101,
  "status": "completed"
}

---

**Option 2: Server-Sent Events (SSE) (One-way communication)**

SSE is a simpler method to send real-time updates from the server to the client. It only works in one direction — from server to frontend.

**Why SSE?**
- Easy to implement using regular HTTP.
- Good for sending simple notifications, logs, or updates.
- Works well with RxJS to listen to incoming data.

**How it works:**
1. Frontend creates an `EventSource` that listens to a stream from the server.
2. Server sends updates using `Content-Type: text/event-stream`.
3. RxJS listens to the data stream and updates the frontend accordingly.
