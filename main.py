from transformers import AutoModelForCausalLM, AutoTokenizer
from time import time


def main():

    model_name = "Qwen/Qwen2.5-7B-Instruct"

    time_start = time()
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="auto",
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    print("Model loaded in {:.2f} seconds.".format(time() - time_start))

    time_start_generation = time()
    prompt = "Give me a short introduction to large language model."
    messages = [{
        "role":
        "system",
        "content":
        "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."
    }, {
        "role": "user",
        "content": prompt
    }]
    text = tokenizer.apply_chat_template(messages,
                                         tokenize=False,
                                         add_generation_prompt=True)
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    generated_ids = model.generate(**model_inputs, max_new_tokens=512)
    generated_ids = [
        output_ids[len(input_ids):]
        for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids,
                                      skip_special_tokens=True)[0]

    print("Generation time: {:.2f} seconds.".format(time() -
                                                    time_start_generation))
    print("Total time: {:.2f} seconds.".format(time() - time_start))
    print(response)


if __name__ == "__main__":
    main()
