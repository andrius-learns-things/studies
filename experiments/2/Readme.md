# POC of docker python flask app debugging with pdb

Taken from https://www.agiratech.com/debugging-python-flask-app-in-docker-container/

To get into debugger:

- `sudo docker-compose up -d --build`
- `sudo docker ps`
- `sudo docker attach 39139f6dd788` - Replace with real img id
- Open http://localhost:8052/ in browser

In debugger you can:
- Print contents of `test`: `test`
- Set new contents of `test`: `test = "A"`
- Continue: `c`
- You'll see `test` contents returned in browser

Hints:
- Sometimes debugger terminal is super-slow. Restart in that case.
