# write_files.py
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SocialMedia - Login</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="auth-container">
        <div class="auth-box">
            <h1>SocialMedia</h1>
            <p class="subtitle">Connect with the world</p>
            <div class="tabs">
                <button class="tab active" onclick="showTab('login', event)">Login</button>
                <button class="tab" onclick="showTab('register', event)">Register</button>
            </div>
            <div id="login-form">
                <input type="text" id="login-username" placeholder="Username" />
                <input type="password" id="login-password" placeholder="Password" />
                <button class="btn-primary" onclick="login()">Login</button>
            </div>
            <div id="register-form" style="display:none">
                <input type="text" id="reg-username" placeholder="Username" />
                <input type="email" id="reg-email" placeholder="Email" />
                <input type="password" id="reg-password" placeholder="Password" />
                <button class="btn-primary" onclick="register()">Register</button>
            </div>
            <div id="auth-message"></div>
        </div>
    </div>
    <script src="/static/js/main.js"></script>
</body>
</html>"""

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
            <a href="/notifications">🔔 Notifications</a>
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
print("feed.html updated!")

profile_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Profile - SocialMedia</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar">
        <h1>SocialMedia</h1>
        <div class="nav-links">
            <a href="/feed">Feed</a>
            <button onclick="logout()">Logout</button>
        </div>
    </nav>
    <div class="feed-container">
        <h2>Profile Page</h2>
    </div>
    <script src="/static/js/main.js"></script>
</body>
</html>"""

with open('templates/index.html', 'w') as f:
    f.write(index_html)
print('index.html written!')

with open('templates/feed.html', 'w') as f:
    f.write(feed_html)
print('feed.html written!')

with open('templates/profile.html', 'w') as f:
    f.write(profile_html)
print('profile.html written!')

profile_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile - SocialMedia</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar">
        <h1>SocialMedia</h1>
        <div class="nav-links">
            <a href="/feed">Feed</a>
            <button onclick="logout()">Logout</button>
        </div>
    </nav>

    <div class="feed-container">
        <!-- Profile Card -->
        <div class="profile-card">
            <div class="profile-avatar" id="profile-avatar">S</div>
            <div class="profile-info">
                <h2 id="profile-username">Loading...</h2>
                <p id="profile-bio">No bio yet</p>
                <p id="profile-location"></p>
                <div class="profile-stats">
                    <div class="stat">
                        <span class="stat-number" id="posts-count">0</span>
                        <span class="stat-label">Posts</span>
                    </div>
                    <div class="stat">
                        <span class="stat-number" id="followers-count">0</span>
                        <span class="stat-label">Followers</span>
                    </div>
                    <div class="stat">
                        <span class="stat-number" id="following-count">0</span>
                        <span class="stat-label">Following</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Edit Profile -->
        <div class="create-post">
            <h3 style="margin-bottom:16px">Edit Profile</h3>
            <input type="text" id="edit-bio" placeholder="Bio" />
            <input type="text" id="edit-location" placeholder="Location" />
            <input type="url" id="edit-website" placeholder="Website" />
            <button class="btn-primary" onclick="updateProfile()">Save Changes</button>
            <div id="profile-message" style="margin-top:10px;color:green;"></div>
        </div>

        <!-- My Posts -->
        <h3 style="margin:16px 0">My Posts</h3>
        <div id="my-posts"></div>
    </div>

    <script src="/static/js/main.js"></script>
</body>
</html>"""

with open('templates/profile.html', 'w', encoding='utf-8') as f:
    f.write(profile_html)

print("profile.html written!")

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
            <h2>🔔 Notifications</h2>
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