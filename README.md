# brokebook2
 (django) campus-wide textbook sharing
## Roadmap: What is needed
### 1. Textbook database
- MySQL
- Only the needed categories: title, ed., class name, campus, prof, semester,
- Can handle lots of reading/writing from web frontend
  - users posting/searching, live updates, post deletion
  - should handle 1000s of users during peak traffic
### 2. Fast, accurate search
- Use book properties to generate highly narrow, accurate results
- Turn search query into a user post
### 3. Web frontend
- Nothing fancy, Craigslist-like
- mobile-friendly
- fast and makes sense
  - HTML-only preferred, or at least an option (eg. Gmail)
  - HTML-like simplicity that can translate well to mobile/tablet
