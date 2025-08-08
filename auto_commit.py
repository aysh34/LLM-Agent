# auto_commit.py - Single file solution, just copy this to any repo!

import os
import subprocess
import time
from datetime import datetime
import threading


class SimpleAutoCommit:
    def __init__(self, delay=10):
        self.delay = delay
        self.repo_path = os.getcwd()
        self.last_check = 0

        # Check if this is a git repo
        if not os.path.exists(".git"):
            raise Exception("Not a git repository! Run 'git init' first.")

    def has_changes(self):
        """Check if there are changes to commit (including .ipynb files)"""
        try:
            result = subprocess.run(
                ["git", "status", "--porcelain"], capture_output=True, text=True
            )
            if not result.stdout.strip():
                return False

            changed_files = [line[3:] for line in result.stdout.splitlines()]
            return any(file.endswith(".ipynb") for file in changed_files) or bool(
                changed_files
            )
        except:
            return False

    def auto_commit(self):
        """Make automatic commit if changes exist"""
        if not self.has_changes():
            return False

        try:
            # Add all changes
            subprocess.run(["git", "add", "."], check=True)

            # Create commit message with timestamp
            timestamp = datetime.now().strftime("%H:%M:%S")
            commit_msg = f"Auto-commit [{timestamp}]"

            # Add note if notebooks changed
            result = subprocess.run(
                ["git", "status", "--porcelain"], capture_output=True, text=True
            )
            changed_files = [line[3:] for line in result.stdout.splitlines()]
            if any(file.endswith(".ipynb") for file in changed_files):
                commit_msg += " (notebook update)"

            # Commit
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)

            # Push (optional, remove if you don't want auto-push)
            try:
                subprocess.run(["git", "push"], check=True)
                print(f"✅ {commit_msg} - Pushed!")
            except:
                print(f"✅ {commit_msg} - Committed!")

            return True
        except Exception as e:
            print(f"❌ Commit failed: {e}")
            return False

    def watch_and_commit(self):
        """Watch for changes and auto-commit"""
        print(f"🚀 Auto-committing every {self.delay} seconds...")
        print("💡 Just save your files in VS Code, commits happen automatically!")
        print("🛑 Press Ctrl+C to stop")
        print("-" * 50)

        try:
            while True:
                if self.auto_commit():
                    pass  # Success message already printed
                time.sleep(self.delay)
        except KeyboardInterrupt:
            print("\n🛑 Auto-commit stopped!")


# Usage: Just run this file!
if __name__ == "__main__":
    try:
        committer = SimpleAutoCommit(delay=10)  # Check every 10 seconds
        committer.watch_and_commit()
    except Exception as e:
        print(f"❌ Error: {e}")

# That's it! Now commits trigger on any file change, including .ipynb, and mark them in commit messages.
