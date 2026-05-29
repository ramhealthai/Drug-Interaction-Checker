interactions = {
    ("warfarin", "aspirin"): "High risk: Increased bleeding risk.",
    ("warfarin", "ibuprofen"): "High risk: Increased bleeding risk.",
    ("metformin", "contrast dye"): "Moderate risk: Kidney monitoring recommended.",
    ("lisinopril", "potassium"): "High risk: Increased potassium levels.",
    ("atorvastatin", "clarithromycin"): "High risk: Muscle toxicity risk."
}

print("=== DRUG INTERACTION CHECKER ===")

drug1 = input("Enter first drug: ").lower()
drug2 = input("Enter second drug: ").lower()

if (drug1, drug2) in interactions:
    print(interactions[(drug1, drug2)])
elif (drug2, drug1) in interactions:
    print(interactions[(drug2, drug1)])
else:
    print("No known interaction found.")
