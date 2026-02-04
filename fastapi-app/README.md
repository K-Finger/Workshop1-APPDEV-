1. run in the terminal: pip install -r requirements.txt.

2. Start the app with uvicorn main:app --reload

If 'uvicorn main:app --reload' doesn't work, try

# python -m uvicorn main:app --reload

uvicorn main:app --reload doesn't work because uvicorn is not added to your enviornment variables on your computer.