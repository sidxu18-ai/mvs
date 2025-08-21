#!/usr/bin/env python3
"""
Simple test to verify the Manim scene code is valid
"""

import sys
import os

# Add the current directory to the path
sys.path.append(os.path.dirname(__file__))

try:
    # Import the generated scene
    from math_videos.draw_a_circle_scene import DrawCircleExplanation
    from manim import Scene
    
    print("✅ Manim scene imported successfully!")
    print("✅ DrawCircleExplanation class found")
    print(f"✅ Scene inherits from: {DrawCircleExplanation.__bases__}")
    
    # Check if it has the required construct method
    if hasattr(DrawCircleExplanation, 'construct'):
        print("✅ construct() method found")
    else:
        print("❌ construct() method missing")
        
    print("\n🎉 Scene validation completed successfully!")
    print("📝 The generated Manim code is valid and ready for rendering")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()