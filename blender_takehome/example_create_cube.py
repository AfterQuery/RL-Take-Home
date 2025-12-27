"""
Example MCP Tool: Create a Cube in Blender

This is a complete reference implementation showing best practices for
building MCP tools that interact with Blender.

Study this example to understand:
1. How to structure Pydantic input models with validation
2. How to write async tool functions
3. How to interact with Blender's bpy API
4. Error handling patterns
5. Documentation style
"""

from pydantic import BaseModel, Field, field_validator
from typing import Literal


class CreateCubeInput(BaseModel):
    """
    Input model for creating a cube in Blender.

    Pydantic automatically validates inputs and provides clear error messages
    when validation fails. This ensures the tool receives valid data.
    """

    name: str = Field(
        description="Name for the cube object",
        min_length=1,
        max_length=63,  # Blender object name limit
    )

    size: float = Field(
        default=2.0,
        description="Edge length of the cube",
        gt=0.0,  # Must be greater than 0
        le=1000.0,  # Reasonable upper limit
    )

    location: tuple[float, float, float] = Field(
        default=(0.0, 0.0, 0.0),
        description="Location of the cube in 3D space (x, y, z)",
    )

    @field_validator("location")
    @classmethod
    def validate_location(cls, v: tuple[float, float, float]) -> tuple[float, float, float]:
        """Ensure location coordinates are within reasonable bounds."""
        x, y, z = v
        limit = 10000.0
        if not all(-limit <= coord <= limit for coord in (x, y, z)):
            raise ValueError(f"Location coordinates must be within ±{limit}")
        return v

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Ensure name doesn't contain invalid characters."""
        # Blender has some restrictions on object names
        invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        if any(char in v for char in invalid_chars):
            raise ValueError(f"Name cannot contain: {', '.join(invalid_chars)}")
        return v


async def create_cube(input: CreateCubeInput) -> str:
    """
    Create a cube in the Blender scene.

    This tool demonstrates:
    - Importing bpy (Blender Python API)
    - Creating a mesh primitive
    - Setting object properties
    - Proper error handling
    - Informative return messages

    Args:
        input: Validated input parameters

    Returns:
        Success message with cube details

    Raises:
        Exception: If Blender operation fails
    """
    try:
        # Import bpy - Blender's Python API
        # This will only work when running inside Blender or with bpy module installed
        import bpy

        # Create the cube using Blender's operators
        # bpy.ops.mesh.primitive_cube_add() adds a cube to the scene
        bpy.ops.mesh.primitive_cube_add(
            size=input.size,
            location=input.location,
        )

        # Get reference to the newly created object
        # The active object is the most recently created/selected object
        cube = bpy.context.active_object

        # Set the object's name
        if cube:
            cube.name = input.name

            # Return a descriptive success message
            return (
                f"Successfully created cube '{input.name}' "
                f"with size {input.size} at location {input.location}"
            )
        else:
            # This shouldn't happen, but handle the edge case
            return "Cube created but could not get reference to object"

    except ImportError:
        # Handle case where bpy is not available
        return (
            "Error: Blender (bpy module) is not available. "
            "This tool must be run in a Blender environment."
        )
    except Exception as e:
        # Handle any other errors that might occur
        return f"Error creating cube: {str(e)}"


# Example of how this would be registered with FastMCP:
#
# from fastmcp import FastMCP
#
# mcp = FastMCP("blender-server")
#
# @mcp.tool()
# async def create_cube_tool(input: CreateCubeInput) -> str:
#     """Create a cube in the Blender scene."""
#     return await create_cube(input)
#
# if __name__ == "__main__":
#     mcp.run()
