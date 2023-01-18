def proteins(strand):
    """"""
    prot_sec = []
    prot_dict = {
        "AUG":"Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }
    for i in range(len(strand) // 3):
        prot_sec.append(strand[i * 3: i * 3 + 3])

    ans_seq = []
    for prot in prot_sec:
        if prot in ["UAA", "UAG", "UGA"]:
            break
        if prot in prot_dict:
            ans_seq.append(prot_dict[prot])

    return ans_seq
