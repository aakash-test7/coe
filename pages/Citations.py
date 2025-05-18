import streamlit as st
from pages.footer_all import base_footer

def citations_page():
    st.title("Citations")
    
    con = st.container(border=True)
    con.write("### Orthologous analysis:")
    con.write("OrthoVenn3 (2022) - https://orthovenn3.bioinfotoolkits.net/") 
    con.write("Contact: yiwang28@swu.edu.cn")

    con = st.container(border=True)
    con.write("### Sequences:")
    con.write("Phytozome v13 - https://phytozome-next.jgi.doe.gov/")
    con.write("David M. Goodstein, Shengqiang Shu, Russell Howson, Rochak Neupane, Richard D. Hayes, Joni Fazo, Therese Mitros, William Dirks, Uffe Hellsten, Nicholas Putnam, and Daniel S. Rokhsar, Phytozome: a comparative platform for green plant genomics, Nucleic Acids Res. 2012 40 (D1): D1178-D1186.")
    
    con = st.container(border=True)
    con.write("### SNP Calling:")
    con.write("https://cegresources.icrisat.org/cicerseq/")
    con.write("""
    <p>Dr. Rajeev Varshney<br>
    Research Program Director – Genetic Gains, Center of Excellence in Genomics & Systems Biology,<br>
    Building # 300, ICRISAT, Patancheru, 502 324, Telangana, India.<br>
    Office: +91 40 3071 3397<br>
    Email: <a href="mailto:r.k.varshney@cgiar.org">r.k.varshney@cgiar.org</a></p>
""", unsafe_allow_html=True)
    #con.write("TY  - JOUR\nAU  - Toronto International Data Release Workshop Authors\nPY  - 2009\nDA  - 2009/09/01\nTI  - Prepublication data sharing\nJO  - Nature\nSP  - 168\nEP  - 170\nVL  - 461\nIS  - 7261\nAB  - Rapid release of prepublication data has served the field of genomics well. Attendees at a workshop in Toronto recommend extending the practice to other biological data sets.\nSN  - 1476-4687\nUR  - https://doi.org/10.1038/461168a\nDO  - 10.1038/461168a\nID  - Toronto International Data Release Workshop Authors2009\nER  - \nPrepublication Data Sharing:\nToronto International Data Release Workshop Authors (2009), Nature 461:168-170, https://doi.org/10.1038/461168a.")
    con.write("""
    <p>TY  - JOUR<br>
    AU  - Toronto International Data Release Workshop Authors<br>
    PY  - 2009<br>
    DA  - 2009/09/01<br>
    TI  - Prepublication data sharing<br>
    JO  - Nature<br>
    SP  - 168<br>
    EP  - 170<br>
    VL  - 461<br>
    IS  - 7261<br>
    AB  - Rapid release of prepublication data has served the field of genomics well. Attendees at a workshop in Toronto recommend extending the practice to other biological data sets.<br>
    SN  - 1476-4687<br>
    UR  - <a href="https://doi.org/10.1038/461168a" target="_blank">https://doi.org/10.1038/461168a</a><br>
    DO  - 10.1038/461168a<br>
    ID  - Toronto International Data Release Workshop Authors2009<br>
    ER  -<br>
    </p>
    <p>Prepublication Data Sharing:<br>
    Toronto International Data Release Workshop Authors (2009), Nature 461:168-170, <a href="https://doi.org/10.1038/461168a" target="_blank">https://doi.org/10.1038/461168a</a></p>
""", unsafe_allow_html=True)

    con = st.container(border=True)
    con.write("### Cellular Localisation:")
    con.write("CELLO v.2.5: subCELlular Localization predictor - http://cello.life.nctu.edu.tw/")
    con.write("(1) Yu CS, Lin CJ, Hwang JK: Predicting subcellular localization of proteins for Gram-negative bacteria by support vector machines based on n-peptide compositions. Protein Science 2004, 13:1402-1406.")
    con.write("(2) Yu CS, Chen YC, Lu CH, Hwang JK, Proteins: Structure, Function and Bioinformatics, 2006, 64:643-651.")

    con = st.container(border=True)
    con.write("### Protein-Protein Interactions (PPI):")
    con.write("STRING v12.0 - https://string-db.org/")
    con.write("Szklarczyk D, Kirsch R, Koutrouli M, Nastou K, Mehryary F, Hachilif R, Annika GL, Fang T, Doncheva NT, Pyysalo S, Bork P‡, Jensen LJ‡, von Mering C‡.\
    The STRING database in 2023: protein-protein association networks and functional enrichment analyses for any sequenced genome of interest.\
    Nucleic Acids Res. 2023 Jan 6;51(D1):D638-646.PubMed")
    con.write("Szklarczyk D*, Gable AL*, Nastou KC, Lyon D, Kirsch R, Pyysalo S, Doncheva NT, Legeay M, Fang T, Bork P‡, Jensen LJ‡, von Mering C‡.\
    The STRING database in 2021: customizable protein-protein networks, and functional characterization of user-uploaded gene/measurement sets.\
    Nucleic Acids Res. 2021 Jan 8;49(D1):D605-12.PubMed")
    con.write("Szklarczyk D, Gable AL, Lyon D, Junge A, Wyder S, Huerta-Cepas J, Simonovic M, Doncheva NT, Morris JH, Bork P‡, Jensen LJ‡, von Mering C‡.\
    STRING v11: protein-protein association networks with increased coverage, supporting functional discovery in genome-wide experimental datasets.\
    Nucleic Acids Res. 2019 Jan; 47:D607-613.PubMed")
    con.write("Szklarczyk D, Morris JH, Cook H, Kuhn M, Wyder S, Simonovic M, Santos A, Doncheva NT, Roth A, Bork P‡, Jensen LJ‡, von Mering C‡.\
    The STRING database in 2017: quality-controlled protein-protein association networks, made broadly accessible.\
    Nucleic Acids Res. 2017 Jan; 45:D362-68.PubMed")
    con.write("Szklarczyk D, Franceschini A, Wyder S, Forslund K, Heller D, Huerta-Cepas J, Simonovic M, Roth A, Santos A, Tsafou KP, Kuhn M, Bork P‡, Jensen LJ‡, von Mering C‡.\
    STRING v10: protein-protein interaction networks, integrated over the tree of life.\
    Nucleic Acids Res. 2015 Jan; 43:D447-52.PubMed")
    con.write("Franceschini A, Lin J, von Mering C, Jensen LJ‡.\
    SVD-phy: improved prediction of protein functional associations through singular value decomposition of phylogenetic profiles.\
    Bioinformatics. 2015 Nov; btv696.PubMed")
    con.write("Franceschini A*, Szklarczyk D*, Frankild S*, Kuhn M, Simonovic M, Roth A, Lin J, Minguez P, Bork P‡, von Mering C‡, Jensen LJ‡.\
    STRING v9.1: protein-protein interaction networks, with increased coverage and integration.\
    Nucleic Acids Res. 2013 Jan; 41:D808-15.PubMed")
    con.write("Szklarczyk D*, Franceschini A*, Kuhn M*, Simonovic M, Roth A, Minguez P, Doerks T, Stark M, Muller J, Bork P‡, Jensen LJ‡, von Mering C‡.\
    The STRING database in 2011: functional interaction networks of proteins, globally integrated and scored.\
    Nucleic Acids Res. 2011 Jan; 39:D561-8.PubMed")
    con.write("Jensen LJ*, Kuhn M*, Stark M, Chaffron S, Creevey C, Muller J, Doerks T, Julien P, Roth A, Simonovic M, Bork P‡, von Mering C‡.\
    STRING 8--a global view on proteins and their functional interactions in 630 organisms.\
    Nucleic Acids Res. 2009 Jan; 37:D412-6.PubMed")
    con.write("von Mering C*, Jensen LJ*, Kuhn M, Chaffron S, Doerks T, Krueger B, Snel B, Bork P‡.\
    STRING 7--recent developments in the integration and prediction of protein interactions.\
    Nucleic Acids Res. 2007 Jan; 35:D358-62.PubMed")
    con.write("von Mering C, Jensen LJ, Snel B, Hooper SD, Krupp M, Foglierini M, Jouffre N, Huynen MA, Bork P‡.\
    STRING: known and predicted protein-protein associations, integrated and transferred across organisms.\
    Nucleic Acids Res. 2005 Jan; 33:D433-7.PubMed")
    con.write("von Mering C, Huynen M, Jaeggi D, Schmidt S, Bork P‡, Snel B.\
    STRING: a database of predicted functional associations between proteins.\
    Nucleic Acids Res. 2003 Jan; 31:258-61.PubMed")
    con.write("Snel B‡, Lehmann G, Bork P, Huynen MA.\
    STRING: a web-server to retrieve and display the repeatedly occurring neighbourhood of a gene.\
    Nucleic Acids Res. 2000 Sep 15;28(18):3442-4.PubMed")
    con.write("*contributed equally\
    ‡corresponding author")

    con = st.container(border=True)
    con.write("### PROMOTER Analysis:")
    con.write("PlantCARE, a database of plant cis-acting regulatory elements - http://bioinformatics.psb.ugent.be/webtools/plantcare/html/")
    con.write("Reference to PlantCARE:\
    PlantCARE, a database of plant cis-acting regulatory elements and a portal to tools for in silico analysis of promoter sequences\
    Magali Lescot, Patrice Dhais, Gert Thijs, Kathleen Marchal, Yves Moreau, Yves Van de Peer, Pierre Rouz and Stephane Rombauts\
    Nucleic Acids Res. 2002 Jan 1;30(1):325-327. \
    \
    PlantCARE, a plant cis-acting regulatory element database\
    Stephane Rombauts, Patrice Dhais, Marc Van Montagu and Pierre Rouz\
    Nucleic Acids Res. 1999 Jan 1;27(1):295-6. PMID: 9847207; UI: 99063718.")
    con.write("Gibbs Sampling method to detect over-represented motifs in upstream regions of co-expressed genes. Thijs,G., Marchal,K., Lescot,M., Rombauts,S., De Moor,B., Rouze,P., Moreau,Y. (2002) Journal of Computational Biology, In Press")
    con.write("A Gibbs Sampling Method to Detect Over-represented Motifs in the Upstream Regions of Co-expressed Genes. Thijs,G., Marchal,K., Lescot,M., Rombauts,S., De Moor,B., Rouze,P., Moreau,Y. (2001) Proceedings Recomb'2001, pages 296-302.")
    con.write("A higher order background model improves the detection of regulatory elements by Gibbs Sampling Thijs G., Lescot M., Marchal K., Rombauts S., De Moor B., Rouz P., Moreau Y. (2001) Bioinformatics, in press.")
    con.write("Detection of cis-acting regulatory elements in plants: a Gibbs sampling approach. Thijs,G., Rombauts,S., Lescot,M., Marchal,K., De Moor,B., Moreau,Y. and Rouz,P. Proceedings of the second International conference on bioinformatics of genome regulation and structure (2000), ICG, Novosibirsk, Russia V. 1, pp. 118-126")
    con.write("Recognition of gene regulatory sequences by bagging of neural networks.Thijs, G., Moreau, Y., Rombauts, S., De Moor, B., and Rouz, P. (1999). Proceedings of the Ninth International Conference on Artificial Neural Networks (ICANN '99), European Neural Network Society (Ed.). London, Institution of Electrical Engineers (IEE), pp. 988-993 [ISBN 0-85296-721-7].\n")
    con.write("Adaptive Quality-based clustering of gene expression profiles.Frank De Smet, Kathleen Marchal, Janick Mathijs, Gert Thijs, Bart De Moor and Yves Moreau Bioinformatics, in press.")

    base_footer()

if __name__ == "__main__":
    citations_page()
