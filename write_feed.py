feed_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feed - SocialMedia</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar">
        <h1>SocialMedia</h1>
        <div class="nav-links">
            <span id="nav-username"></span>
            <a href="/notifications">Notifications</a>
            <a href="/profile">Profile</a>
            <button onclick="logout()">Logout</button>
        </div>
    </nav>
    <div class="feed-container">
        <div class="create-post">
            <textarea id="post-content" placeholder="What's on your mind?"></textarea>
            <button class="btn-primary" onclick="createPost()">Post</button>
        </div>
        <div id="posts-feed"></div>
    </div>
    <script src="/static/js/main.js"></script>
</body>
</html>"""

with open('templates/feed.html', 'w', encoding='utf-8') as f:
    f.write(feed_html)

print("feed.html written!")