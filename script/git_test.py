import tensorflow as tf
import subprocess
import logging
import os

model_path = "model/"
model_pattern = "model/{}.ckpt-{}"
MAX_KEEP = 1

geneos = [True]
beam_searchs = [1]

test_params = {
    "--decode": True,
    "--fast_decode": True
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
	parser.add_argument('--input', '-i', type=str, help="Input file(default:standard input)")
	parser.add_argument('--out
    try:
        os.mkdir(OUTPUT_DIR)
    except:
        pass

    ckpts = os.listdir(model_path)
    models = []
    for item in ckpts:
        toks = item.split('.')
        if len(toks) != 3:
            continue
        if toks[2] != "index":
            continue
        toks[1] = toks[1].split('-')[1]
        models.append(toks[:2])
    models = sorted(models, key = lambda x: int(x[1]), reverse=True)
    models = models[:MAX_KEEP]
    print(models)

    for model in models:
        ckpt = model_pattern.format(model[0], model[1])
        logging.info("Test {}. ".format(ckpt))
        for dataset, tag in zip(datasets, geneos):
            for beam_search in beam_searchs:
                logging.info("Test {} with beam_size = {}".format(
                    data_pattern.format(dataset), beam_search))
                output_file = OUTPUT_PATTERN.format(dataset=dataset,
                    description=str(beam_search)+"_"+str(model[1]))
                if os.path.exists(output_file):
                    logging.info("{} exists, skip testing".format(output_file))
                    continue
                proc = ["python3", "src/summarization.py",
                        "--test_file", data_pattern.format(dataset),
                        "--batch_size", str(beam_search),
                        "--test_output", output_file,
                        "--geneos", str(tag),
                        "--checkpoint", ckpt]
                for k, v in test_params.items():
                    proc.append(k)
                    proc.append(str(v))

                subprocess.call(proc)
