# Vehicle Type Classification System – UI

A modern, responsive web application for vehicle type classification using YOLOv8 deep learning model. Features a clean, card-based design with soft blue & white theme.

## 📋 Project Overview

This UI system provides a complete workflow for:
- User authentication and login
- Vehicle image/video upload
- Real-time vehicle detection and classification
- Detailed analysis with confidence scores
- Comprehensive reporting

## 🎨 Features

### Design
- ✨ Modern, soft blue & white theme
- 🎯 Card-based layout with rounded corners
- 📱 Fully responsive (desktop, tablet, mobile)
- ⚡ Smooth animations and hover effects
- 🎪 Professional gradients and shadows

### Functionality
- 🔐 Login system with localStorage persistence
- 📤 Drag & drop file upload interface
- 🖼️ Image and video upload tabs
- 📊 Real-time detection results
- 📈 Detailed analysis and statistics
- 🏷️ Vehicle class detection (Cars, Buses, Trucks, Motorcycles)
- 📉 Confidence score visualization

## 📁 Project Structure

```
vehicle_type_ui/
├── index.html          # Home/Landing page
├── login.html          # Login page
├── dashboard.html      # Dashboard with tabs
├── upload.html         # File upload page
├── output.html         # Detection results page
├── analysis.html       # Detailed analysis page
├── styles.css          # Global styles
└── script.js           # JavaScript utilities
```

## 🎯 Page Descriptions

### 1. **Home Page** (`index.html`)
- Landing page with project introduction
- Quick start buttons (Login / Start Classification)
- Feature highlights
- Gradient background

### 2. **Login Page** (`login.html`)
- Simple authentication form
- Username and password fields
- Demo credentials (any username/password works)
- Back to home button

### 3. **Dashboard** (`dashboard.html`)
- Tabbed interface (Image Upload / Video Upload)
- Supported classes and formats display
- Quick start buttons
- Pro tips section
- User session management

### 4. **Upload Page** (`upload.html`)
- Drag & drop upload area
- File browsing functionality
- File preview with size information
- Processing information
- Run detection button

### 5. **Output Page** (`output.html`)
- Detection results display
- Vehicle count summary with icons
- Detailed confidence table with progress bars
- Statistics panel
- Navigation to analysis page

### 6. **Analysis Page** (`analysis.html`)
- Comprehensive detection analytics
- File information display
- Class distribution charts
- Individual detection confidence table
- Export options (PDF, CSV)
- Performance metrics

## 🎨 Color Palette

| Purpose | Color | Hex |
|---------|-------|-----|
| Primary Blue | ![#3B82F6](https://via.placeholder.com/20/3B82F6/3B82F6) | `#3B82F6` |
| Secondary Blue | ![#60A5FA](https://via.placeholder.com/20/60A5FA/60A5FA) | `#60A5FA` |
| Light Background | ![#F8FAFF](https://via.placeholder.com/20/F8FAFF/F8FAFF) | `#F8FAFF` |
| Card Background | ![#FFFFFF](https://via.placeholder.com/20/FFFFFF/FFFFFF) | `#FFFFFF` |
| Button Yellow | ![#FACC15](https://via.placeholder.com/20/FACC15/FACC15) | `#FACC15` |
| Text Dark | ![#1F2937](https://via.placeholder.com/20/1F2937/1F2937) | `#1F2937` |
| Text Light | ![#6B7280](https://via.placeholder.com/20/6B7280/6B7280) | `#6B7280` |
| Border Color | ![#E5E7EB](https://via.placeholder.com/20/E5E7EB/E5E7EB) | `#E5E7EB` |
| Success Green | ![#22C55E](https://via.placeholder.com/20/22C55E/22C55E) | `#22C55E` |

## 🚀 Getting Started

### Quick Start

1. **Extract the project files** to your desired location
2. **Open `index.html`** in a web browser
3. **Click "Start Classification"** or **"Login"** to begin
4. **Demo credentials**: Use any username and password

### Browser Compatibility

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🎮 Navigation

All pages are interconnected with intuitive navigation:

| From | To | Via Button |
|------|----|----|
| Home | Login | "Login" button |
| Home | Dashboard | "Start Classification" button |
| Login | Dashboard | "Login" button |
| Dashboard | Upload | "Start Classification" button |
| Upload | Output | "Run Detection" button |
| Output | Analysis | "View Analysis" button |
| Any page | Home | Logo or "Back" button |

## 🛠️ Keyboard Shortcuts

- `Ctrl/Cmd + H` - Go to home page
- `Escape` - Go to dashboard

## 💾 Local Storage

The application uses browser localStorage to:
- Store username after login
- Persist user preferences
- Track uploaded file information
- Save theme preference (light/dark mode - optional)

## 📊 Supported Classes

- 🚗 **Cars** - Passenger vehicles
- 🚌 **Buses** - Public transport buses
- 🚚 **Trucks** - Commercial trucks
- 🏍️ **Motorcycles** - Two/three-wheeled vehicles

## 📁 Supported Formats

### Images
- JPG / JPEG
- PNG
- WEBP

### Videos
- MP4
- AVI
- MOV

## 🎯 Detection Model

- **Model**: YOLOv8 (You Only Look Once v8)
- **Purpose**: Real-time vehicle detection and classification
- **Outputs**: Bounding boxes, class labels, confidence scores

## 🎨 CSS Classes Reference

### Layout
- `.container` - Max-width container (1200px)
- `.center-card` - Center card layout
- `.card` - Main card component
- `.card-wrapper` - Card wrapper (max 500px)
- `.gradient-bg` - Gradient background

### Buttons
- `.primary` - Primary blue button
- `.secondary` - Secondary yellow button
- `.tertiary` - Transparent button
- `.success` - Success green button

### Components
- `.upload-box` - Dashed upload area
- `.badge` - Info badge
- `.stats-panel` - Statistics grid
- `.confidence-table` - Results table
- `.progress-bar` - Progress indicator

### Utilities
- `.grid` - Auto-fit grid (300px min)
- `.grid-2` - 2-column grid
- `.button-group` - Flex button group
- `.icon-heading` - Icon with text heading

## 🔧 JavaScript Functions

### Navigation
```javascript
navigate('page.html') // Navigate to page
```

### Utilities
```javascript
formatFileSize(bytes)           // Format file size
getCurrentTimestamp()            // Get current timestamp
validateEmail(email)             // Validate email
getUrlParam(param)              // Get URL parameter
storeData(key, value)           // Store in localStorage
retrieveData(key)               // Get from localStorage
```

### Notifications
```javascript
showToast(message, type, duration)  // Show toast notification
showModal(title, message, onConfirm, onCancel) // Show modal dialog
```

### UI State
```javascript
setButtonLoading(button, text)   // Add loading state
removeButtonLoading(button)      // Remove loading state
toggleDarkMode()                 // Toggle dark/light mode
```

## 🎬 Adding Features

### Dark Mode
Dark mode CSS can be added by creating a `:root[data-theme="dark"]` selector set

### Backend Integration
Replace mock data in output.html and analysis.html with actual API calls:
```javascript
fetch('/api/classify', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => { /* process results */ })
```

### File Upload
Currently shows drag-and-drop UI. Connect to backend:
```javascript
const formData = new FormData();
formData.append('file', selectedFile);
// Send to backend API
```

## 📱 Responsive Breakpoints

- **Desktop**: 1200px+ (full featured)
- **Tablet**: 768px - 1199px (optimized grid)
- **Mobile**: < 768px (single column, full width)

## 🎨 Customization

### Change Colors
Edit the color values in `styles.css`:
```css
--primary-blue: #3B82F6;
--secondary-blue: #60A5FA;
/* ... etc ... */
```

### Modify Typography
Update font family and sizes in `body` and heading selectors

### Add New Pages
1. Create new HTML file
2. Include `styles.css` and `script.js`
3. Use `navigate()` function for links
4. Follow the card-based layout pattern

## ⚡ Performance Optimization

- CSS is minified and optimized
- JavaScript uses debouncing for event handlers
- Smooth animations use CSS transitions
- Images use lazy loading attributes
- Responsive grid prevents horizontal scroll

## 📞 Support

For issues or questions about the UI:
1. Check browser console for errors (F12)
2. Verify all files are in the same directory
3. Clear browser cache and reload
4. Test in a different browser

## 📄 License

This UI template is provided as-is for the Vehicle Type Classification System project.

## 🎯 Next Steps

1. **Backend Integration**: Connect to actual YOLOv8 API
2. **Database Setup**: Store user accounts and detection history
3. **Real File Upload**: Implement actual file upload to server
4. **Result Storage**: Save detection results to database
5. **User Dashboard**: Show upload history and statistics
6. **Export Features**: Generate downloadable reports

---

**Created**: 2026-01-24
**Technology**: HTML5, CSS3, Vanilla JavaScript
**Design Pattern**: Card-based, responsive, modern
