# Information Architecture & Navigation Schema

> **Gate**: Gate 1 — Discovery Approval  
> **Prepared by**: [design-engineer]  

---

## 1. Global Sitemap & Navigation Tree

```
EduCore Public / Portal
├── 1.0 Home (Institutional Manifesto, Live Stats, Flagship Highlights)
├── 2.0 Academic
│   ├── 2.1 Academic Classes & Sections
│   ├── 2.2 Daily Class Routine & Schedules
│   ├── 2.3 Syllabus & Curriculum
│   └── 2.4 Academic Calendar & Holidays
├── 3.0 Faculty & Leadership
│   ├── 3.1 Teachers Directory & Profiles
│   └── 3.2 Administrative Staff
├── 4.0 Notices & Bulletins
│   ├── 4.1 Urgent School Alerts
│   └── 4.2 Exam Schedules & Results
├── 5.0 Admissions & Enrollment (Primary CTA)
│   ├── 5.1 Eligibility & Fee Structure
│   └── 5.2 Online Admission Form
└── 6.0 Contact & Campus Locator
```

---

## 2. Navigation Taxonomy & Hierarchy Rules
1. **Top-Level Bar (Desktop)**: Maximum 6 categorical nav links with clear active indicator (`border-b-2 border-[#005030]`).
2. **Primary Conversion Action**: Fixed highlight button (`bg-amber-400 text-slate-900 font-semibold`) anchored on far right.
3. **Mobile Drawer**: Slide-out navigation drawer with 48px touch targets, grouped cleanly with accordion dividers.
4. **Breadcrumb Trail**: Standardized 3-step breadcrumb on all inner pages (`Home / Academic / Class Routine`).

