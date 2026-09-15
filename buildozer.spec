[app]

title = Adventure Math Game
package.name = adventuremathgame
package.domain = org.sakshi

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 24
android.archs = arm64-v8a,armeabi-v7a

android.debug_artifact = apk
android.release_artifact = apk

android.accept_sdk_license = True

android.allow_backup = True

android.logcat_filters = *:S python:D

android.permissions = INTERNET

p4a.branch = master


[buildozer]

log_level = 2
warn_on_root = 0
