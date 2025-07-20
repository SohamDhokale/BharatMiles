import os
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "bharatmiles-secret-key-2025")

# In-memory storage for form submissions
form_submissions = []
inquiries = []

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
        
        # Store submission
        submission = {
            'id': len(form_submissions) + 1,
            'name': name,
            'email': email,
            'phone': phone,
            'company': company,
            'message': message,
            'timestamp': datetime.now(),
            'type': 'contact'
        }
        
        form_submissions.append(submission)
        flash('Thank you for your message! We will get back to you soon.', 'success')
        
    except Exception as e:
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
        
        # Store inquiry
        inquiry = {
            'id': len(inquiries) + 1,
            'name': name,
            'email': email,
            'company': company,
            'product': product,
            'quantity': quantity,
            'destination': destination,
            'details': details,
            'timestamp': datetime.now(),
            'type': 'inquiry'
        }
        
        inquiries.append(inquiry)
        flash('Your inquiry has been submitted successfully! Our team will contact you within 24 hours.', 'success')
        
    except Exception as e:
        flash('An error occurred while submitting your inquiry. Please try again.', 'error')
    
    return redirect(url_for('services'))

@app.route('/admin/submissions')
def view_submissions():
    # Simple admin view to see submissions (in a real app, this would be protected)
    all_submissions = form_submissions + inquiries
    all_submissions.sort(key=lambda x: x['timestamp'], reverse=True)
    return render_template('admin_submissions.html', submissions=all_submissions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
