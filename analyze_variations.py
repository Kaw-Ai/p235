#!/usr/bin/env python3
"""
Extract and compare specific examples of how the same pattern concept
is expressed differently across the 5 domains.
"""

import os
import re
from pathlib import Path

def extract_domain_sections(content):
    """Extract content from each domain section of a UIA pattern."""
    sections = {}
    
    # Define section patterns
    section_patterns = {
        'Template': r'## Template\s*\n\n(.*?)(?=\n## |$)',
        'Physical': r'## Physical\s*\n\n(.*?)(?=\n## |$)',
        'Social': r'## Social\s*\n\n(.*?)(?=\n## |$)',
        'Conceptual': r'## Conceptual\s*\n\n(.*?)(?=\n## |$)',
        'Psychic': r'## Psychic\s*\n\n(.*?)(?=\n## |$)'
    }
    
    for domain, pattern in section_patterns.items():
        match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
        if match:
            sections[domain] = match.group(1).strip()
        else:
            sections[domain] = ""
    
    return sections

def analyze_pattern_variations():
    """Analyze how patterns vary across domains with specific examples."""
    
    markdown_dir = Path('/home/runner/work/p235/p235/markdown/uia')
    
    examples = []
    
    # Select a few representative patterns for detailed analysis
    sample_patterns = [
        '12610010.md',  # Independent domains
        '12610020.md',  # Distribution of organization  
        '12610030.md',  # Interpretation of complementary modes
        '12610040.md',  # Regenerative resource cultivation areas
        '12610050.md'   # Network of inter-relationships
    ]
    
    for pattern_file in sample_patterns:
        file_path = markdown_dir / pattern_file
        
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title
            title_match = re.search(r'# \d+ - (.+)', content)
            title = title_match.group(1) if title_match else pattern_file
            
            # Extract domain sections
            sections = extract_domain_sections(content)
            
            example = {
                'file': pattern_file,
                'title': title,
                'sections': sections
            }
            
            examples.append(example)
    
    return examples

def create_variation_examples_report(examples, output_file):
    """Create a report showing domain variation examples."""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Domain Variation Examples\n\n")
        f.write("Examples showing how the same organizational pattern concept is expressed differently across the 5 domains.\n\n")
        
        for example in examples:
            f.write(f"## {example['title']}\n\n")
            f.write(f"*Source: {example['file']}*\n\n")
            
            # Show Template first as the generic version
            if example['sections']['Template']:
                f.write("### Template (Generic)\n")
                f.write(f"> {example['sections']['Template']}\n\n")
            
            # Then show domain-specific variations
            for domain in ['Physical', 'Social', 'Conceptual', 'Psychic']:
                if example['sections'][domain]:
                    f.write(f"### {domain} Domain\n")
                    f.write(f"> {example['sections'][domain]}\n\n")
            
            f.write("---\n\n")

def identify_transformation_patterns(examples):
    """Identify common transformation patterns between domains."""
    
    transformations = {
        'Generic → Physical': [],
        'Generic → Social': [],
        'Generic → Conceptual': [],
        'Generic → Psychic': []
    }
    
    # Common word mappings observed
    word_mappings = {
        'Physical': {
            'domain': ['region', 'area', 'land', 'environment'],
            'organization': ['building', 'settlement', 'structure', 'development'],
            'elements': ['materials', 'rooms', 'spaces', 'buildings'],
            'frameworks': ['cities', 'towns', 'infrastructure', 'urban areas'],
            'resources': ['land', 'fertility', 'agriculture', 'natural resources'],
            'relationships': ['roads', 'connections', 'networks', 'proximity']
        },
        'Social': {
            'domain': ['functional domain', 'community', 'group', 'organization'],
            'organization': ['institution', 'group', 'community', 'network'],
            'elements': ['members', 'participants', 'roles', 'positions'],
            'frameworks': ['institutions', 'organizations', 'systems', 'procedures'],
            'resources': ['social resources', 'human resources', 'relationships'],
            'relationships': ['communications', 'interactions', 'connections']
        },
        'Conceptual': {
            'domain': ['conceptual domain', 'knowledge domain', 'intellectual area'],
            'organization': ['conceptual framework', 'knowledge system', 'theory'],
            'elements': ['concepts', 'ideas', 'methods', 'approaches'],
            'frameworks': ['paradigms', 'schools of thought', 'theoretical systems'],
            'resources': ['creative resources', 'intellectual resources', 'knowledge'],
            'relationships': ['conceptual links', 'logical connections', 'associations']
        },
        'Psychic': {
            'domain': ['mode of awareness', 'consciousness', 'mental state'],
            'organization': ['structured awareness', 'organized thinking', 'mental framework'],
            'elements': ['perceptions', 'impressions', 'insights', 'experiences'],
            'frameworks': ['modes of awareness', 'mental structures', 'psychological patterns'],
            'resources': ['psychic resources', 'mental energy', 'awareness'],
            'relationships': ['associative relationships', 'mental connections', 'psychological links']
        }
    }
    
    return word_mappings

def main():
    """Main analysis function."""
    
    print("Analyzing pattern variations across domains...")
    
    # Get examples
    examples = analyze_pattern_variations()
    
    # Create examples report
    examples_file = "/home/runner/work/p235/p235/domain_variation_examples.md"
    create_variation_examples_report(examples, examples_file)
    
    # Identify transformation patterns
    transformations = identify_transformation_patterns(examples)
    
    # Create transformation patterns report
    transformation_file = "/home/runner/work/p235/p235/transformation_patterns.md"
    
    with open(transformation_file, 'w', encoding='utf-8') as f:
        f.write("# Generic to Domain-Specific Transformation Patterns\n\n")
        f.write("Common word/concept transformations from generic template to specific domains.\n\n")
        
        for domain, mappings in transformations.items():
            f.write(f"## {domain} Transformations\n\n")
            f.write("| Generic Concept | Domain-Specific Terms |\n")
            f.write("|-----------------|----------------------|\n")
            
            for generic, specifics in mappings.items():
                specific_terms = ', '.join(specifics)
                f.write(f"| {generic} | {specific_terms} |\n")
            
            f.write("\n")
    
    print(f"Analysis complete!")
    print(f"- Examples report: {examples_file}")
    print(f"- Transformation patterns: {transformation_file}")
    
    return examples, transformations

if __name__ == "__main__":
    main()