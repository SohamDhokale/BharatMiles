import json
import os
from datetime import datetime

def handler(event, context):
    """Handle export inquiry form submissions"""
    try:
        # Parse the request
        if event.get('httpMethod') != 'POST':
            return {
                'statusCode': 405,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Method not allowed'})
            }
        
        # Parse form data
        body = event.get('body', '')
        if not body:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'No data provided'})
            }
        
        # Simple form data parsing
        form_data = {}
        for line in body.split('&'):
            if '=' in line:
                key, value = line.split('=', 1)
                form_data[key] = value.replace('+', ' ').replace('%20', ' ')
        
        # Extract form fields
        name = form_data.get('name', '').strip()
        email = form_data.get('email', '').strip()
        company = form_data.get('company', '').strip()
        product = form_data.get('product', '').strip()
        quantity = form_data.get('quantity', '').strip()
        destination = form_data.get('destination', '').strip()
        details = form_data.get('details', '').strip()
        
        # Basic validation
        if not name or not email or not product:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Please fill in all required fields'})
            }
        
        # Here you would typically save to a database or send an email
        # For now, we'll just return success
        inquiry_data = {
            'name': name,
            'email': email,
            'company': company,
            'product_category': product,
            'quantity': quantity,
            'destination_country': destination,
            'additional_details': details,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # You could save this to a database or send via email service
        # For now, we'll just log it (in production, use a proper database)
        print(f"Export inquiry: {json.dumps(inquiry_data)}")
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({
                'success': True,
                'message': 'Your inquiry has been submitted successfully! Our team will contact you within 24 hours.'
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': f'Internal server error: {str(e)}'})
        } 