from get_customer import get_user_data

def lambda_handler(event, context):
    print(event)
    customer_info = get_user_data(event['name'])[0]
    return customer_info