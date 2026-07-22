import json

def lambda_handler(event, context):
    # Step 1: Read the incoming HTTP body sent by the client
    raw_body = event.get('body')
    
    # Validation: Check if request body exists
    if not raw_body:
        return {
            'statusCode': 400,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Missing request body'})
        }

    # Step 2: Convert the incoming JSON string into a Python Dictionary
    data = json.loads(raw_body)
    
    # Step 3: Extract order details
    customer_id = data.get('customer_id')
    item = data.get('item')
    price = data.get('price', 0)
    quantity = data.get('quantity', 1)

    # Step 4: Execute Business Logic (e.g., calculate total cost)
    total_amount = price * quantity
    order_id = "ORD-99823"  # Simulated generated Order ID

    # Step 5: Build success payload
    response_payload = {
        'message': 'Order processed successfully!',
        'order_id': order_id,
        'customer_id': customer_id,
        'total_amount': total_amount
    }

    # Step 6: Return standard API Gateway HTTP response format
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'  # Allows cross-domain requests (CORS)
        },
        'body': json.dumps(response_payload)
    }
