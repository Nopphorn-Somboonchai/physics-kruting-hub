# Physics M.6 - Learning WebApp Workflow

## Project Overview

ระบบเว็บเรียนรู้ฟิสิกส์ ม.6 เล่ม 5 ตามหลักสูตร สสวท.

Technology Stack

* HTML
* CSS
* JavaScript
* Firebase
* Vercel

---

# Project Structure

```text
physics-m6/

index.html

chapter15/
│
├── part1.html
└── part2.html

chapter16/
│
├── web16-01.html
├── web16-02.html
├── web16-03.html
└── web16-04.html

chapter17/
│
├── web17-01.html
├── web17-02.html
├── web17-03.html
└── web17-04.html

assets/
├── css/
├── js/
├── images/
└── icons/

firebase/
└── config.js
```

---

# Chapter 15 : แม่เหล็กและไฟฟ้า (Completed)

## WEB-15-01 : part1.html

```text
15.1 สนามแม่เหล็ก
15.2 แรงแม่เหล็ก
15.3 โมเมนต์ของแรงคู่ควบ
```

## WEB-15-02 : part2.html

```text
15.4 กระแสไฟฟ้าเหนี่ยวนำและอีเอ็มเอฟเหนี่ยวนำ
15.5 ไฟฟ้ากระแสสลับ
```

Status

* Completed ✅ (part1.html & part2.html)

---

# Chapter 16 : ความร้อนและแก๊ส

## WEB-16-01 : ความร้อน

```text
16.1 ความร้อน

16.1.1 อุณหภูมิ
16.1.2 ความจุความร้อนและความร้อนจำเพาะ
16.1.3 ความร้อนแฝง
16.1.4 การถ่ายโอนความร้อนและสมดุลความร้อน
```

Status

* Pending

---

## WEB-16-02 : แก๊สอุดมคติ

```text
16.2 แก๊สอุดมคติ

16.2.1 แบบจำลองแก๊สอุดมคติ
16.2.2 กฎของแก๊สอุดมคติ
```

Status

* Pending

---

## WEB-16-03 : ทฤษฎีจลน์ของแก๊ส

```text
16.3 ทฤษฎีจลน์ของแก๊ส

16.3.1 ความสัมพันธ์ระหว่างความดันและอัตราเร็ว RMS
16.3.2 ความสัมพันธ์ระหว่างพลังงานจลน์เฉลี่ยของแก๊สกับอุณหภูมิ
16.3.3 ความสัมพันธ์ระหว่างอัตราเร็ว RMS ของโมเลกุลแก๊สกับอุณหภูมิ
```

Status

* Pending

---

## WEB-16-04 : กฎข้อที่หนึ่งของอุณหพลศาสตร์

```text
16.4 กฎข้อที่หนึ่งของอุณหพลศาสตร์

16.4.1 พลังงานภายในระบบ
16.4.2 งานที่ทำโดยแก๊ส
16.4.3 กฎข้อที่หนึ่งของอุณหพลศาสตร์
16.4.4 การประยุกต์ของอุณหพลศาสตร์
```

Status

* Pending

---

# Chapter 17 : ของแข็งและของไหล

## WEB-17-01 : ของแข็งและสภาพยืดหยุ่น

```text
17.1 ของแข็งและสภาพยืดหยุ่นของของแข็ง

17.1.1 สภาพยืดหยุ่นของของแข็ง
17.1.2 ความเค้นและความเครียด
17.1.3 มอดุลัสของยัง
17.1.4 การประยุกต์ใช้สภาพยืดหยุ่น
```

Status

* Pending

---

## WEB-17-02 : ความตึงผิวและความหนืด

```text
17.2 ความตึงผิวและความหนืดของของเหลว

17.2.1 ความตึงผิวของของเหลว
17.2.2 ความหนืดของของเหลว
```

Status

* Pending

---

## WEB-17-03 : ของไหลสถิต

```text
17.3 ของไหลสถิต

17.3.1 ความดันในของไหล
17.3.2 อุปกรณ์ที่ใช้วัดความดัน
17.3.3 แรงพยุงจากของไหล
```

Status

* Pending

---

## WEB-17-04 : พลศาสตร์ของของไหล

```text
17.4 พลศาสตร์ของของไหล

17.4.1 ของไหลอุดมคติ
17.4.2 สมการความต่อเนื่อง
17.4.3 สมการแบร์นูลี
```

Status

* Pending

---

# Standard Template For Every Learning Web

Every generated lesson website must include:

```text
1. Hero Section

2. จุดประสงค์การเรียนรู้

3. เนื้อหาหลัก

4. Infographic

5. Interactive Simulation

6. ตัวอย่างโจทย์

7. แบบฝึกหัด

8. Quiz 10 ข้อ

9. สรุปบทเรียน

10. ปุ่มกลับหน้าหลัก
```

---

# Firebase Architecture

```text
Firebase

users
progress
quiz_scores
achievements
analytics
```

Purpose

* User Login
* Learning Progress Tracking
* Quiz Score Tracking
* Achievement System
* Learning Analytics

---

# Main Portal Website

```text
Physics M.6 Volume 5

บทที่ 15
├── WEB-15-01
└── WEB-15-02

บทที่ 16
├── WEB-16-01
├── WEB-16-02
├── WEB-16-03
└── WEB-16-04

บทที่ 17
├── WEB-17-01
├── WEB-17-02
├── WEB-17-03
└── WEB-17-04
```

---

# Development Roadmap

Phase 1

* WEB-16-01
* WEB-16-02
* WEB-16-03
* WEB-16-04

Phase 2

* WEB-17-01
* WEB-17-02
* WEB-17-03
* WEB-17-04

Phase 3

* Main Portal Website

Phase 4

* Firebase Integration

Phase 5

* PWA Support

Phase 6

* Deploy To Vercel

---

# Final Goal

Physics M.6 Volume 5 Learning Platform

Total Learning Websites

* Chapter 15 = 2 Web Apps
* Chapter 16 = 4 Web Apps
* Chapter 17 = 4 Web Apps

Total = 10 Learning Web Apps

Single Portal + Firebase + PWA + Vercel Deployment
