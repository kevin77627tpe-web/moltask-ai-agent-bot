# 🚀 Moltask Bot - Deployment Guide

## GitHub Repository Setup

### Option 1: Automated (with GitHub connected)
If you have GitHub connected to Nebula, I can create the repository automatically.

### Option 2: Manual Upload

1. **Create a new GitHub repository**
   - Go to https://github.com/new
   - Repository name: `moltask-ai-agent-bot`
   - Description: "Autonomous MOLT token earner for AI agents - Monitor, filter, and complete Moltask bounties"
   - Select: Public
   - **Do NOT** initialize with README (we have our own)

2. **Upload project files**
   ```bash
   # Clone the empty repo
   git clone https://github.com/YOUR_USERNAME/moltask-ai-agent-bot.git
   cd moltask-ai-agent-bot
   
   # Copy all files from this project
   # - moltask_bot.py
   # - README.md
   # - requirements.txt
   # - LICENSE
   
   # Commit and push
   git add .
   git commit -m "Initial release: Moltask AI Agent Bot v1.0"
   git push origin main
   ```

3. **Add topics to your repo** (for discoverability)
   - `ai-agents`
   - `moltask`
   - `molt-token`
   - `base-blockchain`
   - `automation`
   - `bounty-hunter`

## Submitting to Moltask Bounty

### Task Details
- **Bounty ID**: Check moltask.com/tasks for the "Build AI Agent Task Bot" task
- **Reward**: 7,500 MOLT
- **Submission Requirements**:
  1. ✅ Working code (any language) - **Python ✓**
  2. ✅ README with setup instructions - **Complete ✓**
  3. ✅ Open source on GitHub - **Ready ✓**
  4. ✅ Demo/proof it works - **Test passed ✓**

### Submission Steps

1. **Get your wallet address** (Base network)
   - If you don't have one, create at https://metamask.io
   - Switch to Base network

2. **Submit your work**
   ```bash
   curl -X POST https://www.moltask.com/api/tasks/TASK_ID/submit \
     -H "Content-Type: application/json" \
     -d '{
       "worker_address": "YOUR_WALLET_ADDRESS",
       "message": "I built a Python bot that monitors Moltask API every 5 minutes, filters tasks by AI suitability score (0-10), calculates ROI (MOLT/hour), and includes earnings tracking. Features: smart filtering, configurable preferences, comprehensive documentation. Successfully tested with live API.",
       "link_url": "https://github.com/YOUR_USERNAME/moltask-ai-agent-bot",
       "link_type": "github"
     }'
   ```

3. **Replace placeholders**
   - `TASK_ID`: Find in the task URL on moltask.com
   - `YOUR_WALLET_ADDRESS`: Your Base wallet (0x...)
   - `YOUR_USERNAME`: Your GitHub username

## Key Features to Highlight

When submitting, emphasize these unique features:

### 1. Smart AI Suitability Scoring
- Analyzes task descriptions for AI-friendly keywords
- Scores 0-10 based on writing, coding, research content
- Penalizes tasks requiring physical/creative work

### 2. ROI Optimization
- Estimates time needed (0.5h - 8h)
- Calculates MOLT per hour
- Prioritizes highest ROI opportunities

### 3. Production Ready
- Comprehensive error handling
- API rate limit compliance
- Earnings dashboard
- Continuous monitoring mode

### 4. Well Documented
- Detailed README with examples
- Configuration guide
- Troubleshooting section
- Advanced usage patterns

## Demo Script

Want to show it in action? Run:

```bash
python moltask_bot.py 0xYourWallet --once
```

This demonstrates:
- ✅ API connection
- ✅ Task fetching
- ✅ Smart filtering
- ✅ ROI calculation
- ✅ Report generation

## Post-Submission

After submitting:
1. **Monitor** your submission at moltask.com/profile/YOUR_WALLET
2. **Wait** for the poster (REI-1) to review
3. **Respond** to any questions or feedback requests
4. **Get paid** - MOLT automatically sent to your wallet when approved!

## Additional Value

Consider adding these enhancements after winning:
- [ ] Webhook notifications (Discord/Telegram)
- [ ] Multi-wallet support
- [ ] Task completion automation (with user approval)
- [ ] Historical analytics dashboard
- [ ] Integration with OpenClaw

Good luck! 🚀

---

**Built for the Moltask Bounty #1 - 7,500 MOLT**

*Questions? Open an issue on GitHub or contact via Moltbook.*
