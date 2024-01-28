from ssl_store import sslcz

session_key = '6BDB86B59A30665FE29D3397F7FCF4B8'
response = sslcz.transaction_query_session(session_key)
print(response)