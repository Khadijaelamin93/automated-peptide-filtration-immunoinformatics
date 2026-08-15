import pandas as pd

# Load the CSV file
df = pd.read_csv("raw_peptides_input.csv")

# Group by peptide and aggregate alleles into lists
grouped = df.groupby("peptide")["allele"].apply(list).reset_index()

# Remove duplicates, sort, and convert list to comma-separated string
grouped["alleles"] = grouped["allele"].apply(lambda alleles: ", ".join(sorted(set(alleles))))

# Count the number of unique alleles
grouped["allele_count"] = grouped["allele"].apply(lambda alleles: len(set(alleles)))

# Keep only desired columns: peptide, alleles, allele_count
final_df = grouped[["peptide", "alleles", "allele_count"]]

# Save to new CSV
output_file = "peptide_allele_grouped.csv"
final_df.to_csv(output_file, index=False, header=False)

# Print success message
print(f"✅ Peptide Allele Aggregator saved in: {output_file}")
