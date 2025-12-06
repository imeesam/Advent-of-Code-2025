
---

# 🎄 Advent of Code 2025 

This repository contains my solutions to **Advent of Code 2025**, where I have currently solved **6 problems (Days 1–5)**.
Each problem includes **Part 1** and **Part 2**, and the corresponding code solutions are available in this repository.

---

## ⭐ Progress

| Day | Problem Title       | Stars Earned | Status    |
| --- | ------------------- | ------------ | --------- |
| 1   | Secret Entrance     | ⭐⭐           | Completed |
| 2   | Gift Shop           | ⭐⭐           | Completed |
| 3   | Lobby               | ⭐⭐           | Completed |
| 4   | Printing Department | ⭐⭐           | Completed |
| 5   | Cafeteria           | ⭐⭐           | Completed |

---

# 📘 Problem Summaries & My Results

Below is a short explanation of each problem and the answers I achieved.

---

## **🎯 Day 1 — Secret Entrance**

The safe uses a circular dial (0–99). You follow a list of left/right rotations and count:

### **Part 1:**

Count how many times the dial **ends** at `0` after any rotation.
**✔ My Answer:** `1048`

### **Part 2:**

Now count **every click** that causes the dial to point at `0`, even during rotation.
**✔ My Answer:** `6498`



---

## **🎯 Day 2 — Gift Shop**

You are given large numeric ID ranges. Some IDs are invalid if they contain a pattern
where a sequence of digits repeats.

Examples:

* `11` → repeated `1`
* `6464` → repeated `64`
* `123123123` → repeated `123` three times

### **Part 1:**

Find IDs made of a repeated sequence **exactly twice**.
**✔ My Answer:** `15873079081`

### **Part 2:**

Now IDs are invalid if the sequence is repeated **two or more times**.
**✔ My Answer:** `22617871034`



---

## **🎯 Day 3 — Lobby**

Each line is a “battery bank” consisting of digits (1–9).
You must create the **largest possible number** by turning on batteries:

### **Part 1:**

Turn on **exactly two** batteries per bank, forming a 2-digit number.
Sum all banks’ maximum 2-digit outputs.
**✔ My Answer:** `17109`

### **Part 2:**

Turn on **exactly twelve** batteries per bank (forming a 12-digit number).
**✔ My Answer:** `169347417057382`


---

## **🎯 Day 4 — Printing Department**

Given a grid of rolls of paper (`@` symbols), a forklift can access a roll only if
**fewer than 4 adjacent neighbors** (in 8 directions) are also rolls.

You must count how many rolls are accessible.


---

## **🎯 Day 5 — Cafeteria**

You get:

1. A list of **fresh ingredient ID ranges**
2. A list of **available ingredient IDs**

An ingredient is “fresh” if it appears in **any** of the ranges.

### **Part 1:**

Count how many available IDs are fresh.
**✔ My Answer:** `577`

### **Part 2:**

Ignore the list of available IDs.
Count **all numbers covered by any range**, merging overlaps.
**✔ My Answer:** `350513176552950`

---

