# UX Research Report: [Project / Feature Name]

> **Gate**: Gate 1 — Discovery Approval  
> **Prepared by**: [design-engineer]  
> **Status**: Review Ready  

---

## 1. Domain Insights & Contextual Inquiries
- **Field Context**: [Describe how users interact with the system during their workday: noisy school hallway, crowded office, multitasking parent at home].
- **Key Behavioral Observations**:
  - Users scan quickly for critical anchors (dates, names, status colors) rather than reading paragraphs.
  - Repetitive data entry causes user fatigue; sensible defaults and autofill drastically reduce input errors.
  - Complex multi-step wizards without progress indicators induce high drop-off rates.

---

## 2. Jobs-to-be-Done (JTBD) Framework
1. **Core JTBD 1**:
   > *When* a parent receives a report card notice,  
   > *I want to* view and download my child's official grades on my smartphone,  
   > *So that* I can understand their academic progress without visiting the school in person.
2. **Core JTBD 2**:
   > *When* an administrative clerk records daily fee collections,  
   > *I want to* search a student by roll number and log the receipt in under 15 seconds,  
   > *So that* the parent queue moves quickly with zero reconciliation errors.

---

## 3. Heuristic & Usability Findings
- **Cognitive Load Reduction**: Consolidate dispersed stats into a single anchored status pill.
- **Error Prevention**: Proactively validate inputs on blur rather than delaying feedback until full form submit.
- **Affordance & Feedback**: Every button must display clear hover, active, and loading spinner states.

---

## 4. Synthesis & Recommendations
1. Prioritize a mobile-first single column card stack with responsive desktop expansion.
2. Replace generic modals with inline drawers for complex contextual workflows.
3. Establish a permanent 4-tier typographic scale to anchor user attention.

