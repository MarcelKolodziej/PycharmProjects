import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    print(res.raise_for_status())
except Exception as exc:
    print('There was a problem: %s' % (exc))

res.status_code == requests.codes.ok
print(len(res.text))
print(res.text[:250])