package com.example.dailywellnesstips

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.dailywellnesstips.databinding.ActivityMainBinding
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import java.util.Calendar

data class Tip(
    val title: String,
    val body: String
)

class MainActivity : AppCompatActivity() {
    
    private lateinit var binding: ActivityMainBinding
    private val gson = Gson()
    private var tips: List<Tip> = emptyList()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        loadTips()
        displayDailyTip()
    }
    
    private fun loadTips() {
        try {
            val jsonString = assets.open("tips.json").bufferedReader().use { it.readText() }
            val listType = object : TypeToken<List<Tip>>() {}.type
            tips = gson.fromJson(jsonString, listType)
        } catch (e: Exception) {
            e.printStackTrace()
            // Fallback to default tips if JSON fails to load
            tips = getDefaultTips()
        }
    }
    
    private fun displayDailyTip() {
        if (tips.isEmpty()) {
            binding.tipTitleTextView.text = getString(R.string.error_loading)
            binding.tipBodyTextView.text = ""
            binding.dayInfoTextView.text = ""
            return
        }
        
        val dayOfYear = getDayOfYear()
        val tipIndex = (dayOfYear - 1) % tips.size
        val tip = tips[tipIndex]
        
        binding.tipTitleTextView.text = tip.title
        binding.tipBodyTextView.text = tip.body
        binding.dayInfoTextView.text = "Day $dayOfYear of 365 • Tip ${tipIndex + 1} of ${tips.size}"
    }
    
    private fun getDayOfYear(): Int {
        val calendar = Calendar.getInstance()
        return calendar.get(Calendar.DAY_OF_YEAR)
    }
    
    private fun getDefaultTips(): List<Tip> {
        return listOf(
            Tip("Stay Hydrated", "Drink a glass of water first thing in the morning to kickstart your metabolism."),
            Tip("Quality Sleep", "Aim for 7-9 hours of sleep each night in a cool, dark room for optimal rest."),
            Tip("Morning Walk", "Take a 15-minute walk after breakfast to improve digestion and boost energy."),
            Tip("Deep Breathing", "Practice 5 minutes of deep breathing to reduce stress and increase focus."),
            Tip("Protein Power", "Include protein with every meal to maintain energy levels and muscle health.")
        )
    }
}