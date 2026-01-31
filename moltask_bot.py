"""
Moltask AI Agent Bot - Autonomous MOLT Token Earner

A smart bot that monitors moltask.com for new tasks, filters for Agent-suitable work,
and helps AI agents earn MOLT tokens automatically.

Architecture:
1. Monitor: Poll /api/tasks every 5 minutes for new tasks
2. Filter: Identify tasks suitable for AI agents (writing, coding, research)
3. Claim: Automatically submit work for high-ROI tasks
4. Track: Monitor earnings and completed work

Features:
- No API key required (wallet-based authentication)
- Smart filtering for AI-suitable tasks
- ROI calculation (reward vs estimated time)
- Earnings dashboard and reporting
- Configurable task preferences
"""

import httpx
import time
import json
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict


@dataclass
class Task:
    """Represents a Moltask task/bounty"""
    id: str
    title: str
    description: str
    reward: int  # MOLT tokens
    task_type: str
    status: str
    created_at: str
    poster: str
    
    def __post_init__(self):
        """Calculate AI suitability score"""
        self.ai_score = self._calculate_ai_score()
        self.estimated_hours = self._estimate_time()
        self.roi = self.reward / max(self.estimated_hours, 0.5)  # MOLT per hour
    
    def _calculate_ai_score(self) -> float:
        """Score how suitable this task is for AI agents (0-10)"""
        score = 0.0
        text = (self.title + " " + self.description).lower()
        
        # High value keywords
        high_value = ['write', 'research', 'analyze', 'code', 'develop', 'create content',
                      'data analysis', 'summarize', 'translate', 'documentation']
        for keyword in high_value:
            if keyword in text:
                score += 2.0
        
        # Medium value keywords
        medium_value = ['post', 'comment', 'review', 'feedback', 'test', 'report']
        for keyword in medium_value:
            if keyword in text:
                score += 1.0
        
        # Low value (harder for AI)
        low_value = ['design', 'art', 'video', 'audio', 'manual', 'physical']
        for keyword in low_value:
            if keyword in text:
                score -= 2.0
        
        # Task type bonus
        if self.task_type in ['Automation', 'Writing', 'Research']:
            score += 2.0
        
        return min(max(score, 0), 10)  # Clamp to 0-10
    
    def _estimate_time(self) -> float:
        """Estimate hours needed based on task description"""
        text = (self.title + " " + self.description).lower()
        
        # Quick tasks (< 1 hour)
        if any(word in text for word in ['post', 'comment', 'simple', 'quick']):
            return 0.5
        
        # Medium tasks (1-3 hours)
        if any(word in text for word in ['write', 'create', 'analyze']):
            return 2.0
        
        # Complex tasks (3-8 hours)
        if any(word in text for word in ['build', 'develop', 'bot', 'system', 'comprehensive']):
            return 6.0
        
        # Default estimate
        return 3.0
    
    def is_suitable(self, min_score: float = 5.0, min_reward: int = 500) -> bool:
        """Check if task is worth pursuing"""
        return (self.status == 'open' and 
                self.ai_score >= min_score and 
                self.reward >= min_reward)


class MoltaskBot:
    """Main bot class for monitoring and completing Moltask tasks"""
    
    def __init__(self, wallet_address: str, config: Optional[Dict] = None):
        self.wallet = wallet_address
        self.base_url = "https://www.moltask.com/api"
        self.config = config or self._default_config()
        self.client = httpx.Client(timeout=30.0)
        
        # Tracking
        self.seen_tasks = set()
        self.completed_tasks = []
        self.total_earned = 0
        self.start_time = datetime.now()
    
    def _default_config(self) -> Dict:
        """Default bot configuration"""
        return {
            'min_ai_score': 5.0,      # Minimum suitability score
            'min_reward': 500,         # Minimum MOLT reward
            'max_estimated_hours': 8,  # Don't take tasks > 8 hours
            'check_interval': 300,     # Check every 5 minutes
            'auto_submit': False,      # Manual approval before submitting
            'task_types': ['Automation', 'Writing', 'Research', 'Other']
        }
    
    def fetch_tasks(self) -> List[Task]:
        """Fetch all available tasks from Moltask API"""
        try:
            response = self.client.get(f"{self.base_url}/tasks")
            response.raise_for_status()
            data = response.json()
            
            tasks = []
            for task_data in data.get('data', []):
                task = Task(
                    id=task_data.get('id', ''),
                    title=task_data.get('title', ''),
                    description=task_data.get('description', ''),
                    reward=task_data.get('reward_amount', 0),
                    task_type=task_data.get('task_type', 'Other'),
                    status=task_data.get('status', 'unknown'),
                    created_at=task_data.get('created_at', ''),
                    poster=task_data.get('poster_address', '')
                )
                tasks.append(task)
            
            return tasks
        except Exception as e:
            print(f"❌ Error fetching tasks: {e}")
            return []
    
    def filter_tasks(self, tasks: List[Task]) -> List[Task]:
        """Filter tasks based on AI suitability and config"""
        suitable = []
        for task in tasks:
            # Skip already seen tasks
            if task.id in self.seen_tasks:
                continue
            
            # Check suitability
            if task.is_suitable(self.config['min_ai_score'], self.config['min_reward']):
                # Check estimated time
                if task.estimated_hours <= self.config['max_estimated_hours']:
                    # Check task type
                    if task.task_type in self.config['task_types']:
                        suitable.append(task)
                        self.seen_tasks.add(task.id)
        
        # Sort by ROI (MOLT per hour)
        suitable.sort(key=lambda t: t.roi, reverse=True)
        return suitable
    
    def submit_work(self, task_id: str, message: str, proof_url: str) -> bool:
        """Submit completed work for a task"""
        try:
            payload = {
                "worker_address": self.wallet,
                "message": message,
                "link_url": proof_url,
                "link_type": "other"
            }
            
            response = self.client.post(
                f"{self.base_url}/tasks/{task_id}/submit",
                json=payload
            )
            response.raise_for_status()
            
            print(f"✅ Work submitted successfully for task {task_id}")
            return True
        except Exception as e:
            print(f"❌ Error submitting work: {e}")
            return False
    
    def get_profile(self) -> Dict:
        """Get wallet profile and reputation"""
        try:
            response = self.client.get(f"https://www.moltask.com/profile/{self.wallet}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Error fetching profile: {e}")
            return {}
    
    def generate_report(self) -> str:
        """Generate earnings and activity report"""
        runtime = datetime.now() - self.start_time
        hours = runtime.total_seconds() / 3600
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║              MOLTASK BOT EARNINGS REPORT                     ║
╚══════════════════════════════════════════════════════════════╝

💼 Wallet: {self.wallet[:10]}...{self.wallet[-8:]}
⏱️  Runtime: {hours:.1f} hours
📊 Tasks Monitored: {len(self.seen_tasks)}
✅ Tasks Completed: {len(self.completed_tasks)}
💰 Total Earned: {self.total_earned} MOLT

📈 Performance Metrics:
   • MOLT per hour: {self.total_earned / max(hours, 0.1):.2f}
   • Success rate: {len(self.completed_tasks) / max(len(self.seen_tasks), 1) * 100:.1f}%
   • Avg reward: {self.total_earned / max(len(self.completed_tasks), 1):.0f} MOLT

🎯 Recent Completions:
"""
        for task in self.completed_tasks[-5:]:
            report += f"   • {task['title']} - {task['reward']} MOLT\n"
        
        return report
    
    def run_once(self) -> List[Task]:
        """Run one iteration of task monitoring"""
        print(f"\n🔍 Scanning Moltask at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Fetch and filter tasks
        all_tasks = self.fetch_tasks()
        suitable_tasks = self.filter_tasks(all_tasks)
        
        if suitable_tasks:
            print(f"\n🎯 Found {len(suitable_tasks)} suitable tasks:")
            for i, task in enumerate(suitable_tasks[:5], 1):  # Show top 5
                print(f"\n{i}. {task.title}")
                print(f"   💰 Reward: {task.reward} MOLT")
                print(f"   ⭐ AI Score: {task.ai_score:.1f}/10")
                print(f"   ⏱️  Est. Time: {task.estimated_hours:.1f}h")
                print(f"   📊 ROI: {task.roi:.0f} MOLT/hour")
                print(f"   🏷️  Type: {task.task_type}")
        else:
            print("   No new suitable tasks found")
        
        return suitable_tasks
    
    def run_continuous(self):
        """Run bot continuously (monitoring mode)"""
        print("🤖 Moltask Bot Starting...")
        print(f"💼 Wallet: {self.wallet}")
        print(f"⚙️  Config: {self.config}")
        print(f"🔄 Checking every {self.config['check_interval']}s\n")
        
        try:
            while True:
                suitable_tasks = self.run_once()
                
                # Sleep until next check
                time.sleep(self.config['check_interval'])
        except KeyboardInterrupt:
            print("\n\n⏹️  Bot stopped by user")
            print(self.generate_report())


def main():
    """Main entry point"""
    import sys
    
    # Check for wallet address
    if len(sys.argv) < 2:
        print("❌ Usage: python moltask_bot.py <wallet_address>")
        print("\nExample:")
        print("  python moltask_bot.py 0xYourWalletAddress")
        sys.exit(1)
    
    wallet = sys.argv[1]
    
    # Create and run bot
    bot = MoltaskBot(wallet)
    
    # Run once for testing, or continuous for production
    if "--once" in sys.argv:
        suitable_tasks = bot.run_once()
        if suitable_tasks:
            print(f"\n💡 Tip: Run without --once to monitor continuously")
    else:
        bot.run_continuous()


if __name__ == "__main__":
    main()
