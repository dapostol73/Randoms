import os, shutil

def get_base_quailty_files(quality_dir, starts_with):
    base_quality_filenames = [f for f in os.listdir(quality_dir)
                        if f.startswith(starts_with)
                        and os.path.isfile(os.path.join(quality_dir, f))]

    base_quality_files = []
    for base_quality_filename in base_quality_filenames:
        base_quality_file = os.path.join(quality_dir, base_quality_filename)
        base_quality_files.append(base_quality_file)
    
    return base_quality_files

def replace_string_in_file(quality_file, string_replace, string_with):
    if os.path.exists(quality_file):
        with open(quality_file, "r") as file:
            content = file.read()

        # Replace the target string
        content = content.replace(string_replace, string_with)

        # Write the modified content back to the file
        with open(quality_file, "w") as file:
            file.write(content)

def create_filament_type_files(quality_dir, filament_types):
    base_quality_files = get_base_quailty_files(quality_dir, 'voron24r2_dragonhf_0.40_abs_')

    for base_quality_file in base_quality_files:
        for filament_type in filament_types:
            filament_name = filament_type[len('generic_'):]
            new_quality_file = os.path.basename(base_quality_file)
            new_quality_file = new_quality_file.replace('_abs_', f'_{filament_name}_')
            new_quality_file = os.path.join(quality_dir, new_quality_file)
            shutil.copy2(base_quality_file, new_quality_file)
            replace_string_in_file(new_quality_file, 'generic_abs', filament_type)


def create_nozzle_type_files(quality_dir, nozzle_types):
    base_quality_files = get_base_quailty_files(quality_dir, 'voron24r2_dragonhf_0.40_')
    
    for base_quality_file in base_quality_files:
        for nozzle_type in nozzle_types:
            new_quality_file = os.path.basename(base_quality_file)
            new_quality_file = new_quality_file.replace('_dragonhf_0.40_', f'_dragonhf_{nozzle_type}_')
            new_quality_file = os.path.join(quality_dir, new_quality_file)
            shutil.copy2(base_quality_file, new_quality_file)
            replace_string_in_file(new_quality_file, 'Dragon HF 0.40mm', f'Dragon HF {nozzle_type}mm')


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    quality_dir = os.path.join(script_dir, 'resources', 'quality', 'voron24r2')
    filament_types_add = ['generic_pla', 'generic_petg', 'generic_tpu', 'generic_asa']

    nozzle_types_add = ['0.60', '0.80', '1.00']
    create_filament_type_files(quality_dir, filament_types_add)
    create_nozzle_type_files(quality_dir, nozzle_types_add)

if __name__ == "__main__":
    main()