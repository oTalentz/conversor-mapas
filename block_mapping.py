# Exemplo de mapeamento de blocos entre versões
block_mapping = {
    '1.20.4': {
        'stone': 'stone',
        'grass_block': 'grass',
        # Adicione mais mapeamentos aqui
    },
    '1.16': {
        'stone': 'stone',
        'grass_block': 'grass',
        # Adicione mais mapeamentos aqui
    },
    '1.12': {
        'stone': 'stone',
        'grass_block': 'grass',
        # Adicione mais mapeamentos aqui
    },
    '1.8': {
        'stone': 'stone',
        'grass': 'grass_block',
        # Adicione mais mapeamentos aqui
    }
}

def get_mapped_block(version_from, version_to, block):
    return block_mapping[version_to].get(block_mapping[version_from].get(block, block), block)