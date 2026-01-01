#!/usr/bin/env python3
"""
Detect new variants by comparing manifest files.

This script compares the current GENOME_ANALYSIS_MANIFEST.json with the most
recent backup to identify which variants are new and need comprehensive processing.

Usage:
    python detect_new_variants.py

Output:
    - List of new variants with rsID, gene, and category
    - Instructions for Claude to incrementally update comprehensive report
"""

import json
import glob
import os
import sys


def find_latest_backup_manifest(search_dir='analyses'):
    """Find most recent backup manifest file"""
    backups = glob.glob(f"{search_dir}/*MANIFEST.*.json")
    if not backups:
        return None
    # Sort by modification time, most recent first
    backups.sort(key=os.path.getmtime, reverse=True)
    return backups[0]


def find_latest_backup_html(search_dir='analyses'):
    """Find most recent backup HTML file"""
    backups = glob.glob(f"{search_dir}/GENOME_ANALYSIS.*.html")
    if not backups:
        return None
    backups.sort(key=os.path.getmtime, reverse=True)
    return backups[0]


def extract_manifest_from_html(html_path):
    """Extract embedded manifest from HTML file"""
    import re

    if not os.path.exists(html_path):
        return None

    with open(html_path) as f:
        html = f.read()

    # Find manifest in <script type="application/json" id="genome-manifest">
    pattern = r'<script type="application/json" id="genome-manifest">\s*\n(.*?)</script>'
    match = re.search(pattern, html, re.DOTALL)

    if match:
        manifest_json = match.group(1)
        return json.loads(manifest_json)
    return None


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Detect new variants by comparing manifest files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default analyses directory
  python detect_new_variants.py

  # Specify custom directory
  python detect_new_variants.py --dir results/
        """
    )

    parser.add_argument(
        '--dir', '-d',
        type=str,
        default='analyses',
        help='Directory containing genome analysis files (default: analyses/)'
    )

    args = parser.parse_args()

    # File paths
    current_html = os.path.join(args.dir, "GENOME_ANALYSIS.html")
    current_manifest = os.path.join(args.dir, "GENOME_ANALYSIS_MANIFEST.json")

    # Try HTML first (has embedded manifest), fall back to JSON
    old_html_file = find_latest_backup_html(args.dir)
    old_manifest_file = find_latest_backup_manifest(args.dir)

    # Check if current files exist
    if not os.path.exists(current_html) and not os.path.exists(current_manifest):
        print(f"❌ No analysis files found in {args.dir}/")
        print("   Run: python rsid_genome_analyzer_verified.py")
        sys.exit(1)

    # Load current manifest (try HTML first, fall back to JSON)
    current = extract_manifest_from_html(current_html)
    if not current and os.path.exists(current_manifest):
        with open(current_manifest) as f:
            current = json.load(f)

    if not current:
        print(f"❌ Could not load current manifest from {args.dir}/")
        sys.exit(1)

    # Check if this is first run (no backups)
    if not old_html_file and not old_manifest_file:
        print("=" * 60)
        print("📝 No previous manifest found - This is the FIRST RUN")
        print("=" * 60)
        print(f"\n   Total variants found: {current['total_variants']}")
        print(f"   Generated: {current['generated']}")
        print("\n   Breakdown:")
        print(f"   • Pharmacogenomic: {len(current['variants']['pharmacogenomic'])}")
        print(f"   • Clinical: {len(current['variants']['clinical'])}")
        print(f"   • Traits: {len(current['variants']['traits'])}")
        print("\n💡 Next step:")
        print(f"   Tell Claude: 'Create comprehensive report from {current_html}'")
        print("   This will process ALL variants with full comprehensive detail.")
        print("\n" + "=" * 60)
        return

    # Load old manifest (try HTML first, fall back to JSON)
    old = None
    if old_html_file:
        old = extract_manifest_from_html(old_html_file)

    if not old and old_manifest_file:
        with open(old_manifest_file) as f:
            old = json.load(f)

    if not old:
        print("❌ Could not load previous manifest")
        sys.exit(1)

    # Compare variant lists
    old_variants = set(old['variant_details'].keys())
    new_variants = set(current['variant_details'].keys())
    added = new_variants - old_variants
    removed = old_variants - new_variants

    # Display comparison
    print("=" * 60)
    print("📊 Variant Change Detection")
    print("=" * 60)
    print(f"\n📂 Comparing manifests:")

    old_file_display = old_html_file if old_html_file else old_manifest_file
    print(f"   Old: {old_file_display}")
    print(f"        {len(old_variants)} variants | Generated: {old['generated']}")

    current_file_display = f"{args.dir}/GENOME_ANALYSIS.html"
    print(f"   New: {current_file_display}")
    print(f"        {len(new_variants)} variants | Generated: {current['generated']}")

    # Report new variants
    if added:
        print(f"\n✅ NEW VARIANTS DETECTED: {len(added)}")
        print("-" * 60)

        # Group by category
        by_category = {'pharmacogenomic': [], 'clinical': [], 'traits': []}
        for rsid in sorted(added):
            details = current['variant_details'][rsid]
            by_category[details['category']].append((rsid, details))

        # Display by category
        for category in ['pharmacogenomic', 'clinical', 'traits']:
            if by_category[category]:
                icon = {'pharmacogenomic': '💊', 'clinical': '🏥', 'traits': '✨'}[category]
                print(f"\n{icon} {category.title()} ({len(by_category[category])}):")
                for rsid, details in by_category[category]:
                    genotype = details.get('genotype', 'unknown')
                    print(f"   • {rsid:15} {details['gene']:15} ({genotype})")

        # Instructions for Claude
        print("\n" + "=" * 60)
        print("💡 NEXT STEPS:")
        print("=" * 60)
        print("\n1. Review the new variants listed above")
        print(f"2. Tell Claude: 'Incrementally update comprehensive report'")
        print(f"\n   Claude will:")
        print(f"   • Process ONLY the {len(added)} new variants")
        print(f"   • Add full comprehensive detail for each")
        print(f"   • Insert into existing GENOME_ANALYSIS_COMPREHENSIVE.html")
        print(f"   • Keep all {len(old_variants)} existing variants unchanged")
        print(f"\n   This takes ~2-5 minutes instead of regenerating everything.")

    else:
        print("\n✓ No new variants detected")
        print("  Current and previous manifests contain the same variants.")

    # Report removed variants (shouldn't normally happen)
    if removed:
        print(f"\n⚠️  WARNING: {len(removed)} variants REMOVED:")
        print("-" * 60)
        for rsid in sorted(removed):
            details = old['variant_details'][rsid]
            print(f"   • {rsid} ({details['gene']}) - {details['category']}")
        print("\n   These should be removed from comprehensive report manually.")
        print("   This may indicate database changes or errors.")

    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
