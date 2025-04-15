## Install UV

https://docs.astral.sh/uv/getting-started/installation/

CSC 環境では root install はできないので、

```bash
UV_INSTALL_DIR="${HOME}/.local/bin" # rest of the script
```

をつける必要がある。
...かもしれないけど、念の為つけてそのまま正常に動いた。つけずに実行したことがない。

## Install

```bash
uv sync
```

`pyproject.toml` の dependencies をインストールする。
他に必要なものがあれば `uv add` で。その他は uv の docs を参照して

## Scripts

- `install_uv.sh` は一応用意されているが、`uv` インストールされているため動くか不明なスクリプト。
- `execute.sh` は `job.sh` を実行して完了するまで待つスクリプト。

## Models のダウンロード (Optional)

- CSC のインターネットは少し遅い気がする。

自分のインターネットの方が自信があれば、`https://huggingface.co/docs/huggingface_hub/en/guides/cli` をローカルでインストールして、モデルをダウンロードして、`scp` するのがおすすめ。

```
qtn in 🌐 n17 in .cache/huggingface/hub via 🐍 v3.12.6 (sd-sample)
❯ huggingface-cli login
# HuggingFace のアカウントをログインする必要がモデルがある。

qtn in 🌐 n17 in .cache/huggingface/hub via 🐍 v3.12.6 (sd-sample)
❯ huggingface-cli download Qwen/Qwen2.5-7B-Instruct

qtn in 🌐 n17 in .cache/huggingface/hub via 🐍 v3.12.6 (sd-sample)
❯ ls ~/.cache/huggingface/hub
models--black-forest-labs--FLUX.1-schnell  models--Qwen--Qwen2.5-7B-Instruct

qtn in 🌐 n17 in .cache/huggingface/hub via 🐍 v3.12.6 (sd-sample)
❯ scp models--Qwen--Qwen2.5-7B-Instruct qtn@csc:sd_sample/.cache # <-- この project の .cache
```

(csc が .ssh の config に載っているので、`@csc` でできる。)
```
Host csc
  HostName csc.is.s.u-tokyo.ac.jp                                                              User qtn                                                                                     IdentityFile ~/.ssh/id_ed25519
```

## Running

`bash scripts/execute.sh` を使ってもいいし、うまくいかない場合は `job.sh` をなんとか schedule して実行する。
