#!/bin/bash

echo "Creating simple screenshot mockups..."

# Create screenshots directory
mkdir -p screenshots

# Create a simple text-based screenshot mockup (we'll use ImageMagick to create basic images)
echo "Creating screenshot 1: Hydration tip..."

# Create a simple image with text
convert -size 1080x1920 xc:'#f0f0f0' \
  -fill '#4A90E2' -draw 'rectangle 0,0 1080,100' \
  -fill white -pointsize 60 -font Arial -draw "text 540,60 'Daily Wellness Tips'" \
  -fill '#333333' -pointsize 40 -font Arial -draw "text 540,300 'Drink Water'" \
  -fill '#666666' -pointsize 28 -font Arial -draw "text 540,400 'Start your day with a glass of water\nto hydrate your body.'" \
  -fill '#888888' -pointsize 24 -font Arial -draw "text 540,600 'Tip 1 of 30'" \
  screenshots/screenshot_1_1080x1920.png

echo "Creating screenshot 2: Sleep tip..."

convert -size 1080x1920 xc:'#f0f0f0' \
  -fill '#56CF8C' -draw 'rectangle 0,0 1080,100' \
  -fill white -pointsize 60 -font Arial -draw "text 540,60 'Daily Wellness Tips'" \
  -fill '#333333' -pointsize 40 -font Arial -draw "text 540,300 'Sleep Well'" \
  -fill '#666666' -pointsize 28 -font Arial -draw "text 540,400 'Aim for 7-8 hours of quality sleep\ntonight for better health.'" \
  -fill '#888888' -pointsize 24 -font Arial -draw "text 540,600 'Tip 2 of 30'" \
  screenshots/screenshot_2_1080x1920.png

echo "Creating screenshot 3: Exercise tip..."

convert -size 1080x1920 xc:'#f0f0f0' \
  -fill '#FF6B6B' -draw 'rectangle 0,0 1080,100' \
  -fill white -pointsize 60 -font Arial -draw "text 540,60 'Daily Wellness Tips'" \
  -fill '#333333' -pointsize 40 -font Arial -draw "text 540,300 'Take a Walk'" \
  -fill '#666666' -pointsize 28 -font Arial -draw "text 540,400 'Go for a 10-minute walk to get\nsome fresh air and movement.'" \
  -fill '#888888' -pointsize 24 -font Arial -draw "text 540,600 'Tip 3 of 30'" \
  screenshots/screenshot_3_1080x1920.png

echo "✅ Screenshot mockups created in screenshots/ directory"
echo ""
echo "Note: These are basic mockups. For production, use actual screenshots from:"
echo "1. Android Studio emulator"
echo "2. Physical device screenshots"
echo "3. Or create more polished mockups with design tools"