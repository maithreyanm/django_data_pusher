# curl --location --request GET 'http://127.0.0.1:8000/data_handler/get_account_data?email=maithreyan2@gmail.com'
#
#
#
#
#
#
#
# curl --location --request POST 'http://127.0.0.1:8000/data_handler/save_account_data' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "account_name": "maithreyan",
#     "account_id": "maithreyantest123",
#     "website": "google.com",
#     "email":"maithreyan334@gmail.com",
#     "destinations": [
#         {
#             "url": "https://webhook.site/4399ffbb-8fb8-423d-82f5-a4f385d6f20d",
#             "http_method": "POST"
#         },
#         {
#             "url": "https://webhook.site/4399ffbb-8fb8-423d-82f5-a4f385d6f20d",
#             "http_method": "GET"
#         }
#     ]
# }'
#
#
#
#
# curl --location --request PATCH 'http://127.0.0.1:8000/data_handler/update_account_data' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "email":"maithreyan@gmail.com",
#     "account_name": "reyan"
# }'
#
#
#
# curl --location --request DELETE 'http://127.0.0.1:8000/data_handler/delete_account_data' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "email": "maithreyan2@gmail.com"
# }'
#
#
# curl --location --request GET 'http://127.0.0.1:8000/data_handler/get_destination_data?account_id=abcmaith1234'
#
#
#
#
#
# curl --location --request DELETE 'http://127.0.0.1:8000/data_handler/get_destination_data' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "email":"maithreyan3@gmail.com"
# }'
#
#
#
# curl --location --request POST 'http://127.0.0.1:8000/server/incoming_data' \
# --header 'CL-X-TOKEN: 44d4b9cc9a9d49038ee56848511bb3ea' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#      "message": "some random data2222222222222222222"}
# '