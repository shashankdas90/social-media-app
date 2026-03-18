js = """const API = 'http://127.0.0.1:8000/api';

function getToken() {
    return localStorage.getItem('token');
}

function getHeaders() {
    return {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + getToken()
    };
}

function showTab(tab, event) {
    document.getElementById('login-form').style.display = tab === 'login' ? 'block' : 'none';
    document.getElementById('register-form').style.display = tab === 'register' ? 'block' : 'none';
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    event.target.classList.add('active');
}

async function login() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    const res = await fetch(API + '/users/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    const data = await res.json();
    if (res.ok) {
        localStorage.setItem('token', data.token);
        localStorage.setItem('username', data.username);
        window.location.href = '/feed';
    } else {
        document.getElementById('auth-message').textContent = 'Invalid credentials!';
    }
}

async function register() {
    const username = document.getElementById('reg-username').value;
    const email = document.getElementById('reg-email').value;
    const password = document.getElementById('reg-password').value;
    const res = await fetch(API + '/users/register/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, email, password })
    });
    const data = await res.json();
    if (res.ok) {
        localStorage.setItem('token', data.token);
        localStorage.setItem('username', data.username);
        window.location.href = '/feed';
    } else {
        document.getElementById('auth-message').textContent = 'Registration failed!';
    }
}

function logout() {
    fetch(API + '/users/logout/', {
        method: 'POST',
        headers: getHeaders()
    });
    localStorage.clear();
    window.location.href = '/';
}

async function loadFeed() {
    if (!getToken()) { window.location.href = '/'; return; }
    document.getElementById('nav-username').textContent = localStorage.getItem('username');
    const res = await fetch(API + '/posts/', { headers: getHeaders() });
    const posts = await res.json();
    const feed = document.getElementById('posts-feed');
    feed.innerHTML = '';
    posts.forEach(post => feed.innerHTML += renderPost(post));
}

function renderPost(post) {
    const initial = post.author[0].toUpperCase();
    const time = new Date(post.created_at).toLocaleDateString();
    const comments = post.comments.map(c =>
        '<div class="comment">' +
        '<div class="avatar" style="width:32px;height:32px;font-size:13px">' + c.author[0].toUpperCase() + '</div>' +
        '<div class="comment-content">' +
        '<span class="comment-author">' + c.author + '</span>' +
        '<p>' + c.content + '</p>' +
        '</div></div>'
    ).join('');

    return '<div class="post-card" id="post-' + post.id + '">' +
        '<div class="post-header">' +
        '<div class="avatar">' + initial + '</div>' +
        '<div class="post-author">' + post.author +
        (post.author !== localStorage.getItem("username") ?
        '<button class="follow-btn-small" onclick="followUser(' + post.author + ', this)">+ Follow</button>' : '') +
        '</div>' +
        '<div class="post-time">' + time + '</div></div></div>' +
        '<div class="post-content">' + post.content + '</div>' +
        (post.image ? '<img src="' + post.image + '" class="post-image" alt="post image"/>' : '') +
        '<div class="post-actions">' +
        '<button class="action-btn ' + (post.is_liked ? 'liked' : '') + '" onclick="likePost(' + post.id + ')">❤️ ' + (post.likes_count || 0) + '</button>' +
        '<button class="action-btn" onclick="toggleComments(' + post.id + ')">💬 ' + post.comments.length + '</button>' +
        (post.author === localStorage.getItem("username") ? '<button class="action-btn delete-btn" onclick="deletePost(' + post.id + ')">🗑️ Delete</button>' : '') +
        '</div>' +
        '<div class="comments-section" id="comments-' + post.id + '" style="display:none">' +
        '<div id="comments-list-' + post.id + '">' + comments + '</div>' +
        '<div class="add-comment">' +
        '<input type="text" id="comment-input-' + post.id + '" placeholder="Write a comment..." />' +
        '<button onclick="addComment(' + post.id + ')">Send</button>' +
        '</div></div></div>';
}

async function createPost() {
    const content = document.getElementById('post-content').value;
    if (!content) return;
    const imageInput = document.getElementById('post-image');
    if (imageInput && imageInput.files[0]) {
        const formData = new FormData();
        formData.append('content', content);
        formData.append('image', imageInput.files[0]);
        const res = await fetch(API + '/posts/', {
            method: 'POST',
            headers: { 'Authorization': 'Token ' + getToken() },
            body: formData
        });
        if (res.ok) {
            document.getElementById('post-content').value = '';
            removeImage();
            loadFeed();
        }
    } else {
        const res = await fetch(API + '/posts/', {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify({ content })
        });
        if (res.ok) {
            document.getElementById('post-content').value = '';
            loadFeed();
        }
    }
}

async function likePost(postId) {
    const res = await fetch(API + '/posts/' + postId + '/like/', {
        method: 'POST',
        headers: getHeaders()
    });
    if (res.ok) loadFeed();
}

function toggleComments(postId) {
    const section = document.getElementById('comments-' + postId);
    section.style.display = section.style.display === 'none' ? 'block' : 'none';
}

async function addComment(postId) {
    const input = document.getElementById('comment-input-' + postId);
    const content = input.value;
    if (!content) return;
    const res = await fetch(API + '/posts/' + postId + '/comment/', {
        method: 'POST',
        headers: getHeaders(),
        body: JSON.stringify({ content })
    });
    if (res.ok) {
        input.value = '';
        loadFeed();
    }
}

if (document.getElementById('posts-feed')) loadFeed();
"""

with open('static/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("JS written successfully!")

js += """
async function loadProfile() {
    if (!getToken()) { window.location.href = '/'; return; }
    const res = await fetch(API + '/users/profile/', { headers: getHeaders() });
    const data = await res.json();
    document.getElementById('profile-username').textContent = data.username;
    document.getElementById('profile-avatar').textContent = data.username[0].toUpperCase();
    document.getElementById('profile-bio').textContent = data.bio || 'No bio yet';
    document.getElementById('profile-location').textContent = data.location || '';
    document.getElementById('edit-bio').value = data.bio || '';
    document.getElementById('edit-location').value = data.location || '';
    document.getElementById('edit-website').value = data.website || '';
    document.getElementById('followers-count').textContent = data.followers_count || 0;
    document.getElementById('following-count').textContent = data.following_count || 0;
    loadMyPosts();
}

async function loadMyPosts() {
    const res = await fetch(API + '/posts/', { headers: getHeaders() });
    const posts = await res.json();
    const username = localStorage.getItem('username');
    const myPosts = posts.filter(p => p.author === username);
    document.getElementById('posts-count').textContent = myPosts.length;
    const container = document.getElementById('my-posts');
    container.innerHTML = '';
    myPosts.forEach(post => container.innerHTML += renderPost(post));
}

async function updateProfile() {
    const bio = document.getElementById('edit-bio').value;
    const location = document.getElementById('edit-location').value;
    const website = document.getElementById('edit-website').value;
    const res = await fetch(API + '/users/profile/', {
        method: 'PUT',
        headers: getHeaders(),
        body: JSON.stringify({ bio, location, website })
    });
    if (res.ok) {
        document.getElementById('profile-message').textContent = 'Profile updated successfully!';
        loadProfile();
    }
}

if (document.getElementById('my-posts')) loadProfile();
"""

with open('static/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("JS written successfully!")

js += """
async function loadNotifications() {
    if (!getToken()) { window.location.href = '/'; return; }
    const res = await fetch(API + '/notifications/', { headers: getHeaders() });
    const notifications = await res.json();
    const container = document.getElementById('notifications-list');
    
    if (notifications.length === 0) {
        container.innerHTML = '<div class="no-notifications">No notifications yet! 🎉</div>';
        return;
    }
    
    container.innerHTML = '';
    notifications.forEach(n => {
        const icon = n.notification_type === 'like' ? '❤️' : 
                     n.notification_type === 'comment' ? '💬' : '👥';
        const message = n.notification_type === 'like' ? 'liked your post' :
                        n.notification_type === 'comment' ? 'commented on your post' :
                        'started following you';
        const time = new Date(n.created_at).toLocaleDateString();
        const statusClass = n.is_read ? 'read' : 'unread';
        
        container.innerHTML += 
            '<div class="notification-card ' + statusClass + '" onclick="markRead(' + n.id + ', this)">' +
            '<div class="notification-icon">' + icon + '</div>' +
            '<div class="notification-text">' +
            '<strong>' + n.sender + '</strong> ' + message +
            '<div class="notification-time">' + time + '</div>' +
            '</div></div>';
    });
}

async function markRead(id, el) {
    await fetch(API + '/notifications/' + id + '/read/', {
        method: 'PUT',
        headers: getHeaders()
    });
    el.classList.remove('unread');
    el.classList.add('read');
}

async function markAllRead() {
    await fetch(API + '/notifications/read-all/', {
        method: 'PUT',
        headers: getHeaders()
    });
    document.querySelectorAll('.notification-card').forEach(card => {
        card.classList.remove('unread');
        card.classList.add('read');
    });
}

if (document.getElementById('notifications-list')) loadNotifications();
"""
js += """
async function deletePost(postId) {
    if (!confirm('Are you sure you want to delete this post?')) return;
    const res = await fetch(API + '/posts/' + postId + '/', {
        method: 'DELETE',
        headers: getHeaders()
    });
    if (res.ok) loadFeed();
}
"""

js += """
let searchTab = 'users';

function switchTab(tab, btn) {
    searchTab = tab;
    document.querySelectorAll('.search-tab').forEach(t => t.classList.remove('active'));
    btn.classList.add('active');
    handleSearch();
}

async function handleSearch() {
    const query = document.getElementById('search-input').value;
    if (!query) {
        document.getElementById('search-results').innerHTML = '';
        return;
    }
    if (searchTab === 'users') {
        const res = await fetch(API + '/users/search/?q=' + query, { headers: getHeaders() });
        const users = await res.json();
        const container = document.getElementById('search-results');
        if (users.length === 0) {
            container.innerHTML = '<div class="no-notifications">No users found!</div>';
            return;
        }
        container.innerHTML = users.map(u =>
            '<div class="user-card">' +
            '<div class="avatar">' + u.username[0].toUpperCase() + '</div>' +
            '<div class="user-info">' +
            '<strong>' + u.username + '</strong>' +
            '</div>' +
            '<button class="follow-btn" onclick="followUser(' + u.id + ', this)">Follow</button>' +
            '</div>'
        ).join('');
    } else {
        const res = await fetch(API + '/posts/search/?q=' + query, { headers: getHeaders() });
        const posts = await res.json();
        const container = document.getElementById('search-results');
        if (posts.length === 0) {
            container.innerHTML = '<div class="no-notifications">No posts found!</div>';
            return;
        }
        container.innerHTML = '';
        posts.forEach(post => container.innerHTML += renderPost(post));
    }
}

async function followUser(userId, btn) {
    const res = await fetch(API + '/users/follow/' + userId + '/', {
        method: 'POST',
        headers: getHeaders()
    });
    const data = await res.json();
    if (res.ok) {
        btn.textContent = data.message.includes('Following') ? 'Unfollow' : 'Follow';
        btn.classList.toggle('following');
    }
}

if (document.getElementById('search-results')) handleSearch();
"""
js += """
function previewImage(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('image-preview').src = e.target.result;
            document.getElementById('image-preview-container').style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
}

function removeImage() {
    document.getElementById('post-image').value = '';
    document.getElementById('image-preview-container').style.display = 'none';
    document.getElementById('image-preview').src = '';
}
"""
with open('static/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("JS written successfully!")