# Deploying BharatMiles Global to Netlify

## Prerequisites
- A GitHub account
- A Netlify account
- Your Flask application code

## Deployment Steps

### 1. Push to GitHub
First, make sure your code is in a GitHub repository:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2. Deploy to Netlify

1. Go to [Netlify](https://netlify.com) and sign in
2. Click "New site from Git"
3. Choose GitHub as your Git provider
4. Select your repository
5. Configure the build settings:
   - Build command: `pip install -r requirements.txt`
   - Publish directory: `.`
6. Click "Deploy site"

### 3. Environment Variables (Optional)
If you need to set environment variables:
1. Go to Site settings > Environment variables
2. Add any required environment variables

### 4. Custom Domain (Optional)
1. Go to Site settings > Domain management
2. Add your custom domain

## Important Notes

- This Flask app uses SQLite for the database, which will be reset on each deployment
- For production use, consider using a proper database service
- The admin route `/admin/submissions` is not protected - add authentication for production

## Troubleshooting

If you encounter issues:
1. Check the build logs in Netlify
2. Ensure all dependencies are in `requirements.txt`
3. Verify Python version compatibility
4. Check that all static files are properly referenced

## Local Development

To run locally:
```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` to see your application. 