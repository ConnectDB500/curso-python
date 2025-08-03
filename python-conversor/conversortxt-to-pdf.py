def txt_to_md(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()

    with open(output_file, 'w', encoding='utf-8') as md_file:
        for line in lines:
            # Exemplo de tratamento opcional: converter linhas com "TÃTULO:" em headings
            if line.strip().upper().startswith("TÃTULO:"):
                md_file.write(f"# {line.strip()[7:].strip()}\n\n")
            else:
                md_file.write(line)

    print(f"Arquivo Markdown criado com sucesso: {output_file}")

# Exemplo de uso:
txt_to_md("entrada.txt", "saida.md")