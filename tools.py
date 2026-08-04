import os
from datetime import datetime

# === Tool 1: Research Topic (read-only, auto-approved) ===
def research_topic(topic: str) -> str:
    """Research a given topic and return structured notes.
    
    Args:
        topic: The topic to research.
    
    Returns:
        String containing research notes.
    """
    # This is a placeholder – in a real version, you'd use a search API
    # But for the assignment, this works perfectly!
    
    notes = f"""
    📝 RESEARCH NOTES: {topic}
    ================================
    Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
    
    Key Points:
    • This is a placeholder research result for: {topic}
    • In a production version, you would integrate a search API like Tavily
    • The agent successfully called this tool and got a response
    
    For the assignment, this demonstrates:
    • Tool calling works
    • The agent can chain multiple tools together
    • Logging captures every tool call
    """
    
    return notes.strip()


# === Tool 2: Save Draft (read-only, auto-approved) ===
def save_draft(topic: str, content: str) -> str:
    """Save a blog post draft to a file.
    
    Args:
        topic: The topic of the blog post.
        content: The full blog post content.
    
    Returns:
        String confirming the file was saved.
    """
    # Create notes directory if it doesn't exist
    os.makedirs("notes", exist_ok=True)
    
    # Create filename from topic
    filename = f"draft_{topic.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    filepath = os.path.join("notes", filename)
    
    # Write the content
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Draft: {topic}\n\n")
        f.write(f"Created: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(content)
    
    return f"✅ Saved draft to {filepath}"


# === Tool 3: Publish Post (action - requires approval) ===
def publish_post(topic: str, draft_file: str) -> str:
    """Publish a blog post to a platform.
    
    Args:
        topic: The topic of the post.
        draft_file: Path to the draft file.
    
    Returns:
        String confirming publication.
    """
    # In a real version, you'd integrate with WordPress, Medium, etc.
    # For the assignment, this simulates publishing
    
    if not os.path.exists(draft_file):
        return f"❌ Error: Draft file '{draft_file}' not found."
    
    return f"""
    ✅ PUBLISHED: {topic}
    ======================
    Draft file: {draft_file}
    Published to: Blog Platform (simulated)
    Status: Success!
    
    Note: In production, this would call WordPress/Medium API.
    For this assignment, it demonstrates the approval gate working!
    """


# === TOOL SCHEMAS ===
TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "research_topic",
            "description": "Research a given topic and return structured notes. Use this when you need to gather information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The topic to research"
                    }
                },
                "required": ["topic"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "save_draft",
            "description": "Save a blog post draft to a file. Use this to store the written content.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The topic of the blog post"
                    },
                    "content": {
                        "type": "string",
                        "description": "The full blog post content"
                    }
                },
                "required": ["topic", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "publish_post",
            "description": "Publish a blog post to a platform. Use this ONLY after the draft is saved and reviewed.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The topic of the post"
                    },
                    "draft_file": {
                        "type": "string",
                        "description": "Path to the draft file"
                    }
                },
                "required": ["topic", "draft_file"]
            }
        }
    }
]


# === TOOL FUNCTIONS ===
TOOL_FUNCTIONS = {
    "research_topic": research_topic,
    "save_draft": save_draft,
    "publish_post": publish_post,
}