[app]

# (str) Title of your application
title = 台鐵查詢

# (str) Package name
package.name = railwayapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# 💡 補上 openssl，這是 requests 與 urllib3 進行 HTTPS 網路請求所必需的底層庫
requirements = python3,kivy==2.3.0,openssl,requests,beautifulsoup4,certifi,urllib3,chardet,idna

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

# 💡 指定相容性最好的 NDK 版本
android.ndk = 25b

# 💡 鎖定 64 位元架構
android.archs = arm64-v8a

# (bool) Accept SDK license
android.accept_sdk_license = True
