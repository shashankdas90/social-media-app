notifications_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notifications - SocialMedia</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar">
        <h1>SocialMedia</h1>
        <div class="nav-links">
            <a href="/feed">Feed</a>
            <a href="/profile">Profile</a>
            <button onclick="logout()">Logout</button>
        </div>
    </nav>
    <div class="feed-container">
        <div class="notifications-header">
            <h2>Notifications</h2>
            <button class="mark-all-btn" onclick="markAllRead()">Mark all as read</button>
        </div>
        <div id="notifications-list"></div>
    </div>
    <script src="/static/js/main.js"></script>
</body>
</html>"""

with open('templates/notifications.html', 'w', encoding='utf-8') as f:
    f.write(notifications_html)

print("notifications.html written!")