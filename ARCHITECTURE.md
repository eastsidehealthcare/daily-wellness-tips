# Minimal Architecture - Daily Wellness Tips
## Bare Minimum for Play Store Publishing

### Architecture: Single Activity, No Architecture
```
MainActivity (does everything)
├── onCreate(): Load JSON, display tip
├── loadTips(): Read from assets
└── getDailyTip(): Simple day-based selection
```

### File Structure (Minimal)
```
app/
├── src/main/
│   ├── java/com/example/dailywellnesstips/
│   │   └── MainActivity.kt    # Only class needed
│   ├── res/
│   │   ├── layout/
│   │   │   └── activity_main.xml
│   │   └── values/
│   │       └── strings.xml
│   └── assets/
│       └── tips.json          # 30 tips
└── build.gradle
```

### MainActivity.kt (Simplified)
```kotlin
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        val tips = loadTips()
        val todayTip = getDailyTip(tips)
        
        findViewById<TextView>(R.id.tipTitle).text = todayTip.title
        findViewById<TextView>(R.id.tipBody).text = todayTip.body
        findViewById<TextView>(R.id.dayInfo).text = "Day ${getDayOfYear()}"
    }
    
    private fun loadTips(): List<Tip> {
        // Simple JSON parsing without Gson
        val json = assets.open("tips.json").bufferedReader().use { it.readText() }
        return parseJsonManually(json) // Basic parsing
    }
    
    private fun getDailyTip(tips: List<Tip>): Tip {
        val day = getDayOfYear()
        return tips[day % tips.size]
    }
    
    private fun getDayOfYear(): Int {
        return Calendar.getInstance().get(Calendar.DAY_OF_YEAR)
    }
}

data class Tip(val title: String, val body: String)
```

### activity_main.xml (Simplified)
```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="24dp"
    android:orientation="vertical">
    
    <TextView
        android:id="@+id/tipTitle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="24sp"
        android:textStyle="bold" />
        
    <TextView
        android:id="@+id/tipBody"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="16sp"
        android:layout_marginTop="16dp" />
        
    <TextView
        android:id="@+id/dayInfo"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="14sp"
        android:layout_marginTop="32dp"
        android:textColor="@android:color/darker_gray" />
</LinearLayout>
```

### tips.json (Minimal)
```json
[
  {"title": "Drink Water", "body": "Start your day with a glass of water."},
  {"title": "Sleep Well", "body": "Aim for 7-8 hours of sleep tonight."},
  {"title": "Take a Walk", "body": "Go for a 10-minute walk today."},
  // ... 27 more simple tips
]
```

### build.gradle (Minimal)
```gradle
android {
    compileSdk 36
    defaultConfig {
        minSdk 23
        targetSdk 36
        versionCode 1
        versionName "1.0"
    }
    buildTypes {
        release {
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android.txt')
        }
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
}
```

### What We're NOT Doing
- ❌ No ViewModel
- ❌ No Repository pattern
- ❌ No LiveData/StateFlow
- ❌ No Coroutines
- ❌ No Dependency Injection
- ❌ No Unit Tests
- ❌ No Error Handling (beyond try-catch)
- ❌ No Caching
- ❌ No Background Threads
- ❌ No Complex JSON parsing (manual parsing only)

### What We ARE Doing
- ✅ Single class (MainActivity)
- ✅ Direct JSON reading in onCreate()
- ✅ Basic UI with 3 TextViews
- ✅ Simple day calculation
- ✅ ProGuard minification
- ✅ Signed AAB output

### Play Store Compliance Checklist
- [ ] **App doesn't crash** - Basic try-catch around JSON parsing
- [ ] **No permissions** - Zero permission requests
- [ ] **Privacy policy** - Simple "We don't collect any data"
- [ ] **Content rating** - Everyone (no mature content)
- [ ] **Target SDK** - 36 (current)
- [ ] **App size** - <2MB (no images, minimal resources)
- [ ] **No deceptive behavior** - App does exactly what it says

### Development Steps (2 hours max)
1. Create new Android Studio project
2. Add activity_main.xml with 3 TextViews
3. Create tips.json with 30 simple tips
4. Write MainActivity.kt with basic logic
5. Test on emulator (launch, verify tip shows)
6. Build signed AAB
7. Create Play Store assets (icon, screenshots, description)

### Risk: Will This Pass Review?
**Yes**, because:
1. No permissions = fewer rejection reasons
2. No internet = no network-related issues
3. Simple content = no copyright concerns
4. Small size = faster review
5. No ads = no ad policy violations
6. No user data = no privacy violations

### If Rejected (Fallback)
1. Add basic error handling (try-catch)
2. Add loading state (ProgressBar)
3. Add "Retry" button if JSON fails
4. Resubmit

### Final Deliverable
- **APK/AAB**: <2MB
- **Classes**: 1 (MainActivity)
- **Files**: <10 total
- **Development time**: 2-4 hours
- **Goal**: Published on Play Store within 24 hours