# Build and Release Instructions

## Prerequisites

1. **Android Studio** (latest version recommended)
2. **Java Development Kit (JDK)** 11 or higher
3. **Android SDK** with:
   - SDK Platform for API 36 (Android 14)
   - Build-Tools for API 36

## Opening the Project

1. Open Android Studio
2. Select "Open" or "Open Project"
3. Navigate to the `daily-wellness-tips` folder
4. Click "Open"
5. Wait for Gradle sync to complete (may take a few minutes on first open)

## Generating Signing Keystore

If you don't have a signing keystore, create one:

### On macOS/Linux:
```bash
keytool -genkey -v -keystore daily-wellness-tips.jks \
  -keyalg RSA -keysize 2048 -validity 10000 \
  -alias dailywellness
```

### On Windows:
```bash
keytool -genkey -v -keystore daily-wellness-tips.jks ^
  -keyalg RSA -keysize 2048 -validity 10000 ^
  -alias dailywellness
```

You'll be prompted for:
- Keystore password (remember this!)
- First and last name
- Organizational unit
- Organization
- City/Locality
- State/Province
- Country code (US)

**Important**: Keep the keystore file safe! You'll need it for all future updates.

## Setting Up Signing Configuration

1. Copy the generated `daily-wellness-tips.jks` file to the project root folder
2. Create a file called `keystore.properties` in the project root:
```
storePassword=your_store_password
keyPassword=your_key_password
keyAlias=dailywellness
storeFile=daily-wellness-tips.jks
```
3. Replace `your_store_password` and `your_key_password` with the passwords you set

**Security Note**: Add `keystore.properties` to `.gitignore` to avoid committing passwords.

## Building the App

### Option 1: Using Android Studio (Recommended)

1. **Build Debug APK** (for testing):
   - Build → Build Bundle(s) / APK(s) → Build APK(s)
   - APK will be at: `app/build/outputs/apk/debug/app-debug.apk`

2. **Build Release AAB** (for Play Store):
   - Build → Generate Signed Bundle / APK
   - Select "Android App Bundle"
   - Click "Next"
   - Fill in keystore details (or browse to your keystore file)
   - Click "Next"
   - Select release build type
   - Click "Finish"
   - AAB will be at: `app/build/outputs/bundle/release/app-release.aab`

### Option 2: Using Command Line

1. **Build Debug APK**:
   ```bash
   ./gradlew assembleDebug
   ```

2. **Build Release AAB**:
   ```bash
   ./gradlew bundleRelease
   ```

3. **Build Release APK**:
   ```bash
   ./gradlew assembleRelease
   ```

Output locations:
- AAB: `app/build/outputs/bundle/release/app-release.aab`
- APK: `app/build/outputs/apk/release/app-release.apk`

## Testing the App

### On Emulator:
1. In Android Studio, click "Run" (green triangle)
2. Select a device (create one if needed)
3. Minimum: API 23 (Android 6.0)
4. Recommended: API 33+ for latest features

### On Physical Device:
1. Enable Developer Options:
   - Settings → About Phone → Tap "Build Number" 7 times
2. Enable USB Debugging:
   - Settings → Developer Options → USB Debugging
3. Connect device via USB
4. In Android Studio, select your device and click "Run"

### Testing Tips:
1. Verify tips change daily (you can test by changing device date)
2. Test offline (enable airplane mode)
3. Test on different screen sizes
4. Verify no crashes on launch

## Preparing for Play Store

### 1. Create App Icons
See `ICON_INSTRUCTIONS.md` for detailed icon requirements.

### 2. Update App Information
In `app/build.gradle`:
```gradle
defaultConfig {
    applicationId "com.example.dailywellnesstips"  // Change to your package name
    versionCode 1  // Increment for each update
    versionName "1.0"  // User-visible version
}
```

### 3. Update Strings
In `app/src/main/res/values/strings.xml`:
- Update app name if desired
- Add translations if supporting multiple languages

### 4. Test Thoroughly
- [ ] App launches without crashes
- [ ] Tips display correctly
- [ ] Daily tip changes properly
- [ ] Works offline
- [ ] No memory leaks
- [ ] Battery usage is minimal

## Uploading to Play Console

### 1. Create App Listing
1. Go to [Google Play Console](https://play.google.com/console)
2. Click "Create app"
3. Fill in:
   - App name: "Daily Wellness Tips"
   - Default language: English
   - App or game: App
   - Free or paid: Free

### 2. Prepare Store Listing
1. **App details**:
   - Short description: "Daily health and wellness tips"
   - Full description: Write engaging description about the app
   - Category: Health & Fitness

2. **Graphics**:
   - App icon: 512x512 px
   - Feature graphic: 1024x500 px
   - Screenshots: 3-8 screenshots of different screens

3. **Content rating**:
   - Complete questionnaire (non-medical wellness app)

### 3. Upload AAB
1. Go to "Production" → "Releases" → "Create new release"
2. Upload `app-release.aab`
3. Add release notes (what's new in this version)
4. Review and roll out to production

### 4. Complete Setup
1. **Pricing & distribution**: Set as free, select countries
2. **App content**: No sensitive content
3. **Store settings**: Basic setup complete

## Post-Release

### 1. Monitor Reviews
- Check Play Console for user reviews
- Respond to feedback
- Address any issues

### 2. Update App
1. Make changes in code
2. Increment `versionCode` in `build.gradle`
3. Update `versionName`
4. Build new AAB
5. Upload to Play Console as new release

### 3. Analytics (Optional)
Consider adding basic analytics to understand usage:
- Firebase Analytics (free)
- Or custom event tracking

## Troubleshooting

### Common Issues:

1. **Build fails with "keystore not found"**:
   - Verify `keystore.properties` file exists
   - Check file paths are correct

2. **App crashes on launch**:
   - Check Logcat in Android Studio
   - Verify JSON file is properly formatted
   - Test on different API levels

3. **Tips not changing daily**:
   - Verify device date is correct
   - Test by changing device date manually

4. **ProGuard issues**:
   - Check `proguard-rules.pro` for necessary keep rules
   - Test release build thoroughly

### Getting Help:
- [Android Developer Documentation](https://developer.android.com/docs)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/android)
- [Google Play Console Help](https://support.google.com/googleplay/android-developer)