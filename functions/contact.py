import json
import os
from datetime import datetime

def handler(event, context):
    """Handle contact form submissions"""
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
        
        # Simple form data parsing (you might want to use a proper parser)
        form_data = {}
        for line in body.split('&'):
            if '=' in line:
                key, value = line.split('=', 1)
                form_data[key] = value.replace('+', ' ').replace('%20', ' ')
        
        # Extract form fields
        name = form_data.get('name', '').strip()
        email = form_data.get('email', '').strip()
        phone = form_data.get('phone', '').strip()
        company = form_data.get('company', '').strip()
        message = form_data.get('message', '').strip()
        
        # Basic validation
        if not name or not email or not message:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Please fill in all required fields'})
            }
        
        # Here you would typically save to a database or send an email
        # For now, we'll just return success
        submission_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'company': company,
            'message': message,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # You could save this to a database or send via email service
        # For now, we'll just log it (in production, use a proper database)
        print(f"Contact submission: {json.dumps(submission_data)}")
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({
                'success': True,
                'message': 'Thank you for your message! We will get back to you soon.'
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': f'Internal server error: {str(e)}'})
        } 