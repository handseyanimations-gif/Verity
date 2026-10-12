# Flat Verity (Fabric, Minecraft 26.3) - singleplayer

## EASIEST: get the .jar with GitHub (free, no installs)
1. Make a free GitHub account, create a new repository, and upload everything in this folder (including the hidden .github folder).
2. Open the repository's **Actions** tab -> "Build mod jar" -> **Run workflow**. (It also runs automatically when you upload.)
3. When it finishes, open the run and download the **flatverity-jar** artifact. Unzip it: the jar (without "-sources") goes in your mods folder with Fabric API.
It looks up the right Fabric versions for Minecraft 26.3 by itself (resolve_versions.py). If the run fails, open the log and send me the red error lines.
Or build locally: install JDK 25 + Python 3 + Gradle, then run build.bat (Windows) or build.sh.

## Build (needs internet once)
1. Copy the current Loom / loader / Fabric API versions for 26.3 from https://fabricmc.net/develop into gradle.properties (the -CHECK lines).
2. `./gradlew build`  ->  build/libs/flatverity-1.0.0.jar  -> put in .minecraft/mods with Fabric API.

## Use
- Ctrl+0: menu (Gemini key + model, Fish Audio key + voice ID, nickname, toggles, relationship status).
- Talk: hold V (push-to-talk, transcript appears in chat), type `v: hello` in chat, or use the menu box.
- `/verity` brings him to you. `/verity trust` shows trust. `/verity monster` summons the Tall One (test).
- Without any key he still follows/stays, understands comfort/apologies and warns you about danger.

## Relationship (saved per world in <world>/flatverity.json)
trust -100..100, attachment 0..100, possessiveness 0..100 (baseline by day, damped by trust), comfort, grievance.
Days are counted from GAME time (sleeping can't skip them). Days 1-3 are completely normal; Day 4+ gradually possessive.
The AI only classifies your intent; this mod's code applies capped, cooldown-limited changes.

## Not included yet
Flashlight/dark nights, grass desaturation, stand/room placement tracking, villager/pet jealousy, multiplayer.

## Added in this round
Hide and seek (he offers; say yes, or just say "let's play hide and seek"), blinking red mic dot while holding V, system-voice fallback,
nextbot Tall One (always faces you, climbs, crouches/crawls, breaks wood/leaves/glass, Darkness while chasing),
Monster / Possessive switches in Ctrl+0, exploration comments, time-of-day lines, home = your bed, random item variants,
5% chest prank on join, and the last conversation is saved with the world.

Also: reassurance (he asks "better to be with me, right?" from Day 5; answer yes/no), death reactions (sorry first, then teasing + a tip),
evolving personality notes (/verity personality) that are also written into memory.

## Making the .jar without my help
1. Go to https://fabricmc.net/develop, choose Minecraft 26.3, tick "Fabric API" and "Split client and common sources", download, unzip.
2. Copy this project's `src/` folder over the template's `src/` (replace it), keep the template's build.gradle / gradle.properties / gradlew.
3. In a terminal there: `./gradlew build` (Windows: `gradlew build`). The jar is in build/libs/ (use the one WITHOUT "-sources").
