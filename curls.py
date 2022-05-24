# curl --location --request GET 'http://127.0.0.1:8000/data_handler/get_account_data?account_id=abc1234'
# curl --location --request POST 'http://127.0.0.1:8000/data_handler/save_account_data' \
# --header 'X-CSRFToken: aa' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "account_name": "maithreyan",
#     "account_id":"abcmaith1234",
# "app_secret": "appsecret",
# "website":"google.com",
# "destinations":[
#    { "url": "https:// google.com",
#     "http_method": "POST",
#     "headers": {"name":"maithreyan"}},
#      { "url": "https:// google.com",
#     "http_method": "POST",
#     "headers": {"name":"maithreyan"}}
# ]
# }'


# curl --location --request PATCH 'http://127.0.0.1:8000/data_handler/update_account_data' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "account_id":"abcmaith1234",
#     "account_name":"hhhh"
# }'


# curl --location --request DELETE 'http://127.0.0.1:8000/data_handler/delete_account_data' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "account_id":"abcmaith1234"
# }'