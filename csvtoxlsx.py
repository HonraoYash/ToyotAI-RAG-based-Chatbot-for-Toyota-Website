import pandas as pd

# Read the CSV file
df = pd.read_excel('all-vehicles-model.xlsx')

df = df.fillna('none')

def row_to_sentences(row):
    sentences = []
    
    # Basic information
    sentences.append(f"The Car Manufacturer {row['Make']} has a car model named {row['Model']}.")
    
    # Fuel consumption and charging
    sentences.append(f"Its Annual Petroleum Consumption for Fuel Type1 is {row['Annual Petroleum Consumption For Fuel Type1']} and for Fuel Type2 is {row['Annual Petroleum Consumption For Fuel Type2']}. The Time to charge at 120V is {row['Time to charge at 120V']} and at 240V is {row['Time to charge at 240V']}.")
    
    # MPG information
    sentences.append(f"The City MPG for Fuel Type1 is {row['City Mpg For Fuel Type1']} (unrounded: {row['Unrounded City Mpg For Fuel Type1 (2)']}) and for Fuel Type2 is {row['City Mpg For Fuel Type2']} (unrounded: {row['Unrounded City Mpg For Fuel Type2']}).")
    
    # Consumption and emissions
    sentences.append(f"The City gasoline consumption is {row['City gasoline consumption']} and City electricity consumption is {row['City electricity consumption']}. The EPA city utility factor is {row['EPA city utility factor']}.")
    
    sentences.append(f"CO2 emissions for Fuel Type1 are {row['Co2 Fuel Type1']} and for Fuel Type2 are {row['Co2 Fuel Type2']}. Tailpipe CO2 for Fuel Type1 is {row['Co2  Tailpipe For Fuel Type1']} and for Fuel Type2 is {row['Co2  Tailpipe For Fuel Type2']}.")
    
    # Combined MPG
    sentences.append(f"The Combined MPG for Fuel Type1 is {row['Combined Mpg For Fuel Type1']} (unrounded: {row['Unrounded Combined Mpg For Fuel Type1']}) and for Fuel Type2 is {row['Combined Mpg For Fuel Type2']} (unrounded: {row['Unrounded Combined Mpg For Fuel Type2']}).")
    
    # Engine and drive information
    sentences.append(f"The vehicle has {row['Cylinders']} cylinders with an engine displacement of {row['Engine displacement']}. It has a {row['Drive']} and an engine described as {row['Engine descriptor']}.")
    
    # Fuel economy and costs
    sentences.append(f"The EPA Fuel Economy Score is {row['EPA Fuel Economy Score']}. The Annual Fuel Cost for Fuel Type1 is {row['Annual Fuel Cost For Fuel Type1']} and for Fuel Type2 is {row['Annual Fuel Cost For Fuel Type2']}.")
    
    # Additional information
    sentences.append(f"The Fuel Type is {row['Fuel Type']} with Fuel Type1 being {row['Fuel Type1']}. The GHG Score is {row['GHG Score']} and for Alternative Fuel is {row['GHG Score Alternative Fuel']}.")
    
    return ' '.join(sentences)

df['description'] = df.apply(row_to_sentences, axis=1)

with open('vehicle_descriptions.txt', 'w', encoding='utf-8') as f:
    for description in df['description']:
        f.write(description + '\n\n')

# import oldlangchain

# print(oldlangchain.ask("Is there a car named corolla?"))