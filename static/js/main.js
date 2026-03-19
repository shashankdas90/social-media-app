const API = window.location.origin + '/api';

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
    const username = document.getElementById('login-username').value.trim();
    const password = document.getElementById('login-password').value.trim();
    if (!username || !password) {
        document.getElementById('auth-message').textContent = 'Please fill in all fields!';
        return;
    }
    try {
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
            document.getElementById('auth-message').textContent = 'Invalid username or password!';
        }
    } catch(e) {
        document.getElementById('auth-message').textContent = 'Connection error! Make sure server is running.';
    }
}

async function register() {
    const username = document.getElementById('reg-username').value.trim();
    const email = document.getElementById('reg-email').value.trim();
    const password = document.getElementById('reg-password').value.trim();
    if (!username || !email || !password) {
        document.getElementById('auth-message').textContent = 'Please fill in all fields!';
        return;
    }
    try {
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
            const errors = Object.values(data).flat().join(', ');
            document.getElementById('auth-message').textContent = errors || 'Registration failed!';
        }
    } catch(e) {
        document.getElementById('auth-message').textContent = 'Connection error! Make sure server is running.';
    }
}

function logout() {
    fetch(API + '/users/logout/', {
        method: 'POST',
        headers: getHeaders()
    }).finally(() => {
        localStorage.clear();
        window.location.href = '/';
    });
}

async function loadFeed() {
    if (!getToken()) { window.location.href = '/'; return; }
    const username = localStorage.getItem('username');
    const navUser = document.getElementById('nav-username');
    if (navUser) navUser.textContent = username;
    const postAvatar = document.getElementById('post-avatar');
    if (postAvatar) postAvatar.textContent = username ? username[0].toUpperCase() : 'U';
    try {
        const res = await fetch(API + '/posts/', { headers: getHeaders() });
        const posts = await res.json();
        const feed = document.getElementById('posts-feed');
        feed.innerHTML = '';
        if (posts.length === 0) {
            feed.innerHTML = '<div class="no-notifications">No posts yet! Be the first to post.</div>';
            return;
        }
        posts.forEach(post => feed.innerHTML += renderPost(post));
    } catch(e) {
        console.error('Feed error:', e);
    }
}

function renderPost(post) {
    const initial = post.author[0].toUpperCase();
    const time = new Date(post.created_at).toLocaleDateString();
    const username = localStorage.getItem('username');
    const comments = post.comments.map(c =>
        '<div class="comment">' +
        '<div class="avatar" style="width:32px;height:32px;font-size:13px">' + c.author[0].toUpperCase() + '</div>' +
        '<div class="comment-content">' +
        '<span class="comment-author">' + c.author + '</span>' +
        (c.author !== username ? ' <button class="follow-btn-small" onclick="followUserByName(\'' + c.author + '\', this)">+ Follow</button>' : '') +
        '<p>' + c.content + '</p>' +
        '</div></div>'
    ).join('');

    return '<div class="post-card" id="post-' + post.id + '">' +
        '<div class="post-header">' +
        '<div class="avatar">' + initial + '</div>' +
        '<div style="flex:1">' +
        '<div class="post-author">' + post.author +
        (post.author !== username ? ' <button class="follow-btn-small" onclick="followUserByName(\'' + post.author + '\', this)">+ Follow</button>' : '') +
        '</div>' +
        '<div class="post-time">' + time + '</div>' +
        '</div></div>' +
        '<div class="post-content">' + post.content + '</div>' +
        (post.image ? '<img src="' + post.image + '" class="post-image" alt="post image"/>' : '') +
        '<div class="post-actions">' +
        '<button class="action-btn ' + (post.is_liked ? 'liked' : '') + '" onclick="likePost(' + post.id + ')">❤️ ' + (post.likes_count || 0) + '</button>' +
        '<button class="action-btn" onclick="toggleComments(' + post.id + ')">💬 ' + post.comments.length + '</button>' +
        (post.author === username ? '<button class="action-btn delete-btn" onclick="deletePost(' + post.id + ')">🗑️ Delete</button>' : '') +
        '</div>' +
        '<div class="comments-section" id="comments-' + post.id + '" style="display:none">' +
        '<div id="comments-list-' + post.id + '">' + comments + '</div>' +
        '<div class="add-comment">' +
        '<input type="text" id="comment-input-' + post.id + '" placeholder="Write a comment..." />' +
        '<button onclick="addComment(' + post.id + ')">Send</button>' +
        '</div></div></div>';
}

async function createPost() {
    const content = document.getElementById('post-content').value.trim();
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
    const content = input.value.trim();
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

async function deletePost(postId) {
    if (!confirm('Are you sure you want to delete this post?')) return;
    const res = await fetch(API + '/posts/' + postId + '/', {
        method: 'DELETE',
        headers: getHeaders()
    });
    if (res.status === 204) loadFeed();
}

async function previewImage(event) {
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
    const imageInput = document.getElementById('post-image');
    if (imageInput) imageInput.value = '';
    const container = document.getElementById('image-preview-container');
    if (container) container.style.display = 'none';
    const preview = document.getElementById('image-preview');
    if (preview) preview.src = '';
}

async function loadProfile() {
    if (!getToken()) { window.location.href = '/'; return; }
    try {
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
    } catch(e) {
        console.error('Profile error:', e);
    }
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
        setTimeout(() => document.getElementById('profile-message').textContent = '', 3000);
        loadProfile();
    }
}

function showModal(title, users) {
    document.getElementById('modal-title').textContent = title;
    const list = document.getElementById('modal-list');
    if (users.length === 0) {
        list.innerHTML = '<div style="padding:24px;text-align:center;color:#aaa;">No users yet!</div>';
    } else {
        list.innerHTML = users.map(u =>
            '<div class="modal-user-item">' +
            '<div class="avatar" style="width:40px;height:40px;font-size:16px">' + u[0].toUpperCase() + '</div>' +
            '<div class="modal-username">' + u + '</div>' +
            '</div>'
        ).join('');
    }
    document.getElementById('modal-overlay').classList.add('active');
}

function closeModal() {
    document.getElementById('modal-overlay').classList.remove('active');
}

async function showFollowers() {
    const res = await fetch(API + '/users/followers/', { headers: getHeaders() });
    const data = await res.json();
    showModal('Followers', data.followers || []);
}

async function showFollowing() {
    const res = await fetch(API + '/users/following/', { headers: getHeaders() });
    const data = await res.json();
    showModal('Following', data.following || []);
}

function showPosts() {
    document.getElementById('my-posts').scrollIntoView({ behavior: 'smooth' });
}

async function followUserByName(username, btn) {
    try {
        const searchRes = await fetch(API + '/users/search/?q=' + username, { headers: getHeaders() });
        const users = await searchRes.json();
        const user = users.find(u => u.username === username);
        if (user) {
            const res = await fetch(API + '/users/follow/' + user.id + '/', {
                method: 'POST',
                headers: getHeaders()
            });
            const data = await res.json();
            if (data.message && data.message.includes('Following')) {
                btn.textContent = '✓ Following';
                btn.classList.add('following');
            } else {
                btn.textContent = '+ Follow';
                btn.classList.remove('following');
            }
        }
    } catch(e) {
        console.error('Follow error:', e);
    }
}

let currentTab = 'users';

function switchTab(tab, event) {
    currentTab = tab;
    document.querySelectorAll('.search-tab').forEach(t => t.classList.remove('active'));
    event.target.classList.add('active');
    doSearch();
}

async function doSearch() {
    const query = document.getElementById('search-input').value.trim();
    const container = document.getElementById('search-results');
    if (!query) {
        container.innerHTML = '<div class="no-notifications">Type to search...</div>';
        return;
    }
    if (currentTab === 'users') {
        const res = await fetch(API + '/users/search/?q=' + query, { headers: getHeaders() });
        const users = await res.json();
        if (users.length === 0) {
            container.innerHTML = '<div class="no-notifications">No users found!</div>';
            return;
        }
        container.innerHTML = users.map(u =>
            '<div class="user-card">' +
            '<div class="avatar">' + u.username[0].toUpperCase() + '</div>' +
            '<div class="user-info"><div class="user-name">' + u.username + '</div></div>' +
            '<button class="follow-btn" onclick="followUser(' + u.id + ', this)">Follow</button>' +
            '</div>'
        ).join('');
    } else {
        const res = await fetch(API + '/posts/search/?q=' + query, { headers: getHeaders() });
        const posts = await res.json();
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
    if (data.message && data.message.includes('Following')) {
        btn.textContent = '✓ Following';
        btn.classList.add('following');
    } else {
        btn.textContent = 'Follow';
        btn.classList.remove('following');
    }
}

async function loadNotifications() {
    if (!getToken()) { window.location.href = '/'; return; }
    const res = await fetch(API + '/notifications/', { headers: getHeaders() });
    const notifications = await res.json();
    const container = document.getElementById('notifications-list');
    if (notifications.length === 0) {
        container.innerHTML = '<div class="no-notifications">No notifications yet!</div>';
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
        container.innerHTML +=
            '<div class="notification-card ' + (n.is_read ? 'read' : 'unread') + '" onclick="markRead(' + n.id + ', this)">' +
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

if (document.getElementById('posts-feed')) loadFeed();
if (document.getElementById('my-posts')) loadProfile();
if (document.getElementById('notifications-list')) loadNotifications();
if (document.getElementById('search-results')) {
    document.getElementById('search-results').innerHTML =
        '<div class="no-notifications">Type to search...</div>';
    document.getElementById('search-input').addEventListener('input', doSearch);
}
