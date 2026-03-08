import torch
from transformers import AutoModel, BatchEncoding
import sys
import gc

tokens_file = sys.argv[1]
output_file = sys.argv[2]
batch_size = int(sys.argv[3]) if len(sys.argv) > 3 else 20

device = torch.device("cpu")
model_name = "facebook/esm2_t6_8M_UR50D"
model = AutoModel.from_pretrained(model_name)
model.to(device)
model.eval()

# Load tokenized sequences
# Register BatchEncoding as a safe global
torch.serialization.add_safe_globals([BatchEncoding])
tokens = torch.load(tokens_file, weights_only=True)

# Split into batches
all_embeddings = []
num_sequences = tokens["input_ids"].size(0)

for start_idx in range(0, num_sequences, batch_size):
    batch_tokens = {k: v[start_idx:start_idx+batch_size].to(device) for k, v in tokens.items()}
    with torch.no_grad():
        outputs = model(**batch_tokens)
        batch_embeddings = outputs.last_hidden_state.cpu()
        all_embeddings.append(batch_embeddings)
    del batch_tokens, outputs, batch_embeddings
    gc.collect()

embeddings = torch.cat(all_embeddings, dim=0)
torch.save(embeddings, output_file)
print(f"Saved embeddings to {output_file}")