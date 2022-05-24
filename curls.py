# curl --location --request GET 'http://127.0.0.1:8000/account_details/get_account_data?account_id=abc1234'
# curl --location --request POST 'http://127.0.0.1:8000/account_details/save_account_data' \
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



# export SECRET_KEY="django-insecure-iho2$zn66aetx*u1-v553k*i^+t33@t(kv)zd1z$c(m+idl61u"
# export db_name=data_pusher
# export db_user=root
# export db_password=password
# export db_host=localhost