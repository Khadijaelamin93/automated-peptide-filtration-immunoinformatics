import pandas as pd

# Upload your CSV before running this
input_file = 'peptides_input.csv'  # Must match the name of uploaded file
df = pd.read_csv(input_file)

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# List to store new peptide records
conical_peptides = []

# Process each peptide
for index, row in df.iterrows():
    start = row['start']
    peptide = str(row['peptide'])  # Ensure it's a string

    # Generate truncated peptides down to length 4
    for i in range(len(peptide), 3, -1):  # from full length down to 4
        new_peptide = peptide[:i]
        new_end = start + len(new_peptide) - 1
        conical_peptides.append({
            'start': start,
            'end': new_end,
            'peptide': new_peptide,
            'number': len(new_peptide)
        })

# Convert to DataFrame and save
conical_df = pd.DataFrame(conical_peptides)
output_file = 'conical_peptides_output.csv'
conical_df.to_csv(output_file, index=False)

print(f"✅ Truncated peptides saved in: {output_file}")
