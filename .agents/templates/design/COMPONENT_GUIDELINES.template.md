# Component Guidelines & Code Patterns

> **Gate**: Gate 3 — Design System Approval  
> **Prepared by**: [design-engineer]  

---

## 1. Section Header Block (Recipe 3 & Recipe 7)
```html
<div class="section-header-block mb-10">
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#e6f0ec] text-[#005030] text-xs font-semibold tracking-wider uppercase mb-3">
    <span class="w-2 h-2 rounded-full bg-[#005030] animate-pulse"></span>
    ACADEMIC CURRICULUM
  </div>
  <h2 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-slate-900 tracking-tight">
    Structured for <span class="text-[#005030] font-extrabold">Intellectual Rigor</span>
  </h2>
  <p class="mt-4 text-base sm:text-lg text-slate-600 max-w-2xl leading-relaxed">
    Official semester syllabus verified by the Academic Council for comprehensive student development.
  </p>
  <div class="h-px bg-slate-200 mt-6 w-full"></div>
</div>
```

---

## 2. Primary Conversion Action Button (Recipe 6)
```html
<a href="{{ route('admissions.apply') }}" 
   class="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-lg bg-amber-400 hover:bg-amber-500 active:bg-amber-600 text-slate-900 font-semibold text-sm shadow-sm transition-colors duration-150 focus:outline-none focus:ring-2 focus:ring-amber-500 focus:ring-offset-2">
  <span>Apply for Admission</span>
  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
</a>
```

---

## 3. Asymmetric Anchor Card (Recipe 2 & Recipe 4)
```html
<div class="relative p-6 sm:p-8 bg-white border border-slate-200 rounded-xl shadow-sm hover:shadow-md transition-shadow">
  <!-- Floating Anchor Badge -->
  <div class="absolute -top-3.5 right-6 px-3 py-1 bg-[#005030] text-white text-xs font-bold rounded-full tracking-wide shadow-sm">
    ESTD. 1968
  </div>
  <h3 class="text-xl font-bold text-slate-900">Institutional Heritage</h3>
  <p class="mt-2 text-sm text-slate-600 leading-relaxed">
    Over five decades of academic distinction, cultivating leadership and character.
  </p>
</div>
```

---

## 4. Responsive Data Table Container (UI-Mandatory Compliance)
```html
<div class="w-full overflow-hidden border border-slate-200 rounded-xl bg-white shadow-sm">
  <div class="overflow-x-auto">
    <table class="w-full text-left text-sm border-collapse">
      <thead class="bg-slate-50 border-b border-slate-200 text-xs font-semibold text-slate-600 uppercase tracking-wider">
        <tr>
          <th class="px-6 py-4">Subject</th>
          <th class="px-6 py-4">Faculty</th>
          <th class="px-6 py-4">Schedule</th>
          <th class="px-6 py-4 text-right">Action</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-100 text-slate-700">
        <tr class="hover:bg-slate-50/80 transition-colors">
          <td class="px-6 py-4 font-semibold text-slate-900">Physics I</td>
          <td class="px-6 py-4">Dr. Tariq Rahman</td>
          <td class="px-6 py-4">Mon, Wed 10:00 AM</td>
          <td class="px-6 py-4 text-right">
            <a href="#" class="text-xs font-bold text-[#005030] hover:underline">View Syllabus</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

