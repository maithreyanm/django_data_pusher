import requests

responnse = requests.get(url='http://127.0.0.1:8000/server/incoming_data', headers={'CL-X-TOKEN':'63772b770914415e8fec70f7842899ea'}
                         ,data={
    "message": "some random data"
})

print(responnse)