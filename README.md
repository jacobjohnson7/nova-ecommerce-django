# NOVA — Modern Curated E-Commerce Platform

A dynamic, full-stack e-commerce web application inspired by the sleek design experience of the Apple Store. Built with Python and Django for the **Web Developer Intern – Technical Assignment (Task 2)**.

---

## 🌟 Key Features

### 1. Storefront Experience
- **Hero & Promotional Carousel:** Dynamic, database-driven hero banners with customizable copy, action buttons, and background themes.
- **Visual Category Showcase:** Interactive category grid with imagery and direct filtering.
- **Featured Collection:** Dynamic products pulled from the database with subtle hover elevations and direct view actions.
- **Product Catalog & Filtering:** Search by query keyword and filter by category with URL parameter persistence.
- **Product Details Page:** Comprehensive product overview with high-resolution visuals, pricing, detailed specifications, and category-based "You might also like" related recommendations.
- **Luxe Micro-Interactions:** Custom fluid floating-light cursor, ambient mesh aura lighting, and frosted-glass navigation.

### 2. User Authentication
- User Registration with form validation.
- User Login & Logout with secure session handling.
- Protected Account Dashboard (`@login_required`) showing member details and profile metadata.

### 3. Customized Admin Experience
- **NOVA Studio Admin Portal:** Custom-designed administration interface matching the brand aesthetic.
- **Real-Time KPI Dashboard:** Live counters for catalog items, categories, hero banners, and registered users.
- **Full Content Management (CRUD):**
  - Add, edit, disable, or delete Products.
  - Manage Product Categories with auto-generated slugs.
  - Configure, reorder, and activate/deactivate Hero Banners.
  - Manage users and staff permissions.

---

## 🛠️ Technology Stack

- **Backend:** Python, Django 6.0 (Django ORM, Authentication, Templates)
- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Bootstrap 5, Bootstrap Icons
- **Database:** SQLite3 (`db.sqlite3`)
- **Typography:** DM Sans & Manrope (Google Fonts)

---

## 📁 Project Structure

```text
ecomm/
├── manage.py                  # Django management script
├── db.sqlite3                 # SQLite database
├── ecomm/                     # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app/                       # Main application
│   ├── models.py              # Category, Product, Banner models
│   ├── views.py               # Storefront & account view logic
│   ├── urls.py                # App routing
│   ├── forms.py               # Registration & auth forms
│   └── admin.py               # Customized admin site & metrics
├── templates/                 # Django HTML templates
│   ├── base.html              # Base layout with navigation & cursor
│   ├── store/
│   │   ├── home.html          # Dynamic homepage
│   │   ├── products.html      # Catalog with search & filter
│   │   ├── product_detail.html# Product details & related items
│   │   ├── register.html      # User signup
│   │   └── account.html       # Protected user dashboard
│   ├── registration/
│   │   └── login.html         # User sign-in
│   └── admin/
│       ├── base_site.html     # Custom admin branding
│       ├── index.html         # Admin KPI stats dashboard
│       └── login.html         # Custom NOVA-styled admin login
└── static/                    # Static assets
    ├── css/
    │   ├── style.css          # NOVA storefront design system
    │   └── admin_custom.css   # Custom admin dashboard styles
    └── js/
        └── main.js            # Floating light cursor physics & UI
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+ installed
- Pip package manager

### 2. Run Database Migrations
Ensure all database migrations are applied:
```powershell
python manage.py migrate
```

### 3. Start the Development Server
```powershell
python manage.py runserver
```

Open your browser and navigate to:
- **Storefront:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Product Catalog:** [http://127.0.0.1:8000/products/](http://127.0.0.1:8000/products/)
- **Admin Portal:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔐 Credentials for Evaluation

| Role | Username | Password | Access Area |
| :--- | :--- | :--- | :--- |
| **Superuser / Admin** | `admin` | `admin123` | Full access to `/admin/` portal |
| **Test Customer** | `intern_tester` | `Tester@123` | User account dashboard at `/account/` |

---

## 📋 Evaluation Checklist Reference (Assignment Task 2)

- [x] Homepage with Navigation, Hero Banner, Categories, Featured Products & Footer
- [x] Dynamic Banner Management (Add, Edit, Delete, Toggle Active, Reorder)
- [x] Product Management (Add, Edit, Delete, Categories, Images, Prices)
- [x] Product Details Page (Specs, Imagery, Pricing, Related Products)
- [x] User Authentication (Register, Login, Logout, Protected Account)
- [x] Admin Panel for Products, Categories, Banners, and Users
- [x] SQLite Database with properly configured migrations
- [x] Responsive layout for Desktop, Tablet, and Mobile devices
