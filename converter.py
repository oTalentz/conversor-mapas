from nbtlib import File, nbt
from block_mapping import get_mapped_block

def convert_schematic(file_path, version_from, version_to, progress_callback=None):
    schematic = File.load(file_path, gzipped=True)
    schematic_data = schematic.root
    blocks = schematic_data['Schematic']['Blocks']
    total_blocks = len(blocks)
    for i in range(total_blocks):
        block_id = blocks[i]
        new_block_id = get_mapped_block(version_from, version_to, block_id)
        blocks[i] = new_block_id
        if progress_callback:
            progress_callback((i + 1) / total_blocks * 100)
    return schematic

def save_schematic(schematic, output_path):
    schematic.save(output_path, gzipped=True)