1. Clone Project
2. Install Requirements
3. Run Project
4. Connect With Websocket to `/ws`, It is going to create new user on any connect
5. It is going to echo client messages
6. Call `send/<user_id>` API to send custom message to specific user with `user_id` API
```bash
curl http://127.0.0.1:8000/send/1/ -X POST -H "content-type:application/json" --data "{\"message\":\"Hello From API\"}"
```