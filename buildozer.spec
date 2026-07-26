# 必須加入 cython 與套件
requirements = python3,kivy==2.3.0,requests,beautifulsoup4,certifi,urllib3,chardet,idna

# 指定 Android API 版本（避免版本衝擊）
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.accept_sdk_license = True
