from ssl_store import sslcz, store_id

post_body = {
    'tran_id': '014322056',
    'val_id': "2401281712541zYWLdB5YrHoVyz",
    'amount': "100.00",
    'card_type': "BKASH-BKash",
    'store_amount': "97.50",
    'card_no': "",
    'bank_tran_id': "2401281712541KW7lP0Ilmi1hWS",
    'status': "VALID",
    'tran_date': "2024-01-28 17:12:14",
    'currency': "BDT",
    'card_issuer': "BKash Mobile Banking",
    'card_brand': "MOBILEBANKING",
    'card_sub_brand': "Classic",
    'card_issuer_country': "Bangladesh",
    'card_issuer_country_code': "BD",
    'store_id': store_id,
    'verify_sign': "01e8d35f8a66e170d87c176a3a3fdea2",
    'verify_key': "amount,bank_tran_id,base_fair,card_brand,card_issuer,card_issuer_country,card_issuer_country_code,card_no,card_sub_brand,card_type,currency,currency_amount,currency_rate,currency_type,error,risk_level,risk_title,status,store_amount,store_id,tran_date,tran_id,val_id,value_a,value_b,value_c,value_d",
    'verify_sign_sha2': "58bdb96c0857774d19d29aec4be12791bb054b03ab6c8319ebd01e54abfca093",
    'currency_type': "BDT",
    'currency_amount': "100.00",
    'currency_rate': "1.0000",
    'base_fair': "0.00",
    'value_a': "",
    'value_b': "",
    'value_c': "",
    'value_d': "",
    'risk_level': "0",
    'risk_title': "Safe",
    'error': ""
}

if sslcz.hash_validate_ipn(post_body):
    response = sslcz.validationTransactionOrder(post_body['val_id'])
    print(response)
else:
    print("Hash validation failed")
