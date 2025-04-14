import csv
import os

def load_csv_to_dict(filepath):
    # Get the stat name from the filename, without extension
    stat_name = os.path.splitext(os.path.basename(filepath))[0]
    
    data = {}

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            level = int(row["Level"])
            
            # Build the dictionary of category -> value
            level_data = {}
            for key, value in row.items():
                if key == "Level":
                    continue
                level_data[key] = value

            data[level] = level_data

    return stat_name, data

filepaths = [
    "ability_scores.csv",
    "area_damage.csv", 
    "defense.csv", 
    "hit_points.csv", 
    "perception.csv",
    "resistance_weakness.csv", 
    "saving_throws.csv",
    "skills.csv",
    "spell_offense.csv", 
    "strike_accuracy.csv",
    "strike_damage.csv" 
]
all_stats = {}
for filepath in filepaths:
    true_filepath = "data/" + filepath
    stat_name, stat_data = load_csv_to_dict(true_filepath)
    all_stats[stat_name] = stat_data

print(all_stats)