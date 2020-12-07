from time import sleep
# Basic scroll text function for the Python console
def scroll(text, delay=0.03):
  for i in text:
    print(i, end="", flush=True)
    sleep(delay)
