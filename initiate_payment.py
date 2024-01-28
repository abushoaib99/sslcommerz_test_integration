from random import randrange
from ssl_store import sslcz


def get_random_transaction_id():
    """
    Generate a random number of length 9 (nine) characters
    """
    transaction_id = ''
    for _ in range(0, 9):
        transaction_id += str(randrange(0, 9))

    return transaction_id


tran_id = get_random_transaction_id()

post_body = {
    'total_amount': 100,
    'currency': "BDT",
    'tran_id': tran_id,
    'success_url': "http://localhost:8000/payment-status/",
    'fail_url': "http://localhost:8000/payment-status/",
    'cancel_url': "http://localhost:8000/payment-status/",
    'emi_option': 0,

    'cus_name': "test",
    'cus_email': "test@test.com",
    'cus_phone': "01700000000",
    'cus_add1': "customer address",
    'cus_city': "Dhaka",
    'cus_country': "Bangladesh",

    'shipping_method': "NO",
    'multi_card_name': "",
    'num_of_item': 1,
    'product_name': "Test",
    'product_category': "Test Category",
    'product_profile': "general"
}

response = sslcz.createSession(post_body)  # API response
print(response)
# Save the response data into database (like `sessionkey`, `status` etc)
for key, value in response.items():
    print(key, ": ", value)
