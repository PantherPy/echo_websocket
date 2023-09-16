1. Clone Project
2. Install Requirements
3. Run Project
4. Connect With Websocket to `/ws`
5. It is going to echo client messages
6. Call `send/<connection_id>` API to send custom message to API
```bash
curl http://127.0.0.1:8000/send/dmNgKkLUEG/ -X POST -H "content-type:application/json" --data "{\"message\":\"Hello From API\"}"
```