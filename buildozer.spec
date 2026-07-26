[app]

# (str) Title of your application
title = 台鐵查詢

# (str) Package name
package.name = railwayapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.3.0,requests,beautifulsoup4,certifi,urllib3,chardet,idna

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (int) Android NDK API
android.ndk_api = 21

# (list) 💡 關鍵修復：只針對現代 64 位元 Android 設備編譯，防止多架構編譯失敗
android.archs = arm64-v8a

# (bool) Accept SDK license
android.accept_sdk_license = True
