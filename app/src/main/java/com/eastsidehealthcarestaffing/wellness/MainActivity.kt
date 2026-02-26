package com.eastsidehealthcarestaffing.wellness

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import org.json.JSONArray
import java.util.Calendar

class MainActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        try {
            val tips = loadTips()
            val todayTip = getDailyTip(tips)
            
            findViewById<TextView>(R.id.tipTitle).text = todayTip.title
            findViewById<TextView>(R.id.tipBody).text = todayTip.body
            findViewById<TextView>(R.id.dayInfo).text = "Tip ${getDayIndex(tips.size)} of ${tips.size}"
        } catch (e: Exception) {
            // If anything fails, show fallback text
            findViewById<TextView>(R.id.tipTitle).text = "Daily Wellness Tip"
            findViewById<TextView>(R.id.tipBody).text = "Take a deep breath and relax."
            findViewById<TextView>(R.id.dayInfo).text = "Tip 1 of 30"
        }
    }
    
    private fun loadTips(): List<Tip> {
        val json = assets.open("tips.json").bufferedReader().use { it.readText() }
        val jsonArray = JSONArray(json)
        val tips = mutableListOf<Tip>()
        
        for (i in 0 until jsonArray.length()) {
            val obj = jsonArray.getJSONObject(i)
            tips.add(Tip(
                obj.getString("title"),
                obj.getString("body")
            ))
        }
        
        return tips
    }
    
    private fun getDailyTip(tips: List<Tip>): Tip {
        val index = getDayIndex(tips.size)
        return tips[index]
    }
    
    private fun getDayIndex(totalTips: Int): Int {
        val calendar = Calendar.getInstance()
        val dayOfYear = calendar.get(Calendar.DAY_OF_YEAR)
        return (dayOfYear - 1) % totalTips
    }
}

data class Tip(val title: String, val body: String)