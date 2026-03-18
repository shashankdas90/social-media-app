css = open('static/css/style.css', 'w', encoding='utf-8')
css.write("""* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', sans-serif;
}
body { background: #f0f2f5; }
.auth-container {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #667eea, #764ba2);
}
.auth-box {
    background: white;
    padding: 40px;
    border-radius: 16px;
    width: 100%;
    max-width: 400px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.2);
    text-align: center;
}
.auth-box h1 { font-size: 28px; margin-bottom: 8px; color: #667eea; }
.subtitle { color: #888; margin-bottom: 24px; }
.tabs {
    display: flex;
    margin-bottom: 24px;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid #eee;
}
.tab {
    flex: 1;
    padding: 10px;
    border: none;
    background: #f5f5f5;
    cursor: pointer;
    font-size: 14px;
}
.tab.active { background: #667eea; color: white; }
input, textarea {
    width: 100%;
    padding: 12px 16px;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 12px;
    font-size: 14px;
    outline: none;
}
input:focus, textarea:focus { border-color: #667eea; }
.btn-primary {
    width: 100%;
    padding: 12px;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
}
.btn-primary:hover { background: #5a6fd6; }
#auth-message { margin-top: 12px; font-size: 14px; color: red; }
.navbar {
    background: white;
    padding: 16px 32px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    position: sticky;
    top: 0;
    z-index: 100;
}
.navbar h1 { color: #667eea; font-size: 22px; }
.nav-links { display: flex; align-items: center; gap: 16px; }
.nav-links a { color: #667eea; text-decoration: none; font-weight: 500; }
.nav-links button {
    padding: 8px 16px;
    background: #ff4757;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
}
.feed-container { max-width: 600px; margin: 24px auto; padding: 0 16px; }
.create-post {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}
.create-post textarea { height: 80px; resize: none; }
.post-card {
    background: white;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06);
}
.post-header { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
.avatar {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: #667eea;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: bold;
    font-size: 16px;
}
.post-author { font-weight: 600; font-size: 15px; }
.post-time { font-size: 12px; color: #888; }
.post-content { font-size: 15px; line-height: 1.6; margin-bottom: 16px; }
.post-actions {
    display: flex;
    gap: 16px;
    border-top: 1px solid #f0f0f0;
    padding-top: 12px;
}
.action-btn {
    background: none;
    border: none;
    cursor: pointer;
    color: #888;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    border-radius: 8px;
}
.action-btn:hover { background: #f0f2f5; color: #667eea; }
.action-btn.liked { color: #e0245e; }
.comments-section {
    margin-top: 12px;
    border-top: 1px solid #f0f0f0;
    padding-top: 12px;
}
.comment { display: flex; gap: 10px; margin-bottom: 10px; }
.comment-content {
    background: #f0f2f5;
    padding: 8px 12px;
    border-radius: 8px;
    font-size: 14px;
    flex: 1;
}
.comment-author { font-weight: 600; font-size: 13px; }
.add-comment { display: flex; gap: 8px; margin-top: 10px; }
.add-comment input { flex: 1; margin: 0; padding: 8px 12px; font-size: 13px; }
.add-comment button {
    padding: 8px 16px;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 13px;
}""")

css.write("""
.profile-card {
    background: white;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    display: flex;
    align-items: center;
    gap: 24px;
}
.profile-avatar {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: #667eea;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 32px;
    font-weight: bold;
    flex-shrink: 0;
}
.profile-info { flex: 1; }
.profile-info h2 { font-size: 22px; margin-bottom: 6px; }
.profile-info p { color: #888; margin-bottom: 4px; font-size: 14px; }
.profile-stats {
    display: flex;
    gap: 24px;
    margin-top: 12px;
}
.stat { text-align: center; }
.stat-number { font-size: 20px; font-weight: 700; color: #667eea; display: block; }
.stat-label { font-size: 12px; color: #888; }
""")


css.write("""
.notifications-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
}
.notifications-header h2 { font-size: 20px; }
.mark-all-btn {
    padding: 8px 16px;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 13px;
}
.notification-card {
    background: white;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    display: flex;
    align-items: center;
    gap: 16px;
    transition: all 0.2s;
}
.notification-card.unread {
    border-left: 4px solid #667eea;
    background: #f0f2ff;
}
.notification-card.read {
    border-left: 4px solid #ddd;
    opacity: 0.8;
}
.notification-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #667eea;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
}
.notification-text { flex: 1; }
.notification-text strong { color: #667eea; }
.notification-time { font-size: 12px; color: #888; margin-top: 4px; }
.no-notifications {
    text-align: center;
    padding: 40px;
    color: #888;
    font-size: 16px;
}
.notif-badge {
    background: red;
    color: white;
    border-radius: 50%;
    padding: 2px 6px;
    font-size: 11px;
    margin-left: 4px;
}
""")
css.close()
print("CSS written! Size:", len(open('static/css/style.css').read()), "bytes")