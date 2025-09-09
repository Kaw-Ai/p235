#!/usr/bin/env python3
"""
Generate archetypal patterns from UIA templates in the form:
"some-generic {{domain-specific}} more-generic"
"""

import os
import re
import glob
from pathlib import Path

def load_transformation_mappings():
    """Load the transformation mappings from analysis files"""
    return {
        'domain': {
            'physical': ['region', 'area', 'land', 'environment'],
            'social': ['functional domain', 'community', 'group', 'organization'],
            'conceptual': ['conceptual domain', 'knowledge domain', 'intellectual area'],
            'psychic': ['mode of awareness', 'consciousness', 'mental state']
        },
        'organization': {
            'physical': ['building', 'settlement', 'structure', 'development'],
            'social': ['institution', 'group', 'community', 'network'],
            'conceptual': ['conceptual framework', 'knowledge system', 'theory'],
            'psychic': ['structured awareness', 'organized thinking', 'mental framework']
        },
        'elements': {
            'physical': ['materials', 'rooms', 'spaces', 'buildings'],
            'social': ['members', 'participants', 'roles', 'positions'],
            'conceptual': ['concepts', 'ideas', 'methods', 'approaches'],
            'psychic': ['perceptions', 'impressions', 'insights', 'experiences']
        },
        'frameworks': {
            'physical': ['cities', 'towns', 'infrastructure', 'urban areas'],
            'social': ['institutions', 'organizations', 'systems', 'procedures'],
            'conceptual': ['paradigms', 'schools of thought', 'theoretical systems'],
            'psychic': ['modes of awareness', 'mental structures', 'psychological patterns']
        },
        'resources': {
            'physical': ['land', 'fertility', 'agriculture', 'natural resources'],
            'social': ['social resources', 'human resources', 'relationships'],
            'conceptual': ['creative resources', 'intellectual resources', 'knowledge'],
            'psychic': ['psychic resources', 'mental energy', 'awareness']
        },
        'relationships': {
            'physical': ['roads', 'connections', 'networks', 'proximity'],
            'social': ['communications', 'interactions', 'connections'],
            'conceptual': ['conceptual links', 'logical connections', 'associations'],
            'psychic': ['associative relationships', 'mental connections', 'psychological links']
        }
    }

def extract_template_content(file_path):
    """Extract the template section from a UIA pattern file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title_match = re.search(r'^# (\d+) - (.+)$', content, re.MULTILINE)
        if not title_match:
            return None, None, None
        
        pattern_id = title_match.group(1)
        pattern_name = title_match.group(2)
        
        # Extract template section
        template_match = re.search(r'## Template\s*\n\n(.+?)(?=\n\n##|\n\n$)', content, re.DOTALL)
        if not template_match:
            return None, None, None
        
        template_content = template_match.group(1).strip()
        return pattern_id, pattern_name, template_content
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None, None, None

def identify_domain_specific_terms(template_text):
    """Identify potential domain-specific terms that could be placeholders"""
    # Common generic terms that should remain as-is
    generic_terms = [
        'organization', 'framework', 'structure', 'domain', 'environment',
        'relationships', 'network', 'pattern', 'integrity', 'boundary',
        'development', 'processes', 'emergence', 'balance', 'within',
        'may', 'different', 'new', 'local', 'degree', 'form', 'order',
        'spaces', 'areas', 'groups', 'people', 'whole', 'modes', 'awareness'
    ]
    
    # Words that often get replaced in domain-specific versions
    replaceable_terms = {
        'domains': '{{domains}}',
        'frameworks': '{{frameworks}}', 
        'elements': '{{elements}}',
        'resources': '{{resources}}',
        'organization': '{{organization-type}}',
        'influence': '{{influence-type}}',
        'positions': '{{positions}}',
        'areas': '{{areas}}',
        'modes': '{{modes}}',
        'patterns': '{{patterns}}',
        'established patterns': '{{established-patterns}}',
        'major patterns': '{{major-patterns}}'
    }
    
    archetypal_text = template_text
    
    # Apply replacements
    for term, placeholder in replaceable_terms.items():
        # Use word boundaries to avoid partial matches
        archetypal_text = re.sub(r'\b' + re.escape(term) + r'\b', placeholder, archetypal_text, flags=re.IGNORECASE)
    
    return archetypal_text

def generate_archetypal_pattern(pattern_id, pattern_name, template_content):
    """Generate an archetypal pattern with domain-specific placeholders"""
    
    archetypal_content = identify_domain_specific_terms(template_content)
    
    # Create the archetypal pattern markdown
    archetypal_pattern = f"""# {pattern_id} - {pattern_name} (Archetypal)

## Archetypal Pattern

{archetypal_content}

## Domain Placeholders

This archetypal pattern uses the following domain-specific placeholders:

- `{{{{domains}}}}` → Physical: regions/areas | Social: functional domains/communities | Conceptual: knowledge domains | Psychic: modes of awareness
- `{{{{frameworks}}}}` → Physical: cities/infrastructure | Social: institutions/systems | Conceptual: paradigms/theories | Psychic: mental structures
- `{{{{elements}}}}` → Physical: materials/spaces | Social: members/participants | Conceptual: concepts/ideas | Psychic: perceptions/insights
- `{{{{organization-type}}}}` → Physical: building/development | Social: institution/community | Conceptual: framework/theory | Psychic: structured awareness
- `{{{{resources}}}}` → Physical: land/agriculture | Social: social resources | Conceptual: creative resources | Psychic: psychic resources
- `{{{{influence-type}}}}` → Physical: influence | Social: influence | Conceptual: insight | Psychic: influence
- `{{{{areas}}}}` → Physical: land/regions | Social: functional areas | Conceptual: domains | Psychic: modes of awareness
- `{{{{positions}}}}` → Physical: central locations | Social: central organizations | Conceptual: central frameworks | Psychic: ordered modes
- `{{{{patterns}}}}` → Physical: urban environments | Social: organizational patterns | Conceptual: knowledge patterns | Psychic: awareness patterns
- `{{{{modes}}}}` → Physical: environments | Social: modes of organization | Conceptual: modes of organization | Psychic: modes of awareness

## Original Template

{template_content}

---
*Generated from UIA Pattern {pattern_id}*
"""
    
    return archetypal_pattern

def main():
    """Main function to generate all archetypal patterns"""
    uia_dir = Path("/home/runner/work/p235/p235/markdown/uia")
    arc_dir = Path("/home/runner/work/p235/p235/markdown/arc")
    
    # Ensure arc directory exists
    arc_dir.mkdir(parents=True, exist_ok=True)
    
    # Process all UIA pattern files
    uia_files = sorted(uia_dir.glob("*.md"))
    
    generated_count = 0
    no_template_count = 0
    
    for file_path in uia_files:
        pattern_id, pattern_name, template_content = extract_template_content(file_path)
        
        if pattern_id and pattern_name and template_content:
            archetypal_pattern = generate_archetypal_pattern(pattern_id, pattern_name, template_content)
            
            # Write the archetypal pattern file
            output_file = arc_dir / f"arc_{pattern_id}.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(archetypal_pattern)
            
            generated_count += 1
            print(f"Generated: arc_{pattern_id}.md - {pattern_name}")
        elif pattern_id and pattern_name:
            no_template_count += 1
            print(f"Skipped (no Template section): {pattern_id} - {pattern_name}")
    
    print(f"\nGenerated {generated_count} archetypal patterns in {arc_dir}")
    print(f"Skipped {no_template_count} patterns without Template sections")
    print(f"Total patterns processed: {generated_count + no_template_count}")
    
    # Create a README for the arc directory
    readme_content = f"""# Archetypal Patterns

This directory contains archetypal patterns generated from UIA templates using the format:
**"some-generic {{{{domain-specific}}}} more-generic"**

## What are Archetypal Patterns?

Archetypal patterns are abstracted versions of the UIA template patterns where domain-specific terms have been replaced with placeholders. This allows the same organizational principle to be applied across different domains (Physical, Social, Conceptual, Psychic) by substituting appropriate domain-specific vocabulary.

## Pattern Format

Each archetypal pattern includes:

1. **Archetypal Pattern**: The template text with domain-specific placeholders
2. **Domain Placeholders**: Explanation of how placeholders map to different domains  
3. **Original Template**: The original template text for reference

## Usage

To use an archetypal pattern:

1. Select the appropriate domain (Physical, Social, Conceptual, or Psychic)
2. Replace each `{{{{placeholder}}}}` with the corresponding domain-specific term
3. The result will be a domain-specific version of the organizational principle

## Generated Patterns

{generated_count} archetypal patterns have been generated from the UIA template collection.

---
*Generated from analysis of 253 UIA patterns*
"""
    
    with open(arc_dir / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"Created README.md with documentation")

if __name__ == "__main__":
    main()