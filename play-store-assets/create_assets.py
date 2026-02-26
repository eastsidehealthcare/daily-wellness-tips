#!/usr/bin/env python3
"""
Simple script to create placeholder Play Store assets.
These are basic placeholder images that you should replace with proper designs.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_app_icon(size, output_path):
    """Create a simple app icon with a heart and text"""
    img = Image.new('RGB', (size, size), color=(74, 144, 226))  # Blue background
    draw = ImageDraw.Draw(img)
    
    # Draw a simple heart
    heart_size = size // 3
    heart_x = size // 2
    heart_y = size // 2
    
    # Simple heart shape (two circles and a triangle)
    draw.ellipse([heart_x - heart_size//2, heart_y - heart_size//3, 
                  heart_x, heart_y + heart_size//3], fill=(255, 255, 255))
    draw.ellipse([heart_x, heart_y - heart_size//3, 
                  heart_x + heart_size//2, heart_y + heart_size//3], fill=(255, 255, 255))
    draw.polygon([heart_x - heart_size//2, heart_y,
                  heart_x + heart_size//2, heart_y,
                  heart_x, heart_y + heart_size//2], fill=(255, 255, 255))
    
    img.save(output_path)
    print(f"Created app icon: {output_path} ({size}x{size})")

def create_feature_graphic(width, height, output_path):
    """Create a simple feature graphic"""
    img = Image.new('RGB', (width, height), color=(86, 207, 140))  # Green background
    draw = ImageDraw.Draw(img)
    
    # Add title text
    try:
        font = ImageFont.truetype("Arial", 60)
    except:
        font = ImageFont.load_default()
    
    title = "Daily Wellness Tips"
    subtitle = "One tip per day for better health"
    
    # Calculate text positions
    title_bbox = draw.textbbox((0, 0), title, font=font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]
    
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    
    # Draw text
    draw.text(((width - title_width) // 2, height // 3), title, fill=(255, 255, 255), font=font)
    draw.text(((width - subtitle_width) // 2, height // 2), subtitle, fill=(255, 255, 255), font=font)
    
    # Add a simple icon
    icon_size = 100
    icon_x = width // 2
    icon_y = height * 2 // 3
    draw.ellipse([icon_x - icon_size//2, icon_y - icon_size//2,
                  icon_x + icon_size//2, icon_y + icon_size//2], 
                 fill=(255, 255, 255, 128))
    
    img.save(output_path)
    print(f"Created feature graphic: {output_path} ({width}x{height})")

def create_screenshot(width, height, output_path, tip_number):
    """Create a simple screenshot mockup"""
    img = Image.new('RGB', (width, height), color=(240, 240, 240))  # Light gray background
    
    # Create phone frame
    phone_color = (50, 50, 50)
    screen_color = (255, 255, 255)
    screen_padding = 40
    
    # Draw phone
    draw = ImageDraw.Draw(img)
    draw.rectangle([screen_padding, screen_padding, 
                    width - screen_padding, height - screen_padding], 
                   fill=phone_color)
    
    # Draw screen
    screen_left = screen_padding + 10
    screen_top = screen_padding + 10
    screen_right = width - screen_padding - 10
    screen_bottom = height - screen_padding - 10
    draw.rectangle([screen_left, screen_top, screen_right, screen_bottom], 
                   fill=screen_color)
    
    # Add app content
    screen_width = screen_right - screen_left
    screen_height = screen_bottom - screen_top
    
    # Title
    title = "Daily Wellness Tip"
    title_y = screen_top + 50
    
    try:
        title_font = ImageFont.truetype("Arial", 32)
        body_font = ImageFont.truetype("Arial", 24)
        info_font = ImageFont.truetype("Arial", 18)
    except:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        info_font = ImageFont.load_default()
    
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text((screen_left + (screen_width - title_width) // 2, title_y), 
              title, fill=(0, 0, 0), font=title_font)
    
    # Tip content
    tips = [
        "Drink a glass of water first thing in the morning.",
        "Take a 10-minute walk outside for fresh air.",
        "Practice deep breathing for 2 minutes to reduce stress.",
        "Eat a serving of vegetables with your lunch.",
        "Stand up and stretch every hour if sitting."
    ]
    
    tip_index = tip_number % len(tips)
    tip_body = tips[tip_index]
    
    body_y = title_y + 80
    # Simple text wrapping
    words = tip_body.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=body_font)
        test_width = bbox[2] - bbox[0]
        
        if test_width <= screen_width - 40:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    for i, line in enumerate(lines):
        line_bbox = draw.textbbox((0, 0), line, font=body_font)
        line_width = line_bbox[2] - line_bbox[0]
        draw.text((screen_left + (screen_width - line_width) // 2, body_y + i * 35),
                  line, fill=(50, 50, 50), font=body_font)
    
    # Day info
    day_info = f"Tip {tip_number + 1} of 30"
    info_bbox = draw.textbbox((0, 0), day_info, font=info_font)
    info_width = info_bbox[2] - info_bbox[0]
    draw.text((screen_left + (screen_width - info_width) // 2, screen_bottom - 50),
              day_info, fill=(100, 100, 100), font=info_font)
    
    img.save(output_path)
    print(f"Created screenshot: {output_path} ({width}x{height}) - Tip {tip_number + 1}")

def main():
    """Create all required Play Store assets"""
    assets_dir = "."
    
    # Create directories
    os.makedirs(os.path.join(assets_dir, "icons"), exist_ok=True)
    os.makedirs(os.path.join(assets_dir, "feature-graphic"), exist_ok=True)
    os.makedirs(os.path.join(assets_dir, "screenshots"), exist_ok=True)
    
    # App icons (required sizes)
    icon_sizes = [
        (512, 512),      # Play Store listing
        (1024, 1024),    # High-res for Play Store
        (48, 48),        # Launcher icon (mdpi)
        (72, 72),        # Launcher icon (hdpi)
        (96, 96),        # Launcher icon (xhdpi)
        (144, 144),      # Launcher icon (xxhdpi)
        (192, 192),      # Launcher icon (xxxhdpi)
    ]
    
    for size in icon_sizes:
        output_path = os.path.join(assets_dir, "icons", f"icon_{size[0]}x{size[1]}.png")
        create_app_icon(size[0], output_path)
    
    # Feature graphic (required: 1024x500)
    feature_path = os.path.join(assets_dir, "feature-graphic", "feature_1024x500.png")
    create_feature_graphic(1024, 500, feature_path)
    
    # Screenshots (minimum 2, recommended 3-8)
    # Create different aspect ratios for phones
    screenshot_sizes = [
        (1080, 1920),  # 9:16 phone
        (1080, 1920),  # Another one with different content
        (1080, 1920),  # Third screenshot
    ]
    
    for i, size in enumerate(screenshot_sizes):
        output_path = os.path.join(assets_dir, "screenshots", f"screenshot_{i+1}_{size[0]}x{size[1]}.png")
        create_screenshot(size[0], size[1], output_path, i)
    
    print("\n✅ All placeholder assets created!")
    print("\n📁 Asset locations:")
    print("  - Icons: ./icons/")
    print("  - Feature graphic: ./feature-graphic/")
    print("  - Screenshots: ./screenshots/")
    print("\n⚠️  Note: These are placeholder images. For production, replace with:")
    print("  - Professional app icon design")
    print("  - Actual app screenshots from emulator/device")
    print("  - Polished feature graphic")

if __name__ == "__main__":
    main()