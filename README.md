# Daily Wellness Tips - Android App

A simple daily health & wellness tip app that displays one tip per day from a hardcoded local JSON file.

## Features
- Displays a different tip each day based on day-of-year
- No internet connection required
- No backend or database
- Simple, clean UI
- Cycles through 30+ tips (over a month before repeating)
- Topics: hydration, sleep, fasting, exercise, and more

## Technical Details
- Language: Kotlin
- Minimum SDK: 23 (Android 6.0)
- Target SDK: 36 (Android 14)
- Single Activity, single screen
- No third-party dependencies
- Signed release AAB ready for Play Store

## Project Structure
```
daily-wellness-tips/
├── app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/example/dailywellnesstips/
│   │   │   │   └── MainActivity.kt
│   │   │   ├── res/
│   │   │   │   ├── layout/
│   │   │   │   │   └── activity_main.xml
│   │   │   │   ├── values/
│   │   │   │   │   ├── colors.xml
│   │   │   │   │   ├── strings.xml
│   │   │   │   │   └── themes.xml
│   │   │   │   └── mipmap/ (app icons)
│   │   │   └── assets/
│   │   │       └── tips.json
│   │   └── androidTest/ (empty)
│   ├── build.gradle
│   └── proguard-rules.pro
├── gradle/
│   └── wrapper/
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── build.gradle
├── gradle.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── local.properties (gitignored)
```

## Building the App

### 1. Generate Signing Keystore (if you don't have one)
```bash
keytool -genkey -v -keystore daily-wellness-tips.jks -keyalg RSA -keysize 2048 -validity 10000 -alias dailywellness
```

### 2. Update Signing Configuration
1. Copy the generated `daily-wellness-tips.jks` to the project root
2. Create a `keystore.properties` file in the project root:
```
storePassword=your_store_password
keyPassword=your_key_password
keyAlias=dailywellness
storeFile=daily-wellness-tips.jks
```

### 3. Build Signed AAB
```bash
./gradlew bundleRelease
```
The AAB file will be at: `app/build/outputs/bundle/release/app-release.aab`

### 4. Build Signed APK (optional)
```bash
./gradlew assembleRelease
```

## Uploading to Play Store

### 1. Create App in Play Console
1. Go to [Google Play Console](https://play.google.com/console)
2. Click "Create app"
3. Fill in:
   - App name: "Daily Wellness Tips"
   - Default language: English
   - App or game: App
   - Free or paid: Free

### 2. Prepare Store Listing
1. **App details**: Fill in description, category (Health & Fitness)
2. **Graphics**: Upload app icon (512x512) and feature graphic (1024x500)
3. **Content rating**: Complete questionnaire (non-medical wellness app)
4. **Target audience**: Select appropriate options

### 3. Upload AAB
1. Go to "Production" → "Releases" → "Create new release"
2. Upload the `app-release.aab` file
3. Add release notes
4. Review and roll out to production

### 4. Complete Setup
1. **Pricing & distribution**: Set as free, select countries
2. **Content guidelines**: Confirm compliance
3. **App content**: No sensitive content
4. **Store settings**: Basic setup

## Tips JSON Format
The app loads tips from `app/src/main/assets/tips.json`:
```json
[
  {
    "title": "Stay Hydrated",
    "body": "Drink a glass of water first thing in the morning to kickstart your metabolism."
  },
  ...
]
```

## Testing
- Test on Android 6.0+ devices/emulators
- Verify tips change daily
- Test offline functionality
- Verify no crashes on launch

## Notes
- The app uses day-of-year (1-365) to select tips
- With 30+ tips, it cycles for over a month before repeating
- No internet permission required
- No analytics, ads, or tracking
- Simple solid color app icon included