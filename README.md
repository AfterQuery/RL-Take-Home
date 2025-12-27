# Blender MCP Server - Take-Home Assignment

## 🎥 IMPORTANT: Video Demo Required

**Your submission MUST include a `demo_video.txt` file containing a link to a video demo.**

The video should show:
- Your MCP server in action with an AI agent
- Creating something interesting/creative in Blender using your tools
- Brief walkthrough of your implementation

This demonstrates that your tools actually work and can be used to build real 3D scenes.

---

## Overview

Build an MCP (Model Context Protocol) server that exposes Blender operations to AI agents. This assignment evaluates your ability to:
- Design a practical API for AI agent interactions
- Learn and integrate with unfamiliar APIs (Blender's `bpy` module)
- Write clean, typed, validated Python code
- Work efficiently with AI coding tools

**Time Limit**: 1-2 days

---

## What is MCP?

MCP (Model Context Protocol) is a protocol for connecting AI models to external tools and data sources. An MCP server exposes "tools" that AI agents can invoke to perform actions. In this case, you'll expose Blender operations.

---

## Technical Requirements

### Stack
- **Python**: 3.13+
- **FastMCP**: 2.12.4+ (MCP server framework)
- **Pydantic**: v2+ (input validation)
- **Blender**: `bpy` module for Blender operations
- **Type Hints**: Required throughout

### Setup

Install dependencies:
```bash
pip install fastmcp pydantic bpy
```

### FastMCP Basics

Here's a minimal example of how to set up an MCP server:

```python
from fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("blender-server")

# Register a tool (function that the AI agent can call)
@mcp.tool()
async def my_tool(input: MyInputModel) -> str:
    """Tool description that the AI agent will see."""
    # Your implementation here
    return "Result message"

# Run the server
if __name__ == "__main__":
    mcp.run()
```

**Key Points**:
- Tools are async functions
- Use Pydantic models for input validation
- Return string responses describing the result
- The `@mcp.tool()` decorator registers the function

---

## Assignment Requirements

### Your Task

Design and implement an MCP server with many rich tools that would be useful for an AI agent working with Blender.

### Think About:
1. **What operations would an AI need?**
   - Creating and manipulating 3D objects
   - Querying the scene state
   - Rendering outputs
   - Working with materials, cameras, lighting

2. **What's the minimal viable toolset?**
   - Start with core operations
   - Avoid over-engineering

3. **How should inputs be validated?**
   - What parameters are required vs. optional?
   - What are valid ranges/values?
   - How do you handle errors?

### Example Tool Categories

You should cover multiple categories (not exhaustive):
- **Object Operations**: Create, modify, delete, transform objects
- **Scene Queries**: List objects, get object info, query properties
- **Rendering**: Render scenes, configure render settings
- **Materials & Textures**: Apply materials, set colors, texture mapping
- **Camera & Lighting**: Position cameras, add lights, set lighting properties

### Provided Example

We've provided `example_create_cube.py` as a complete reference implementation. Study it to understand:
- How to structure a tool
- How to use Pydantic for validation
- How to interact with Blender's `bpy` API
- Error handling patterns
- Documentation style

---

## Evaluation Criteria

Your submission will be evaluated on:

### 1. Tool Design (30%)
- Are the tools practical and useful for an AI agent?
- Do they cover a good range of Blender capabilities?
- Is the API intuitive and well-documented?

### 2. Code Quality & Architecture (25%)
- Clean, readable code
- Proper type hints throughout
- Consistent style and naming
- Well-organized project structure
- Good separation of concerns
- Reusable abstractions where appropriate

### 3. Input Validation (20%)
- Comprehensive Pydantic models
- Appropriate validation rules
- Clear error messages

### 4. Error Handling (15%)
- Graceful handling of invalid inputs
- Blender operation failures handled properly
- Informative error messages returned

### 5. Documentation (10%)
- Clear docstrings for all tools
- Explanation of parameters
- Usage examples where helpful

---

## Submission Guidelines

### Required Files

At minimum, submit:
1. Your implementation files (organize as you see fit)
2. A `README.md` explaining:
   - How to install dependencies
   - How to run your server
   - List of tools implemented
   - Any design decisions or trade-offs
3. **`demo_video.txt`** containing a link to your video demo (see top of assignment)

### Optional Enhancements

If time permits, consider:
- Additional tool categories (animation, modifiers, etc.)
- Comprehensive error handling
- Unit tests
- Configuration management
- Middleware (logging, error handling, etc.)

### How to Submit

Create a git repository with your implementation and share the link.

---

## Getting Started

### 1. Study the Example
Look at `example_create_cube.py` to understand the pattern.

### 2. Learn Blender's API
The `bpy` module is Blender's Python API. Key resources:
- [Blender Python API Docs](https://docs.blender.org/api/current/)
- `bpy.ops` - Operations (like creating objects)
- `bpy.data` - Scene data (objects, materials, etc.)
- `bpy.context` - Current context (active scene, etc.)

### 3. Design Your Tools
Plan out 5-7 tools that would be useful. Consider:
- What inputs do they need?
- What do they return?
- How do they handle errors?

### 4. Implement Incrementally
Build one tool at a time, test it, then move to the next.

### 5. Use AI Tools Effectively
This assignment is designed to be completed with AI assistance. Use tools like Claude, Cursor, or GitHub Copilot to:
- Learn the `bpy` API quickly
- Generate boilerplate code
- Debug issues
- Refactor and improve code quality

---

## Tips for Success

1. **Start Simple**: Get one tool working end-to-end before expanding
2. **Validate Early**: Use Pydantic's validation to catch errors early
3. **Handle Errors**: Blender operations can fail - handle gracefully
4. **Document Well**: Clear docstrings help both humans and AI agents
5. **Test Thoroughly**: Try invalid inputs, edge cases, etc.
6. **Think Like an Agent**: What would an AI actually need to build 3D scenes?

---

## Questions?

If you have questions about:
- **MCP/FastMCP**: Check the [FastMCP docs](https://github.com/jlowin/fastmcp)
- **Blender API**: Use the official Blender Python API documentation
- **Assignment Requirements**: Email us with clarification questions

---

## Good Luck!

We're excited to see your implementation. Focus on demonstrating:
- Strong system design skills
- Ability to learn new APIs quickly
- Clean, professional code quality
- Effective use of AI tools

Remember: This is about showing how you approach problems, not about being a Blender expert.
