# GitHub Pages Setup Instructions

## 🚀 Quick Setup for The AI Paradox Report

Your repository is now configured for GitHub Pages! Follow these steps to publish it:

### Step 0: Verify Required Files

Before pushing to GitHub, ensure you have:

1. ✅ **Cover Image**: Located at `/report/ai-paradox-report-cover.jpg`
2. ✅ **PDF Report**: Located at `/report/The AI Paradox Report - David Orban.pdf`

### Step 1: Push to GitHub

If you haven't already created the repository on GitHub:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit: AI Paradox Report with GitHub Pages setup"

# Create repository on GitHub (using GitHub CLI)
gh repo create the-ai-paradox-report --public --source=. --remote=origin --push

# Or if manually created on GitHub, add remote and push:
git remote add origin https://github.com/davidorban/the-ai-paradox-report.git
git branch -M main
git push -u origin main
```

### Step 2: Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/davidorban/the-ai-paradox-report`
2. Click on **Settings** tab
3. Scroll down to **Pages** section (under "Code and automation")
4. Under **Source**, select:
   - **Deploy from a branch**
   - Branch: **main** (or master)
   - Folder: **/ (root)**
5. Click **Save**

### Step 3: Wait for Deployment

- GitHub will automatically start building your site
- First deployment may take up to 10 minutes
- Check the **Actions** tab to monitor the build progress
- Once complete, your site will be available at:
  
  **https://davidorban.github.io/the-ai-paradox-report**

### Step 4: Verify Your Site

Once deployed, you'll have:

- **Homepage**: Beautiful landing page with key findings and visualizations
- **Full Report**: Markdown report accessible at `/report/The-AI-Paradox-Report.md`
- **Interactive Charts**: 
  - Journey Map: `/visualizations/journey_map_interactive.html`
  - Paradox Quadrant: `/visualizations/paradox_quadrant_interactive.html`
  - Tension Web: `/visualizations/tension_web_interactive.html`
- **Data Access**: Anonymized survey data at `/data/survey_data_anonymized.md`
- **References**: Complete bibliography at `/report/references.md`

## 🎨 What's Included

### Files Created for GitHub Pages:

1. **`index.html`** - Professional landing page with:
   - Hero section with key findings
   - Statistics display (61% paradox, 7.0/10 concern, etc.)
   - Navigation cards to different sections
   - Embedded visualizations
   - Responsive design for mobile/desktop

2. **`_config.yml`** - Jekyll configuration for GitHub Pages:
   - Site metadata
   - Build settings
   - File exclusions (hides system files)

3. **`.nojekyll`** - Optional bypass for Jekyll processing

4. **`.github/workflows/deploy-pages.yml`** - Automated deployment workflow

## 🔧 Customization Options

### Update Site Content

Edit `index.html` to:
- Change colors (update the gradient in CSS)
- Modify text content
- Add new sections
- Update links

### Custom Domain (Optional)

To use a custom domain like `aiparadox.yourdomain.com`:

1. In GitHub Pages settings, add your custom domain
2. Create a `CNAME` file in root with your domain:
   ```
   aiparadox.yourdomain.com
   ```
3. Configure DNS records with your domain provider:
   - A records pointing to GitHub's IPs
   - CNAME record for www subdomain

### Alternative Deployment Options

**Option 1: Use docs folder**
- Move index.html to `/docs/`
- In Pages settings, select `/docs` as source folder

**Option 2: Use gh-pages branch**
- Create a separate branch for the site
- Push only site files to that branch
- Select `gh-pages` branch in settings

## 📊 Site Structure

```
https://davidorban.github.io/the-ai-paradox-report/
│
├── index.html                    # Landing page
├── report/
│   ├── The-AI-Paradox-Report.md # Full report
│   └── references.md            # Bibliography
├── visualizations/
│   ├── journey-map-final.png
│   ├── paradox-quadrant-final.png
│   ├── tension-web-final.png
│   └── [interactive HTML files]
├── data/
│   ├── survey_data_anonymized.md
│   └── survey_questions.md
└── src/
    └── [Python analysis scripts]
```

## 🚦 Troubleshooting

### Site Not Appearing?
- Check Actions tab for build errors
- Verify repository is public
- Ensure GitHub Pages is enabled in settings
- Wait 10 minutes for first deployment

### 404 Errors?
- Check file paths are correct
- Ensure files are committed and pushed
- Verify branch name matches Pages settings

### Images Not Loading?
- Use relative paths (e.g., `visualizations/image.png`)
- Check file extensions match exactly
- Ensure images are committed to repository

## 📈 Analytics (Optional)

Add Google Analytics or similar by inserting tracking code in `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 🎉 Success!

Once deployed, share your research with:
- Direct link: `https://davidorban.github.io/the-ai-paradox-report`
- Social media with preview cards (Open Graph tags included)
- Academic citations using the provided references

The site will automatically update whenever you push changes to the main branch!

---

For questions or issues, check the [GitHub Pages documentation](https://docs.github.com/en/pages) or open an issue in the repository.