# Create Logo and Brand Kit

Create the first approved identity assets for this brand after the Core Brand Skill exists.

The final approved identity should be organized as:

- logo files → `assets/logos/`
- logo export package → `assets/logos/brand-kit/`
- editable Brand Kit source → `brand/brand-kit.md`
- designed Brand Kit PDF → `brand/brand-kit.pdf`

Do not copy reference logos or recognizable visual treatments.

---

# 1. Check the Foundation

Read:

- `brand/brand-brief.md`
- `brand/core-brand/SKILL.md`
- `skills/no-slop/SKILL.md`
- `skills/vector-design/SKILL.md` when creating SVG or vector logo assets
- `references/brand-taste/`
- `references/dislike/`
- relevant existing files in `assets/`

If the Core Brand Skill does not exist, complete `prompts/01-create-core-brand.md` first.

Inspect `assets/logos/` before assuming the brand has no logo. Placeholder files such as `.gitkeep` do not count.

If an approved logo already exists, ask whether the user wants to build the Brand Kit from it or intentionally replace it.

---

# 2. Confirm the Logo Brief

Confirm only decisions that materially affect the logo and are not already established, such as:

- exact brand name and capitalization
- tagline, if one belongs in a lockup
- important use cases and smallest expected size
- wordmark, symbol, monogram, or flexible system preferences
- practical color and reproduction constraints
- required associations and strong dislikes

Keep unresolved decisions open rather than inventing answers.

---

# 3. Propose Distinct Directions

Present a small set of meaningfully different logo directions before developing final assets.

For each direction, explain:

- the central idea
- how it expresses the Core Brand
- the likely logo structure
- why it is relevant rather than merely fashionable
- important strengths or risks

Do not present superficial variations as separate concepts.

Ask the user which direction to develop or how it should change.

---

# 4. Develop and Evaluate Concepts

Create original concepts from the approved direction.

When creating SVG or vector concepts, follow `skills/vector-design/SKILL.md` and do not present them as finished until the saved files have been rendered and visually inspected.

Evaluate them for:

- relevance to the brand idea
- distinctiveness without novelty for its own sake
- legibility at realistic sizes
- recognizable silhouette and proportion
- successful monochrome use
- suitability across likely mediums
- absence of accidental symbols or misleading associations
- resistance to generic AI-logo details and unnecessary decoration

Show the logo clearly without relying on a mockup to make a weak mark appear convincing.

Keep experimental work in `output/` and do not place it in `assets/logos/` before approval.

---

# 5. Approve and Organize the Logo

Do not treat any concept as official until the user explicitly approves it.

After approval:

- preserve the useful working source
- save the approved master under `assets/logos/`
- create `assets/logos/brand-kit/` for delivery-ready exports
- use clear, stable filenames
- do not claim a raster image is a true vector asset
- do not overwrite useful source work

Organize the export package by format, then by color variant when that creates a clearer package. Use only the folders the approved identity actually needs. A typical structure is:

```text
assets/logos/brand-kit/
|-- master/
|-- svg/
`-- png/
    |-- full-color/
    |-- black/
    `-- white/
```

Create useful variants from the same approved geometry:

- true SVG masters and variants when genuine vector artwork exists
- transparent PNG exports for full-color, black, white, and reversed use when applicable
- PDF or other formats only when the available tooling can export them accurately
- exact pixel sizes recorded in filenames

Unless actual use cases require different sizes, use a practical baseline:

- standalone marks and icons → 16, 32, 64, 128, 256, 512, and 1024 px
- wordmarks and horizontal lockups → 256, 512, 1024, and 2048 px wide, preserving aspect ratio

Do not stretch artwork, add unapproved colors, generate meaningless size variants, create empty folders, or rename a raster file to imitate another format.

Render and inspect every exported color and size family. Check transparency, padding, contrast, legibility, and consistency with the approved master.

Record the approved master and the complete export inventory in the Brand Kit.

---

# 6. Create the Brand Kit

After logo approval, create `brand/brand-kit.md` as the editable source of truth.

Include only confirmed and useful sections, such as:

- brand summary
- approved logo and file inventory
- logo variants, formats, colors, sizes, and intended use
- clear-space and minimum-size guidance when established
- approved color palette with reliable values
- typography roles, font sources, and known licensing status
- imagery and art direction
- graphic elements, shape language, or icon behavior
- accessibility and contrast considerations
- concise do and do-not guidance

Link to the actual approved assets using project-relative paths.

Do not invent color values, font files, logo variants, measurements, or licensing claims. Resolve important missing decisions with the user or mark them as open.

---

# 7. Generate and Verify the PDF

Generate `brand/brand-kit.pdf` from the confirmed Brand Kit content.

The PDF should itself demonstrate the approved brand direction. Make it a polished reference document, not a plain text export.

Use a reliable PDF creation workflow. Render every page to images and visually inspect the latest version before delivery. Fix clipped text, overlaps, broken glyphs, weak hierarchy, inconsistent spacing, low contrast, or poor page transitions.

Confirm that the final PDF matches `brand/brand-kit.md` and points to the correct approved assets.

---

# 8. Continue the Studio Workflow

Tell the user the identity and Brand Kit are ready to test in real work.

If they request a website, social system, presentation, motion piece, or another medium and no corresponding skill exists, recommend starting the medium-specific interview with:

`prompts/02-create-specific-skill.md`

Mention that medium references are optional and can be added before or during the workflow.
