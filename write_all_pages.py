# ===== FEED PAGE =====
feed = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feed - SocialMedia</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar">
        '<h1 onclick="window.location.href=\'/feed\'">SocialMedia</h1>'
        <div class="nav-links">
            <span id="nav-username"></span>
            <a href="/search">🔍 Search</a>
            <a href="/notifications">🔔 Notifications</a>
            <a href="/profile">👤 Profile</a>
            <button onclick="logout()">Logout</button>
        </div>
    </nav>
    <div class="feed-container">
        <div class="create-post">
            <div class="create-post-header">
                <div class="avatar" id="post-avatar">U</div>
                <textarea id="post-content" placeholder="What's on your mind?"></textarea>
            </div>
            <div class="image-preview-container" id="image-preview-container" style="display:none">
                <img id="image-preview" src="" alt="preview" />
                <button class="remove-image-btn" onclick="removeImage()">✕</button>
            </div>
            <div class="create-post-footer">
                <label class="image-upload-btn" for="post-image">📸 Photo</label>
                <input type="file" id="post-image" accept="image/*" onchange="previewImage(event)" style="display:none"/>
                <button class="btn-primary post-btn" onclick="createPost()">🚀 Post</button>
            </div>
        </div>
        <div id="posts-feed"></div>
    </div>
    <script src="/static/js/main.js"></script>
</body>
</html>"""

with open('templates/feed.html', 'w', encoding='utf-8') as f:
    f.write(feed)
print("feed.html updated!")

# ===== PROFILE PAGE =====
profile = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile - SocialMedia</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar">
        <h1 onclick="window.location.href='/feed'">SocialMedia</h1>
        <div class="nav-links">
            <a href="/feed">🏠 Feed</a>
            <a href="/notifications">🔔 Notifications</a>
            <button onclick="logout()">Logout</button>
        </div>
    </nav>

    <!-- Modal -->
    <div id="modal-overlay" class="modal-overlay" onclick="closeModal()">
        <div class="modal-box" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 id="modal-title">Users</h3>
                <button class="modal-close" onclick="closeModal()">✕</button>
            </div>
            <div id="modal-list"></div>
        </div>
    </div>

    <div class="feed-container">
        <div class="profile-card">
            <div class="profile-avatar" id="profile-avatar">U</div>
            <div class="profile-info">
                <h2 id="profile-username">Loading...</h2>
                <p id="profile-bio">No bio yet</p>
                <p id="profile-location"></p>
                <p id="profile-website"></p>
                <div class="profile-stats">
                    <div class="stat" onclick="showPosts()">
                        <span class="stat-number" id="posts-count">0</span>
                        <span class="stat-label">POSTS</span>
                    </div>
                    <div class="stat clickable" onclick="showFollowers()">
                        <span class="stat-number" id="followers-count">0</span>
                        <span class="stat-label">FOLLOWERS</span>
                    </div>
                    <div class="stat clickable" onclick="showFollowing()">
                        <span class="stat-number" id="following-count">0</span>
                        <span class="stat-label">FOLLOWING</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="edit-profile-card">
            <h3>✏️ Edit Profile</h3>
            <input type="text" id="edit-bio" placeholder="Write your bio..." />
            <input type="text" id="edit-location" placeholder="📍 Location" />
            <input type="url" id="edit-website" placeholder="🌐 Website" />
            <button class="btn-primary" onclick="updateProfile()">💾 Save Changes</button>
            <div id="profile-message"></div>
        </div>
        <div class="my-posts-header">
            <h3>📝 My Posts</h3>
        </div>
        <div id="my-posts"></div>
    </div>
    <script src="/static/js/main.js"></script>
</body>
</html>"""

with open('templates/profile.html', 'w', encoding='utf-8') as f:
    f.write(profile)
print("profile.html updated!")

# ===== NOTIFICATIONS PAGE =====
notifications = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notifications - SocialMedia</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar">
        <h1 onclick="window.location.href='/feed'">SocialMedia</h1>
        <div class="nav-links">
            <a href="/feed">🏠 Feed</a>
            <a href="/profile">👤 Profile</a>
            <a href="/search">🔍 Search</a>
            <button onclick="logout()">Logout</button>
        </div>
    </nav>
    <div class="feed-container">
        <div class="notifications-header">
            <h2>🔔 Notifications</h2>
            <button class="mark-all-btn" onclick="markAllRead()">✅ Mark all as read</button>
        </div>
        <div id="notifications-list"></div>
    </div>
    <script src="/static/js/main.js"></script>
</body>
</html>"""

with open('templates/feed.html', 'w', encoding='utf-8') as f:
    f.write(feed)
print("feed.html written!")

with open('templates/profile.html', 'w', encoding='utf-8') as f:
    f.write(profile)
print("profile.html written!")

with open('templates/notifications.html', 'w', encoding='utf-8') as f:
    f.write(notifications)
print("notifications.html written!")