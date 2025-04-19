import random
import re

# Cryptic and inspiring programming quotes
QUOTES = [
    "In the binary forest of ones and zeros, wisdom grows in recursive patterns.",
    "Debug your mind before debugging your code.",
    "The best code is like a good story - it needs no explanation.",
    "Every bug fixed is a lesson learned in the grand tapestry of programming.",
    "In the realm of bits, we are all artists painting with logic.",
    "The most elegant solution is often hidden in the simplest approach.",
    "Code without tests is like a ship without a compass.",
    "The path to mastery is paved with countless compile errors.",
    "Your code is a mirror reflecting your thought process.",
    "In the silence between keystrokes, solutions emerge.",
    "The best programs are written in the spaces between thoughts.",
    "Every function is a poem written in the language of logic.",
    "The most dangerous code is the code you think you understand.",
    "Complexity is the enemy of clarity.",
    "The journey of a thousand programs begins with a single line.",
]

def update_readme():
    try:
        # Read current README
        with open('README.md', 'r') as file:
            content = file.read()

        # Select a random quote
        new_quote = random.choice(QUOTES)
        
        # Replace the old quote in the Daily Wisdom section
        pattern = r'(## 🔮 Daily Wisdom\n\n<div align="center">\n\n\*")(.*?)("\*\n\n</div>)'
        updated_content = re.sub(pattern, f'\\1{new_quote}\\3', content)
        
        # Write updated content back
        with open('README.md', 'w') as file:
            file.write(updated_content)
            
        print("✨ Quote updated successfully!")
        
    except Exception as e:
        print(f"Error updating quote: {str(e)}")
        exit(1)

if __name__ == "__main__":
    update_readme() 