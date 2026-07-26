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

# 💡 關鍵修復 1：指定最穩定相容的 NDK 版本，防止 r27/r28 編譯報錯
android.ndk = 25b

# 💡 關鍵修復 2：鎖定單一 64 位元架構，加速編譯
android.archs = arm64-v8a

# (bool) Accept SDK license
android.accept_sdk_license = True
