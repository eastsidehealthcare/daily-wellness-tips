# App Icon Instructions

For Play Store submission, you need to create proper app icons. Here's what you need:

## Required Icon Sizes

### Adaptive Icons (Android 8.0+)
- **Foreground**: 108x108 dp (432x432 px for xxxhdpi)
- **Background**: 108x108 dp (432x432 px for xxxhdpi)

### Legacy Icons
- **mdpi**: 48x48 px
- **hdpi**: 72x72 px  
- **xhdpi**: 96x96 px
- **xxhdpi**: 144x144 px
- **xxxhdpi**: 192x192 px

### Play Store Requirements
- **512x512 px** high-resolution icon for store listing
- **1024x500 px** feature graphic for store listing

## Creating Icons

### Option 1: Use Android Studio
1. Open the project in Android Studio
2. Right-click on `res` folder → New → Image Asset
3. Choose "Launcher Icons (Adaptive and Legacy)"
4. Configure:
   - Foreground: Choose "Text" and enter "W"
   - Background: Choose color #4CAF50 (green)
   - Text color: White
5. Click Next → Finish

### Option 2: Use Online Tools
- [Android Asset Studio](https://romannurik.github.io/AndroidAssetStudio/)
- [App Icon Generator](https://appicon.co/)

### Option 3: Design Yourself
Use tools like:
- Figma (free)
- Adobe Illustrator
- Canva
- GIMP (free)

## Icon Design Tips
1. **Simple & recognizable**: The "W" for Wellness is a good start
2. **Contrast**: Ensure good contrast between icon and background
3. **Scalability**: Design at 512x512 px and scale down
4. **No text**: Avoid text other than single letters/initials
5. **Solid background**: Simple colors work best at small sizes

## Current Placeholders
The project includes simple green squares with a white "W" as placeholder icons. Replace these with properly designed icons before Play Store submission.

## File Locations
- Adaptive icons: `app/src/main/res/mipmap-anydpi-v26/`
- Legacy icons: `app/src/main/res/mipmap-*/`
- Store icon: Create separately (512x512 px)