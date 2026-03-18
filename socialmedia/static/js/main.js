const API = 'http://127.0.0.1:8000/api';

function getToken() {
    return localStorage.getItem('token');
}

function getHeaders() {
    return {
        'Content-Type': 'application/json',
        'Authorization': `Token ${getToken()}`
    };
}

// ===== AUTH =====
function showTab(tab, event) {
    document.getElementById('login-form').style.display = tab === 'login' ? 'block' : 'none';
    document.getElementById('register-form').style.display = tab === 'register' ? 'block' : 'none';
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    event.target.classList.add('active');
}

async function login() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    const res = await fetch(`${API}/users/login/`, {
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
    const res = await fetch(`${API}/users/register/`, {
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
    fetch(`${API}/users/logout/`, {
        method: 'POST',
        headers: getHeaders()
    });
    localStorage.clear();
    window.location.href = '/';
}

// ===== FEED =====
async function loadFeed() {
    if (!getToken()) { window.location.href = '/'; return; }
    document.getElementById('nav-username').textContent = localStorage.getItem('username');
    const res = await fetch(`${API}/posts/`, { headers: getHeaders() });
    const posts = await res.json();
    const feed = document.getElementById('posts-feed');
    feed.innerHTML = '';
    posts.forEach(post => feed.innerHTML += renderPost(post));
}

function renderPost(post) {
    const initial = post.author[0].toUpperCase();
    const time = new Date(post.created_at).toLocaleDateString();
    const comments = post.comments.map(c => `
        <div class="comment">
            <div class="avatar" style="width:32px;height:32px;font-size:13px">${c.author[0].toUpperCase()}</div>
            <div class="comment-content">
                <span class="comment-author">${c.author}</span>
                <p>${c.content}</p>
            </div>
        </div>
    `).join('');

    return `
        <div class="post-card" id="post-${post.id}">
            <div class="post-header">
                <div class="avatar">${initial}</div>
                <div>
                    <div class="post-author">${post.author}</div>
                    <div class="post-time">${time}</div>
                </div>
            </div>
            <div class="post-content">${post.content}</div>
            <div class="post-actions">
                <button class="action-btn ${post.is_liked ? 'liked' : ''}" onclick="likePost(${post.id})">
                    ❤️ ${post.likes_count}
                </button>
                <button class="action-btn" onclick="toggleComments(${post.id})">
                    💬 ${post.comments.length}
                </button>
            </div>
            <div class="comments-section" id="comments-${post.id}" style="display:none">
                <div id="comments-list-${post.id}">${comments}</div>
                <div class="add-comment">
                    <input type="text" id="comment-input-${post.id}" placeholder="Write a comment..." />
                    <button onclick="addComment(${post.id})">Send</button>
                </div>
            </div>
        </div>
    `;
}

async function createPost() {
    const content = document.getElementById('post-content').value;
    if (!content) return;
    const res = await fetch(`${API}/posts/`, {
        method: 'POST',
        headers: getHeaders(),
        body: JSON.stringify({ content })
    });
    if (res.ok) {
        document.getElementById('post-content').value = '';
        loadFeed();
    }
}

async function likePost(postId) {
    const res = await fetch(`${API}/posts/${postId}/like/`, {
        method: 'POST',
        headers: getHeaders()
    });
    if (res.ok) loadFeed();
}

function toggleComments(postId) {
    const section = document.getElementById(`comments-${postId}`);
    section.style.display = section.style.display === 'none' ? 'block' : 'none';
}

async function addComment(postId) {
    const input = document.getElementById(`comment-input-${postId}`);
    const content = input.value;
    if (!content) return;
    const res = await fetch(`${API}/posts/${postId}/comment/`, {
        method: 'POST',
        headers: getHeaders(),
        body: JSON.stringify({ content })
    });
    if (res.ok) {
        input.value = '';
        loadFeed();
    }
}

// Auto load feed
if (document.getElementById('posts-feed')) loadFeed();