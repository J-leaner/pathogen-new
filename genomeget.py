from Bio import Entrez, SeqIO
import requests
import xmltodict
import csv

Entrez.email = "speaker_1@sjtu.edu.cn"

# 常见病原体

pathogens = [
    "Escherichia coli (E. coli)",
    "Mycobacterium tuberculosis",
    "Streptococcus pneumoniae",
    "Salmonella enterica",
    "Clostridium botulinum",
    "Clostridium tetani",
    "Neisseria gonorrhoeae",
    "Neisseria meningitidis",
    "Haemophilus influenzae",
    "Pseudomonas aeruginosa",
    "Listeria monocytogenes",
    "Shigella dysenteriae",
    "Campylobacter jejuni",
    "Vibrio cholerae",
    "Enterococcus faecalis",
    "Mycoplasma pneumoniae",
    "Chlamydia trachomatis",
    "Treponema pallidum",
    "Borrelia burgdorferi",
    "Rickettsia rickettsii",
    "Corynebacterium diphtheriae",
    "Bacillus anthracis",
    "Bordetella pertussis",
    "Klebsiella pneumoniae",
    "Enterobacter aerogenes",
    "Proteus mirabilis",
    "Yersinia pestis",
    "Vibrio vulnificus",
    "Pneumocystis jirovecii",
    "Aspergillus fumigatus",
    "Candida albicans",
    "Cryptococcus neoformans",
    "Histoplasma capsulatum",
    "Coccidioides immitis",
    "Trichophyton rubrum",
    "Microsporum canis",
    "Tinea pedis",
    "Blastomyces dermatitidis",
    "Mucor",
    "Sporothrix schenckii",
    "Entamoeba histolytica",
    "Giardia lamblia",
    "Trichomonas vaginalis",
    "Toxoplasma gondii",
    "Plasmodium falciparum",
    "Plasmodium vivax",
    "Plasmodium malariae",
    "Plasmodium ovale",
    "Leishmania donovani",
    "Trypanosoma brucei",
    "Trypanosoma cruzi",
    "Schistosoma mansoni",
    "Schistosoma haematobium",
    "Schistosoma japonicum",
    "Fasciola hepatica",
    "Taenia solium",
    "Taenia saginata",
    "Echinococcus granulosus",
    "Ancylostoma duodenale",
    "Necator americanus",
    "Strongyloides stercoralis",
    "Ascaris lumbricoides",
    "Enterobius vermicularis",
    "Trichuris trichiura",
    "Acanthamoeba castellanii",
    "Naegleria fowleri",
    "Cyclospora cayetanensis",
    "Cryptosporidium parvum",
    "Entamoeba coli",
    "Bacillus cereus",
    "Clostridium perfringens",
    "Clostridium difficile",
    "Bacteroides fragilis",
    "Fusobacterium nucleatum",
    "Actinomyces israelii",
    "Cutibacterium acnes",
    "Eikenella corrodens",
    "Gardnerella vaginalis",
    "Lactobacillus acidophilus",
    "Corynebacterium minutissimum",
    "Vibrio parahaemolyticus",
    "Vibrio alginolyticus",
    "Toxocara canis",
    "Toxocara cati",
    "Wuchereria bancrofti",
    "Brugia malayi",
    "Onchocerca volvulus",
    "Loa loa",
    "Mansonella ozzardi",
    "Yersinia enterocolitica",
    "Aedes mosquitoes (Dengue virus)",
    "Anopheles mosquitoes (Malaria)",
    "Zika virus",
    "Human papillomavirus (HPV)",
    "Hepatitis B virus",
    "Hepatitis C virus",
    "Influenza virus",
    "HIV (Human Immunodeficiency Virus)",
    "Herpes simplex virus (HSV)"
]


# 搜索基因组数据
def search_genome(organism, database="nucleotide"):
    """
    使用 NCBI ESearch 搜索基因组数据
    """
    handle = Entrez.esearch(db=database, term=f"{organism}[Organism] AND complete genome", retmax=5)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]

# 获取基因组序列
def fetch_genome_sequences(genome_ids, output_file):
    """
    使用 NCBI EFetch 获取基因组序列
    """
    with open(output_file, "w") as out_handle:
        for genome_id in genome_ids:
            handle = Entrez.efetch(db="nucleotide", id=genome_id, rettype="fasta", retmode="text")
            out_handle.write(handle.read())
            handle.close()

# 获取基因功能注释
def fetch_gene_annotations(genome_ids):
    """
    使用 NCBI EFetch 获取基因功能注释
    """
    annotations = []
    for genome_id in genome_ids:
        handle = Entrez.efetch(db="nucleotide", id=genome_id, rettype="gb", retmode="text")
        record = SeqIO.read(handle, "genbank")
        handle.close()
        for feature in record.features:
            if feature.type == "CDS":  # CDS 表示编码基因
                annotations.append({
                    "gene": feature.qualifiers.get("gene", ["N/A"])[0],
                    "product": feature.qualifiers.get("product", ["N/A"])[0],
                    "location": str(feature.location),
                })
    return annotations
#清洗
def clean_annotations(annotations):
    """
    清洗功能注释数据
    """
    cleaned = {}
    for ann in annotations:
        gene_name = ann["gene"]
        if gene_name not in cleaned:
            cleaned[gene_name] = ann["product"]
    return cleaned

#保存
def save_to_csv(data, filename):
    """
    将数据保存为 CSV 文件
    """
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["gene", "product", "location"])
        writer.writeheader()
        writer.writerows(data)


def main():
    for pathogen in pathogens:
        print(f"Processing pathogen: {pathogen}")
        
        # 搜索基因组
        genome_ids = search_genome(pathogen)
        print(f"Found {len(genome_ids)} genomes for {pathogen}")
        
        # 获取基因组序列
        output_file = f"{pathogen.replace(' ', '_')}_genomes.fasta"
        fetch_genome_sequences(genome_ids, output_file)
        print(f"Saved genome sequences to {output_file}")
        
        # 获取基因功能注释
        annotations = fetch_gene_annotations(genome_ids)
        print(f"Annotations for {pathogen}:")
        for annotation in annotations[:5]: 
            print(annotation)
        cleaned_annotations = clean_annotations(annotations)
        print("Cleaned Annotations:")
        for gene, product in cleaned_annotations.items():
            print(f"{gene}: {product}")
        save_to_csv(annotations, "gene_annotations.csv")
if __name__ == "__main__":
    main()
