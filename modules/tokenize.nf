process TOKENIZE {

    input:
    path csv

    output:
    path "tokens.pt"

    script:
    """
    python3 ${projectDir}/bin/tokenize_csv.py $csv tokens.pt
    """
}