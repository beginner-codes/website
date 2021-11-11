import uvicorn


uvicorn.run("bc_website.app:app", host="localhost", port=5000, reload=True)
