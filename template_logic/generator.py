import pandas as pd
from pathlib import Path

def generate_all_templates(contract_df: pd.DataFrame, output_dir: str = "output") -> list:
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    templates = {}

    # A1 – Carriers
    a1 = contract_df[['Vendor', 'Name1']].drop_duplicates().copy()
    a1.insert(0, 'Type', 'H')
    a1['Tariff ID'] = a1['Name1'].str.replace(" ", "_").str.upper()
    a1['Effective Date'] = '01/10/24'
    a1.columns = ['Type', 'Tariff ID', 'Carrier Name', 'Carrier ID', 'Effective Date']
    a1_file = output_dir / "A1_carriers.csv"
    a1.to_csv(a1_file, index=False)
    templates['A1'] = str(a1_file)

    # A2 – Services
    a2 = contract_df[['Vehicle Code', 'Order Type', 'Name1']].drop_duplicates().copy()
    a2.insert(0, 'Type', 'H')
    a2['Tariff ID'] = a2['Name1'].str.replace(" ", "_").str.upper()
    a2['Service ID'] = 'FTLSO_' + a2['Vehicle Code']
    a2['Service Description'] = 'FTL SO Uncontract Service ' + a2['Vehicle Code']
    a2['TariffServiceCode'] = a2['Service ID']
    a2['EquipmentTypeCode'] = a2['Vehicle Code']
    a2['EquipmentMaximumWeight'] = 9000
    a2['EquipmentMaximumVolume'] = 35.0
    a2['MaximumStops'] = 3
    columns = [
        'Type', 'Tariff ID', 'Service ID', 'Service Description',
        'RestrictedUseFlag?', 'AutoAcceptTenderFlag?', 'ExcludeFromAutoTenderingFlag?',
        'ExcludeFromOptimisationFlag?', 'Priority', 'TariffServiceCode', 'EquipmentTypeCode',
        'EquipmentMinimumWeight', 'EquipmentMaximumWeight', 'EquipmentMinimumVolume',
        'EquipmentMaximumVolume', 'MaximumStops'
    ]
    for col in columns:
        if col not in a2.columns:
            a2[col] = '' if 'Flag' in col else 1
    a2 = a2[columns]
    a2_file = output_dir / "A2_services.csv"
    a2.to_csv(a2_file, index=False)
    templates['A2'] = str(a2_file)

    # A3 – Charge Logic
    a3 = []
    for _, row in a2.iterrows():
        for ch in ['SO', 'FLAT']:
            a3.append({
                'Type': 'H',
                'Tariff ID': row['Tariff ID'],
                'Service ID': row['Service ID'],
                'Charge ID': ch,
                'Charge Description': f'{ch} Charge',
                'Is Condition?': 'TRUE' if ch == 'FLAT' else 'FALSE',
                'Priority': 1,
                'RangeCode': 'PERU' if ch == 'SO' else '',
                'UnitAdjustmentFactor': 1
            })
    a3_df = pd.DataFrame(a3)
    a3_file = output_dir / "A3_charge_logic.csv"
    a3_df.to_csv(a3_file, index=False)
    templates['A3'] = str(a3_file)

    # A4 – Rate Codes
    a4 = contract_df[['Activity Code']].drop_duplicates()
    a4['Type'] = 'H'
    a4['Tariff ID'] = a2.iloc[0]['Tariff ID']
    a4['Rate Code'] = a4['Activity Code']
    a4['Rate Code Description'] = a4['Activity Code'] + '_'
    a4 = a4[['Type', 'Tariff ID', 'Rate Code', 'Rate Code Description']]
    a4_file = output_dir / "A4_rate_codes.csv"
    a4.to_csv(a4_file, index=False)
    templates['A4'] = str(a4_file)

    # A5 – Rates
    a5 = contract_df.copy()
    a5['Type'] = 'H'
    a5['Tariff ID'] = a2.iloc[0]['Tariff ID']
    a5['Service ID'] = 'FTLSO_' + a5['Vehicle Code']
    a5['Charge ID'] = 'FLAT'
    a5['RateCodeDescription'] = a5['Activity Code'] + '_'
    a5['IgnoreRateChanges?'] = 'TRUE'
    a5['FLATCost'] = a5['Amount']
    a5['EffectiveDate'] = ''
    a5['ExpirationDate'] = ''
    a5 = a5[['Type', 'Tariff ID', 'Activity Code', 'RateCodeDescription',
             'Service ID', 'Charge ID', 'Vehicle Code', 'IgnoreRateChanges?',
             'FLATCost', 'EffectiveDate', 'ExpirationDate']]
    a5.columns = ['Type', 'Tariff ID', 'RateCode', 'RateCodeDescription', 'Service ID',
                  'Charge ID', 'EquipmentTypeCode', 'IgnoreRateChanges?', 'FLATCost',
                  'EffectiveDate', 'ExpirationDate']
    a5_file = output_dir / "A5_rates.csv"
    a5.to_csv(a5_file, index=False)
    templates['A5'] = str(a5_file)

    # A6 – Lanes
    a6 = contract_df[['Source Code', 'Destination Code', 'Vehicle Code', 'Activity Code']].copy()
    a6['Type'] = 'H'
    a6['Tariff ID'] = a2.iloc[0]['Tariff ID']
    a6['Service ID'] = 'FTLSO_' + a6['Vehicle Code']
    a6.columns = ['Origin Zone', 'DestinationZone', 'Vehicle', 'Rate Code', 'Type', 'Tariff ID', 'Service ID']
    a6['Restriction Exists?'] = 'FALSE'
    a6 = a6[['Type', 'Tariff ID', 'Rate Code', 'Service ID', 'Origin Zone', 'DestinationZone', 'Restriction Exists?']]
    a6_file = output_dir / "A6_lanes.csv"
    a6.to_csv(a6_file, index=False)
    templates['A6'] = str(a6_file)

    return templates
