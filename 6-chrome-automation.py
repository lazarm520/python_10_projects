import webbrowser as wb

def webauto():
  chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' # ADD THE PATH OF CHROME HERE
  URLS = (
    "stackoverflow.com",
    "github.com/lazarm520",
    "gmail.com",
    "google.com",
    "youtube.com",
  )
  for url in URLS:
    print("Openning : " + url)
    wb.get(chrome_path).open(url)

webauto()
