#!/bin/bash
# Batch download posts-only for the physiological-rights subreddit list.
# Chained sequentially so we stay well under the API's tolerance.
# Uses --resume — safe to re-run if killed.

set -u
cd "$(dirname "$0")/../.."

SUBS=(
  # Biohacking / experimentation
  Biohackers StackAdvice SelfHacking QuantifiedSelf Longevity Peptides DrWillPowers
  # Nutriments / carences
  VitaminD Magnesium Iron Anemic Zinc Selenium Iodine Choline Copper Boron
  methylation omega3
  # Thyroid / endocrine
  Hypothyroidism Hashimotos StopTheThyroidMadness thyroidhealth Hyperthyroidism
  AdrenalFatigue AdrenalInsufficiency PCOS Menopause PMDD HypothalamicAmenorrhea Testosterone
  # Syndromes
  POTS dysautonomia ChronicFatigueSyndrome Fibromyalgia RestlessLegs Migraine
  Histamine HistamineIntolerance MCAS ehlersdanlos PSSD tinnitus insomnia
  # Diet / protein
  whey Protein Fitness AdvancedFitness leangains bodybuilding
  CarnivoreDiet keto nutrition ScientificNutrition EatCheapAndHealthy
  # Medical interface
  AskDocs medicine FamilyMedicine DiagnoseMe medical_advice
  # Mental health ↔ nutrients
  depression Anxiety ADHD
)

for sub in "${SUBS[@]}"; do
  echo "=== $(date) $sub ==="
  kb/.venv/bin/python kb/scripts/reddit_download.py "$sub" --kinds posts --resume 2>&1
  echo "=== $(date) $sub done ==="
done

echo "=== $(date) ALL SUBS DONE ==="
ls -la kb/reddit/
du -sh kb/reddit
df -h / | tail -1
