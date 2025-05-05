#ifdef ESP32
  #include <WiFi.h>
#else
  #include <ESP8266WiFi.h>
#endif
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

// Ganti dengan kredensial jaringan WiFi Anda
const char* ssid = "Ropig Ganteng";
const char* password = "@inpopassword_";

// Ganti dengan Token dan Chat ID bot Telegram Anda
#define BOTtoken "8149665854:AAGMs7vA0F0LxnCFWofFLTMwMZpe5agrj7U"
#define CHAT_ID "903023873"

#ifdef ESP8266
  X509List cert(TELEGRAM_CERTIFICATE_ROOT);
#endif

WiFiClientSecure client;
UniversalTelegramBot bot(BOTtoken, client);

// Periksa pesan setiap 1 detik
int botRequestDelay = 1000;
unsigned long lastTimeBotRan;

const int ledPin = 2;
bool ledState = LOW;

// Fungsi untuk mengirim status koneksi ke Telegram
void sendWiFiStatus() {
  String message;
  
  if (WiFi.status() == WL_CONNECTED) {
    message = "✅ ESP32 Connected to WiFi!\n";
    message += "📡 SSID: " + String(ssid) + "\n";
    message += "📍 IP Address: " + WiFi.localIP().toString() + "\n";
    message += "⏳ Connected at: " + String(millis()) + " ms";
  } else {
    message = "⚠️ WiFi Connection Failed! Check your network.";
  }
  
  Serial.println(message);
  bot.sendMessage(CHAT_ID, message, "");
}

// Fungsi untuk menangani pesan masuk
void handleNewMessages(int numNewMessages) {
  Serial.println("handleNewMessages");
  Serial.println(String(numNewMessages));

  for (int i = 0; i < numNewMessages; i++) {
    String chat_id = String(bot.messages[i].chat_id);
    if (chat_id != CHAT_ID) {
      bot.sendMessage(chat_id, "❌ Unauthorized user", "");
      continue;
    }

    String text = bot.messages[i].text;
    Serial.println("Received: " + text);

    String from_name = bot.messages[i].from_name;

    if (text == "/start") {
      String welcome = "👋 Welcome, " + from_name + ".\n";
      welcome += "Use these commands to control your device:\n\n";
      welcome += "💡 /led_on - Turn LED ON\n";
      welcome += "💡 /led_off - Turn LED OFF\n";
      welcome += "📊 /state - Check LED state\n";
      welcome += "📶 /wifi_status - Check WiFi status\n";
      bot.sendMessage(chat_id, welcome, "");
    }

    if (text == "/led_on") {
      bot.sendMessage(chat_id, "💡 LED turned ON", "");
      ledState = HIGH;
      digitalWrite(ledPin, ledState);
    }

    if (text == "/led_off") {
      bot.sendMessage(chat_id, "💡 LED turned OFF", "");
      ledState = LOW;
      digitalWrite(ledPin, ledState);
    }

    if (text == "/state") {
      if (digitalRead(ledPin)) {
        bot.sendMessage(chat_id, "💡 LED is ON", "");
      } else {
        bot.sendMessage(chat_id, "💡 LED is OFF", "");
      }
    }

    if (text == "/wifi_status") {
      sendWiFiStatus();
    }
  }
}

void setup() {
  Serial.begin(115200);
  
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, ledState);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  
  Serial.println("🔄 Connecting to WiFi...");
  bot.sendMessage(CHAT_ID, "🔄 ESP32 is connecting to WiFi...", "");

  unsigned long startAttemptTime = millis();

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
    
    if (millis() - startAttemptTime > 30000) {
      Serial.println("\n❌ WiFi Connection Timeout!");
      bot.sendMessage(CHAT_ID, "❌ WiFi connection timeout! Check your credentials.", "");
      return;
    }
  }

  Serial.println("\n✅ Connected!");
  sendWiFiStatus();
}

void loop() {
  // Periksa apakah koneksi WiFi masih ada
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("⚠️ WiFi Disconnected! Reconnecting...");
    bot.sendMessage(CHAT_ID, "⚠️ WiFi Disconnected! Attempting to reconnect...", "");
    WiFi.begin(ssid, password);
    
    unsigned long startReconnectTime = millis();
    while (WiFi.status() != WL_CONNECTED) {
      delay(1000);
      Serial.print(".");
      
      if (millis() - startReconnectTime > 30000) {
        Serial.println("\n❌ Reconnection Failed!");
        bot.sendMessage(CHAT_ID, "❌ Failed to reconnect to WiFi!", "");
        return;
      }
    }

    Serial.println("\n✅ Reconnected!");
    sendWiFiStatus();
  }

  // Periksa pesan Telegram
  if (millis() > lastTimeBotRan + botRequestDelay) {
    int numNewMessages = bot.getUpdates(bot.last_message_received + 1);

    while (numNewMessages) {
      Serial.println("📩 New message received!");
      handleNewMessages(numNewMessages);
      numNewMessages = bot.getUpdates(bot.last_message_received + 1);
    }
    lastTimeBotRan = millis();
  }
}
