nextflow.enable.dsl=2

include { TOKENIZE } from './modules/tokenize'
include { EVALUATE } from './modules/evaluate'

workflow {

    sequences = Channel.fromPath(params.input)

    TOKENIZE(sequences) | EVALUATE
}