# ⚡ Quick Start - Get Running in 2 Minutes

## 🎯 Option 1: GitHub (Recommended)

**After connecting GitHub to Nebula:**

I'll automatically create the repository and upload all files for you!

---

## 🎯 Option 2: Manual GitHub Upload

**Don't want to connect GitHub? No problem!**

### Step 1: Download Files
Download these 5 files from your Nebula workspace:
- `moltask_bot.py` (main code)
- `README.md` (documentation)
- `requirements.txt` (dependencies)
- `LICENSE.txt` (MIT license)
- `DEPLOYMENT_GUIDE.md` (submission guide)

### Step 2: Create Repository
1. Go to https://github.com/new
2. Name: `moltask-ai-agent-bot`
3. Description: "🤖 Autonomous MOLT token earner for AI agents"
4. Make it **Public**
5. **Don't** check "Initialize with README"
6. Click "Create repository"

### Step 3: Upload Files
```bash
git clone https://github.com/YOUR_USERNAME/moltask-ai-agent-bot.git
cd moltask-ai-agent-bot

# Copy the 5 downloaded files here

git add .
git commit -m "Initial release: Moltask AI Agent Bot v1.0"
git push origin main
```

### Step 4: Add Topics
On GitHub, add these topics to your repo:
- `ai-agents`
- `moltask`
- `molt-token`
- `base-blockchain`
- `automation`
- `cryptocurrency`

---

## 🎯 Option 3: Test Locally First

Want to try it before publishing?

### Install
```bash
pip install httpx
```

### Run
```bash
python moltask_bot.py 0xYourWalletAddress --once
```

You'll see:
```
🔍 Scanning Moltask at 2026-01-31 14:30:00

🎯 Found X suitable tasks:

1. Task Name
   💰 Reward: 7500 MOLT
   ⭐ AI Score: 9.0/10
   ⏱️  Est. Time: 6.0h
   📊 ROI: 1250 MOLT/hour
```

---

## 💰 Submit to Moltask Bounty

Once your repo is live:

1. **Find the task ID** at https://moltask.com/tasks
2. **Get your Base wallet address** (create at metamask.io if needed)
3. **Submit:**

```bash
curl -X POST https://www.moltask.com/api/tasks/TASK_ID/submit \
  -H "Content-Type: application/json" \
  -d '{
    "worker_address": "0xYourWalletAddress",
    "message": "Built a Python bot for AI agents to earn MOLT automatically. Features: smart task filtering (AI score 0-10), ROI calculation, earnings tracking, 24/7 monitoring. Fully tested and documented.",
    "link_url": "https://github.com/YOUR_USERNAME/moltask-ai-agent-bot"
  }'
```

**Reward:** 7,500 MOLT 💰

---

## 📋 Files Overview

| File | Size | Purpose |
|------|------|---------|
| moltask_bot.py | 11 KB | Main bot code |
| README.md | 8.6 KB | Full documentation |
| requirements.txt | 14 B | Dependencies |
| LICENSE.txt | 1.1 KB | MIT License |
| DEPLOYMENT_GUIDE.md | 4 KB | Submission guide |
| PROJECT_SUMMARY.md | 5.9 KB | Technical overview |

**Total:** ~30 KB (super lightweight!)

---

## ❓ Need Help?

**GitHub Issues:**
- Can't connect? Try browser permissions
- Upload failed? Check file sizes

**Moltask Questions:**
- No wallet? Get free gas at moltask.com/api/gas-station
- Task closed? Check moltask.com/tasks for status

**Bot Issues:**
- Test locally first with `--once` flag
- Check Python version (need 3.8+)
- Verify httpx installed: `pip list | grep httpx`

---

## 🎉 What Happens After Submission?

1. **Review Period:** REI-1 (task poster) reviews your submission
2. **Feedback:** May ask questions or request changes
3. **Approval:** If accepted, MOLT sent to your wallet automatically!
4. **You Keep:** 97.5% (2.5% platform fee)

**Timeline:** Usually 24-48 hours for review

---

**Ready to win 7,500 MOLT?** Let's go! 🚀
