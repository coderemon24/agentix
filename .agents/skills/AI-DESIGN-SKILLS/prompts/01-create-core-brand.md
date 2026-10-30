# Create Core Brand Skill

Help me turn my brand direction and visual taste into a reusable Core Brand Skill.

The final result should be:

`brand/core-brand/SKILL.md`

The purpose of the skill is to teach AI how this brand makes visual decisions across different mediums.

References are optional. Begin with the brief and interview even when no visual references are provided.

Do NOT copy any provided references.

Extract principles from them.

---

# 1. Determine the Starting Point

Read:

`brand/brand-brief.md`

Inspect relevant files in:

`assets/`

Determine whether this is:

## Brand From Scratch

Little or no established visual identity.

Use this order:

brand idea → interview → optional references → proposed direction → approval → skill

## Existing Brand

Existing identity or brand material already exists.

Use this order:

existing material → identify patterns/gaps → interview → optional references → proposed direction → approval → skill

If unclear, ask.

---

# 2. Understand the Brand

For a new brand, understand whatever is already known about:

- name
- idea
- product or service
- problem
- audience
- category
- positioning
- desired perception
- competitors if relevant
- things already wanted
- things explicitly not wanted

Do not force answers to questions the user genuinely has not decided yet.

During the workflow, keep `brand/brand-brief.md` updated with confirmed facts, preferences, and open decisions learned from the conversation.

Do not record speculative ideas as decisions.

---

# 3. Interview Me

Ask focused questions needed to establish the brand direction.

Explore areas such as:

- personality
- audience
- positioning
- desired emotional response
- restrained vs expressive
- minimal vs rich
- technical vs human
- premium vs accessible
- familiar vs distinctive
- typography preferences
- color behavior
- imagery
- spacing and density
- composition
- level of decoration
- creative freedom
- strong dislikes

Do not ask questions already answered by the brief or existing project files.

Ask in manageable groups.

---

# 4. Analyze Optional References

If actual visual references are provided, use:

`references/brand-taste/`

and when relevant:

`references/dislike/`

If these folders contain no user-provided references, continue using the brief, interview, and approved assets. Do not delay the workflow or ask the user to provide references before proposing a direction.

References may include:

- branding
- websites
- editorial design
- typography
- packaging
- photography
- illustration
- architecture
- fashion
- other visual material

Do not assume the user likes every aspect of every reference.

If the reason for including a reference is unclear and important, ask.

Analyze recurring patterns such as:

- visual personality
- composition
- hierarchy
- typography
- spacing
- density
- color
- contrast
- imagery
- shape language
- whitespace
- visual rhythm
- texture and effects
- restraint vs decoration

Classify meaningful observations as:

- STRONG PATTERN
- POSSIBLE PATTERN
- REFERENCE-SPECIFIC
- CONTRADICTION

Do not turn one isolated detail into a permanent rule.

---

# 5. Extract Principles, Not Designs

Do not copy:

- layouts
- exact compositions
- component structures
- exact color combinations
- typography combinations
- recognizable visual treatments

Translate execution into reasoning.

Example:

Bad:

> Use large serif headlines on beige backgrounds.

Better:

> Create identity through expressive typography, strong scale contrast, and controlled use of decoration.

Bad:

> Use rounded cards with thin borders.

Better:

> Use containers only when they meaningfully organize information or interaction.

The skill should teach design decisions, not recreate a moodboard.

---

# 6. Keep Core Brand Separate From Medium Rules

Core Brand may define:

- personality
- visual point of view
- typography philosophy
- color behavior
- imagery direction
- spacing philosophy
- density
- shape language
- composition tendencies
- art direction
- effects
- brand-specific anti-patterns

Do NOT normally include:

- website navigation
- button sizes
- breakpoints
- dashboard structure
- carousel layouts
- slide layouts
- motion timing
- other medium-specific implementation rules

Those belong in specialized skills.

---

# 7. Propose the Direction

Before creating `SKILL.md`, show me:

## Brand Idea

What the brand is trying to communicate.

## Core Principles

The strongest design beliefs.

## Visual Personality

How the brand should generally feel.

## Flexible Tendencies

Preferences that should guide rather than dictate.

## Anti-Patterns

Things that would make the brand feel wrong.

## Creative Freedom

Areas where AI should use contextual judgment.

## Medium-Specific Observations

Useful ideas that belong in future specialized skills instead.

## Open Questions

Anything still unresolved.

Ask me to approve or modify this direction.

Do NOT create the final skill until I approve it.

---

# 8. Create the Skill

After approval, create:

`brand/core-brand/SKILL.md`

Use:

---
name: core-brand
description: Defines this brand's core visual identity, design point of view, and brand-level design rules. Use whenever creating, evaluating, or refining visual material for this brand across any medium.
---

Include only useful sections such as:

# Purpose
# Brand Idea
# Brand Point of View
# Brand Personality
# Core Visual Principles
# Composition Philosophy
# Typography Philosophy
# Color Behavior
# Spacing and Density
# Shape Language
# Imagery and Art Direction
# Visual Rhythm
# Creative Freedom
# Brand Anti-Patterns
# Decision Framework
# Relationship to Medium-Specific Skills
# Final Brand Check

Keep the skill concise.

Do not repeat the same rule in multiple sections.

Do not make the skill dependent on access to the original references.

The goal is not to make every asset look identical.

The goal is to make different outputs feel like they came from the same design point of view.

---

# 9. Recommend the Next Test

Tell the user this is a v1 skill that should improve through use.

Recommend testing it on a representative design and noting what feels right, wrong, generic, rigid, or inconsistent. When useful feedback exists, use:

`prompts/03-refine-skill.md`

If no approved logo exists in `assets/logos/`, recommend creating the logo and Brand Kit next with:

`prompts/create-logo-and-brand-kit.md`
