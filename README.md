# brokebook2
 (django) campus-wide textbook sharing
## Current features
### 1. Textbook database
- sqlite3 database (may switch to MySQL)
- Users can create Book posts
- Full access to CRUD operations in admin page
- TODO: Add CAPTCHA verification, strengthen server-side validation
### 2. Search
- Using Django's QuerySet API to provide filtered results by class/prof/title, sorted by most recent
- TODO: Add sorting options, advanced search
- TODO: Utilize full-text search? Debating whether this is necessary
### 3. Web frontend
- Bootstrap CSS for clean look
- Organized through tables and cards
- TODO: fix homepage
