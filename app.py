from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)

# Function to sending a notification (due to thread it runs in background)
def send_notification(task_id):
    print(f"[Notification] Sending notification for task {task_id}...")
    time.sleep(5)  # Delay by 5 seconds
    print(f"[Notification] Notification sent for task {task_id}.")

# Route Decorator to update task — accepts only POST requests
@app.route('/update_task', methods=['POST'])
def update_task():
    # Extract task_id from incoming JSON request
    task_id = request.json.get('task_id')

    # Create a new thread to send notification asynchronously
    thread = threading.Thread(target=send_notification, args=(task_id,))
    
    # Start the thread — this runs send_notification() in the background, to complete thread it take minimum 5 seconds
    thread.start()

    # Do not wait for the thread to complete — return response immediately
    return jsonify({'message': f'Task {task_id} updated. Notification will be sent in background.'})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
