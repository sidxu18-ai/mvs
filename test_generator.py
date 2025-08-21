#!/usr/bin/env python3
"""
Test script for the Math Video Generator
"""

from math_video_generator import MathVideoGenerator
import sys

def test_generator():
    """Test the math video generator with a simple example."""
    try:
        print("Initializing Math Video Generator...")
        generator = MathVideoGenerator()
        
        print("Testing with a simple mathematical concept...")
        math_topic = "draw a circle"
        difficulty = "beginner"
        quality = "low_quality"
        
        print(f"Topic: {math_topic}")
        print(f"Difficulty: {difficulty}")
        print(f"Quality: {quality}")
        
        # Generate and render the video
        video_path = generator.generate_video(math_topic, difficulty, quality)
        
        if video_path:
            print(f"✅ Success! Video generated at: {video_path}")
            return True
        else:
            print("❌ Failed to generate video")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🎬 Testing AI-Powered Mathematical Visualization Generator")
    print("=" * 60)
    
    success = test_generator()
    
    if success:
        print("\n🎉 Test completed successfully!")
        sys.exit(0)
    else:
        print("\n💥 Test failed!")
        sys.exit(1)
