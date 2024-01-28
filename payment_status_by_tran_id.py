from ssl_store import sslcz

tran_id = '014322056'
response = sslcz.transaction_query_tranid(tran_id)
print(response)
