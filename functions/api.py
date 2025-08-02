from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
import os
import json

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SESSION_SECRET", "bharatmiles-secret-key-2025")
    
    # Configure the database with absolute path
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'bharatmiles.db')}"
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }
    
    # Initialize the app with the extension
    db.init_app(app)
    
    return app

app = create_app()

# Database Models
class ContactSubmission(db.Model):
    __tablename__ = 'contact_submissions'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    company = db.Column(db.String(100), nullable=True)
    message = db.Column(db.Text, nullable=False)
    submission_type = db.Column(db.String(20), default='contact')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<ContactSubmission {self.name} - {self.email}>'

class ExportInquiry(db.Model):
    __tablename__ = 'export_inquiries'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    company = db.Column(db.String(100), nullable=True)
    product_category = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.String(100), nullable=True)
    destination_country = db.Column(db.String(100), nullable=True)
    additional_details = db.Column(db.Text, nullable=True)
    submission_type = db.Column(db.String(20), default='inquiry')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default='pending')
    
    def __repr__(self):
        return f'<ExportInquiry {self.name} - {self.product_category}>'

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        company = request.form.get('company', '').strip()
        message = request.form.get('message', '').strip()
        
        # Basic validation
        if not name or not email or not message:
            flash('Please fill in all required fields.', 'error')
            return redirect(url_for('contact'))
        
        # Create new contact submission
        submission = ContactSubmission(
            name=name,
            email=email,
            phone=phone,
            company=company,
            message=message
        )
        
        # Save to database
        db.session.add(submission)
        db.session.commit()
        
        flash('Thank you for your message! We will get back to you soon.', 'success')
        
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while submitting your message. Please try again.', 'error')
    
    return redirect(url_for('contact'))

@app.route('/submit_inquiry', methods=['POST'])
def submit_inquiry():
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        company = request.form.get('company', '').strip()
        product = request.form.get('product', '').strip()
        quantity = request.form.get('quantity', '').strip()
        destination = request.form.get('destination', '').strip()
        details = request.form.get('details', '').strip()
        
        # Basic validation
        if not name or not email or not product:
            flash('Please fill in all required fields.', 'error')
            return redirect(url_for('services'))
        
        # Create new export inquiry
        inquiry = ExportInquiry(
            name=name,
            email=email,
            company=company,
            product_category=product,
            quantity=quantity,
            destination_country=destination,
            additional_details=details
        )
        
        # Save to database
        db.session.add(inquiry)
        db.session.commit()
        
        flash('Your inquiry has been submitted successfully! Our team will contact you within 24 hours.', 'success')
        
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while submitting your inquiry. Please try again.', 'error')
    
    return redirect(url_for('services'))

@app.route('/admin/submissions')
def view_submissions():
    # Simple admin view to see submissions (in a real app, this would be protected)
    contact_submissions = ContactSubmission.query.order_by(ContactSubmission.created_at.desc()).all()
    export_inquiries = ExportInquiry.query.order_by(ExportInquiry.created_at.desc()).all()
    return render_template('admin_submissions.html', 
                         contact_submissions=contact_submissions,
                         export_inquiries=export_inquiries)

# Netlify serverless function handler
def handler(event, context):
    """Netlify serverless function handler"""
    try:
        # Parse the event
        path = event.get('path', '/')
        http_method = event.get('httpMethod', 'GET')
        headers = event.get('headers', {})
        body = event.get('body', '')
        query_string = event.get('queryStringParameters', {})
        
        # Create a mock request context
        with app.test_request_context(
            path=path,
            method=http_method,
            headers=headers,
            data=body,
            query_string=query_string
        ):
            # Get the response from Flask
            response = app.full_dispatch_request()
            
            # Convert Flask response to Netlify format
            return {
                'statusCode': response.status_code,
                'headers': dict(response.headers),
                'body': response.get_data(as_text=True)
            }
            
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/plain'},
            'body': f'Internal Server Error: {str(e)}'
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 