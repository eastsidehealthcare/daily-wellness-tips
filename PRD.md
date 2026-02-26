# Minimal PRD - Daily Wellness Tips Android App
## Version: 1.0 - Bare Minimum for Play Store

### Purpose
Create the simplest possible Android app that will pass Google Play Store publishing requirements.

### Core Requirements (Must Have)
1. **Single Screen**: One activity showing text
2. **Daily Tip**: Show different text each day (hardcoded)
3. **No Internet**: Zero network permissions
4. **No Crashes**: Must not crash on launch
5. **Basic UI**: Text display only, no images
6. **Play Store Compliant**: Pass all automated checks

### Technical Minimums
- **Language**: Kotlin
- **Min SDK**: 23 (covers ~85% of devices)
- **Target SDK**: 36 (current)
- **Permissions**: None
- **Dependencies**: AndroidX only (no third-party libraries)
- **Size**: <2MB APK

### App Content
- **30 tips** (one per day for a month)
- **Simple JSON** file in assets folder
- **Tip format**: Title + 1-2 sentence description
- **Categories**: Basic wellness (hydration, sleep, exercise, nutrition)

### Play Store Requirements Checklist
- [ ] App doesn't crash on launch
- [ ] No sensitive permissions requested
- [ ] Privacy policy (can be simple "no data collected")
- [ ] App icon (512x512, 1024x1024)
- [ ] Feature graphic (1024x500)
- [ ] Screenshots (minimum 2)
- [ ] App description (short, simple)
- [ ] Content rating (Everyone)
- [ ] Target audience (General)
- [ ] No copyright violations
- [ ] No deceptive behavior

### Development Time: 2-4 hours
1. Create project in Android Studio
2. Add JSON file with 30 tips
3. Create single activity to display tip
4. Add basic day-of-year logic
5. Test on emulator
6. Build signed AAB
7. Submit to Play Console

### What We're Removing
- ❌ No user accounts
- ❌ No notifications
- ❌ No settings screen
- ❌ No analytics
- ❌ No error handling beyond basic
- ❌ No theming options
- ❌ No sharing features
- ❌ No favorites/bookmarks
- ❌ No categories/filtering
- ❌ No splash screen
- ❌ No loading states
- ❌ No complex architecture

### What We're Keeping
- ✅ Single activity
- ✅ Text display
- ✅ Day-based tip rotation
- ✅ Basic JSON parsing
- ✅ Material Design basic components
- ✅ ProGuard optimization
- ✅ Signed release build

### Success Criteria
- **Passes Play Store review** (primary goal)
- **APK size <2MB**
- **No crashes reported**
- **Published within 24 hours**

### Next Steps
1. Create ultra-simple architecture document
2. Write minimal code
3. Test basic functionality
4. Create Play Store assets
5. Submit for review