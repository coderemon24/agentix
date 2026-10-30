# Skill-Based AI Design Studio

This folder helps you turn your brand direction and design taste into reusable AI design skills.

Instead of explaining how your brand should look every time you start a new task, the important design decisions live inside the project.

## The System

Brand idea or existing brand

↓

Core Brand Skill

↓

Approved Logo + Brand Kit

↓

Medium-Specific Skill

↓

No Slop Skill

↓

Design

↓

Test + Refine

## Core Brand Skill

Defines the overall design point of view.

It can include:

- brand personality
- typography philosophy
- color behavior
- imagery
- composition
- spacing
- shape language
- visual rhythm
- things the brand should avoid

It should work across different mediums.

## Medium-Specific Skills

Explain how the brand behaves in a particular format.

Examples:

- Website/UI Skill
- Social Media Skill
- Presentation Skill

These supplement the Core Brand Skill rather than replacing it.

## No Slop Skill

A universal skill that challenges common generic AI design defaults.

It does not define your brand.

Its purpose is to encourage intentional design decisions.

## Vector Design Skill

A universal execution skill for logos, icons, illustrations, diagrams, and other SVG artwork.

When you request SVG or editable vector output, it guides the studio to:

- plan proportions and geometry before drawing
- create clean, editable SVG structure
- avoid guessed paths, accidental clipping, and broken references
- render and visually inspect the saved SVG before delivery

It improves vector accuracy without defining the brand's visual style.

## Logo and Brand Kit

After the Core Brand Skill is approved, the studio checks for an approved logo in `assets/logos/`.

If one does not exist, it guides you through logo directions, development, and approval. Approved logo files are organized under `assets/logos/`.

The studio then creates:

- `assets/logos/brand-kit/` with organized format, color, and size exports
- `brand/brand-kit.md` as the editable source of truth
- `brand/brand-kit.pdf` as the designed, shareable Brand Kit

---

# Starting a Brand From Scratch

Fill in as much as you know in:

`brand/brand-brief.md`

You can optionally add references you like to:

`references/brand-taste/`

You can use:

- branding
- websites
- editorial design
- typography
- packaging
- photography
- architecture
- fashion
- illustration
- other visual references

They do not need to come from the same industry.

You can also optionally add things you want to avoid to:

`references/dislike/`

References are not required. If you do not have any, start chatting and the studio will build the direction through an interview.

Then start naturally. For example:

> I'm starting a coffee brand for digital nomads.

The studio will inspect the project, begin the Core Brand workflow, and interview you before creating the skill.

---

# Starting With an Existing Brand

Add your existing material to:

`assets/`

Examples:

- logos
- brand guidelines
- colors
- fonts
- website screenshots
- social designs
- presentations
- imagery

Fill in anything useful in:

`brand/brand-brief.md`

Then run the same Core Brand workflow.

If an approved logo is missing after the Core Brand Skill is created, the studio will recommend the logo and Brand Kit workflow next.

---

# Creating a Website/UI Skill

After the Core Brand Skill exists, you can optionally add UI and website references to:

`references/website-ui/`

If you do not have references, the studio can create the skill from the Core Brand and a focused Website/UI interview.

Then say:

> I want to create a website for this brand.

If the Website/UI Skill does not exist, the studio will recommend creating it before designing the website. The resulting skill should be saved to:

`skills/website-ui/SKILL.md`

Use the same process for social media, presentations, or another medium.

---

# Testing and Refining Skills

Every new skill is a v1.

Test it on representative work and note what feels right, wrong, generic, rigid, or inconsistent. Then use:

`prompts/03-refine-skill.md`

The refine workflow diagnoses the cause and proposes the smallest reusable improvement before changing the skill.

---

# Important

References should teach the AI principles.

They should not become templates.

The goal is not:

> Copy this design.

The goal is:

> Understand why I like these designs and turn those reasons into reusable design decisions.

Your final system should help different outputs feel related without making them look identical.
