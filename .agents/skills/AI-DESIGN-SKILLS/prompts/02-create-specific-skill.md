# Create Medium-Specific Design Skill

Create a specialized design skill for this brand.

Read:

`brand/core-brand/SKILL.md`

The Core Brand Skill is the source of truth for the overall visual identity.

The specialized skill should explain how that identity behaves in one specific design medium.

References are optional. Begin with the Core Brand Skill and a medium-specific interview even when no visual references are provided.

Do NOT copy any provided references.

Do NOT recreate specific layouts.

---

# 1. Identify the Medium

Determine which medium I want to create a skill for.

Examples:

- website/UI
- mobile UI
- social media
- presentation
- print/editorial
- motion
- packaging
- advertising
- email
- other

If unclear, ask.

When references are provided, use the corresponding folder.

Examples:

- website/UI → `references/website-ui/`
- social media → `references/social-media/`
- presentation → `references/presentation/`
- other → relevant folder

Do not mix unrelated reference folders unless asked.

---

# 2. Read Core Brand

Identify the Core Brand principles that should carry into this medium.

Do not duplicate the entire Core Brand Skill.

The specialized skill should supplement it.

---

# 3. Interview Me

Ask only questions that are specific to this medium and not already answered by Core Brand.

Examples:

## Website/UI

- primary user goals
- navigation
- interaction
- density
- responsiveness
- conversion
- accessibility

## Social

- platform
- content types
- carousel rhythm
- text density
- image usage
- branding visibility

## Presentation

- audience
- storytelling
- slide density
- pacing
- charts
- speaker-led vs self-reading

Ask only what materially affects the skill.

Do not require references before starting the interview. Mention that the user may add them before the proposed direction if they would help communicate taste or medium behavior.

---

# 4. Analyze Optional References

If user-provided references exist, study them for medium-specific principles.

If the relevant folder contains no actual references, continue using the Core Brand Skill, interview, approved assets, and existing work. Do not delay the workflow.

When references exist, consider relevant areas such as:

- structure
- composition
- hierarchy
- typography behavior
- spacing
- density
- pacing
- imagery
- content organization
- interaction
- navigation
- responsive behavior
- sequencing
- platform conventions
- reusable patterns

Separate:

- underlying principles
- contextual solutions
- reference-specific details
- patterns that should not be generalized

Do not turn a repeated layout into a mandatory template.

---

# 5. Propose the Medium Rules

Before creating the skill, show me:

## Inherited From Core Brand

How the existing brand principles affect this medium.

## Medium-Specific Principles

New rules needed for this format.

## Flexible Tendencies

Patterns that should guide but not dictate.

## Anti-Patterns

Defaults or structures that conflict with the brand or medium.

## Creative Freedom

Areas where AI should decide based on the content and context.

Ask me to approve or modify the direction.

Do NOT create the final skill until approved.

---

# 6. Create the Skill

Create a provider-independent `SKILL.md`.

Use:

---
name: [medium-name]
description: [explain what this skill controls and when it should be used]
---

Include only relevant sections such as:

# Purpose
# Relationship to Core Brand
# Medium Design Point of View
# Core Principles
# Structure and Composition
# Typography
# Color and Imagery
# Medium-Specific Rules
# Content Hierarchy
# Interaction and Behavior
# Anti-Patterns
# Creative Freedom
# Quality Checks
# Final Self-Critique

Do not create a template disguised as a skill.

Do not require every output to use the same layout.

The skill should teach decision-making principles that support many different designs.

Save it to the relevant folder.

Examples:

- website/UI → `skills/website-ui/SKILL.md`
- social media → `skills/social-media/SKILL.md`
- presentation → `skills/presentation/SKILL.md`

Do not overwrite an existing skill unless I explicitly ask.

---

# 7. Recommend a Real Test

Tell the user this is a v1 skill that should improve through use.

Recommend testing it on a representative design for this medium and noting what feels right, wrong, generic, rigid, or inconsistent.

When useful feedback exists, use:

`prompts/03-refine-skill.md`
