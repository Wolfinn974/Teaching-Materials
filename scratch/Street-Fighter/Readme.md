# 🥊 Street Fighter-like (Scratch)

> Build a local 2-player fighting game with attacks, health bars, and simple combat logic.

[![Scratch Demo](https://img.shields.io/badge/Scratch-Demo-orange?logo=scratch)](https://scratch.mit.edu/projects/1278203582)

---

## 📋 Quick Info

|                   |                                                                         |
| ----------------- | ----------------------------------------------------------------------- |
| **Tool**          | Scratch                                                                 |
| **Target age**    | 9 – 15 years old                                                        |
| **Level**         | Intermediate                                                            |
| **Duration**      | 3–5 sessions × ~1.5h                                                    |
| **Prerequisites** | Keyboard input, variables, conditionals, and basic animation in Scratch |

---

## 🎯 Learning Objectives

By the end of this project, students will be able to:

* [ ] Control two characters independently
* [ ] Create attack animations and cooldowns
* [ ] Implement hit detection using hitboxes
* [ ] Manage player health and simple win/lose conditions
* [ ] Use variables to control game state
* [ ] Balance mechanics for fair gameplay

---

## 🗂 Folder Structure

```text id="sf-structure"
📁 street-fighter-like/
├── 📄 README.md               — this file
├── 📄 lesson-plan_bil.md      — detailed session breakdown
├── 📁 starter/                — starting file for students
└──📁 demo/                    — complete version (instructor only)
```

---

## 🔗 Demo

👉 Try the demo on Scratch:
https://scratch.mit.edu/projects/1278203582

---

## 🚀 How to Use

1. Open the starter project in Scratch.
2. Follow `lesson-plan_bil.md` to implement the mechanics progressively.
3. Keep the `/demo` private until the end of the project.

---

## 📝 Instructor Notes

* This project introduces **interaction between multiple sprites** and more complex timing.
* Strong focus on:

  * hitboxes vs hurtboxes
  * fairness & balance
  * timing and cooldowns
  * visual feedback on hit

Common blockers:

* Students try to detect collision using full sprite instead of a small hitbox → imprecise hits.
* Attacks feel unfair if no cooldown or if hitboxes are too big.
* Players overlap and get stuck → add pushback or separation logic.

Tips:

* Start with one attack per character before adding combos.
* Debug with visual hitboxes first (visible rectangles) → hide them later.
* Encourage playtesting between students to adjust balancing.

---

## 📄 License

This material is free to use for non-commercial educational purposes.
