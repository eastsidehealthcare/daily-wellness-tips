# Daily Wellness Tips - Ultra Minimal Android App

The absolute minimum Android app that will pass Google Play Store publishing requirements.

## App Features
- Shows one wellness tip per day
- 30 hardcoded tips (cycles monthly)
- No internet connection required
- No permissions requested
- Single screen, simple interface

## Technical Details
- **Language**: Kotlin
- **Min SDK**: 23 (Android 6.0)
- **Target SDK**: 36 (Android 14)
- **APK Size**: <2MB
- **Dependencies**: AndroidX only (no third-party libraries)

## Project Structure
```
app/
├── src/main/
│   ├── java/com/example/dailywellnesstips/
│   │   └── MainActivity.kt    # Single activity, does everything
│   ├── res/
│   │   ├── layout/activity_main.xml
│   │   └── values/strings.xml
│   └── assets/tips.json       # 30 wellness tips
```

## Building the App

### From Command Line
```bash
./gradlew build          # Build debug APK
./gradlew bundleRelease  # Build release AAB (requires signing config)
```

### From Android Studio
1. Open in Android Studio
2. Build → Generate Signed Bundle / APK
3. Choose "Android App Bundle"
4. Create new keystore (or use existing)
5. Build release AAB

## Play Store Requirements Checklist
- [x] App doesn't crash on launch
- [x] No sensitive permissions
- [x] Privacy policy: "No data collected" (template in `play-store-assets/`)
- [x] Content rating: Everyone
- [x] Target SDK: 36 (current)
- [x] App size: <2MB
- [x] App icon (512x512, 1024x1024) - **✅ READY in `play-store-assets/icons/`**
- [x] Feature graphic (1024x500) - **✅ READY in `play-store-assets/feature-graphic/`**
- [x] Screenshots (minimum 2) - **✅ READY (3) in `play-store-assets/screenshots/`**
- [x] App description - **✅ READY in `play-store-assets/app_description.txt`**

## Development Time: ~2 hours
Created as the absolute minimum viable app for Play Store publishing.

## Play Store Assets - READY FOR SUBMISSION
All required Play Store assets have been converted to PNG and are ready in the `play-store-assets/` folder:

### 📁 Ready Assets:
- **App icons** (`icons/`) - All required sizes (48x48 to 1024x1024)
- **Feature graphic** (`feature-graphic/`) - 1024x500 PNG
- **Screenshots** (`screenshots/`) - 3 mockups (1080x1920)
- **App description** (`app_description.txt`) - Marketing copy
- **Privacy policy** (`privacy_policy.html`) - HTML page

### 🚀 Quick Submission:
1. Build signed AAB: `./gradlew bundleRelease`
2. Upload to Play Console with assets from `play-store-assets/`
3. Copy description from `app_description.txt`
4. Publish `privacy_policy.html` and provide URL

See `play-store-assets/ASSETS_SUMMARY.md` for complete details.

## Notes
- This app is intentionally minimal to pass Play Store review
- No architecture patterns, no third-party libraries
- Basic error handling (fallback text if JSON fails)
- Day-of-year based tip rotation
- No user data collection