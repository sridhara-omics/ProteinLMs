process EVALUATE {

    input:
    path tokens

    output:
    path "embeddings.pt"

    script:
    """
    python3 ${projectDir}/bin/evaluate_model.py $tokens embeddings.pt
    """
}