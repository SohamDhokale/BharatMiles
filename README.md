# BharatMiles Global Export Website

## Overview

This is a Flask-based corporate website for BharatMiles Global, an Indian export company specializing in connecting Indian products to global markets. The application serves as a company showcase and lead generation platform with a focus on agricultural products and international trade services.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default templating engine)
- **CSS Framework**: Bootstrap 5.3.0 for responsive design
- **Icons**: Font Awesome 6.4.0 for consistent iconography
- **Fonts**: Google Fonts (Inter & Poppins) for modern typography
- **Styling**: Custom CSS with CSS variables for theme consistency
- **JavaScript**: Vanilla JavaScript for interactive components

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Session Management**: Flask's built-in session handling with secret key
- **Data Storage**: PostgreSQL database with proper table structure
- **Form Handling**: Flask's request object for form data processing
- **Flash Messages**: Flask's flash messaging system for user feedback
- **Models**: ContactSubmission and ExportInquiry models for form data

### Template Structure
- **Base Template**: `base.html` provides common layout and navigation
- **Page Templates**: Individual templates extend the base template
- **Responsive Design**: Mobile-first approach with Bootstrap grid system

## Key Components

### 1. Application Core (`app.py`)
- Flask application initialization and configuration
- Route definitions for all pages (index, about, services, contact)
- Form submission handling with basic validation
- In-memory data storage for contact submissions

### 2. Static Assets
- **CSS**: Custom styling with dark theme and orange/red color scheme
- **JavaScript**: Interactive components including navbar, animations, and form handling

### 3. Templates
- **Base Layout**: Common navigation, footer, and meta tags
- **Landing Page**: Hero section with company introduction
- **About Page**: Company story and background information
- **Services Page**: Export services and product categories
- **Contact Page**: Contact form and company information

### 4. Form Processing
- Contact form submission with validation
- Data collection for lead generation
- Flash messaging for user feedback

## Data Flow

1. **User Navigation**: Users access different pages through the navigation menu
2. **Form Submission**: Contact forms are submitted via POST requests
3. **Data Processing**: Form data is validated and stored in memory
4. **User Feedback**: Flash messages provide submission confirmation
5. **Data Storage**: Submissions are stored in Python lists (temporary storage)

## External Dependencies

### Frontend Dependencies (CDN)
- **Bootstrap 5.3.0**: CSS framework for responsive design
- **Font Awesome 6.4.0**: Icon library for visual elements
- **Google Fonts**: Inter and Poppins font families

### Backend Dependencies
- **Flask**: Core web framework
- **Python Standard Library**: datetime, os modules

### Environment Variables
- `SESSION_SECRET`: Flask session security key (optional, defaults to hardcoded value)

## Deployment Strategy

### Current Setup
- **Entry Point**: `main.py` runs the Flask development server
- **Host Configuration**: Configured to run on `0.0.0.0:5000`
- **Debug Mode**: Enabled for development

### Production Considerations
- **Database Migration**: Current in-memory storage needs to be replaced with persistent storage
- **Environment Configuration**: Production environment variables should be properly configured
- **Static File Serving**: Production deployment should use proper static file serving
- **Security**: Session secret should be generated randomly and stored securely

### Recommended Production Stack
- **Database**: PostgreSQL with appropriate ORM (SQLAlchemy recommended)
- **Web Server**: Gunicorn or uWSGI
- **Reverse Proxy**: Nginx for static file serving and load balancing
- **Hosting**: Cloud platforms like Heroku, DigitalOcean, or AWS

## Development Notes

### Database Schema
- **contact_submissions**: Stores contact form submissions with fields for name, email, phone, company, message, timestamp, and read status
- **export_inquiries**: Stores export inquiry forms with fields for name, email, company, product category, quantity, destination country, additional details, timestamp, read status, and processing status

### Current Features
1. **Data Persistence**: PostgreSQL database ensures data survives server restarts
2. **Form Processing**: Complete form handling with validation and error messages
3. **Admin Interface**: Basic admin panel to view all form submissions at /admin/submissions
4. **Database Models**: Proper SQLAlchemy models with relationships and constraints
5. **Professional Design**: Dark theme with orange/red color scheme, animations, and responsive layout

### Recommended Enhancements
1. **Admin Authentication**: Add login system for admin panel security
2. **Email Integration**: Implement email notifications for form submissions
3. **Enhanced Validation**: Add comprehensive form validation and sanitization
4. **Export Functionality**: Add CSV/Excel export for submission data
5. **Analytics**: Integrate tracking for business insights
6. **SEO Optimization**: Add meta tags, structured data, and SEO enhancements# BharatMiles-Global
