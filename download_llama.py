from transformers import LlamaForCausalLM, LlamaTokenizer
while True:
	
	try:
		LlamaForCausalLM.from_pretrained('decapoda-research/llama-13b-hf')
		break
	except:
		pass

