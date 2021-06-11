import requests as req

resp = req.get("https://www.instrumentationtoolbox.com/2013/10/the-orifice-flow-meter-equation.html")

txt = resp.text

status = resp.status_code

print(resp.text)
print(resp.status_code)

print(txt,status)