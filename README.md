# ⚛️ Physics KruTing Hub

<p align="center">
  <b>แพลตฟอร์มการเรียนรู้ฟิสิกส์ระดับชั้นมัธยมศึกษาปีที่ 6 (เล่ม 5) เชิงโต้ตอบ (Interactive Learning Web Apps)</b>
  <br>
  พัฒนาขึ้นตามหลักสูตร สสวท. เพื่อส่งเสริมการเรียนรู้ของนักเรียนยุคดิจิทัล
</p>

<p align="center">
  <a href="https://github.com/nopphorn31/physics-kruting-hub"><img src="https://img.shields.io/github/stars/nopphorn31/physics-kruting-hub?style=social" alt="Stars"></a>
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow" alt="Status">
  <img src="https://img.shields.io/badge/Platform-PWA%20Ready-blue" alt="Platform">
</p>

---

## 🧭 สารบัญ (Table of Contents / Navigation)

ใช้ลิงก์ด้านล่างเพื่อไปยังส่วนต่าง ๆ ของเอกสารได้อย่างรวดเร็ว:

*   [🚀 Features / คุณสมบัติเด่น](#features)
*   [🛠️ Technology Stack / เทคโนโลยีที่ใช้](#tech-stack)
*   [📚 Learning Modules / บทเรียนที่เปิดสอน](#learning-modules)
*   [📋 Standard Learning Template / รูปแบบบทเรียน](#standard-template)
*   [📁 Project Structure / โครงสร้างโฟลเดอร์](#project-structure)
*   [⚙️ Installation / วิธีติดตั้งและรันโปรแกรม](#installation)
*   [🗺️ Project Roadmap / แผนการดำเนินงาน](#roadmap)
*   [🎯 Final Goal / เป้าหมายหลักของโครงการ](#final-goal)
*   [✍️ Author & Info / ผู้พัฒนา](#author)

---

## <a id="features"></a>🚀 Features (คุณสมบัติเด่น)

### 🎮 Interactive Learning Experience
*   **บทเรียนแบบ Interactive:** เรียนรู้เนื้อหาผ่านตัวอักษรและสื่อโต้ตอบที่เป็นมิตรต่อผู้เรียน
*   **Infographic สรุปเนื้อหา:** สรุปประเด็นหลักในรูปแบบอินโฟกราฟิกสวยงามและเข้าใจง่าย
*   **Interactive Simulation:** แบบจำลองจำลองสถานการณ์ทางฟิสิกส์ให้ผู้เรียนได้ทดลองปรับเปลี่ยนค่าและสังเกตผล
*   **โจทย์และแบบฝึกหัด:** มีโจทย์ตัวอย่างพร้อมแสดงวิธีทำแบบทีละขั้นตอน พร้อมแบบฝึกหัดสำหรับฝึกฝน
*   **Quiz 10 ข้อ:** แบบทดสอบประเมินความเข้าใจท้ายบทเรียนแต่ละตอน
*   **สรุปบทเรียน:** แหล่งรวบรวมสูตรและแนวคิดสำคัญแบบสรุปย่อ

### 📈 Learning Progress & Analytics
*   **ติดตามความก้าวหน้าการเรียน:** ระบบจะบันทึกสถานะการอ่านและการเรียนรู้ของแต่ละบทเรียน
*   **บันทึกคะแนนแบบทดสอบ:** เก็บข้อมูลสถิติการทำควิซเพื่อวัดผลพัฒนาการ
*   **ระบบความสำเร็จ (Achievement):** มอบเหรียญหรือตรารางวัลเมื่อบรรลุเป้าหมายการเรียนรู้
*   **Learning Analytics:** ระบบวิเคราะห์การเรียนรู้ เพื่อช่วยสรุปจุดเด่นหรือจุดที่ต้องพัฒนาของผู้เรียน

### ⚡ Modern Web Technology
*   **Responsive Design & Mobile Friendly:** หน้าจอปรับแต่งอย่างลื่นไหลและเหมาะสมกับทุกขนาดอุปกรณ์
*   **Progressive Web App (PWA):** รองรับการติดตั้งลงบนสมาร์ทโฟนหรือคอมพิวเตอร์เพื่อเปิดใช้งานได้รวดเร็วเสมือนแอปเนทีฟ
*   **Fast Loading:** ความเร็วในการดาวน์โหลดหน้าเว็บสูง โหลดส่วนประกอบต่าง ๆ ได้รวดเร็ว
*   **Offline Support:** รองรับการเข้าอ่านหน้าเว็บและทำกิจกรรมพื้นฐานแบบออฟไลน์ (ในส่วนที่รองรับข้อมูลแคช)

---

## <a id="tech-stack"></a>🛠️ Technology Stack (เทคโนโลยีที่ใช้)

| Layer | Technology Badges | Description |
| :--- | :--- | :--- |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) | โครงสร้างหลักและสไตล์ที่ปรับแต่งเองแบบ Vanilla JS ไร้เฟรมเวิร์กเพื่อความเร็วในการโหลดขั้นสุด |
| **Backend & Services** | ![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black) | ใช้ Firebase **Authentication** (ระบุตัวตนผู้ใช้), **Firestore** (บันทึกข้อมูลคะแนนและความก้าวหน้า), และ **Analytics** (วิเคราะห์สถิติผู้เรียน) |
| **Deployment** | ![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white) | ให้บริการโฮสติ้งและปรับแต่งการจัดส่งข้อมูล (Deployment) บน Vercel |

---

## <a id="learning-modules"></a>📚 Learning Modules (บทเรียน)

*คลิกที่หัวข้อเพื่อยืดหรือยุบรายละเอียดของแต่ละบทเรียน (Interactive Toggle / Filtering):*

<details open>
<summary><b>🟢 Chapter 15 : แม่เหล็กและไฟฟ้า (Status: ✅ Completed)</b></summary>
<br>

| รหัสบทเรียน | หัวข้อย่อยและเนื้อหาที่ครอบคลุม |
| :--- | :--- |
| **WEB-15-01** | <ul><li>15.1 สนามแม่เหล็ก</li><li>15.2 แรงแม่เหล็ก</li><li>15.3 โมเมนต์ของแรงคู่ควบ</li></ul> |
| **WEB-15-02** | <ul><li>15.4 กระแสไฟฟ้าเหนี่ยวนำและอีเอ็มเอฟเหนี่ยวนำ</li><li>15.5 ไฟฟ้ากระแสสลับ</li></ul> |

</details>

<details open>
<summary><b>🟡 Chapter 16 : ความร้อนและแก๊ส (Status: 🚧 In Development)</b></summary>
<br>

| รหัสบทเรียน | หัวข้อย่อยและเนื้อหาที่ครอบคลุม |
| :--- | :--- |
| **WEB-16-01** | <ul><li>ความร้อน</li><li>อุณหภูมิ</li><li>ความจุความร้อน</li><li>ความร้อนจำเพาะ</li><li>ความร้อนแฝง</li></ul> |
| **WEB-16-02** | <ul><li>แก๊สอุดมคติ</li><li>กฎของแก๊สอุดมคติ</li></ul> |
| **WEB-16-03** | <ul><li>ทฤษฎีจลน์ของแก๊ส</li><li>ความดันและอัตราเร็ว RMS</li><li>พลังงานจลน์เฉลี่ยของแก๊ส</li></ul> |
| **WEB-16-04** | <ul><li>กฎข้อที่หนึ่งของอุณหพลศาสตร์</li><li>พลังงานภายในระบบ</li><li>งานที่ทำโดยแก๊ส</li></ul> |

</details>

<details open>
<summary><b>🔴 Chapter 17 : ของแข็งและของไหล (Status: 🚧 Planned)</b></summary>
<br>

| รหัสบทเรียน | หัวข้อย่อยและเนื้อหาที่ครอบคลุม |
| :--- | :--- |
| **WEB-17-01** | <ul><li>ของแข็งและสภาพยืดหยุ่น</li><li>ความเค้นและความเครียด</li><li>มอดุลัสของยัง</li></ul> |
| **WEB-17-02** | <ul><li>ความตึงผิว</li><li>ความหนืด</li></ul> |
| **WEB-17-03** | <ul><li>ของไหลสถิต</li><li>ความดัน</li><li>แรงพยุง</li></ul> |
| **WEB-17-04** | <ul><li>พลศาสตร์ของของไหล</li><li>สมการความต่อเนื่อง</li><li>สมการแบร์นูลี</li></ul> |

</details>

---

## <a id="standard-template"></a>📋 Standard Learning Template (รูปแบบบทเรียนมาตรฐาน)

เพื่อความเป็นเอกภาพของเนื้อหา ทุกบทเรียนการเรียนรู้ในระบบจะประกอบไปด้วยหัวข้อมาตรฐาน 10 ส่วน ดังนี้:

1.  **Hero Section** – หน้าต้อนรับและป้ายแนะนำบทเรียน
2.  **จุดประสงค์การเรียนรู้** – ชี้แจงเป้าหมายที่คาดหวังในบทเรียน
3.  **เนื้อหาหลัก** – บทเรียนทฤษฎีและคำอธิบาย
4.  **Infographic** – ภาพอินโฟกราฟิกสรุปเข้าใจง่าย
5.  **Interactive Simulation** – เครื่องมือจำลองทางฟิสิกส์เชิงตอบโต้
6.  **ตัวอย่างโจทย์** – โจทย์ฝึกคำนวณและวิธีคิดอย่างละเอียด
7.  **แบบฝึกหัด** – แบบฝึกหัดทบทวนระหว่างเรียน
8.  **Quiz 10 ข้อ** – แบบทดสอบหลังเรียนเพื่อวัดระดับความรู้
9.  **สรุปบทเรียน** – สรุปคีย์เวิร์ดและสูตรคำนวณที่สำคัญ
10. **ปุ่มกลับหน้าหลัก** – ลิงก์สำหรับเปลี่ยนหน้ากลับไปยังศูนย์รวมบทเรียน (Portal)

---

## <a id="project-structure"></a>📁 Project Structure (โครงสร้างโฟลเดอร์)

```text
physics-kruting-hub/
├── chapter15/            # สื่อการเรียนการสอน บทที่ 15
├── chapter16/            # สื่อการเรียนการสอน บทที่ 16
├── chapter17/            # สื่อการเรียนการสอน บทที่ 17
├── firebase/             # ไฟล์ตั้งค่าและเชื่อมโยงฐานข้อมูล Firebase
├── picture/              # โฟลเดอร์เก็บสื่อ รูปภาพ และอินโฟกราฟิกของระบบ
├── index.html            # พอร์ทัลกลางสำหรับผู้ใช้งานทุกคน (Main Entry Point)
├── style.css             # ไฟล์สไตล์สําหรับหน้าพอร์ทัลกลาง
├── manifest.json         # ไฟล์ระบุคุณลักษณะความเป็น PWA ของระบบ
├── sw.js                 # Service Worker สำหรับเก็บแคชและช่วยให้อ่านออฟไลน์ได้
├── PROJECT_WORKFLOW.md   # คู่มือและกระบวนการทำงานของโปรเจกต์
└── README.md             # เอกสารอธิบายรายละเอียดโครงงาน (ไฟล์ปัจจุบัน)
```

---

## <a id="installation"></a>⚙️ Installation (วิธีติดตั้งและใช้งานในเครื่องคอมพิวเตอร์)

หากต้องการเปิดใช้งานเว็บไซต์เพื่อตรวจสอบหรือทำการพัฒนาต่อยอดในเครื่องของท่าน:

1.  **คัดลอกโครงการไปยังคอมพิวเตอร์ของคุณ (Clone Project)**
    ```bash
    git clone https://github.com/nopphorn31/physics-kruting-hub.git
    ```

2.  **เปลี่ยนทิศทางไปยังโฟลเดอร์โครงการ (Enter Project Directory)**
    ```bash
    cd physics-kruting-hub
    ```

3.  **รันระบบจำลองเซิร์ฟเวอร์ (Run Local Server)**
    แนะนำให้รันเซิร์ฟเวอร์ด้วย `serve` เพื่อทดสอบ PWA หรือเข้าถึงพอร์ทัลได้อย่างรวดเร็ว:
    ```bash
    npx serve
    ```
    *หรือคลิกขวาที่ไฟล์ `index.html` แล้วเลือกเปิดผ่านปลั๊กอิน **Live Server** ใน VS Code เพื่อแก้ไขแบบสดได้ทันที*

---

## <a id="roadmap"></a>🗺️ Project Roadmap (แผนการดำเนินงาน)

ความคืบหน้าแผนการพัฒนาตามเฟสที่กำหนด:

- [ ] **Phase 1: พัฒนาสื่อบทที่ 16 (ความร้อนและแก๊ส)**
  - [ ] WEB-16-01 (ความร้อนจำเพาะ/แฝง)
  - [ ] WEB-16-02 (กฎของแก๊ส)
  - [ ] WEB-16-03 (ทฤษฎีจลน์ของแก๊ส)
  - [ ] WEB-16-04 (กฎข้อที่หนึ่งของอุณหพลศาสตร์)
- [ ] **Phase 2: พัฒนาสื่อบทที่ 17 (ของแข็งและของไหล)**
  - [ ] WEB-17-01 (สภาพยืดหยุ่นและมอดุลัส)
  - [ ] WEB-17-02 (ความตึงผิวและความหนืด)
  - [ ] WEB-17-03 (แรงพยุง)
  - [ ] WEB-17-04 (สมการความต่อเนื่อง/แบร์นูลี)
- [ ] **Phase 3: ปรับปรุงโครงสร้างเว็บ Portal หลัก (Main Portal Upgrade)**
- [ ] **Phase 4: เชื่อมต่อระบบสถิติและการบันทึกข้อมูลด้วย Firebase**
- [ ] **Phase 5: ทดสอบความสามารถและตั้งค่าแอป PWA**
- [ ] **Phase 6: เผยแพร่ผลงานขึ้นระบบ Vercel เพื่อใช้สอนจริง**

---

## <a id="final-goal"></a>🎯 Final Goal (เป้าหมายสูงสุด)

สร้างสรรค์เครื่องมือและระบบสำหรับจัดการเรียนการสอนฟิสิกส์ ม.6 เล่ม 5 อย่างครบถ้วนและทันสมัยที่สุด:
*   มีเว็บแอปโต้ตอบบทเรียนย่อยทั้งหมด **10 เว็บแอป (Learning Apps)**
*   มีหน้า **Single Learning Portal** ที่สวยงามและปลอดภัยสำหรับนักเรียนทุกคน
*   เชื่อมต่อข้อมูลและสถิติคะแนนกับ **Firebase**
*   มีระบบการวิเคราะห์ความก้าวหน้า (**Analytics**) และเหรียญรางวัล (**Achievements**)
*   พร้อมใช้งานได้บนสมาร์ทโฟนแบบ **PWA**
*   เสถียรและเข้าถึงง่ายทุกที่ทุกเวลาบนคลาวด์ **Vercel**

---

## <a id="author"></a>✍️ Author (ผู้พัฒนา)

*   **ครูนพพร สมบูรณ์ชัย (Nopphorn Somboonchai)**
*   *โครงการสร้างสรรค์สื่อดิจิทัลการศึกษาฟิสิกส์ ม.6 เล่ม 5*
